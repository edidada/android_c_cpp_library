#!/usr/bin/env bash
# 使用 xmake 为 Android 编译 libevent 等库（固定 target = Android）。
# 默认编译 presets.core，可通过 --libs 覆盖。
#
# 示例:
#   scripts/android/xmake/build.sh
#   scripts/android/xmake/build.sh --libs libevent,zlib --abis arm64-v8a
#   scripts/android/xmake/build.sh --libs all --abis arm64-v8a,armeabi-v7a
#
# shellcheck source=../../lib/common.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../../lib/common.sh"

usage() {
    cat <<'EOF'
用法: scripts/android/xmake/build.sh [选项]

固定使用 xmake 后端，目标平台为 Android，默认编译 presets.core。

选项:
  --libs LIST           core（默认）/ all / 逗号分隔的库名或 preset
  其余参数直接透传给 scripts/build.sh:
  --abis LIST --api LEVEL --build-type TYPE --experimental MODE
  --ndk PATH --jobs N --out DIR --clean --fail-fast --no-header-check
EOF
}

libs="core"
build_args=()
while [ $# -gt 0 ]; do
    case "$1" in
        --libs)
            [ $# -ge 2 ] || die "--libs 需要一个参数"
            libs="$2"
            shift 2
            ;;
        --backends)
            die "该脚本固定使用 xmake，请不要再传 --backends"
            ;;
        -h | --help)
            usage
            exit 0
            ;;
        *)
            build_args+=("$1")
            shift
            ;;
    esac
done

exec bash "$REPO_ROOT/scripts/build.sh" \
    --libs "$libs" \
    --backends xmake \
    ${build_args[@]+"${build_args[@]}"}
