#!/usr/bin/env bash
# 为 Android 交叉编译清单中的 C/C++ 库（xmake 与 Conan 2 两种后端）。
#
# 示例:
#   scripts/build.sh                                        # 全部库 × 默认 ABI
#   scripts/build.sh --libs zlib,openssl --abis arm64-v8a
#   scripts/build.sh --backends conan --libs all
#   scripts/build.sh --libs ffmpeg --abis arm64-v8a,armeabi-v7a --fail-fast
#
# shellcheck source=lib/common.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/lib/common.sh"

usage() {
    cat <<'EOF'
用法: scripts/build.sh [选项]

选项:
  --libs LIST           all（默认）、core 或逗号分隔的库名 / preset
  --backends LIST       all（默认）/ xmake / conan / xmake,conan
  --abis LIST           逗号分隔的 ABI，默认取清单 defaults.abis
  --api LEVEL           Android API level，默认取清单 defaults.androidApi
  --build-type TYPE     Release（默认）/ Debug / RelWithDebInfo / MinSizeRel
  --experimental MODE   all（默认）/ stable（排除实验库）/ only（仅实验库）
  --ndk PATH            指定 NDK 根目录
  --jobs N              并行编译任务数，默认 CPU 核数
  --out DIR             产物目录，默认 dist/
  --clean               构建前删除 dist/ 与 build/
  --fail-fast           任一库失败后立即停止
  --no-header-check     探针不 include 头文件（只验证包能编译）
  -h, --help            显示帮助

环境变量:
  ANDROID_NDK / ANDROID_NDK_HOME / ANDROID_NDK_ROOT / ANDROID_NDK_LATEST_HOME
  DIST_DIR / WORK_DIR   自定义产物目录 / 临时构建目录
  GITHUB_STEP_SUMMARY   GitHub Actions 会追加构建摘要
EOF
}

libs="all"
backends="all"
abis=""
api=""
build_type=""
experimental="all"
ndk_arg=""
jobs=""
dist_dir="${DIST_DIR:-$REPO_ROOT/dist}"
work_root="${WORK_DIR:-$REPO_ROOT/build}"
clean=0
fail_fast=0
header_check=1

while [ $# -gt 0 ]; do
    case "$1" in
        --libs) [ $# -ge 2 ] || die "--libs 需要一个参数"; libs="$2"; shift 2 ;;
        --backends) [ $# -ge 2 ] || die "--backends 需要一个参数"; backends="$2"; shift 2 ;;
        --abis) [ $# -ge 2 ] || die "--abis 需要一个参数"; abis="$2"; shift 2 ;;
        --api) [ $# -ge 2 ] || die "--api 需要一个参数"; api="$2"; shift 2 ;;
        --build-type) [ $# -ge 2 ] || die "--build-type 需要一个参数"; build_type="$2"; shift 2 ;;
        --experimental) [ $# -ge 2 ] || die "--experimental 需要一个参数"; experimental="$2"; shift 2 ;;
        --ndk) [ $# -ge 2 ] || die "--ndk 需要一个参数"; ndk_arg="$2"; shift 2 ;;
        --jobs) [ $# -ge 2 ] || die "--jobs 需要一个参数"; jobs="$2"; shift 2 ;;
        --out) [ $# -ge 2 ] || die "--out 需要一个参数"; dist_dir="$2"; shift 2 ;;
        --clean) clean=1; shift ;;
        --fail-fast) fail_fast=1; shift ;;
        --no-header-check) header_check=0; shift ;;
        -h | --help) usage; exit 0 ;;
        *) die "未知参数: $1（使用 --help 查看用法）" ;;
    esac
done

require_file "$MANIFEST"
require_python
manifest validate >/dev/null

# 兼容 setup.sh 在子进程安装工具后 PATH 未传递到当前 shell 的情况。
add_toolchain_paths

