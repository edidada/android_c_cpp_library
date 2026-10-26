#!/usr/bin/env bash
# Windows(Git Bash) 宿主机 -> Android 交叉编译入口。
# 默认编译 presets.core 中的常用库，最终产物为 Android 静态库。
#
# 在 Windows 上请使用 Git Bash 运行，例如:
#   "C:\Program Files\Git\bin\bash.exe" scripts/win/build.sh
#
# shellcheck source=../lib/platform.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../lib/platform.sh"

platform_build win "$@"
