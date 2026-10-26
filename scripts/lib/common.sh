#!/usr/bin/env bash
# 公共函数库：路径、日志、NDK 解析、ABI 映射等。
# 该文件只应被 source，不直接执行。
# shellcheck shell=bash

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MANIFEST="${MANIFEST:-$REPO_ROOT/libraries/manifest.json}"
MANIFEST_TOOL="$REPO_ROOT/scripts/lib/manifest.py"
PYTHON="${PYTHON:-python3}"

log() {
    printf '\033[1;34m[%s]\033[0m %s\n' "$(date +%H:%M:%S)" "$*"
}

warn() {
    printf '\033[1;33m[warn]\033[0m %s\n' "$*" >&2
}

err() {
    printf '\033[1;31m[error]\033[0m %s\n' "$*" >&2
}

die() {
    err "$*"
    exit 1
}

have() {
    command -v "$1" >/dev/null 2>&1
}

# 去掉 xmake 等工具输出中的 ANSI 颜色控制符，避免污染 CI summary。
strip_ansi() {
    sed -E 's/\x1b\[[0-9;]*[[:alpha:]]//g'
}

require_file() {
    [ -f "$1" ] || die "缺少文件: $1"
}

require_dir() {
    [ -d "$1" ] || die "缺少目录: $1"
}

require_python() {
    if ! have "$PYTHON"; then
        if is_windows_shell && have python; then
            PYTHON="python"
        elif have python3; then
            PYTHON="python3"
        elif have python; then
            PYTHON="python"
        else
            die "需要 Python 3（找不到 python3/python）"
        fi
    fi
    "$PYTHON" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)' \
        || die "需要 Python >= 3.8"
}

manifest() {
    require_python
    "$PYTHON" "$MANIFEST_TOOL" --manifest "$MANIFEST" "$@"
}

manifest_default() {
    manifest defaults --field "$1"
}

# 统一路径分隔符：Windows 宿主生成的 NDK 路径可能包含反斜杠，
# 传给 xmake / Conan / CMake 时使用正斜杠更稳定。
normalize_path() {
    printf '%s' "${1//\\//}"
}

# 判断一个目录是否是合法的 NDK 根目录。
is_ndk_dir() {
    [ -n "${1:-}" ] && [ -d "$1/toolchains/llvm/prebuilt" ]
}

# 打印 NDK 当前平台的 host tag，例如 linux-x86_64。
android_ndk_host_tag() {
    case "$(uname -s)" in
        Linux*) echo "linux-x86_64" ;;
        Darwin*) echo "darwin-x86_64" ;;
        MINGW* | MSYS* | CYGWIN*) echo "windows-x86_64" ;;
        *) echo "linux-x86_64" ;;
    esac
}

is_windows_shell() {
    case "$(uname -s)" in
        MINGW* | MSYS* | CYGWIN*) return 0 ;;
        *) return 1 ;;
    esac
}

# 在某个目录下按版本倒序列出子目录（GNU sort 不可用时退化为普通倒序）。
_list_version_dirs() {
    local base="$1"
    [ -d "$base" ] || return 0
    if sort -V </dev/null >/dev/null 2>&1; then
        find "$base" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | sort -V -r
    else
        find "$base" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | sort -r
    fi
}

# 解析 Android NDK，优先级：
#   --ndk / ANDROID_NDK > ANDROID_NDK_HOME > ANDROID_NDK_ROOT > ANDROID_NDK_LATEST_HOME
#   > $ANDROID_HOME/ndk/* > $ANDROID_SDK_ROOT/ndk/*
# 只在 stdout 输出路径，日志写入 stderr。
resolve_ndk() {
    local explicit="${1:-}"

    if [ -n "$explicit" ]; then
        is_ndk_dir "$explicit" || die "--ndk 不是合法 NDK 目录: $explicit"
        printf '%s\n' "$(normalize_path "$explicit")"
        return 0
    fi

    local var value
    for var in ANDROID_NDK ANDROID_NDK_HOME ANDROID_NDK_ROOT ANDROID_NDK_LATEST_HOME; do
        value="${!var:-}"
        if is_ndk_dir "$value"; then
            printf '%s\n' "$(normalize_path "$value")"
            return 0
        fi
    done

    local sdk candidate
    for sdk in "${ANDROID_HOME:-}" "${ANDROID_SDK_ROOT:-}"; do
        [ -n "$sdk" ] || continue
        while IFS= read -r candidate; do
            if is_ndk_dir "$candidate"; then
                printf '%s\n' "$(normalize_path "$candidate")"
                return 0
            fi
        done < <(_list_version_dirs "$sdk/ndk")
    done

    return 1
}