case "$dist_dir" in
    /*) ;;
    *) dist_dir="$REPO_ROOT/$dist_dir" ;;
esac
case "$work_root" in
    /*) ;;
    *) work_root="$REPO_ROOT/$work_root" ;;
esac

[ -n "$abis" ] || abis="$(manifest_default abis)"
[ -n "$api" ] || api="$(manifest_default androidApi)"
[ -n "$build_type" ] || build_type="$(manifest_default buildType)"
[ -n "$jobs" ] || jobs="$(getconf _NPROCESSORS_ONLN 2>/dev/null || echo 2)"

case "$build_type" in
    Release | Debug | RelWithDebInfo | MinSizeRel) ;;
    *) die "--build-type 非法: $build_type" ;;
esac
case "$api" in
    '' | *[!0-9]*) die "--api 必须是整数: $api" ;;
esac
[ "$api" -ge 21 ] || die "--api 必须 >= 21"

if [ "$clean" -eq 1 ]; then
    log "清理: $dist_dir, $work_root"
    rm -rf "$dist_dir" "$work_root"
fi

mkdir -p "$dist_dir" "$work_root"

if printf '%s' "$backends" | tr ',' '\n' | grep -qx xmake || [ "$backends" = "all" ]; then
    have xmake || die "找不到 xmake，请先运行 scripts/setup.sh"
fi
if printf '%s' "$backends" | tr ',' '\n' | grep -qx conan || [ "$backends" = "all" ]; then
    have conan || die "找不到 conan，请先运行 scripts/setup.sh"
fi

if [ -n "$ndk_arg" ]; then
    ndk="$(resolve_ndk "$ndk_arg")"
else
    ndk="$(resolve_ndk "" || true)"
fi
[ -n "$ndk" ] || die "未找到 Android NDK，请设置 ANDROID_NDK_HOME 或使用 --ndk"

if printf '%s' "$backends" | tr ',' '\n' | grep -qx conan || [ "$backends" = "all" ]; then
    for abi in $(split_csv "$abis"); do
        abi_to_conan_arch "$abi" >/dev/null
        profile="$(conan_home)/profiles/$(conan_profile_name "$abi")"
        [ -f "$profile" ] || die "缺少 Conan profile: $profile
请先运行: scripts/setup.sh --abis $abis --api $api"
    done
fi

log "NDK: $ndk"
log "ABI: $abis"
log "API level: $api"
log "构建类型: $build_type"
log "后端: $backends"
log "并行任务: $jobs"

log "待编译库列表:"
manifest list --format table --libs "$libs" --backends "$backends" --experimental "$experimental"

# ------------------------------------------------------------------ helpers

to_lua_value() {
    local value="$1"
    case "$value" in
        true | false) printf '%s' "$value" ;;
        nil) printf 'nil' ;;
        *)
            if [[ "$value" =~ ^-?[0-9]+([.][0-9]+)?$ ]]; then
                printf '%s' "$value"
            else
                value="${value//\\/\\\\}"
                value="${value//\"/\\\"}"
                printf '"%s"' "$value"
            fi
            ;;
    esac
}

render_lua_configs() {
    local configs="$1"
    [ -n "$configs" ] || return 0
    local pair key value rendered="" sep=""
    local -a pairs
    IFS=';' read -r -a pairs <<<"$configs"
    for pair in "${pairs[@]}"; do
        [ -n "$pair" ] || continue
        key="${pair%%=*}"
        value="${pair#*=}"
        rendered+="${sep}${key} = $(to_lua_value "$value")"
        sep=", "
    done
    printf '%s' "$rendered"
}

write_probe_project() {
    local dir="$1"
    local xmake_pkg="$2"
    local xmake_version="$3"
    local xmake_configs="$4"
    local headers="$5"
    local defines="$6"
    local package_spec="$xmake_pkg"
    local lua_configs=""
    local repo_root_lua

    repo_root_lua="${REPO_ROOT//\\//}"
    repo_root_lua="${repo_root_lua//\"/\\\"}"

    if [ -n "$xmake_version" ]; then
        package_spec="$xmake_pkg $xmake_version"
    fi
    if [ -n "$xmake_configs" ]; then
        lua_configs="$(render_lua_configs "$xmake_configs")"
        lua_configs=", {configs = {${lua_configs}}}"
    fi

    {
        printf 'add_repositories("android-libs scripts/android/xmake/repo", {rootdir = "%s"})\n' "$repo_root_lua"
        printf 'add_rules("mode.release")\n'
        printf 'add_requires("%s"%s)\n\n' "$package_spec" "$lua_configs"
        printf 'target("probe")\n'
        printf '    set_kind("static")\n'
        printf '    add_files("probe.cpp")\n'
        printf '    set_languages("c++17")\n'
        printf '    add_packages("%s")\n' "$xmake_pkg"
    } >"$dir/xmake.lua"

    {
        echo "// Generated by scripts/build.sh -- only used to verify the package."
        if [ -n "$defines" ]; then
            local define dname dvalue
            for define in $(split_csv "$defines"); do
                dname="${define%%=*}"
                dvalue=""
                case "$define" in
                    *=*) dvalue="${define#*=}" ;;
                esac
                echo "#ifndef $dname"
                if [ -n "$dvalue" ]; then
                    echo "#define $dname $dvalue"
                else
                    echo "#define $dname"
                fi
                echo "#endif"
            done
        fi
        if [ "$header_check" -eq 1 ] && [ -n "$headers" ]; then
            local header
            for header in $(split_csv "$headers"); do
                echo "#include <$header>"
            done
        fi
        echo "int android_library_probe() { return 0; }"
    } >"$dir/probe.cpp"
}

build_with_xmake() {
    local name="$1" abi="$2" lib_api="$3"
    local xmake_pkg="$4" xmake_version="$5" xmake_configs="$6"
    local headers="$7" defines="$8"
    local work="$work_root/$name/$abi/xmake"
    local artifact="$dist_dir/$name/$abi/xmake"
    local log_file="$dist_dir/$name/logs/$abi-xmake.log"

    rm -rf "$work"
    mkdir -p "$work" "$artifact" "$(dirname "$log_file")"
    : >"$log_file"
    write_probe_project "$work" "$xmake_pkg" "$xmake_version" "$xmake_configs" "$headers" "$defines"

    log "[$name][$abi][xmake] 配置 (xmake 包: $xmake_pkg)"
    if ! run_logged "$log_file" \
        xmake f -y -P "$work" -p android -a "$abi" --ndk="$ndk" --ndk_sdkver="$lib_api" -m release -o "$work/build"; then
        print_log_tail "$log_file"
        return 1
    fi

    log "[$name][$abi][xmake] 编译"
    if ! run_logged "$log_file" xmake -y -P "$work" -j "$jobs"; then
        print_log_tail "$log_file"
        return 1
    fi

    log "[$name][$abi][xmake] 导出产物"
    if ! run_logged "$log_file" \
        xmake require --export --packagedir="$artifact" -P "$work" "$xmake_pkg"; then
        print_log_tail "$log_file"
        return 1
    fi

    touch "$artifact/.ok"
    return 0
}

build_with_conan() {
    local name="$1" abi="$2" lib_api="$3"
    local conan_ref="$4" conan_options="$5"
    local work="$work_root/$name/$abi/conan"
    local artifact="$dist_dir/$name/$abi/conan"
    local log_file="$dist_dir/$name/logs/$abi-conan.log"
    local profile
    local -a option_args=()
    local -a config_args=()

    # Bionic supplies pthreads in libc but has no pthread_cancel, so the
    # generic FindThreads libc probe fails for libevent on Android.
    if [ "$name" = "libevent" ]; then
        config_args+=(-c:h 'tools.cmake.cmaketoolchain:extra_variables={"CMAKE_HAVE_LIBC_PTHREAD": True}')
    fi

    profile="$(conan_profile_name "$abi")"
    rm -rf "$work"
    mkdir -p "$work" "$artifact" "$(dirname "$log_file")"
    : >"$log_file"

    if [ -n "$conan_options" ]; then
        local opt pkg_name="${conan_ref%%/*}"
        local -a options
        IFS=';' read -r -a options <<<"$conan_options"
        for opt in "${options[@]}"; do
            [ -n "$opt" ] || continue
            case "$opt" in
                *:*) ;;
                *) opt="$pkg_name:$opt" ;;
            esac
            option_args+=("-o" "$opt")
        done
    fi

    log "[$name][$abi][conan] 安装/编译 (引用: $conan_ref, API: $lib_api)"
    if ! run_logged "$log_file" \
        conan install --requires="$conan_ref" \
        -pr:h="$profile" -pr:b=default \
        -s:h "build_type=$build_type" \
        -s:h "os.api_level=$lib_api" \
        -c:h "tools.build:jobs=$jobs" \
        ${option_args[@]+"${option_args[@]}"} \
        ${config_args[@]+"${config_args[@]}"} \
        --build=missing \
        --deployer=full_deploy \
        --deployer-folder="$artifact" \
        -of "$work/out"; then
        print_log_tail "$log_file"
        return 1
    fi

    touch "$artifact/.ok"
    return 0
}

# ------------------------------------------------------------------ summary

write_summary() {
    local title="$1" status="$2"
    local summary_md="$dist_dir/$name/summary.md"
    local summary_tsv="$dist_dir/$name/summary.tsv"
    local xmake_version_text="n/a"
    local conan_version_text="n/a"

    if have xmake; then
        xmake_version_text="$(xmake --version 2>/dev/null | head -n 1 | strip_ansi)"
    fi
    if have conan; then
        conan_version_text="$(conan --version 2>/dev/null)"
    fi

    {
        echo "### Android 构建: $name ($title)"
        echo
        echo "- 结果: $status"
        echo "- NDK: \`$ndk\`"
        echo "- ABI: \`$abis\`"
        echo "- API level: ${api}（单库最低要求会取最大值）"
        echo "- 构建类型: $build_type"
        echo "- xmake: ${xmake_version_text}"
        echo "- Conan: ${conan_version_text}"
        echo
        echo "| ABI | 后端 | 状态 | 耗时 | 产物 |"
        echo "| --- | --- | --- | ---: | --- |"
        local row
        while IFS=$'\t' read -r _r_abi _r_backend _r_status _r_seconds _r_artifact _r_log; do
            local icon="✅"
            [ "$_r_status" = "ok" ] || icon="❌"
            echo "| $_r_abi | $_r_backend | $icon | ${_r_seconds}s | \`$_r_artifact\` |"
        done <"$summary_tsv"
    } >"$summary_md"

    cat "$summary_md"
    append_github_summary "$summary_md"
}

# ------------------------------------------------------------------ main loop

summary_tsv_root="$dist_dir/summary.tsv"
: >"$summary_tsv_root"

total=0
failed=0
skipped=0

while IFS=$'\x1f' read -r name title category is_experimental min_api xmake_pkg xmake_version xmake_configs conan_ref conan_options headers defines lib_backends; do
    [ -n "$name" ] || continue

    lib_dir="$dist_dir/$name"
    mkdir -p "$lib_dir/logs"
    lib_summary="$lib_dir/summary.tsv"
    : >"$lib_summary"

    lib_api="$api"
    if [ "$min_api" -gt "$lib_api" ]; then
        lib_api="$min_api"
    fi

    log "================================================================"
    log "编译 $name ($title) | ABI: $abis | 最低 API: $lib_api | 后端: $lib_backends"
    log "================================================================"

    lib_failed=0
    for abi in $(split_csv "$abis"); do
        abi_to_xmake_arch "$abi" >/dev/null
        if [ -n "$conan_ref" ]; then
            abi_to_conan_arch "$abi" >/dev/null
        fi

        for backend in $(split_csv "$lib_backends"); do
            total=$((total + 1))
            started="$(date +%s)"
            status="ok"

            case "$backend" in
                xmake)
                    [ -n "$xmake_pkg" ] || {
                        warn "$name 没有 xmake 包信息，跳过 $abi/xmake"
                        skipped=$((skipped + 1))
                        continue
                    }
                    if ! build_with_xmake "$name" "$abi" "$lib_api" \
                        "$xmake_pkg" "$xmake_version" "$xmake_configs" "$headers" "$defines"; then
                        status="failed"
                    fi
                    artifact="$dist_dir/$name/$abi/xmake"
                    log_file="$dist_dir/$name/logs/$abi-xmake.log"
                    ;;
                conan)
                    [ -n "$conan_ref" ] || {
                        warn "$name 没有 Conan 引用，跳过 $abi/conan"
                        skipped=$((skipped + 1))
                        continue
                    }
                    if ! build_with_conan "$name" "$abi" "$lib_api" "$conan_ref" "$conan_options"; then
                        status="failed"
                    fi
                    artifact="$dist_dir/$name/$abi/conan"
                    log_file="$dist_dir/$name/logs/$abi-conan.log"
                    ;;
                *)
                    warn "未知后端: $backend"
                    skipped=$((skipped + 1))
                    continue
                    ;;
            esac

            elapsed=$(($(date +%s) - started))
            printf '%s\t%s\t%s\t%s\t%s\t%s\n' \
                "$abi" "$backend" "$status" "$elapsed" "$artifact" "$log_file" >>"$lib_summary"
            printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
                "$name" "$abi" "$backend" "$status" "$elapsed" "$artifact" "$log_file" >>"$summary_tsv_root"

            if [ "$status" = "ok" ]; then
                log "[$name][$abi][$backend] 成功（${elapsed}s）"
            else
                err "[$name][$abi][$backend] 失败（${elapsed}s），日志: $log_file"
                lib_failed=1
                failed=$((failed + 1))
                if [ "$fail_fast" -eq 1 ]; then
                    break 3
                fi
            fi
        done
    done

    if [ "$lib_failed" -eq 0 ]; then
        write_summary "$name" "成功"
    else
        write_summary "$name" "失败（允许实验库失败时为 continue-on-error）"
    fi
done < <(manifest list --format tsv --libs "$libs" --backends "$backends" --experimental "$experimental")

# 汇总所有库。
overall_md="$dist_dir/summary.md"
{
    echo "## Android C/C++ 库构建汇总"
    echo
    echo "- 总计: ${total}，失败: ${failed}，跳过: $skipped"
    echo "- ABI: \`$abis\`，API: ${api}，构建类型: $build_type"
    echo
    echo "| 库 | ABI | 后端 | 状态 | 耗时 | 日志 |"
    echo "| --- | --- | --- | --- | ---: | --- |"
    while IFS=$'\t' read -r r_name r_abi r_backend r_status r_seconds r_artifact r_log; do
        icon="✅"
        [ "$r_status" = "ok" ] || icon="❌"
        echo "| $r_name | $r_abi | $r_backend | $icon | ${r_seconds}s | \`$r_log\` |"
    done <"$summary_tsv_root"
} >"$overall_md"

log "构建汇总: $overall_md"
append_github_summary "$overall_md"

if [ "$failed" -gt 0 ]; then
    err "有 $failed 个构建任务失败"
    exit 1
fi

log "全部构建任务完成（共 $total 个）"
