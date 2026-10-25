#!/usr/bin/env bash
# 在 Linux（GitHub Actions / 本地）安装并初始化 xmake + Conan 2 的 Android 交叉编译环境。
#
# 示例:
#   scripts/setup.sh --abis arm64-v8a --api 21
#   scripts/setup.sh --ndk /opt/android-ndk-r27c
#   scripts/setup.sh --backends xmake
#
# shellcheck source=lib/common.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/common.sh"

usage() {
    cat <<'EOF'
用法: scripts/setup.sh [选项]

选项:
  --backends LIST        all（默认）/ xmake / conan / xmake,conan
  --abis LIST            逗号分隔的 ABI，默认取清单 defaults.abis
  --api LEVEL            Android API level，默认取清单 defaults.androidApi（21）
  --build-type TYPE      Release（默认）/ Debug / RelWithDebInfo / MinSizeRel
  --ndk PATH             指定 NDK 根目录
  --ndk-version VERSION  找不到 NDK 时通过 sdkmanager 安装，例如 27.2.12479018
  --conan-version VER    指定 Conan 版本，默认安装最新的 Conan 2.x
  --force                强制重新生成 Conan profile
  --skip-profiles        只安装工具，不生成 Android Conan profiles
  -h, --help             显示帮助

环境变量:
  ANDROID_NDK / ANDROID_NDK_HOME / ANDROID_NDK_ROOT / ANDROID_NDK_LATEST_HOME
                         用于定位 NDK
  ANDROID_HOME / ANDROID_SDK_ROOT
                         用于在 $SDK/ndk/* 下查找 NDK
  CONAN_HOME             默认 ~/.conan2
  CONAN_VENV             未安装 Conan 2 时创建的虚拟环境路径
  CONAN_ANDROID_STL      Android C++ STL，默认 c++_static
EOF
}

backends="all"
abis=""
api=""
build_type=""
ndk_arg=""
ndk_version=""
conan_version=""
force=0
skip_profiles=0

while [ $# -gt 0 ]; do
    case "$1" in
        --backends) [ $# -ge 2 ] || die "--backends 需要一个参数"; backends="$2"; shift 2 ;;
        --abis) [ $# -ge 2 ] || die "--abis 需要一个参数"; abis="$2"; shift 2 ;;
        --api) [ $# -ge 2 ] || die "--api 需要一个参数"; api="$2"; shift 2 ;;
        --build-type) [ $# -ge 2 ] || die "--build-type 需要一个参数"; build_type="$2"; shift 2 ;;
        --ndk) [ $# -ge 2 ] || die "--ndk 需要一个参数"; ndk_arg="$2"; shift 2 ;;
        --ndk-version) [ $# -ge 2 ] || die "--ndk-version 需要一个参数"; ndk_version="$2"; shift 2 ;;
        --conan-version) [ $# -ge 2 ] || die "--conan-version 需要一个参数"; conan_version="$2"; shift 2 ;;
        --force) force=1; shift ;;
        --skip-profiles) skip_profiles=1; shift ;;
        -h | --help) usage; exit 0 ;;
        *) die "未知参数: $1（使用 --help 查看用法）" ;;
    esac
done

require_file "$MANIFEST"
require_python

[ -n "$abis" ] || abis="$(manifest_default abis)"
[ -n "$api" ] || api="$(manifest_default androidApi)"
[ -n "$build_type" ] || build_type="$(manifest_default buildType)"

want_xmake=0
want_conan=0
case "$backends" in
    all) want_xmake=1; want_conan=1 ;;
    xmake) want_xmake=1 ;;
    conan) want_conan=1 ;;
    *)
        if printf '%s' "$backends" | tr ',' '\n' | grep -qx xmake; then want_xmake=1; fi
        if printf '%s' "$backends" | tr ',' '\n' | grep -qx conan; then want_conan=1; fi
        [ "$want_xmake" -eq 1 ] || [ "$want_conan" -eq 1 ] \
            || die "--backends 非法: $backends（可选 all, xmake, conan, xmake,conan）"
        ;;
esac

# ---------------------------------------------------------------- xmake

install_xmake() {
    if have xmake; then
        log "xmake 已安装: $(xmake --version 2>/dev/null | head -n 1 | strip_ansi)"
        return 0
    fi

    have curl || die "安装 xmake 需要 curl"
    log "安装 xmake（官方安装脚本）..."
    local script
    script="$(mktemp)"
    curl -fsSL https://xmake.io/shget.text -o "$script" || die "下载 xmake 安装脚本失败"
    # shellcheck disable=SC1090
    bash "$script" || die "xmake 安装失败"
    rm -f "$script"

    append_path_if_dir "$HOME/.local/bin"
    hash -r
    have xmake || die "xmake 安装后仍找不到命令，请检查 \$HOME/.local/bin 是否在 PATH 中"
    log "xmake 安装完成: $(xmake --version 2>/dev/null | head -n 1 | strip_ansi)"
}

# ---------------------------------------------------------------- Conan 2

install_conan() {
    if have conan && conan --version 2>/dev/null | grep -q '^Conan version 2\.'; then
        log "Conan 已安装: $(conan --version 2>/dev/null)"
        return 0
    fi

    have "$PYTHON" || die "安装 Conan 需要 Python 3"
    local venv="${CONAN_VENV:-$HOME/.local/share/android-c-cpp-library/conan-venv}"
    local spec="conan>=2,<3"
    [ -n "$conan_version" ] && spec="conan==$conan_version"

    log "在虚拟环境中安装 Conan 2: $venv"
    "$PYTHON" -m venv "$venv" || die "创建 Python venv 失败: $venv"
    "$venv/bin/python" -m pip install --upgrade pip >/dev/null
    "$venv/bin/python" -m pip install --upgrade "$spec" || die "安装 $spec 失败"

    append_path_if_dir "$venv/bin"
    hash -r
    have conan || die "Conan 安装后仍找不到命令"
    conan --version 2>/dev/null | grep -q '^Conan version 2\.' \
        || die "当前 Conan 不是 2.x，请检查 PATH 中是否有旧版 conan"
    log "Conan 安装完成: $(conan --version 2>/dev/null)"
}

ensure_conan_remote() {
    if ! conan remote list 2>/dev/null | grep -q '^conancenter'; then
        log "添加 ConanCenter remote..."
        conan remote add conancenter https://center2.conan.io --force
    fi
}

ensure_conan_default_profile() {
    if ! conan profile show -pr:b=default >/dev/null 2>&1; then
        log "生成 Conan 默认 build profile..."
        conan profile detect --force
    fi
}

install_ndk_with_sdkmanager() {
    local sdk_manager=""
    local sdk
    for sdk in "${ANDROID_HOME:-}" "${ANDROID_SDK_ROOT:-}"; do
        [ -n "$sdk" ] || continue
        if [ -x "$sdk/cmdline-tools/latest/bin/sdkmanager" ]; then
            sdk_manager="$sdk/cmdline-tools/latest/bin/sdkmanager"
            break
        fi
    done

    if [ -z "$sdk_manager" ]; then
        warn "找不到 sdkmanager，无法自动安装 NDK ${ndk_version}"
        return 1
    fi

    log "通过 sdkmanager 安装 NDK ${ndk_version}（可能需要几分钟）..."
    set +o pipefail
    yes | "$sdk_manager" --install "ndk;${ndk_version}" >/dev/null
    local status=$?
    set -o pipefail
    return "$status"
}

# ---------------------------------------------------------------- profiles

write_conan_profile() {
    local abi="$1"
    local compiler_version="$2"
    local profile_dir
    profile_dir="$(conan_home)/profiles"
    mkdir -p "$profile_dir"

    cat >"$profile_dir/$(conan_profile_name "$abi")" <<EOF
# Generated by scripts/setup.sh -- do not edit manually.
[settings]
os=Android
arch=$(abi_to_conan_arch "$abi")
compiler=clang
compiler.version=${compiler_version}
compiler.libcxx=${CONAN_ANDROID_STL:-c++_static}
build_type=${build_type}
os.api_level=${api}
[conf]
tools.android:ndk_path=${ndk}
EOF
}

generate_conan_profiles() {
    local clang clang_major abi version
    clang="$(android_ndk_clang "$ndk")" || die "NDK 中找不到 clang: $ndk"
    clang_major="$(android_ndk_clang_major "$clang")"
    [ -n "$clang_major" ] || die "无法识别 NDK clang 版本: $clang"
    log "NDK clang 主版本: $clang_major"

    for abi in $(split_csv "$abis"); do
        abi_to_conan_arch "$abi" >/dev/null

        if [ "$force" -eq 0 ] && [ -f "$(conan_home)/profiles/$(conan_profile_name "$abi")" ]; then
            log "Conan profile 已存在: $(conan_profile_name "$abi")（--force 可覆盖）"
            continue
        fi

        # Conan 的 settings.yml 未必立即支持最新 clang，逐级回退到可用的版本。
        version="$clang_major"
        while [ "$version" -ge 14 ]; do
            write_conan_profile "$abi" "$version"
            if conan profile show -pr:h="$(conan_profile_name "$abi")" >/dev/null 2>&1; then
                log "生成 Conan profile: $(conan_profile_name "$abi")（clang $version, API $api）"
                break
            fi
            warn "Conan settings 不支持 clang $version，尝试 $((version - 1))"
            version=$((version - 1))
        done

        if [ "$version" -lt 14 ]; then
            die "无法为 ABI $abi 生成 Conan profile：Conan 不支持 NDK clang $clang_major 及更低的版本"
        fi
    done
}

# ---------------------------------------------------------------- main

log "仓库根目录: $REPO_ROOT"
log "目标 ABI: $abis"
log "Android API level: $api"
log "构建类型: $build_type"

if [ "$want_xmake" -eq 1 ]; then
    install_xmake
fi
if [ "$want_conan" -eq 1 ]; then
    install_conan
fi

if [ "$skip_profiles" -eq 0 ]; then
    if [ -n "$ndk_arg" ]; then
        ndk="$(resolve_ndk "$ndk_arg")"
    else
        ndk="$(resolve_ndk "" || true)"
    fi
    if [ -z "$ndk" ] && [ -n "$ndk_version" ]; then
        install_ndk_with_sdkmanager || true
        ndk="$(resolve_ndk "" || true)"
    fi
    [ -n "$ndk" ] || die "未找到 Android NDK。
请安装 NDK 后设置 ANDROID_NDK_HOME，或使用:
  scripts/setup.sh --ndk /path/to/ndk
  scripts/setup.sh --ndk-version 27.2.12479018"

    export ANDROID_NDK_HOME="$ndk"
    log "Android NDK: $ndk"

    if [ "$want_conan" -eq 1 ]; then
        ensure_conan_remote
        ensure_conan_default_profile
        generate_conan_profiles
    fi
fi

log "环境准备完成"
if have xmake; then
    log "  xmake: $(xmake --version 2>/dev/null | head -n 1 | strip_ansi)"
fi
if have conan; then
    log "  conan: $(conan --version 2>/dev/null)"
fi
if [ -n "${ndk:-}" ]; then
    log "  ndk:   $ndk"
fi