# 返回 NDK 中的 clang 可执行文件路径。
android_ndk_clang() {
    local ndk="$1"
    local tag candidate
    tag="$(android_ndk_host_tag)"
    for candidate in \
        "$ndk/toolchains/llvm/prebuilt/$tag/bin/clang" \
        "$ndk/toolchains/llvm/prebuilt/$tag/bin/clang.exe"; do
        if [ -x "$candidate" ]; then
            printf '%s\n' "$(normalize_path "$candidate")"
            return 0
        fi
    done
    candidate="$(find "$ndk/toolchains/llvm/prebuilt" -type f \( -name clang -o -name clang.exe \) -perm -u+x 2>/dev/null | head -n 1)"
    [ -n "$candidate" ] || return 1
    printf '%s\n' "$(normalize_path "$candidate")"
}

# 获取 NDK clang 的主版本号，例如 18。
android_ndk_clang_major() {
    local clang="$1"
    "$clang" --version 2>/dev/null \
        | sed -n '1s/.*[Cc]lang version \([0-9][0-9]*\).*/\1/p' \
        | head -n 1
}

# xmake 直接使用 ABI 名称作为 -a 参数。
abi_to_xmake_arch() {
    case "$1" in
        arm64-v8a | armeabi-v7a | x86 | x86_64) printf '%s\n' "$1" ;;
        *) die "xmake 不支持的 ABI: $1" ;;
    esac
}

# Conan 2 的 Android arch 名称。
abi_to_conan_arch() {
    case "$1" in
        arm64-v8a) echo "armv8" ;;
        armeabi-v7a) echo "armv7" ;;
        x86) echo "x86" ;;
        x86_64) echo "x86_64" ;;
        *) die "Conan 不支持的 ABI: $1" ;;
    esac
}

conan_profile_name() {
    printf 'android-%s\n' "$1"
}

conan_home() {
    if [ -n "${CONAN_HOME:-}" ]; then
        printf '%s\n' "$CONAN_HOME"
    else
        printf '%s\n' "${HOME}/.conan2"
    fi
}

split_csv() {
    # 输出换行分隔，去掉空白与空项
    printf '%s' "$1" | tr ',' '\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | sed '/^$/d'
}

append_path_if_dir() {
    local dir="$1"
    [ -d "$dir" ] || return 0
    case ":${PATH}:" in
        *":${dir}:"*) ;;
        *) export PATH="${dir}:${PATH}" ;;
    esac
    if [ -n "${GITHUB_PATH:-}" ]; then
        if is_windows_shell && have cygpath; then
            cygpath -w "$dir" >>"$GITHUB_PATH"
        else
            printf '%s\n' "$dir" >>"$GITHUB_PATH"
        fi
    fi
}

# setup.sh 作为子进程运行时，其 PATH 修改不会自动传给父进程。
# 构建脚本与平台入口调用该函数，把已知的工具链目录加入当前 PATH。
add_toolchain_paths() {
    append_path_if_dir "$HOME/.local/bin"
    append_path_if_dir "$HOME/xmake"
    append_path_if_dir "${LOCALAPPDATA:-$HOME/AppData/Local}/Programs/xmake"

    local venv="${CONAN_VENV:-$HOME/.local/share/android-c-cpp-library/conan-venv}"
    if is_windows_shell; then
        append_path_if_dir "$venv/Scripts"
    else
        append_path_if_dir "$venv/bin"
    fi

    hash -r 2>/dev/null || true
}

# 在 GitHub Actions 中把 Markdown 追加到当前 job 的 summary。
append_github_summary() {
    local file="$1"
    [ -f "$file" ] || return 0
    if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
        cat "$file" >>"$GITHUB_STEP_SUMMARY"
    fi
}

# 让 tee 保留管道中命令的退出码。
run_logged() {
    local log_file="$1"
    shift
    mkdir -p "$(dirname "$log_file")"
    if "$@" 2>&1 | tee -a "$log_file"; then
        return 0
    fi
    return 1
}

# 打印日志尾部，便于 CI 快速定位失败原因。
print_log_tail() {
    local log_file="$1"
    local lines="${2:-40}"
    [ -f "$log_file" ] || return 0
    err "最近 ${lines} 行日志（${log_file}）："
    tail -n "$lines" "$log_file" >&2 || true
}
