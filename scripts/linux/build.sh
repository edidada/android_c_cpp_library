#!/usr/bin/env bash
# Linux 宿主机 -> Android 交叉编译入口。
# 默认编译 presets.core 中的常用库，最终产物为 Android 静态库。
#
# shellcheck source=../lib/platform.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../lib/platform.sh"

platform_build linux "$@"
