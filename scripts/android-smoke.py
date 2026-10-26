#!/usr/bin/env python3
"""Linux/macOS/Windows Android smoke build; usable without GitHub Actions."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "libraries/android-smoke.json"


def host_platform():
    return {"Linux": "linux", "Darwin": "mac", "Windows": "win"}[platform.system()]


def ndk_bin_dir(ndk):
    tag = {"linux": "linux-x86_64", "mac": "darwin-x86_64", "win": "windows-x86_64"}[host_platform()]
    return Path(ndk) / "toolchains/llvm/prebuilt" / tag / "bin"


def ensure_ndk_ranlib(ndk):
    directory = ndk_bin_dir(ndk)
    suffix = ".exe" if host_platform() == "win" else ""
    source = directory / ("llvm-ranlib" + suffix)
    if not source.is_file():
        raise RuntimeError(f"NDK llvm-ranlib missing: {source}")
    for triple in ("aarch64-linux-android", "arm-linux-androideabi", "i686-linux-android", "x86_64-linux-android"):
        alias = directory / (triple + "-ranlib" + suffix)
        if not alias.exists():
            if suffix:
                shutil.copy2(source, alias)
            else:
                alias.symlink_to(source.name)


def resolve_ndk():
    for name in ("ANDROID_NDK", "ANDROID_NDK_HOME", "ANDROID_NDK_ROOT", "ANDROID_NDK_LATEST_HOME"):
        path = os.environ.get(name)
        if path and Path(path, "build/cmake/android.toolchain.cmake").is_file():
            return Path(path).resolve().as_posix()
    for name in ("ANDROID_HOME", "ANDROID_SDK_ROOT"):
        sdk = os.environ.get(name)
        if not sdk:
            continue
        versions = sorted((Path(sdk) / "ndk").glob("*"),
                          key=lambda path: tuple(int(part) for part in re.findall(r"\d+", path.name)), reverse=True)
        for path in versions:
            if (path / "build/cmake/android.toolchain.cmake").is_file():
                return path.resolve().as_posix()
    raise RuntimeError("Android NDK not found; use --ndk or ANDROID_NDK_HOME")


def read_config():
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    manifest = json.loads((ROOT / "libraries/manifest.json").read_text(encoding="utf-8"))
    by_name = {item["name"]: item for item in manifest["libraries"]}
    names = [item["name"] for item in config["libraries"]]
    if len(names) != 10 or len(set(names)) != 10:
        raise ValueError("smoke selection must contain 10 unique libraries")
    for name in names:
        if name not in by_name:
            raise ValueError(f"unknown library: {name}")
        if config["api"] < by_name[name].get("minAndroidApi", 21):
            raise ValueError(f"API too low for {name}")
    return config, by_name


def run(command, log, env=None):
    command = list(command)
    print("+ " + " ".join(map(str, command)), flush=True)
    with log.open("a", encoding="utf-8") as output:
        output.write("\n+ " + " ".join(map(str, command)) + "\n")
        output.flush()
        result = subprocess.run(list(map(str, command)), cwd=ROOT, env=env,
                                stdout=output, stderr=subprocess.STDOUT)
    print(f"exit={result.returncode}; log={log}", flush=True)
    if result.returncode:
        print("\n".join(log.read_text(encoding="utf-8", errors="replace").splitlines()[-50:]), flush=True)
    return result.returncode


def build(backend, output, ndk_arg, jobs, library=None):
    config, manifest = read_config()
    if library is not None:
        selected = [item for item in config["libraries"] if item["name"] == library]
        if not selected:
            raise ValueError(f"Library is not in the smoke selection: {library}")
        config = dict(config, libraries=selected)
    directory = output / backend
    if library is not None:
        directory = directory / library
    directory.mkdir(parents=True, exist_ok=True)
    log = directory / "build.log"
    log.write_text("", encoding="utf-8")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    rows = [{"name": item["name"], "status": "not_run", "seconds": 0} for item in config["libraries"]]
    result = {"backend": backend, "revision": revision, "host": platform.platform(), "hostPlatform": host_platform(),
              "abi": config["abi"], "api": config["api"], "ndk": "",
              "generated": datetime.now(timezone.utc).isoformat(), "rows": rows}
    try:
        ndk = Path(ndk_arg).resolve().as_posix() if ndk_arg else resolve_ndk()
        if not Path(ndk, "build/cmake/android.toolchain.cmake").is_file():
            raise ValueError(f"Invalid Android NDK: {ndk}")
        result["ndk"] = ndk
        result["ndkVersion"] = (Path(ndk) / "source.properties").read_text(encoding="utf-8").strip()
        # OpenSSL's Android Configure locates clang through PATH, including
        # recipes that do not generate a compiler environment themselves.
        ndk_bin = str(ndk_bin_dir(ndk))
        if backend == "xmake":
            ensure_ndk_ranlib(ndk)
        env = dict(os.environ, ANDROID_NDK_HOME=ndk, PYTHONUTF8="1",
                   PATH=ndk_bin + os.pathsep + os.environ.get("PATH", ""))
        if backend == "vcpkg":
            build_vcpkg(config, rows, directory, log, env, jobs)
            result["toolReference"] = config["vcpkgRevision"]
        elif host_platform() == "win":
            build_windows(config, manifest, rows, backend, directory, log, env, jobs)
        else:
            command = ["bash", "scripts/setup.sh", "--backends", backend,
                       "--abis", config["abi"], "--api", str(config["api"]), "--ndk", ndk, "--force"]
            if run(command, log, env):
                raise RuntimeError(f"{backend} setup failed")
            # Existing entry points own all package-specific build logic.
            code = run(["bash", "scripts/build.sh", "--libs", ",".join(row["name"] for row in rows),
                        "--backends", backend, "--abis", config["abi"], "--api", str(config["api"]),
                        "--ndk", ndk, "--jobs", str(jobs), "--out", str(directory / "packages")], log, env)
            summary = directory / "packages/summary.tsv"
            if summary.is_file():
                records = {line[0]: line for line in csv.reader(summary.open(encoding="utf-8"), delimiter="\t") if len(line) == 7}
                for row in rows:
                    if row["name"] in records:
                        record = records[row["name"]]
                        row.update(status="success" if record[3] == "ok" else "failure", seconds=int(record[4]))
                    row["package"] = manifest[row["name"]][backend].get("reference", manifest[row["name"]][backend].get("package"))
                    if row["status"] == "success":
                        try:
                            row["archivesVerified"] = verify_archives(directory / "packages" / row["name"], ndk, config["abi"])
                        except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
                            row.update(status="failure", error=str(error))
            if code:
                result["error"] = f"build entry exited {code}; see build.log and per-library logs"
    except Exception as error:
        result["error"] = str(error)
        print(f"ERROR: {error}", flush=True)
    finally:
        (directory / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if all(row["status"] == "success" for row in rows) else 1


def lua_value(value):
    if isinstance(value, dict):
        return "{" + ", ".join(f"[{json.dumps(key)}] = {lua_value(item)}" for key, item in value.items()) + "}"
    return json.dumps(value, ensure_ascii=False)


def build_windows(config, manifest, rows, backend, directory, log, env, jobs):
    """Native Windows commands: no Bash entry points or shell path conversion."""
    def checked(command):
        if run(command, log, env):
            raise RuntimeError(f"Command failed: {command[0]}")

    if backend == "xmake":
        home = Path.home()
        candidates = [home / "xmake", Path(os.environ.get("LOCALAPPDATA", home / "AppData/Local")) / "Programs/xmake"]
        env["PATH"] = os.pathsep.join(map(str, candidates)) + os.pathsep + env["PATH"]
        if not shutil.which("xmake", path=env["PATH"]):
            checked(["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command",
                     "$ErrorActionPreference='Stop'; Invoke-Expression (New-Object Net.WebClient).DownloadString('https://xmake.io/psget.text')"])
        tool = shutil.which("xmake", path=env["PATH"])
        if not tool:
            raise RuntimeError("xmake was not found after installation")
    else:
        tool = shutil.which("conan", path=env["PATH"])
        if not tool:
            venv = ROOT / "build/smoke-conan-venv"
            checked([sys.executable, "-m", "venv", str(venv)])
            checked([str(venv / "Scripts/python.exe"), "-m", "pip", "install", "conan>=2,<3"])
            env["PATH"] = str(venv / "Scripts") + os.pathsep + env["PATH"]
            tool = str(venv / "Scripts/conan.exe")
        checked([tool, "profile", "detect", "--force"])
        conan_home = subprocess.check_output([tool, "config", "home"], env=env, text=True).strip()
        clang = ndk_bin_dir(env["ANDROID_NDK_HOME"]) / "clang.exe"
        version = re.search(r"clang version (\d+)", subprocess.check_output([str(clang), "--version"], text=True)).group(1)
        arch = {"arm64-v8a": "armv8", "armeabi-v7a": "armv7", "x86_64": "x86_64", "x86": "x86"}[config["abi"]]
        profile = Path(conan_home) / "profiles" / f"android-{config['abi']}"
        profile.write_text(f"[settings]\nos=Android\narch={arch}\ncompiler=clang\ncompiler.version={version}\n"
                           f"compiler.libcxx=c++_static\nbuild_type=Release\nos.api_level={config['api']}\n"
                           f"[conf]\ntools.android:ndk_path={env['ANDROID_NDK_HOME']}\n", encoding="utf-8")
    for row in rows:
        started = time.monotonic()
        name = row["name"]
        package = manifest[name][backend]
        work = ROOT / "build/smoke-native" / backend / name
        artifact = directory / "packages" / name
        work.mkdir(parents=True, exist_ok=True)
        artifact.mkdir(parents=True, exist_ok=True)
        try:
            if backend == "xmake":
                package_name = package["package"]
                requirement = package_name + (" " + package["version"] if package.get("version") else "")
                configs = ", " + lua_value({"configs": package["configs"]}) if package.get("configs") else ""
                (work / "xmake.lua").write_text(
                    f'add_repositories("android-libs scripts/android/xmake/repo", {{rootdir = {lua_value(ROOT.as_posix())}}})\n'
                    f'add_rules("mode.release")\nadd_requires({lua_value(requirement)}{configs})\n'
                    f'target("probe")\nset_kind("static")\nadd_files("probe.cpp")\nset_languages("c++17")\nadd_packages({lua_value(package_name)})\n', encoding="utf-8")
                (work / "probe.cpp").write_text("".join(f"#include <{header}>\n" for header in manifest[name].get("headers", []))
                                                 + "int android_library_probe() { return 0; }\n", encoding="utf-8")
                checked([tool, "f", "-y", "-P", str(work), "-p", "android", "-a", config["abi"],
                         f"--ndk={env['ANDROID_NDK_HOME']}", f"--ndk_sdkver={config['api']}", "-m", "release"])
                checked([tool, "-y", "-P", str(work), "-j", str(jobs)])
                checked([tool, "require", "--export", f"--packagedir={artifact}", "-P", str(work), package_name])
            else:
                command = [tool, "install", f"--requires={package['reference']}", f"-pr:h=android-{config['abi']}",
                           "-pr:b=default", "-c:h", f"tools.build:jobs={jobs}", "--build=missing", "--deployer=full_deploy",
                           f"--deployer-folder={artifact}", "-of", str(work)]
                for option in package.get("options", []):
                    command.extend(["-o", option if ":" in option else package["reference"].split("/")[0] + ":" + option])
                if name == "libevent":
                    command.extend(["-c:h", 'tools.cmake.cmaketoolchain:extra_variables={"CMAKE_HAVE_LIBC_PTHREAD": True}'])
                checked(command)
            row["archivesVerified"] = verify_archives(artifact, env["ANDROID_NDK_HOME"], config["abi"])
            row["status"] = "success"
        except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
            row.update(status="failure", error=str(error))
        row.update(seconds=round(time.monotonic() - started), package=package.get("reference", package.get("package")))


def build_vcpkg(config, rows, directory, log, env, jobs):
    work = ROOT / "build/smoke-vcpkg"
    tool = work / "tool"
    tool.mkdir(parents=True, exist_ok=True)
    commands = [
        ["git", "init", str(tool)],
        ["git", "-C", str(tool), "fetch", "--depth", "1", "https://github.com/microsoft/vcpkg.git", config["vcpkgRevision"]],
        ["git", "-C", str(tool), "checkout", "--detach", "FETCH_HEAD"],
    ]
    if host_platform() == "win":
        commands.append(["cmd.exe", "/d", "/c", str(tool / "bootstrap-vcpkg.bat"), "-disableMetrics"])
    else:
        commands.append(["bash", str(tool / "bootstrap-vcpkg.sh"), "-disableMetrics"])
    for command in commands:
        if run(command, log, env):
            raise RuntimeError("vcpkg setup failed")
    arch = {"arm64-v8a": "arm64", "armeabi-v7a": "arm", "x86_64": "x64", "x86": "x86"}[config["abi"]]
    triplet = f"{arch}-android-api{config['api']}"
    overlays = work / "triplets"
    overlays.mkdir(parents=True, exist_ok=True)
    (overlays / f"{triplet}.cmake").write_text(
        f"set(VCPKG_TARGET_ARCHITECTURE {arch})\nset(VCPKG_CRT_LINKAGE dynamic)\n"
        "set(VCPKG_LIBRARY_LINKAGE static)\nset(VCPKG_CMAKE_SYSTEM_NAME Android)\n"
        f"set(VCPKG_CMAKE_SYSTEM_VERSION {config['api']})\nset(VCPKG_BUILD_TYPE release)\n"
        f"set(VCPKG_CMAKE_CONFIGURE_OPTIONS -DANDROID_ABI={config['abi']})\n"
        f"set(VCPKG_MAKE_BUILD_TRIPLET --host={dict(arm64='aarch64', arm='arm', x64='x86_64', x86='i686')[arch]}-linux-android)\n", encoding="utf-8")
    env = dict(env, VCPKG_MAX_CONCURRENCY=str(jobs), VCPKG_BINARY_SOURCES="clear", VCPKG_DISABLE_METRICS="1")
    installed = directory / "installed"
    result_ports = {item["name"]: item["vcpkg"] for item in config["libraries"]}
    for row in rows:
        port = result_ports[row["name"]]
        started = time.monotonic()
        executable = tool / ("vcpkg.exe" if host_platform() == "win" else "vcpkg")
        code = run([executable, "install", f"{port}:{triplet}", "--classic",
                    f"--overlay-triplets={overlays}", f"--x-install-root={installed}",
                    f"--x-buildtrees-root={work / 'buildtrees'}", f"--x-packages-root={work / 'packages'}"], log, env)
        if code == 0:
            try:
                row["archivesVerified"] = verify_archives(installed / triplet / "lib", env["ANDROID_NDK_HOME"], config["abi"])
            except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
                code = 1
                row["error"] = str(error)
        row.update(status="success" if code == 0 else "failure", seconds=round(time.monotonic() - started), package=port)
    status = installed / "vcpkg/status"
    if status.is_file():
        (directory / "installed-versions.txt").write_text(status.read_text(encoding="utf-8"), encoding="utf-8")


def verify_archives(directory, ndk, abi):
    expected = {"arm64-v8a": "AArch64", "armeabi-v7a": "ARM", "x86_64": "Advanced Micro Devices X86-64", "x86": "Intel 80386"}[abi]
    readelf = ndk_bin_dir(ndk) / ("llvm-readelf.exe" if host_platform() == "win" else "llvm-readelf")
    archives = [path for path in directory.rglob("*.a") if "/full_deploy/build/" not in path.as_posix()]
    if not archives:
        raise RuntimeError(f"No static archives found: {directory}")
    for archive in archives:
        headers = subprocess.check_output([str(readelf), "-h", str(archive)], text=True)
        machines = [line.split(":", 1)[1].strip() for line in headers.splitlines() if "Machine:" in line]
        if not machines or any(machine != expected for machine in machines):
            raise RuntimeError(f"ABI mismatch: {archive}: {set(machines)}; expected {expected}")
    print(f"Verified {len(archives)} archives: {expected}", flush=True)
    return len(archives)


def report(output, destination, run_url):
    config, _ = read_config()
    results = {}
    for path in sorted(output.rglob("results.json")):
        result = json.loads(path.read_text(encoding="utf-8"))
        backend = result["backend"]
        if backend not in config["backends"]:
            raise ValueError(f"unknown backend in {path}: {backend}")
        if backend not in results:
            results[backend] = dict(result, rows=[], errors=[])
        combined = results[backend]
        for field in ("revision", "abi", "api", "ndk"):
            if combined[field] != result[field]:
                raise ValueError(f"inconsistent {field} in {path}")
        names = {row["name"] for row in combined["rows"]}
        if any(row["name"] in names for row in result["rows"]):
            raise ValueError(f"duplicate library results for {backend}: {path}")
        combined["rows"].extend(result["rows"])
        if result.get("error"):
            combined["errors"].append(result["error"])
    hosts = {result.get("hostPlatform", "linux") for result in results.values()}
    if len(hosts) > 1:
        raise ValueError("Cannot merge results from different host platforms")
    host = {"linux": "Linux", "mac": "macOS", "win": "Windows"}[next(iter(hosts), "linux")]
    lines = ["# 常用 10 库 Android 编译验证", "",
             f"目标：{host} → Android `{config['abi']}` / API {config['api']} / Release。", "",
             f"[GitHub Actions 运行与日志]({run_url})" if run_url else "独立脚本运行。", "",
             "验证的是选定配置下包的实际构建与产物导出；不是 Android 设备运行测试，也不证明所有 ABI/选项可用。",
             "xmake 会编译头文件探针；Conan/vcpkg 构建包。各后端版本及默认功能可能不同。", "",
             "所有成功项还需通过 NDK llvm-readelf 的静态库架构检查；arm64 目标必须为 AArch64。", "",
             "| 库 | vcpkg | Conan 2 | xmake |", "| --- | --- | --- | --- |"]
    passed = 0
    for item in config["libraries"]:
        cells = [item["name"]]
        for backend in config["backends"]:
            row = next((row for row in results.get(backend, {}).get("rows", []) if row["name"] == item["name"]), {})
            status = row.get("status", "not_run")
            passed += status == "success"
            cells.append({"success": "✅ 编译通过", "failure": "❌ 编译失败", "not_run": "未完成"}.get(status, "未知"))
        lines.append("| " + " | ".join(cells) + " |")
    lines += ["", f"通过 **{passed}/{len(config['libraries']) * len(config['backends'])}** 个组合。", "", "## 环境与证据", ""]
    for backend in config["backends"]:
        result = results.get(backend)
        if result is None:
            lines.append(f"- {backend}：未取得结果，不能判定成功。")
            continue
        lines += [f"- {backend}：源码 `{result['revision']}`；NDK `{result['ndk']}`；时间 {result['generated']}。"]
        if result.get("toolReference"):
            lines.append(f"  vcpkg 快照：`{result['toolReference']}`。")
        for error in result.get("errors", []):
            lines.append("  错误：" + error.replace("\n", " "))
    lines += ["", "每个后端的 artifact 含 results.json、build.log、安装产物及可取得的单库日志；vcpkg 版本见 installed-versions.txt，Conan/xmake 版本见构建日志。",
              "", "## 独立使用", "", "```bash", "bash scripts/linux/libevent.sh # 默认使用三个后端",
              "bash scripts/linux/libevent.sh --backend conan", "bash scripts/linux/zlib.sh --backend vcpkg",
              "python scripts/android-smoke.py report", "```", "",
              "库选择与 vcpkg 映射位于 libraries/android-smoke.json；Conan/xmake 包信息复用 libraries/manifest.json。脚本不读取 YAML 或依赖 GitHub 环境变量。"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{passed}/30 passed; report={destination}")
    return 0 if passed == len(config["libraries"]) * len(config["backends"]) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    matrix_parser = sub.add_parser("matrix")
    matrix_parser.add_argument("--platform", choices=("linux", "mac", "win"), default="linux")
    matrix_parser.add_argument("--all-platforms", action="store_true")
    matrix_parser.add_argument("--group-by-backend", action="store_true")
    sub.add_parser("libraries")
    builder = sub.add_parser("build")
    builder.add_argument("--backend", choices=("all", "vcpkg", "conan", "xmake"), default="all")
    builder.add_argument("--library", help="Build only this library from the smoke selection")
    builder.add_argument("--ndk")
    builder.add_argument("--jobs", type=int, default=2)
    builder.add_argument("--output", type=Path, default=ROOT / "dist/smoke")
    reporter = sub.add_parser("report")
    reporter.add_argument("--output", type=Path, default=ROOT / "dist/smoke")
    reporter.add_argument("--destination", type=Path)
    reporter.add_argument("--platform", choices=("linux", "mac", "win"), default="linux")
    reporter.add_argument("--run-url", default="")
    args = parser.parse_args()
    if args.command == "libraries":
        config, _ = read_config()
        print("\n".join(item["name"] for item in config["libraries"]))
        return 0
    if args.command == "matrix":
        config, _ = read_config()
        libraries = [item["name"] for item in config["libraries"]]
        for library in libraries:
            extension = "bat" if args.platform == "win" else "sh"
            if not (ROOT / "scripts" / args.platform / f"{library}.{extension}").is_file():
                raise ValueError(f"Missing library entry: {library}.{extension}")
        runners = {"linux": "ubuntu-24.04", "mac": "macos-14", "win": "windows-2022"}
        runner = runners[args.platform]
        if args.group_by_backend:
            hosts = list(runners) if args.all_platforms else [args.platform]
            print(json.dumps({"include": [dict(platform=host, os=runners[host], backend=backend)
                                          for host in hosts for backend in config["backends"]]}))
            return 0
        print(json.dumps({"backend": config["backends"], "library": libraries,
                          "include": [{"platform": args.platform, "os": runner}]}))
        return 0
    if args.command == "build":
        config, _ = read_config()
        backends = config["backends"] if args.backend == "all" else [args.backend]
        codes = [build(backend, args.output.resolve(), args.ndk, args.jobs, args.library) for backend in backends]
        return 0 if all(code == 0 for code in codes) else 1
    suffix = "" if args.platform == "linux" else "-" + args.platform
    destination = args.destination or ROOT / f"docs/android-support/common10-build{suffix}.md"
    return report(args.output.resolve(), destination, args.run_url)


if __name__ == "__main__":
    sys.exit(main())
