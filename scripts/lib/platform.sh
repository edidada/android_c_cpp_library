#!/usr/bin/env bash
# 平台入口公共实现：scripts/linux|mac|win/build.sh 调用 platform_build。
# 这些脚本只作为宿主环境的入口，最终目标平台固定为 Android。
# shellcheck shell=bash

# shellcheck source=common.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/common.sh"

platform_usage() {
    cat <<'EOF'
用法: scripts/<linux|mac|win>/build.sh [选项]

说明:
  在 Linux / macOS / Windows(Git Bash) 宿主机上交叉编译 Android 库。
  默认编译 manifest 中 presets.core 的常用库，目标为 Android。

选项:
  --libs LIST           core（默认）/ all / 逗号分隔的库名或 preset
  --backends LIST       all（默认）/ xmake / conan / xmake,conan
  --abis LIST           逗号分隔的 ABI，默认取清单 defaults.abis
  --api LEVEL           Android API level，默认取清单 defaults.androidApi
  --build-type TYPE     Release（默认）/ Debug / RelWithDebInfo / MinSizeRel
  --experimental MODE   all（默认）/ stable / only
  --ndk PATH            指定 NDK 根目录
  --jobs N              并行编译任务数
  --out DIR             产物目录，默认 dist/
  --clean               构建前删除 dist/ 与 build/
  --fail-fast           任一库失败后立即停止
  --no-header-check     探针不 include 头文件
  --skip-setup          跳过 xmake/Conan/NDK profile 初始化
  -h, --help            显示帮助
EOF
}

platform_build() {
    local platform="$1"
    shift

    local libs="core"
    local backends="all"
    local abis=""
    local api=""
    local build_type=""
    local experimental="all"
    local ndk=""
    local jobs=""
    local out=""
    local clean=0
    local fail_fast=0
    local header_check=1
    local skip_setup=0

    while [ $# -gt 0 ]; do
        case "$1" in
            --libs) [ $# -ge 2 ] || die "--libs 需要一个参数"; libs="$2"; shift 2 ;;
            --backends) [ $# -ge 2 ] || die "--backends 需要一个参数"; backends="$2"; shift 2 ;;
            --abis) [ $# -ge 2 ] || die "--abis 需要一个参数"; abis="$2"; shift 2 ;;
            --api) [ $# -ge 2 ] || die "--api 需要一个参数"; api="$2"; shift 2 ;;
            --build-type) [ $# -ge 2 ] || die "--build-type 需要一个参数"; build_type="$2"; shift 2 ;;
            --experimental) [ $# -ge 2 ] || die "--experimental 需要一个参数"; experimental="$2"; shift 2 ;;
            --ndk) [ $# -ge 2 ] || die "--ndk 需要一个参数"; ndk="$2"; shift 2 ;;
            --jobs) [ $# -ge 2 ] || die "--jobs 需要一个参数"; jobs="$2"; shift 2 ;;
            --out) [ $# -ge 2 ] || die "--out 需要一个参数"; out="$2"; shift 2 ;;
            --clean) clean=1; shift ;;
            --fail-fast) fail_fast=1; shift ;;
            --no-header-check) header_check=0; shift ;;
            --skip-setup) skip_setup=1; shift ;;
            -h | --help) platform_usage; exit 0 ;;
            *) die "未知参数: $1（使用 --help 查看用法）" ;;
        esac
    done

    local system
    system="$(uname -s)"
    case "$platform" in
        linux)
            [ "$system" = "Linux" ] || die "scripts/linux/build.sh 只能在 Linux 上运行（当前: $system）"
            ;;
        mac)
            [ "$system" = "Darwin" ] || die "scripts/mac/build.sh 只能在 macOS 上运行（当前: $system）"
            ;;
        win)
            is_windows_shell || die "scripts/win/build.sh 需要在 Windows 的 Git Bash 中运行（当前: $system）"
            # Git Bash 下 python3 可能是 Microsoft Store 别名，优先使用 python。
            if have python; then
                export PYTHON=python
            fi
            ;;
        *)
            die "未知平台: $platform"
            ;;
    esac

    [ -n "$abis" ] || abis="$(manifest_default abis)"
    [ -n "$api" ] || api="$(manifest_default androidApi)"
    [ -n "$build_type" ] || build_type="$(manifest_default buildType)"

    log "宿主平台: $platform ($system)"
    log "目标平台: Android"
    log "库: $libs"
    log "后端: $backends"
    log "ABI: $abis"
    log "API level: $api"

    # 如果工具已安装在默认目录，先加入 PATH，方便 setup 复用。
    add_toolchain_paths

    if [ "$skip_setup" -eq 0 ]; then
        local -a setup_args=(--backends "$backends" --abis "$abis" --api "$api")
        if [ -n "$ndk" ]; then
            setup_args+=(--ndk "$ndk")
        fi
        if [ -n "$build_type" ]; then
            setup_args+=(--build-type "$build_type")
        fi
        log "初始化 xmake / Conan 2 / Android NDK 环境..."
        bash "$REPO_ROOT/scripts/setup.sh" "${setup_args[@]}"
    fi

    # setup.sh 在子进程中运行，重新把安装目录加入当前 PATH。
    add_toolchain_paths

    local -a build_args=(
        --libs "$libs"
        --backends "$backends"
        --abis "$abis"
        --api "$api"
        --experimental "$experimental"
    )
    if [ -n "$ndk" ]; then
        build_args+=(--ndk "$ndk")
    fi
    if [ -n "$build_type" ]; then
        build_args+=(--build-type "$build_type")
    fi
    if [ -n "$jobs" ]; then
        build_args+=(--jobs "$jobs")
    fi
    if [ -n "$out" ]; then
        build_args+=(--out "$out")
    fi
    if [ "$clean" -eq 1 ]; then
        build_args+=(--clean)
    fi
    if [ "$fail_fast" -eq 1 ]; then
        build_args+=(--fail-fast)
    fi
    if [ "$header_check" -eq 0 ]; then
        build_args+=(--no-header-check)
    fi

    log "开始交叉编译 Android 库..."
    bash "$REPO_ROOT/scripts/build.sh" "${build_args[@]}"
}
