#!/usr/bin/env python3
"""Linux Android smoke build. Run --help; usable without GitHub Actions."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "libraries/android-smoke.json"


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


def build(backend, output, ndk_arg, jobs):
    config, manifest = read_config()
    if platform.system() != "Linux":
        raise ValueError("This smoke entry currently requires a Linux host")
    directory = output / backend
    directory.mkdir(parents=True, exist_ok=True)
    log = directory / "build.log"
    log.write_text("", encoding="utf-8")
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    rows = [{"name": item["name"], "status": "not_run", "seconds": 0} for item in config["libraries"]]
    result = {"backend": backend, "revision": revision, "host": platform.platform(),
              "abi": config["abi"], "api": config["api"], "ndk": "",
              "generated": datetime.now(timezone.utc).isoformat(), "rows": rows}
    try:
        ndk = ndk_arg or subprocess.check_output(
            ["bash", "-c", 'source scripts/lib/common.sh; resolve_ndk'], cwd=ROOT, text=True).strip()
        if not Path(ndk, "build/cmake/android.toolchain.cmake").is_file():
            raise ValueError(f"Invalid Android NDK: {ndk}")
        result["ndk"] = ndk
        result["ndkVersion"] = (Path(ndk) / "source.properties").read_text(encoding="utf-8").strip()
        env = dict(os.environ, ANDROID_NDK_HOME=ndk, PYTHONUTF8="1")
        if backend == "vcpkg":
            build_vcpkg(config, rows, directory, log, env, jobs)
            result["toolReference"] = config["vcpkgRevision"]
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
                records = {line[0]: line for line in csv.reader(summary.open(), delimiter="\t") if len(line) == 7}
                for row in rows:
                    if row["name"] in records:
                        record = records[row["name"]]
                        row.update(status="success" if record[3] == "ok" else "failure", seconds=int(record[4]))
                    row["package"] = manifest[row["name"]][backend].get("reference", manifest[row["name"]][backend].get("package"))
            if code:
                result["error"] = f"build entry exited {code}; see build.log and per-library logs"
    except Exception as error:
        result["error"] = str(error)
        print(f"ERROR: {error}", flush=True)
    finally:
        (directory / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if all(row["status"] == "success" for row in rows) else 1


def build_vcpkg(config, rows, directory, log, env, jobs):
    work = ROOT / "build/smoke-vcpkg"
    tool = work / "tool"
    tool.mkdir(parents=True, exist_ok=True)
    commands = [
        ["git", "init", str(tool)],
        ["git", "-C", str(tool), "fetch", "--depth", "1", "https://github.com/microsoft/vcpkg.git", config["vcpkgRevision"]],
        ["git", "-C", str(tool), "checkout", "--detach", "FETCH_HEAD"],
        ["bash", str(tool / "bootstrap-vcpkg.sh"), "-disableMetrics"],
    ]
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
        f"set(VCPKG_CMAKE_SYSTEM_VERSION {config['api']})\nset(VCPKG_BUILD_TYPE release)\n", encoding="utf-8")
    env = dict(env, VCPKG_MAX_CONCURRENCY=str(jobs), VCPKG_BINARY_SOURCES="clear", VCPKG_DISABLE_METRICS="1")
    installed = directory / "installed"
    result_ports = {item["name"]: item["vcpkg"] for item in config["libraries"]}
    for row in rows:
        port = result_ports[row["name"]]
        started = time.monotonic()
        code = run([tool / "vcpkg", "install", f"{port}:{triplet}", "--classic",
                    f"--overlay-triplets={overlays}", f"--x-install-root={installed}",
                    f"--x-buildtrees-root={work / 'buildtrees'}", f"--x-packages-root={work / 'packages'}"], log, env)
        row.update(status="success" if code == 0 else "failure", seconds=round(time.monotonic() - started), package=port)
    status = installed / "vcpkg/status"
    if status.is_file():
        (directory / "installed-versions.txt").write_text(status.read_text(), encoding="utf-8")


def report(output, destination, run_url):
    config, _ = read_config()
    results = {}
    for backend in config["backends"]:
        paths = list(output.rglob(f"{backend}/results.json"))
        if len(paths) > 1:
            raise ValueError(f"duplicate results for {backend}")
        if paths:
            results[backend] = json.loads(paths[0].read_text(encoding="utf-8"))
    lines = ["# 常用 10 库 Android 编译验证", "",
             f"目标：Linux → Android `{config['abi']}` / API {config['api']} / Release。", "",
             f"[GitHub Actions 运行与日志]({run_url})" if run_url else "独立脚本运行。", "",
             "验证的是选定配置下包的实际构建与产物导出；不是 Android 设备运行测试，也不证明所有 ABI/选项可用。",
             "xmake 会编译头文件探针；Conan/vcpkg 构建包。各后端版本及默认功能可能不同。", "",
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
        if result.get("error"):
            lines.append("  错误：" + result["error"].replace("\n", " "))
    lines += ["", "每个后端的 artifact 含 results.json、build.log、安装产物及可取得的单库日志；vcpkg 版本见 installed-versions.txt，Conan/xmake 版本见构建日志。",
              "", "## 独立使用", "", "```bash", "python scripts/android-smoke.py build --backend vcpkg",
              "python scripts/android-smoke.py build --backend conan", "python scripts/android-smoke.py build --backend xmake",
              "python scripts/android-smoke.py report", "```", "",
              "库选择与 vcpkg 映射位于 libraries/android-smoke.json；Conan/xmake 包信息复用 libraries/manifest.json。脚本不读取 YAML 或依赖 GitHub 环境变量。"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{passed}/30 passed; report={destination}")
    return 0 if passed == len(config["libraries"]) * len(config["backends"]) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("matrix")
    builder = sub.add_parser("build")
    builder.add_argument("--backend", choices=("vcpkg", "conan", "xmake"), required=True)
    builder.add_argument("--ndk")
    builder.add_argument("--jobs", type=int, default=2)
    builder.add_argument("--output", type=Path, default=ROOT / "dist/smoke")
    reporter = sub.add_parser("report")
    reporter.add_argument("--output", type=Path, default=ROOT / "dist/smoke")
    reporter.add_argument("--destination", type=Path, default=ROOT / "docs/android-support/common10-build.md")
    reporter.add_argument("--run-url", default="")
    args = parser.parse_args()
    if args.command == "matrix":
        config, _ = read_config()
        print(json.dumps({"backend": config["backends"]}))
        return 0
    if args.command == "build":
        return build(args.backend, args.output.resolve(), args.ndk, args.jobs)
    return report(args.output.resolve(), args.destination, args.run_url)


if __name__ == "__main__":
    sys.exit(main())
