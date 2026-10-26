#!/usr/bin/env python3
"""Inventory upstream metadata without executing third-party build recipes."""
from __future__ import annotations

import argparse
import ast
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess


REPOS = {
    "vcpkg": "microsoft/vcpkg",
    "conan": "conan-io/conan-center-index",
    "xmake": "xmake-io/xmake-repo",
}
ABIS = {"arm64-v8a": "arm64", "armeabi-v7a": "arm", "x86_64": "x64", "x86": "x86"}


def escape(value):
    return str(value).replace("|", "&#124;").replace("\n", " ").replace("\r", "")


def supports(expression, arch):
    """Parse vcpkg !, &, | and parentheses, preserving unknown identifiers."""
    if not expression:
        return True
    tokens = re.findall(r"[A-Za-z0-9_-]+|[!&|()]", expression)
    if re.sub(r"\s+", "", expression) != "".join(tokens):
        return None
    position = 0
    enabled = {"android", arch, "static"}
    known = enabled | {"arm", "arm64", "x86", "x64", "windows", "linux", "osx", "ios",
                       "uwp", "mingw", "emscripten", "wasm32", "wasm64", "xbox",
                       "freebsd", "openbsd", "netbsd", "solaris", "qnx", "native",
                       "staticcrt", "riscv32", "riscv64", "ppc64", "s390x", "loongarch64"}

    def atom():
        nonlocal position
        token = tokens[position]
        position += 1
        if token == "!":
            result = atom()
            return None if result is None else not result
        if token == "(":
            result = parse_or()
            if tokens[position] != ")":
                raise ValueError("unclosed expression")
            position += 1
            return result
        if token in "&|)":
            raise ValueError("unexpected operator")
        return token in enabled if token in known else None

    def parse_and():
        nonlocal position
        result = atom()
        while position < len(tokens) and tokens[position] == "&":
            position += 1
            right = atom()
            result = False if result is False or right is False else (None if result is None or right is None else True)
        return result

    def parse_or():
        nonlocal position
        result = parse_and()
        while position < len(tokens) and tokens[position] == "|":
            position += 1
            right = parse_and()
            result = True if result is True or right is True else (None if result is None or right is None else False)
        return result

    try:
        result = parse_or()
        return result if position == len(tokens) else None
    except (IndexError, ValueError):
        return None


def vcpkg_rows(root):
    rows = []
    for port in sorted((root / "ports").iterdir()):
        path = port / "vcpkg.json"
        if path.is_file():
            data = json.loads(path.read_text(encoding="utf-8-sig"))
            expression = data.get("supports", "")
            name = data.get("name", port.name)
            legacy = False
        elif (port / "CONTROL").is_file():
            path = port / "CONTROL"
            text = path.read_text(encoding="utf-8-sig")
            match = re.search(r"^Supports:\s*(.*)$", text, re.M)
            expression = match.group(1).strip() if match else ""
            name, legacy = port.name, True
        else:
            continue
        results = [supports(expression, arch) for arch in ABIS.values()]
        status = "元数据允许" if True in results else ("待验证" if None in results else "元数据排除")
        # Legacy CONTROL may contain feature paragraphs; do not treat it as a manifest.
        if legacy:
            status, results = "待验证", [None] * 4
        evidence = expression or "未设置 supports；未限制平台"
        if legacy:
            evidence = "旧 CONTROL 格式，需人工核对：" + evidence
        rows.append((name, status, evidence, path, results))
    return rows


def conan_rows(root):
    rows = []
    for recipe in sorted((root / "recipes").glob("*/**/conanfile.py")):
        relative = recipe.relative_to(root / "recipes")
        if len(relative.parts) != 3:
            continue  # exclude test_package and helper projects
        text = recipe.read_text(encoding="utf-8-sig")
        try:
            tree = ast.parse(text)
            mentions = sorted({node.lineno for node in ast.walk(tree)
                               if isinstance(node, ast.Constant) and isinstance(node.value, str)
                               and "android" in node.value.lower()})
        except SyntaxError:
            mentions = []
        status = "含 Android 逻辑" if mentions else "待验证"
        evidence = "配方包含 Android 字符串，可能是支持、排除或补丁；需核对 L" + ", L".join(map(str, mentions[:8])) if mentions else "未检测到 Android 字符串；通用配方也可能支持 Android"
        rows.append((f"{relative.parts[0]}/{relative.parts[1]}", status, evidence, recipe, None))
    return rows


def xmake_rows(root):
    rows = []
    for recipe in sorted((root / "packages").glob("*/*/xmake.lua")):
        text = recipe.read_text(encoding="utf-8-sig")
        # Evidence only: Lua hooks, host predicates and dependency constraints
        # cannot safely be evaluated by matching strings.
        lines = [f"L{number}: {line.strip()}" for number, line in enumerate(text.splitlines(), 1)
                 if "android" in line.lower() and not line.lstrip().startswith("--")]
        status = "含 Android 逻辑" if lines else "待验证"
        evidence = "; ".join(lines[:3])[:600] if lines else "无显式 Android 字符串；通用 on_install 仍可能支持 Android"
        rows.append((recipe.parent.name, status, evidence, recipe, None))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=Path("docs/android-support"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    index = ["# Android 库支持信息", "", f"生成时间：{stamp}", "",
             "全量扫描三个包仓库的元数据，不执行配方、不编译。**本报告不等于编译通过清单。**",
             "", "- vcpkg：按默认静态库、动态 CRT 的 Android triplet 计算顶层 supports；不求解依赖、默认 features 或 portfile 条件。",
             "- Conan 2：Conan Center 是配方仓库，存在配方不代表支持 Android；Android 字符串可能表示支持或排除。每个配方目录单列，版本见上游 config.yml。",
             "- xmake：Lua 安装回调、宿主条件及依赖需要运行时求解；Android 字符串仅作为人工核对入口。",
             "- 待验证并不表示不支持。要确认可用，需指定版本、宿主、ABI、API、选项并在 Actions 编译。",
             "- Android 目标 ABI：arm64-v8a、armeabi-v7a、x86_64、x86；宿主 Linux/macOS/Windows 的支持不能直接互换。",
             "", "| 包管理器 | 扫描条目 | 元数据允许 | 含 Android 逻辑 | 待验证 | 元数据排除 | 上游快照 |",
             "| --- | ---: | ---: | ---: | ---: | ---: | --- |"]
    for manager, scanner in (("vcpkg", vcpkg_rows), ("conan", conan_rows), ("xmake", xmake_rows)):
        root = (args.sources / manager).resolve()
        sha = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
        rows = scanner(root)
        if not rows:
            raise RuntimeError(f"{manager}: no recipes found; refusing to publish an empty inventory")
        counts = Counter(row[1] for row in rows)
        upstream = f"https://github.com/{REPOS[manager]}/tree/{sha}"
        index.append(f"| [{manager}]({manager}.md) | {len(rows)} | {counts['元数据允许']} | {counts['含 Android 逻辑']} | {counts['待验证']} | {counts['元数据排除']} | [{sha[:12]}]({upstream}) |")
        document = [f"# {manager} Android 元数据清单", "", f"生成时间：{stamp}", "",
                    "[判定方法与限制](README.md)。以下条目均未在本扫描工作流中编译验证。", "",
                    f"上游：[固定快照 {sha}]({upstream})；共 {len(rows)} 条。", ""]
        if manager == "vcpkg":
            document += ["ABI 列：允许 / 排除 / 未知；仅顶层 supports 条件，不保证依赖或 features 可构建。", "",
                         "| 库 | 判定 | arm64-v8a | armeabi-v7a | x86_64 | x86 | supports / 依据 |",
                         "| --- | --- | --- | --- | --- | --- | --- |"]
        else:
            document += ["| 库 / 配方目录 | 判定 | 依据（含排除条件也会列出） |", "| --- | --- | --- |"]
        for name, status, evidence, path, results in rows:
            link = f"https://github.com/{REPOS[manager]}/blob/{sha}/{path.relative_to(root).as_posix()}"
            cells = [f"[{escape(name)}]({link})", status]
            if results is not None:
                cells += [{True: "允许", False: "排除", None: "未知"}[value] for value in results]
            cells.append(escape(evidence))
            document.append("| " + " | ".join(cells) + " |")
        (args.output / f"{manager}.md").write_text("\n".join(document) + "\n", encoding="utf-8")
        print(f"{manager}: {len(rows)} entries; {dict(counts)}")
    index += ["", "## 实际编译结果", "",
              "现有 Android C/C++ Libraries 与 Android Cross-Platform Build 工作流负责实际编译 xmake/Conan 库，详见各次运行的 Summary 与 dist artifact。",
              "本报告尚不含 vcpkg 编译结果，也不将既有手工 manifest 视为全量支持清单。"]
    (args.output / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
