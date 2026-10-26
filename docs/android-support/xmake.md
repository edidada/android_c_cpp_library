# xmake Android 元数据清单

生成时间：2026-10-26 11:42 UTC

[判定方法与限制](README.md)。以下条目均未在本扫描工作流中编译验证。

上游：[固定快照 58f6e9c1bd2e930aadb332fec7c37281edd798b3](https://github.com/xmake-io/xmake-repo/tree/58f6e9c1bd2e930aadb332fec7c37281edd798b3)；共 2028 条。

| 库 / 配方目录 | 判定 | 依据（含排除条件也会列出） |
| --- | --- | --- |
| [11zip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/1/11zip/xmake.lua) | 含 Android 逻辑 | L15: on_install("macosx", "android", "linux", "windows", "mingw", function (package) |
| [7z](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/7/7z/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aargh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aargh/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [abseil](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/abseil/xmake.lua) | 含 Android 逻辑 | L37: on_check("android", function (package); L42: assert(ndkver and tonumber(ndkver) >= 27, "package(abseil): need ndk version >= 27 for android since 20260526.0") |
| [access_private](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/access_private/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ace](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/ace/xmake.lua) | 含 Android 逻辑 | L22: if not package:is_plat("android") then; L37: on_install("linux", "macosx", "bsd", "iphoneos", "android", function(package); L56: io.writefile("ace/config.h", [[#include "ace/config-android.h"]]) |
| [acl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/acl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [acl-dev](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/acl-dev/xmake.lua) | 含 Android 逻辑 | L3: set_description("C/C++ server and network library, including coroutine, redis client, http/https/websocket, mqtt, mysql/postgresql/sqlite client with C/C++ for Linux, Android, iOS, MacOS, Windows."); L18: add_patches(">=3.6.2", "patches/v3.6.2/fix_android_install_path.diff", "19917bd1852af4ddecc27ef402ecf9806b89ec78d91e62c806ba00fc05f41e94"); L53: if package:is_plat("android") then |
| [actor-framework](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/actor-framework/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ada](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/ada/xmake.lua) | 含 Android 逻辑 | L44: on_check("android", function (package) |
| [adaptive_cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/adaptive_cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ade](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/ade/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [agg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/agg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aitoolkit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aitoolkit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aklomp-base64](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aklomp-base64/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [alcatraz](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/alcatraz/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [alembic](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/alembic/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [algo_plus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/algo_plus/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [alpaca](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/alpaca/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [alpaka](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/alpaka/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [alsa-lib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/alsa-lib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [amgcl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/amgcl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [amgx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/amgx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [amqp-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/amqp-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [amrex](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/amrex/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [anari](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/anari/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [angelscript](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/angelscript/xmake.lua) | 含 Android 逻辑 | L32: on_load("windows&#124;x86", "windows&#124;x64", "linux", "android", "msys", "mingw", function (package); L36: on_install("windows&#124;x86", "windows&#124;x64", "linux", "android", "msys", "mingw", function (package); L46: if package:is_plat("android") then |
| [angle](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/angle/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [annoy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/annoy/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [antlr4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/antlr4/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [antlr4-runtime](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/antlr4-runtime/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aom](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aom/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [appimage](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/appimage/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [approval-tests-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/approval-tests-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [apr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/apr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aqt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aqt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aravis](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aravis/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [arduinojson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/arduinojson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [argh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/argh/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [argp-standalone](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/argp-standalone/xmake.lua) | 含 Android 逻辑 | L13: on_install("macosx", "android", function (package) |
| [argparse](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/argparse/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [argtable3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/argtable3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [argus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/argus/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [argz](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/argz/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [arkari](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/arkari/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [armadillo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/armadillo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [arrayfire](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/arrayfire/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [arrow](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/arrow/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [asap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/asap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [asbind20](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/asbind20/xmake.lua) | 含 Android 逻辑 | L45: on_install("windows", "linux", "android", "msys", "mingw", function (package) |
| [aseprite-tga](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aseprite-tga/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [asio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/asio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [asio2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/asio2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [asio3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/asio3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [asmjit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/asmjit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [asmtk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/asmtk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [asn1c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/asn1c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [assimp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/assimp/xmake.lua) | 含 Android 逻辑 | L51: add_configs("android_jniiosysystem", {description = "Enable Android JNI IOSystem support.", default = false, type = "boolean"}); L63: on_check("android", function (package); L67: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 26, "package(assimp): need ndk api level >= 26 for android") |
| [astc-encoder](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/astc-encoder/xmake.lua) | 含 Android 逻辑 | L51: if package:is_plat("mingw", "android", "bsd") or package:has_tool("cxx", "clang", "clang_cl") then |
| [async_simple](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/async_simple/xmake.lua) | 含 Android 逻辑 | L21: on_check("android", function (package) |
| [at-spi2-core](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/at-spi2-core/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [atk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/atk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [atomic_queue](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/atomic_queue/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [attr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/attr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aubio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aubio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [audiofile](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/audiofile/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [audit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/audit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aui/xmake.lua) | 含 Android 逻辑 | L62: if package:is_plat("android") then; L77: elseif package:is_plat("android") then; L100: elseif package:is_plat("android") then |
| [aui-toolbox](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aui-toolbox/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aurora-au](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aurora-au/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [autoconf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/autoconf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [autoconf-archive](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/autoconf-archive/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [autodiff](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/autodiff/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [automake](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/automake/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [autotools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/autotools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [avir](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/avir/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [avisynthplus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/avisynthplus/xmake.lua) | 含 Android 逻辑 | L29: on_install("!wasm and !android and !cross", function (package) |
| [awk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/awk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aws-c-auth](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-c-auth/xmake.lua) | 含 Android 逻辑 | L34: on_install("windows", "linux", "bsd", "cross", "android", "mingw&#124;!i386", "macosx&#124;arm64", function (package) |
| [aws-c-cal](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-c-cal/xmake.lua) | 含 Android 逻辑 | L42: if package:is_plat("linux", "macosx", "bsd", "cross", "android") then |
| [aws-c-common](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-c-common/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aws-c-compression](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-c-compression/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aws-c-event-stream](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-c-event-stream/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aws-c-http](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-c-http/xmake.lua) | 含 Android 逻辑 | L45: on_install("windows", "linux", "bsd", "cross", "android", "mingw&#124;!i386", "macosx&#124;arm64", function (package) |
| [aws-c-io](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-c-io/xmake.lua) | 含 Android 逻辑 | L52: elseif is_plat("linux", "bsd", "cross", "android") then; L66: on_install("windows", "linux", "bsd", "cross", "android", "mingw&#124;!i386", "macosx&#124;arm64", function (package) |
| [aws-c-mqtt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-c-mqtt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aws-c-s3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-c-s3/xmake.lua) | 含 Android 逻辑 | L48: on_install("windows", "linux", "bsd", "cross", "android", "mingw&#124;!i386", "macosx&#124;arm64", function (package) |
| [aws-c-sdkutils](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-c-sdkutils/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aws-checksums](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-checksums/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aws-crt-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-crt-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aws-lc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-lc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [aws-sdk-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/a/aws-sdk-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [b2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/b2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [babl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/babl/xmake.lua) | 含 Android 逻辑 | L18: if is_plat("linux", "bsd", "android") then |
| [backportcpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/backportcpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [backward-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/backward-cpp/xmake.lua) | 含 Android 逻辑 | L25: elseif is_plat("linux", "bsd", "android") then; L58: on_install("(!windows or windows&#124;!arm64) and !android and !bsd and !wasm and !cross", function (package) |
| [bandit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bandit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [barkeep](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/barkeep/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [base-n](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/base-n/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [base64-terrakuh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/base64-terrakuh/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [base64-zhicheng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/base64-zhicheng/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [basisu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/basisu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bass24](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bass24/xmake.lua) | 含 Android 逻辑 | L28: elseif is_plat("android") then; L29: add_urls("https://www.un4seen.com/files/bass$(version)-android.zip", {version = function (version); L84: on_install("android", function (package) |
| [bazel](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bazel/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bc_crunch](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bc_crunch/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bcg729](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bcg729/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bddisasm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bddisasm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bdwgc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bdwgc/xmake.lua) | 含 Android 逻辑 | L17: on_check("android", function (package) |
| [beaengine](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/beaengine/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [benchmark](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/benchmark/xmake.lua) | 含 Android 逻辑 | L49: on_check("android", function (package); L50: if package:is_plat("android") and package:is_arch("armeabi-v7a") then |
| [bento4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bento4/xmake.lua) | 含 Android 逻辑 | L12: on_check("android", function (package); L16: assert(ndk_sdkver and tonumber(ndk_sdkver) > 21, "package(bento4): need ndk api level >= 21 for android") |
| [bestsource](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bestsource/xmake.lua) | 含 Android 逻辑 | L33: on_install("windows", "mingw@windows,linux,cygwin,msys", "linux", "macosx", "android", "iphoneos", function (package) |
| [better-enums](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/better-enums/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bgfx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bgfx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bght](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bght/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bhook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bhook/xmake.lua) | 含 Android 逻辑 | L3: set_description("ByteHook is an Android PLT hook library which supports armeabi-v7a, arm64-v8a, x86 and x86_64."); L18: on_install("android", function (package) |
| [bin2c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bin2c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [binn](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/binn/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [binutils](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/binutils/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bison](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bison/xmake.lua) | 含 Android 逻辑 | L52: on_install("macosx", "linux", "bsd", "android", "iphoneos", "cross", function (package) |
| [bitsery](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bitsery/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [blackbone](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/blackbone/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [blah](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/blah/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [blake2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/blake2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [blake3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/blake3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [blaze](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/blaze/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [blend2d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/blend2d/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [blitz](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/blitz/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [blobify](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/blobify/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [blook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/blook/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [blosc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/blosc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bluez](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bluez/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bnm-android](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bnm-android/xmake.lua) | 含 Android 逻辑 | L1: package("bnm-android"); L2: set_homepage("https://github.com/ByNameModding/BNM-Android"); L3: set_description("Modding il2cpp games by classes, methods, fields names on Android.") |
| [boost](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_assert](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_assert/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_config](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_config/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_di](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_di/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_math](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_math/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_pfr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_pfr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_reflect](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_reflect/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_sml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_sml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_static_assert](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_static_assert/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_throw_exception](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_throw_exception/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_type_traits](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_type_traits/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_ut](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_ut/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boost_uuid](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boost_uuid/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boostdep](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boostdep/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boringssl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boringssl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [botan](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/botan/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [box2d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/box2d/xmake.lua) | 含 Android 逻辑 | L35: if package:is_plat("android") then |
| [box3d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/box3d/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [boxfort](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/boxfort/xmake.lua) | 含 Android 逻辑 | L10: add_patches("2024.05.02", "patches/android-shm.patch", "619a3e56cd6bb040d522acbf610603bf22e68a435742aadc1746793c32d44e99") |
| [bqlog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bqlog/xmake.lua) | 含 Android 逻辑 | L16: elseif is_plat("android") then; L17: add_syslinks("log", "android"); L35: on_install("windows&#124;x64", "linux", "macosx", "bsd", "android", "iphoneos", function (package) |
| [brainflow](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/brainflow/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [branchless-utf8](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/branchless-utf8/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [breakpad](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/breakpad/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bredis](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bredis/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [brotli](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/brotli/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [brpc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/brpc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [brynet](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/brynet/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bsdiff](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bsdiff/xmake.lua) | 含 Android 逻辑 | L3: set_homepage("https://android.googlesource.com/platform/external/bsdiff/"); L6: add_urls("https://android.googlesource.com/platform/external/bsdiff.git") |
| [buddy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/buddy/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bullet3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bullet3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bvh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bvh/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [byte-lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/byte-lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bytepack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bytepack/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [bzip2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bzip2/xmake.lua) | 含 Android 逻辑 | L28: if not package:is_plat("iphoneos", "android") then |
| [bzip3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/b/bzip3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [c-ares](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/c-ares/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [c-blosc2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/c-blosc2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [c-vector](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/c-vector/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [c4core](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/c4core/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ca-certificates](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/ca-certificates/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cairo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cairo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cairomm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cairomm/xmake.lua) | 含 Android 逻辑 | L41: on_install("!android and !bsd and !wasm", function (package) |
| [capnproto](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/capnproto/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [capstone](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/capstone/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cargs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cargs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cartographer](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cartographer/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [catch2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/catch2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [caudio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/caudio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cdt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cdt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cef](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cef/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [celero](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/celero/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cello](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cello/xmake.lua) | 含 Android 逻辑 | L17: elseif is_plat("cross", "android", "wasm") then; L40: elseif is_plat("cross", "android", "wasm") then |
| [centurion](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/centurion/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cereal](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cereal/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ceres-solver](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/ceres-solver/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ceval](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/ceval/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cfitsio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cfitsio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cgal](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cgal/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cgetopt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cgetopt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cgif](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cgif/xmake.lua) | 含 Android 逻辑 | L30: on_check("android", function (package) |
| [cglm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cglm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cgltf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cgltf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cgns](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cgns/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cgraph](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cgraph/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [chaiscript](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/chaiscript/xmake.lua) | 含 Android 逻辑 | L16: on_install("windows", "linux", "android", "macosx", "iphoneos", function (package) |
| [charls](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/charls/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [checkpolicy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/checkpolicy/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [chipmunk2d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/chipmunk2d/xmake.lua) | 含 Android 逻辑 | L11: add_patches("7.0.3", path.join(os.scriptdir(), "patches", "7.0.3", "android.patch"), "d0bbefe66852cdadb974dce24d4383c356bc3fa88656739ff1d5baf4e3792a96"); L27: elseif is_plat("android") then; L45: on_install("windows", "linux", "macosx", "iphoneos", "mingw", "android", "wasm", "bsd",function (package) |
| [choc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/choc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [chromium_zlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/chromium_zlib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cimg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cimg/xmake.lua) | 含 Android 逻辑 | L61: on_install("windows", "linux", "macosx", "android", "mingw", "cygwin", "bsd", "cross", function (package) |
| [cimgui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cimgui/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cinatra](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cinatra/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cista](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cista/xmake.lua) | 含 Android 逻辑 | L18: if package:is_plat("android") then; L21: assert(ndk_sdkver and tonumber(ndk_sdkver) > 21, "package(cista): need ndk api level > 21 for android"); L29: on_install("windows&#124;x64", "windows&#124;x86", "linux", "macosx", "bsd", "android", "iphoneos", "cross", function (package) |
| [citor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/citor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [civetweb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/civetweb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cjson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cjson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ck](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/ck/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [clap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [clara](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clara/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [clay](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clay/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [clblast](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clblast/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [clean-test](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clean-test/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [clhep](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clhep/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cli](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cli/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cli11](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cli11/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [clib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [clip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clip/xmake.lua) | 含 Android 逻辑 | L46: on_install("!android and !iphoneos and !bsd and !cross", function(package) |
| [clipboard_lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clipboard_lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [clipper2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clipper2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [clove-unit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/clove-unit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cmake](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cmake/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cmark](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cmark/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cmdline](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cmdline/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cmdparser](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cmdparser/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cmidi2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cmidi2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cminpack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cminpack/xmake.lua) | 含 Android 逻辑 | L29: on_install("windows", "linux", "macosx", "mingw", "msys", "android", "iphoneos", "wasm", function (package) |
| [cmocka](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cmocka/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cnats](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cnats/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cnl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cnl/xmake.lua) | 含 Android 逻辑 | L14: on_check("android", function (package) |
| [cnpy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cnpy/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [coal](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/coal/xmake.lua) | 含 Android 逻辑 | L19: on_check("android", function (package) |
| [coin-or-asl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/coin-or-asl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [coin-or-clp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/coin-or-clp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [coin-or-coinutils](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/coin-or-coinutils/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [coin-or-ipopt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/coin-or-ipopt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [coin-or-osi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/coin-or-osi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [collada-dom](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/collada-dom/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [colmap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/colmap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [commata](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/commata/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [commonlibsse-ng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/commonlibsse-ng/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [concerto-core](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/concerto-core/xmake.lua) | 含 Android 逻辑 | L17: on_check("android", function (package) |
| [concurrencpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/concurrencpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [concurrentqueue](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/concurrentqueue/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [console-bridge](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/console-bridge/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [continuable](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/continuable/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [convertutf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/convertutf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [coost](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/coost/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [corrade](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/corrade/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cosmocc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cosmocc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-async](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-async/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-channel](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-channel/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-dump](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-dump/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-httplib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-httplib/xmake.lua) | 含 Android 逻辑 | L81: if package:is_plat("android") then; L84: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 24, "package(httplib): need ndk api level >= 24 for android") |
| [cpp-ipc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-ipc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-jwt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-jwt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-lazy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-lazy/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-linenoise](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-linenoise/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-mcp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-mcp/xmake.lua) | 含 Android 逻辑 | L23: on_check("android", function (package); L26: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 24, "package(cpp-mcp): need ndk api level >= 24 for android") |
| [cpp-peglib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-peglib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-rotor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-rotor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-semver](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-semver/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-semver-easz](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-semver-easz/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-sort](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-sort/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-subprocess](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-subprocess/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp-tbox](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp-tbox/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpp20-http-client](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpp20-http-client/xmake.lua) | 含 Android 逻辑 | L28: on_install("windows", "linux", "macosx", "bsd", "android", "cross", function (package) |
| [cppad](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppad/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppast](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppast/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppcheck](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppcheck/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppcodec](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppcodec/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppcoro](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppcoro/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppfront](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppfront/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppgpio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppgpio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppitertools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppitertools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppjieba](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppjieba/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppli](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppli/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppp-reiconv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppp-reiconv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpptrace](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpptrace/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cppunit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppunit/xmake.lua) | 含 Android 逻辑 | L18: on_install("!android and !wasm", function (package) |
| [cppzmq](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cppzmq/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpr/xmake.lua) | 含 Android 逻辑 | L57: if package:is_plat("linux", "bsd", "android", "cross") then; L68: if package:is_plat("windows") or (package:is_plat("android") and is_subhost("windows")) then; L86: if package:is_plat("linux", "bsd", "android", "cross") then |
| [cpu-features](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpu-features/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cpuinfo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cpuinfo/xmake.lua) | 含 Android 逻辑 | L3: set_description("CPU INFOrmation library (x86/x86-64/ARM/ARM64, Linux/Windows/Android/macOS/iOS)"); L58: if (package:is_cross() or package:is_plat("mingw")) and (not package:is_plat("android")) then |
| [cr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cr/xmake.lua) | 含 Android 逻辑 | L10: on_install("windows", "linux", "macosx", "mingw", "msys", "android", "iphoneos", "cross", function (package) |
| [crashcatch](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/crashcatch/xmake.lua) | 含 Android 逻辑 | L21: on_install("!android and !macosx", function(package) |
| [crashpad](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/crashpad/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [crc32c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/crc32c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [criterion](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/criterion/xmake.lua) | 含 Android 逻辑 | L24: if not is_plat("android") then; L34: on_check("android", function (package); L57: if package:is_plat("android") then |
| [croaring](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/croaring/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [croncpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/croncpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [crossguid](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/crossguid/xmake.lua) | 含 Android 逻辑 | L21: on_install("windows", "linux", "macosx", "iphoneos", "android", "mingw", function (package) |
| [crow](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/crow/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [crstl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/crstl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [crypto-algorithms](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/crypto-algorithms/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cryptopp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cryptopp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cs_libguarded](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cs_libguarded/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [csa](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/csa/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cserialport](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cserialport/xmake.lua) | 含 Android 逻辑 | L37: on_install("!cross and !iphoneos and !android", function (package) |
| [csfml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/csfml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cspice](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cspice/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [csv2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/csv2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [csvparser](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/csvparser/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cthash](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cthash/xmake.lua) | 含 Android 逻辑 | L10: on_install("linux", "macosx", "bsd", "mingw", "msys", "android", "iphoneos", "cross", "wasm", function (package) |
| [ctpg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/ctpg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ctrack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/ctrack/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ctre](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/ctre/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ctrl-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/ctrl-c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cubeb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cubeb/xmake.lua) | 含 Android 逻辑 | L22: on_install("windows", "linux", "macosx", "bsd", "mingw", "msys", "android", "wasm", "cross", function (package) |
| [cuda](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cuda/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cuda-samples](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cuda-samples/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cumem](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cumem/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cunit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cunit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [curl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/curl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [curlcpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/curlcpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [curlpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/curlpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cute_headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cute_headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cutlass](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cutlass/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cwt-cucumber](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cwt-cucumber/xmake.lua) | 含 Android 逻辑 | L19: on_check("android", function (package) |
| [cxxgraph](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cxxgraph/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cxxopts](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cxxopts/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [cyrus-sasl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/c/cyrus-sasl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [d3d12-memory-allocator](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/d3d12-memory-allocator/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [daemonpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/daemonpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [darts](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/darts/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dartsim](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dartsim/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dascript](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dascript/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dataframe](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dataframe/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [datatype99](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/datatype99/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [date](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/date/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dav1d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dav1d/xmake.lua) | 含 Android 逻辑 | L26: on_check("android", function (package) |
| [davix](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/davix/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [daw_header_libraries](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/daw_header_libraries/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [daw_json_link](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/daw_json_link/xmake.lua) | 含 Android 逻辑 | L25: on_check("android", function (package); L28: assert(ndk_sdkver and tonumber(ndk_sdkver) > 21, "package(daw_json_link): need ndk api level > 21 for android"); L32: on_install("windows", "linux", "macosx", "bsd", "mingw", "msys", "android@linux,macosx", "iphoneos", "cross", function (package) |
| [dawn](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dawn/xmake.lua) | 含 Android 逻辑 | L31: add_configs("vulkan", {description = "Enable the Vulkan backend.", default = is_plat("windows", "linux", "android"), type = "boolean"}); L33: add_configs("opengles", {description = "Enable the OpenGL ES backend.", default = is_plat("linux", "android"), type = "boolean"}); L45: on_check("windows", "linux", "macosx", "android", "iphoneos", function (package) |
| [daxa](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/daxa/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dbg-macro](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dbg-macro/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dbus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dbus/xmake.lua) | 含 Android 逻辑 | L14: add_patches("1.16.2", "patches/1.16.2/android-socklen_t-signed.patch", "c5c98e1300e05c737cfcf3a6904973dbb9fa0a71c036d5c96bd8c29f81f5b3a5"); L30: on_check("android", function (package); L34: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 24, "package(dbus): need ndk api level >= 24 for android") |
| [dbus-cxx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dbus-cxx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dcmtk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dcmtk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [debug-hpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/debug-hpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [debug_assert](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/debug_assert/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [debugbreak](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/debugbreak/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [decimal_for_cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/decimal_for_cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [demumble](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/demumble/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [depot_tools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/depot_tools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [devil](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/devil/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dexbuilder](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dexbuilder/xmake.lua) | 含 Android 逻辑 | L25: on_install("android", function (package) |
| [dfdutils](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dfdutils/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [diasdk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/diasdk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [digestpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/digestpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [diligentcore](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/diligentcore/xmake.lua) | 含 Android 逻辑 | L98: PLATFORM_ANDROID PLATFORM_EMSCRIPTEN PLATFORM_IOS PLATFORM_LINUX PLATFORM_MACOS PLATFORM_TVOS PLATFORM_UNIVERSAL_WINDOWS PLATFORM_WIN32 |
| [diligentfx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/diligentfx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [diligenttools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/diligenttools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dipp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dipp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [directx-headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/directx-headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [directx12-agility](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/directx12-agility/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [directxmath](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/directxmath/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [directxshadercompiler](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/directxshadercompiler/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [directxtex](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/directxtex/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [directxtk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/directxtk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [directxtk12](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/directxtk12/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dirent](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dirent/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dirent_h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dirent_h/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [discord](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/discord/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dispenso](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dispenso/xmake.lua) | 含 Android 逻辑 | L28: on_install("windows&#124;x64", "linux", "macosx", "bsd", "mingw", "msys", "android", "iphoneos", "cross", "wasm", function (package) |
| [distorm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/distorm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dlfcn-win32](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dlfcn-win32/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dlib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dlpack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dlpack/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dlss](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dlss/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dobby](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dobby/xmake.lua) | 含 Android 逻辑 | L14: add_configs("android_bionic_linker_utils", {description = "Enable android bionic linker utils.",  default = false, type = "boolean", readonly = not is_plat("android")}); L24: on_install("linux", "macosx", "android", "iphoneos", function (package); L29: table.insert(configs, "-DPlugin.Android.BionicLinkerUtil=" .. (package:config("android_bionic_linker_utils") and "ON" or "OFF")) |
| [docopt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/docopt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [doctest](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/doctest/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dotnet](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dotnet/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [double-conversion](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/double-conversion/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [doxygen](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/doxygen/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dr_flac](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dr_flac/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dr_mp3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dr_mp3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dr_wav](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dr_wav/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [draco](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/draco/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dragonbox](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dragonbox/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [drogon](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/drogon/xmake.lua) | 含 Android 逻辑 | L105: on_install("!android", function (package) |
| [duckdb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/duckdb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [duckx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/duckx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [duilib_ultimate](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/duilib_ultimate/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [duktape](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/duktape/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dune-common](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dune-common/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dxsdk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dxsdk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dylib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dylib/xmake.lua) | 含 Android 逻辑 | L15: on_install("!android and !bsd", function (package) |
| [dynareadout](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dynareadout/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [dyncall](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/d/dyncall/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [e2fsprogs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/e2fsprogs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [eabase](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/eabase/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [eastl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/eastl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [easy_profiler](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/easy_profiler/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [easyhook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/easyhook/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [easyloggingpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/easyloggingpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [easywsclient](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/easywsclient/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ed](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/ed/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [edlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/edlib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [effcee](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/effcee/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [effolkronium-random](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/effolkronium-random/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [efsw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/efsw/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [egl-headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/egl-headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [eigen](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/eigen/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [elfio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/elfio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [elfutils](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/elfutils/xmake.lua) | 含 Android 逻辑 | L28: if package:is_plat("android") then; L32: elseif is_plat("android") then; L37: if package:is_plat("android") then |
| [embedded-xoodyak](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/embedded-xoodyak/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [embree](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/embree/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [emhash](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/emhash/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [emio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/emio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [emmylua_debugger](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/emmylua_debugger/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [emock](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/emock/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [emscripten](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/emscripten/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [emscripten-glfw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/emscripten-glfw/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [enet](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/enet/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [enet6](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/enet6/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [enkits](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/enkits/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [enoki](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/enoki/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ensmallen](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/ensmallen/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [entt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/entt/xmake.lua) | 含 Android 逻辑 | L41: on_check("android", function (package) |
| [epoll-shim](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/epoll-shim/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [esp32-arduino-libs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/esp32-arduino-libs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [esp32-devel](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/esp32-devel/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [esptool](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/esptool/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [etl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/etl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [eudev](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/eudev/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [eui-neo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/eui-neo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [eve](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/eve/xmake.lua) | 含 Android 逻辑 | L16: elseif package:is_plat("android") then |
| [eventpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/eventpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [exosip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/exosip/xmake.lua) | 含 Android 逻辑 | L118: on_install("linux", "macosx", "android@linux,macosx", "cross", "wasm", function (package); L124: if package:is_plat("android") then; L127: io.replace("src/eXutils.c", [[#elif (_POSIX_C_SOURCE >= 200112L &#124;&#124; _XOPEN_SOURCE >= 600 &#124;&#124; __APPLE__ &#124;&#124; defined(ANDROID)) && !_GNU_SOURCE]], |
| [expat](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/expat/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [expected-lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/expected-lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [expresscpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/expresscpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [exprtk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/exprtk/xmake.lua) | 含 Android 逻辑 | L19: on_install("windows", "linux", "macosx", "bsd", "iphoneos", "android", "wasm", "cross", function (package) |
| [extra-cmake-modules](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/extra-cmake-modules/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ezc3d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/e/ezc3d/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [faac](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/faac/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [faad2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/faad2/xmake.lua) | 含 Android 逻辑 | L17: if is_plat("linux", "bsd", "cross", "android") then |
| [fadec](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fadec/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [faiss](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/faiss/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fakeit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fakeit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [faker-cxx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/faker-cxx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fann](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fann/xmake.lua) | 含 Android 逻辑 | L20: on_check("android", function (package); L36: elseif package:is_plat("macosx", "linux", "cross", "android", "mingw", "msys", "bsd") then; L41: on_install("windows", "macosx", "linux", "cross", "android", "mingw", "msys", "bsd", function (package) |
| [farmhash](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/farmhash/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fast-cdr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fast-cdr/xmake.lua) | 含 Android 逻辑 | L27: on_install("windows", "linux", "macosx", "bsd", "msys", "android", "iphoneos", "cross", "wasm", function (package) |
| [fast-lzma2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fast-lzma2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fast_double_parser](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fast_double_parser/xmake.lua) | 含 Android 逻辑 | L15: on_install("windows&#124;x64", "macosx", "linux", "mingw", "android", function (package) |
| [fast_float](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fast_float/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fast_io](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fast_io/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fast_obj](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fast_obj/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fastcppcsvparser](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fastcppcsvparser/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fastgltf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fastgltf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fastmod](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fastmod/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fastor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fastor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fatal](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fatal/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fbgemm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fbgemm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fbthrift](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fbthrift/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fcgi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fcgi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fcl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fcl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fcpw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fcpw/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fdk-aac](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fdk-aac/xmake.lua) | 含 Android 逻辑 | L3: set_description("A standalone library of the Fraunhofer FDK AAC code from Android."); L19: if package:is_plat("android") then; L20: io.replace("libSBRdec/src/lpp_tran.cpp", "#ifdef __ANDROID__", "#if 0") |
| [ffmpeg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/ffmpeg/xmake.lua) | 含 Android 逻辑 | L71: elseif is_plat("android") then; L72: add_syslinks("dl", "android", "mediandk"); L132: if package:config("pic") ~= false and package:is_plat("linux", "android") then |
| [ffms2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/ffms2/xmake.lua) | 含 Android 逻辑 | L35: on_install("windows", "mingw@windows,linux,cygwin,msys", "linux", "macosx", "android", "iphoneos", function (package) |
| [ffts](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/ffts/xmake.lua) | 含 Android 逻辑 | L34: if package:is_plat("android") then |
| [fftw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fftw/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fgt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fgt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [field3d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/field3d/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [filament](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/filament/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [filc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/filc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fixed-containers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fixed-containers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fizz](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fizz/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [flann](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/flann/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [flashlight](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/flashlight/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [flatbuffers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/flatbuffers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [flatcc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/flatcc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [flecs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/flecs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [flex](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/flex/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [floatengine](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/floatengine/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fls-float-raylib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fls-float-raylib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fls-float-rlimgui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fls-float-rlimgui/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fltk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fltk/xmake.lua) | 含 Android 逻辑 | L30: elseif is_plat("android") then; L31: add_syslinks("android") |
| [fluidsynth](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fluidsynth/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [flux](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/flux/xmake.lua) | 含 Android 逻辑 | L15: on_check("android", function (package) |
| [fluxent](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fluxent/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fluxsort](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fluxsort/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fmi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fmi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fmi4cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fmi4cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fmm3d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fmm3d/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fmt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fmt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fmtlog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fmtlog/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [folly](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/folly/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fontconfig](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fontconfig/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [foxglove-sdk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/foxglove-sdk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fpm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fpm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fpng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fpng/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [freeglut](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/freeglut/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [freeimage](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/freeimage/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [freerdp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/freerdp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [freetype](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/freetype/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [freexl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/freexl/xmake.lua) | 含 Android 逻辑 | L25: on_check("android", function (package) |
| [fribidi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fribidi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [frozen](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/frozen/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [frozenca-btree](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/frozenca-btree/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [frugally-deep](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/frugally-deep/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fruit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fruit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ftgl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/ftgl/xmake.lua) | 含 Android 逻辑 | L30: on_install("!android and !cross and !iphoneos and !bsd", function (package) |
| [ftxui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/ftxui/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [funchook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/funchook/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [function2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/function2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [functionalplus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/functionalplus/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fx-gltf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fx-gltf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [fxdiv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/f/fxdiv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [g2o](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/g2o/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [g3log](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/g3log/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gamenetworkingsockets](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gamenetworkingsockets/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gaussianlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gaussianlib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gcem](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gcem/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gdal](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gdal/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gdcm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gdcm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gdk-pixbuf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gdk-pixbuf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [geant4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/geant4/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gecode](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gecode/xmake.lua) | 含 Android 逻辑 | L36: on_install("linux", "cross", "android", function (package) |
| [gelldur-eventbus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gelldur-eventbus/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [genie](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/genie/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [geo-utils-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/geo-utils-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [geode-sdk-result](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/geode-sdk-result/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [geode-sdk-tuliphook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/geode-sdk-tuliphook/xmake.lua) | 含 Android 逻辑 | L3: set_description("Low level hooking lib specialized for Geometry Dash. Supports Windows x86/x86_64, macOS x86_64/aarch64, Android armv7/aarch64, iOS aarch64"); L19: if not is_plat("android") then; L50: if not is_plat("android") then |
| [geographiclib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/geographiclib/xmake.lua) | 含 Android 逻辑 | L12: on_install("android", "cross", "windows", "macosx", "linux", function (package) |
| [geos](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/geos/xmake.lua) | 含 Android 逻辑 | L27: on_check("android", function (package) |
| [gettext](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gettext/xmake.lua) | 含 Android 逻辑 | L28: on_check("android", function (package); L45: on_install("macosx", "linux", "android", "windows&#124;x64", function (package); L87: if package:is_plat("android") then |
| [gflags](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gflags/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gfortran](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gfortran/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gfx-timsort](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gfx-timsort/xmake.lua) | 含 Android 逻辑 | L17: if package:is_plat("android") then |
| [ggml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/ggml/xmake.lua) | 含 Android 逻辑 | L61: elseif package:is_plat("android") then |
| [ghc_filesystem](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/ghc_filesystem/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ghostscript](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/ghostscript/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gifdec](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gifdec/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [giflib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/giflib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ginkgo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/ginkgo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [girlhook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/girlhook/xmake.lua) | 含 Android 逻辑 | L18: on_install("android", function (package); L48: add_syslinks("android", "log") |
| [girlloader](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/girlloader/xmake.lua) | 含 Android 逻辑 | L10: on_install("android", function (package) |
| [git-crypt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/git-crypt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gklib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gklib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gl2ps](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gl2ps/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glad](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glad/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glaze](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glaze/xmake.lua) | 含 Android 逻辑 | L74: elseif package:is_plat("android") then |
| [glbinding](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glbinding/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glew](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glew/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glfw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glfw/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glfw3webgpu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glfw3webgpu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glgpuselect](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glgpuselect/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gli](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gli/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glibmm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glibmm/xmake.lua) | 含 Android 逻辑 | L44: on_install("!android and !wasm and !iphoneos", function (package) |
| [glm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glob](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glob/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glog/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gloo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gloo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glosshook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glosshook/xmake.lua) | 含 Android 逻辑 | L3: set_description("A simple android NativeHook library."); L15: on_check("android", function (package); L21: on_install("android", function (package) |
| [glpk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glpk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glshaderpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glshaderpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glslang](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glslang/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glslang-nihui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glslang-nihui/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glut](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glut/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [glx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/glx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gmm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gmm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gmp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gmp/xmake.lua) | 含 Android 逻辑 | L76: on_install("!wasm and (!android or android@!windows)", function (package) |
| [gmsh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gmsh/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gmssl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gmssl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gn](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gn/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gnu-gsl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gnu-gsl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gnu-rm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gnu-rm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gnu-sed](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gnu-sed/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [go](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/go/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gobject-introspection](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gobject-introspection/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [godotcpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/godotcpp/xmake.lua) | 含 Android 逻辑 | L21: on_install("linux", "windows", "macosx", "mingw", "cygwin", "iphoneos", "android", "msys", function (package); L34: if package:is_plat("android") then; L45: os.cp("godot-headers/android",            package:installdir("include")) |
| [godotcpp4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/godotcpp4/xmake.lua) | 含 Android 逻辑 | L17: on_check("android", function (package); L42: on_install("linux", "windows&#124;x64", "windows&#124;x86", "macosx", "iphoneos", "android", "mingw", function(package) |
| [google-cloud-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/google-cloud-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gperf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gperf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gperftools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gperftools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gpm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gpm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gpujpeg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gpujpeg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [graaf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/graaf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [graphene](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/graphene/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [grpc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/grpc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gsl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gsl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gsl-lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gsl-lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gsound](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gsound/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gspell](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gspell/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gstreamer](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gstreamer/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gte](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gte/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gtest](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gtest/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gtk+4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gtk+4/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gtk3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gtk3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gtk4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gtk4/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gtl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gtl/xmake.lua) | 含 Android 逻辑 | L22: on_check("android", function (package); L26: assert(ndkver and tonumber(ndkver) > 25, "package(gtl): need ndk revision >= 26 for android") |
| [guetzli](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/guetzli/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [guilite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/guilite/xmake.lua) | 含 Android 逻辑 | L12: on_install("windows", "macosx", "linux", "mingw", "android", "iphoneos", function (package) |
| [gumbo-parser](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gumbo-parser/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gyp-next](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gyp-next/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gz-cmake](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gz-cmake/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gz-math](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gz-math/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gz-utils](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gz-utils/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [gzip-hpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/g/gzip-hpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [h2o](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/h2o/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [h3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/h3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [h5cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/h5cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [haclog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/haclog/xmake.lua) | 含 Android 逻辑 | L29: on_install("windows", "linux", "macosx", "android", "cross", function (package) |
| [half](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/half/xmake.lua) | 含 Android 逻辑 | L11: on_install("windows", "linux", "macosx", "iphoneos", "android", "bsd", function (package) |
| [handy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/handy/xmake.lua) | 含 Android 逻辑 | L18: on_check("android", function (package); L26: if package:is_plat("android") then; L27: io.replace("CMakeLists.txt", [[elseif(CMAKE_HOST_UNIX)]], [[elseif(CMAKE_HOST_UNIX OR ANDROID)]], {plain = true}) |
| [happly](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/happly/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [harfbuzz](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/harfbuzz/xmake.lua) | 含 Android 逻辑 | L57: on_check("android", function (package) |
| [hash-library](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hash-library/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hashcat](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hashcat/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hdbscan-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hdbscan-cpp/xmake.lua) | 含 Android 逻辑 | L14: on_install("macosx", "android", "linux", "windows", "mingw", function(package) |
| [hdf5](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hdf5/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hdrhistogram_c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hdrhistogram_c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hedley](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hedley/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hexl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hexl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hffix](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hffix/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hidapi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hidapi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [highfive](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/highfive/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [highs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/highs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [highway](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/highway/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hiredis](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hiredis/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hiredis-vip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hiredis-vip/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hlslpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hlslpp/xmake.lua) | 含 Android 逻辑 | L21: on_install("linux&#124;!arm64", "macosx", "bsd", "windows", "android", "iphoneos", function (package) |
| [hookmanager](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hookmanager/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hopscotch-map](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hopscotch-map/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [houdini](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/houdini/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hpsocket](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hpsocket/xmake.lua) | 含 Android 逻辑 | L16: {name = "zlib",   package = is_plat("android", "windows") and "" or "zlib"},; L50: elseif package:is_plat("android") then; L64: if package:is_plat("android") then |
| [hpx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hpx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [http_parser](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/http_parser/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hwdata](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hwdata/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hwinfo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hwinfo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hwloc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hwloc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hyperscan](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hyperscan/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hypre](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hypre/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [hyprwayland-scanner](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/h/hyprwayland-scanner/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [icbc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/icbc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [icey](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/icey/xmake.lua) | 含 Android 逻辑 | L21: on_check("android", function (package); L23: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 24, "package(icey) requires Android API level >= 24 for libuv") |
| [icu4c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/icu4c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [idna](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/idna/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ifort](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/ifort/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ignite3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/ignite3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [igraph](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/igraph/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [iguana](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/iguana/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [il2cpp_resolver](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/il2cpp_resolver/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [im3d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/im3d/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [imagemagick](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imagemagick/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [imath](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imath/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [imcoolbar](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imcoolbar/xmake.lua) | 含 Android 逻辑 | L11: on_install("windows", "linux", "macosx", "mingw", "android", "iphoneos", function (package) |
| [imgui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imgui/xmake.lua) | 含 Android 逻辑 | L115: add_configs("android",          {description = "Enable the android backend", default = false, type = "boolean"}); L221: android          = package:config("android"), |
| [imgui-color-text-edit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imgui-color-text-edit/xmake.lua) | 含 Android 逻辑 | L11: on_install("macosx", "linux", "windows", "mingw", "android", "iphoneos", function (package) |
| [imgui-file-dialog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imgui-file-dialog/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [imgui-filebrowser](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imgui-filebrowser/xmake.lua) | 含 Android 逻辑 | L13: on_install("macosx", "linux", "windows", "mingw", "android", "iphoneos", function (package) |
| [imgui-sfml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imgui-sfml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [imguitextselect](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imguitextselect/xmake.lua) | 含 Android 逻辑 | L29: on_install("windows", "linux", "macosx", "mingw", "android", "iphoneos", function (package) |
| [imguizmo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imguizmo/xmake.lua) | 含 Android 逻辑 | L32: on_install("macosx", "linux", "windows", "mingw", "android", "iphoneos", function (package) |
| [immer](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/immer/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [imnodes](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/imnodes/xmake.lua) | 含 Android 逻辑 | L13: on_install("windows", "linux", "macosx", "mingw", "android", "iphoneos", function (package) |
| [implot](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/implot/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [implot3d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/implot3d/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [incbin](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/incbin/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [indicators](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/indicators/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [infoware](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/infoware/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [inifile-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/inifile-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [inih](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/inih/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [iniparser](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/iniparser/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [inipp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/inipp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [inja](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/inja/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [injector](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/injector/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [innoextract](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/innoextract/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [innosetup](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/innosetup/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [interface99](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/interface99/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [intx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/intx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [iowow](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/iowow/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ip2region](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/ip2region/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [irrlicht](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/irrlicht/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [irrxml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/irrxml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [iso-codes](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/iso-codes/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [isocline](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/isocline/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ispc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/ispc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [itk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/itk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [itlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/itlib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [itstool](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/itstool/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ittapi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/ittapi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [iverilog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/iverilog/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ixwebsocket](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/i/ixwebsocket/xmake.lua) | 含 Android 逻辑 | L17: if is_plat("android", "iphoneos", "wasm") then |
| [jack2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jack2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jansson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jansson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jasper](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jasper/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jemalloc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jemalloc/xmake.lua) | 含 Android 逻辑 | L15: add_configs("prefix", {description = "Prefix to prepend to all public APIs", default = (is_plat("android") and "je_" or ""), type = "string"}); L29: if package:is_plat("android") and package:config("prefix") == "je_" then; L30: wprint("package(jemalloc): set API prefix to \"je_\" on Android to avoid C++ declaration conflicts.") |
| [jerryscript](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jerryscript/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jnif](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jnif/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jnipp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jnipp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [johnnyengine](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/johnnyengine/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [joltphysics](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/joltphysics/xmake.lua) | 含 Android 逻辑 | L30: add_patches("v2.0.1", path.join(os.scriptdir(), "patches", "v2.0.1", "android_fixes.patch"), "43b3d38ea5a01c281ad7b580859acaf0b30eac9a7bdc271a54199fcc88b8d491"); L190: on_install("windows", "mingw", "linux", "macosx", "iphoneos", "android", "wasm", "bsd", function (package) |
| [jom](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jom/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jpcre2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jpcre2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jrl-cmakemodules](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jrl-cmakemodules/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jrtplib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jrtplib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jsbsim](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jsbsim/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jsmn](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jsmn/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [json-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/json-c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [json-glib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/json-glib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [json-schema-validator](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/json-schema-validator/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [json.h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/json.h/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jsoncons](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jsoncons/xmake.lua) | 含 Android 逻辑 | L26: on_check("android", function (package) |
| [jsoncpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jsoncpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jthread](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jthread/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jwasm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jwasm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [jwt-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jwt-cpp/xmake.lua) | 含 Android 逻辑 | L38: on_install("windows", "linux", "macosx", "bsd", "mingw", "msys", "android", "cross", function (package) |
| [jxrlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/j/jxrlib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kahip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kahip/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kangaru](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kangaru/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kcp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kcp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kdbindings](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kdbindings/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kenlm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kenlm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [keynub_licdongle](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/keynub_licdongle/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [keystone](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/keystone/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [khaledhosny-ots](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/khaledhosny-ots/xmake.lua) | 含 Android 逻辑 | L34: on_install("!iphoneos and !mingw and !android", function (package) |
| [khrplatform](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/khrplatform/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kittymemory](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kittymemory/xmake.lua) | 含 Android 逻辑 | L3: set_description("This library aims for runtime code patching for both Android and iOS"); L23: on_install("android", "iphoneos", function (package); L24: io.replace("KittyMemory/KittyUtils.hpp", [[#ifdef __ANDROID__]], [[#ifdef __ANDROID__ |
| [kiwisolver](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kiwisolver/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [klib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/klib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kokkos](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kokkos/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kokkos-kernels](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kokkos-kernels/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kokyu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kokyu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kompute](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kompute/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kotlin-native](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kotlin-native/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [krabs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/krabs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [krb5](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/krb5/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ktx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/ktx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kuba-zip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kuba-zip/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [kvazaar](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/k/kvazaar/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lame](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lame/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lapack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lapack/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lastools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lastools/xmake.lua) | 含 Android 逻辑 | L17: on_check("android", function (package); L21: raise("package(lastools >= 2.0.5) does not support Android API levels earlier than 30") |
| [lazy_importer](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lazy_importer/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lbuild](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lbuild/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lcc-license-generator](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lcc-license-generator/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lcms](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lcms/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ldtkloader](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/ldtkloader/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [leancrypto](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/leancrypto/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lemon](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lemon/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [leptonica](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/leptonica/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lerc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lerc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [leveldb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/leveldb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lexbor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lexbor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lexy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lexy/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [liba52](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/liba52/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libaco](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libaco/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libaesgm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libaesgm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libaio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libaio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libarchive](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libarchive/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libargon2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libargon2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libass](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libass/xmake.lua) | 含 Android 逻辑 | L27: on_check("android", function (package) |
| [libassert](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libassert/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libatomic_ops](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libatomic_ops/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libavif](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libavif/xmake.lua) | 含 Android 逻辑 | L34: on_check("android", function (package) |
| [libb2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libb2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libbacktrace](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libbacktrace/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libbcrypt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libbcrypt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libbigwig](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libbigwig/xmake.lua) | 含 Android 逻辑 | L33: on_install("linux", "macosx", "bsd", "mingw", "msys", "android", "iphoneos", "cross", function (package) |
| [libbpf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libbpf/xmake.lua) | 含 Android 逻辑 | L16: on_check("android", function (package); L20: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 23, "package(libbpf) dep(libelf): need ndk api level >= 23 for android"); L23: assert(ndk_sdkver and tonumber(ndk_sdkver) == 23, "package(libbpf) dep(elfutils): need ndk api level == 23 for android") |
| [libbpg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libbpg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libbsd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libbsd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libc++](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libc++/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libcanberra](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libcanberra/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libcap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libcap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libcap-ng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libcap-ng/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libcbor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libcbor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libccd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libccd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libco](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libco/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libcoro](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libcoro/xmake.lua) | 含 Android 逻辑 | L64: on_install("!android", function (package) |
| [libcpuid](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libcpuid/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libcroco](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libcroco/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libcron](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libcron/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libcurl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libcurl/xmake.lua) | 含 Android 逻辑 | L18: add_patches("8.7.1", path.join(os.scriptdir(), "patches", "8.7.1", "android_armv7.patch"), "b172fd25063fcf4bce987b47a3d95d9d79bcf80f45e7e45dbf4aba72c685fb24"); L34: if is_plat("android") and is_host("windows") then; L43: if package:is_plat("linux", "bsd", "android", "cross") or needs_openssl_on_apple then |
| [libdatachannel](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdatachannel/xmake.lua) | 含 Android 逻辑 | L41: on_check("android", function (package) |
| [libdatrie](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdatrie/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libdc1394](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdc1394/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libde265](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libde265/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libdeflate](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdeflate/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libdicom](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdicom/xmake.lua) | 含 Android 逻辑 | L25: on_check("android", function (package) |
| [libdill](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdill/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libdisasm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdisasm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libdispatch](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdispatch/xmake.lua) | 含 Android 逻辑 | L34: if package:is_plat("android") then |
| [libdisplay-info](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdisplay-info/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libdivide](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdivide/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libdivsufsort](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdivsufsort/xmake.lua) | 含 Android 逻辑 | L3: set_homepage("https://android.googlesource.com/platform/external/libdivsufsort/"); L6: add_urls("https://android.googlesource.com/platform/external/libdivsufsort.git") |
| [libdom](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdom/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libdrm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdrm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libdwarf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libdwarf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libebur128](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libebur128/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libeconf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libeconf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libedit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libedit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libelf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libelf/xmake.lua) | 含 Android 逻辑 | L17: on_install("cross", "linux", "android", function (package); L26: if package:is_plat("android") then |
| [libelfin](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libelfin/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libenvpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libenvpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libepoxy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libepoxy/xmake.lua) | 含 Android 逻辑 | L47: on_install("!android and !bsd", function (package) |
| [libev](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libev/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libevdev](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libevdev/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libevent](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libevent/xmake.lua) | 含 Android 逻辑 | L29: on_install("!android and (!mingw or mingw&#124;!i386)", function (package) |
| [libfabric](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfabric/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libfacedetection](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfacedetection/xmake.lua) | 含 Android 逻辑 | L18: on_install("windows", "linux", "macosx", "bsd", "mingw", "msys", "android", "iphoneos", function (package) |
| [libffi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libffi/xmake.lua) | 含 Android 逻辑 | L36: on_install("windows", "iphoneos", "cross", "android", function (package) |
| [libfiber](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfiber/xmake.lua) | 含 Android 逻辑 | L17: on_install("linux", "macosx", "android", function (package) |
| [libfido2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfido2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libfive](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfive/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libfixmath](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfixmath/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libfixmatrix](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfixmatrix/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libflac](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libflac/xmake.lua) | 含 Android 逻辑 | L20: if is_plat("android") then; L21: add_patches("1.5.0", "patches/1.5.0/android_fseek.diff", "75377f3a309094d91ff2e56727df09a00baa23cbec44b03193253cfec9b5324a") |
| [libfork](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfork/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libfreenect2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfreenect2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libfswatch](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfswatch/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libfuse](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfuse/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libfyaml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libfyaml/xmake.lua) | 含 Android 逻辑 | L16: on_check("android", function (package); L23: on_install("linux", "macosx", "android", "iphoneos", "cross", function (package) |
| [libgcrypt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libgcrypt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libgd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libgd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libgda](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libgda/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libgeotiff](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libgeotiff/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libgit2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libgit2/xmake.lua) | 含 Android 逻辑 | L55: on_check("android", function (package); L82: if package:is_plat("android") then |
| [libgit2cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libgit2cpp/xmake.lua) | 含 Android 逻辑 | L21: on_check("android", function (package) |
| [libglvnd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libglvnd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libgpg-error](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libgpg-error/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libgpiod](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libgpiod/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libharu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libharu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libhat](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libhat/xmake.lua) | 含 Android 逻辑 | L33: on_check("android", function (package) |
| [libheif](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libheif/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libhubbub](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libhubbub/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libhv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libhv/xmake.lua) | 含 Android 逻辑 | L68: on_install("cross", "windows", "linux", "macosx", "android", "iphoneos", "mingw@windows", function(package) |
| [libice](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libice/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libiconv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libiconv/xmake.lua) | 含 Android 逻辑 | L36: on_install("windows", "mingw", "android", "iphoneos", function (package); L52: if package:is_plat("android") then |
| [libid3tag](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libid3tag/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libidn2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libidn2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libigl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libigl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libimagequant](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libimagequant/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libimobiledevice](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libimobiledevice/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libimobiledevice-glue](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libimobiledevice-glue/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libinterpolate](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libinterpolate/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libintl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libintl/xmake.lua) | 含 Android 逻辑 | L28: on_install("windows", "macosx", "bsd", "android", "mingw", function (package) |
| [libisl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libisl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libjpeg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libjpeg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libjpeg-turbo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libjpeg-turbo/xmake.lua) | 含 Android 逻辑 | L32: if is_plat("android") then; L45: on_install("windows", "linux", "macosx", "bsd", "android", "mingw", "cross", function (package) |
| [libjq](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libjq/xmake.lua) | 含 Android 逻辑 | L36: assert(not (package:is_plat("android") and is_subhost("windows")), "package(libjq): does not support windows@android.") |
| [libjuice](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libjuice/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libjxl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libjxl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libkdtree](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libkdtree/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libkeyfinder](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libkeyfinder/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libkmod](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libkmod/xmake.lua) | 含 Android 逻辑 | L27: on_check("android", function (package); L53: on_install("linux", "android@linux,macosx", function (package); L54: if package:is_plat("android") then |
| [liblas](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/liblas/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [liblifthttp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/liblifthttp/xmake.lua) | 含 Android 逻辑 | L13: on_install("linux", "macosx", "android", "iphoneos", function (package) |
| [libllvm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libllvm/xmake.lua) | 含 Android 逻辑 | L64: if is_plat("android") then; L151: on_install("linux", "macosx", "bsd", "android", "iphoneos", "cross", function (package); L252: if package:is_plat("android") then |
| [liblo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/liblo/xmake.lua) | 含 Android 逻辑 | L20: on_check("android", function (package) |
| [liblsl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/liblsl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmagic](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmagic/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmaxminddb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmaxminddb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmd/xmake.lua) | 含 Android 逻辑 | L14: on_install("linux", "android@linux,macosx", "cross", "bsd", "mingw", "wasm", function (package) |
| [libmem](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmem/xmake.lua) | 含 Android 逻辑 | L34: on_check("android", function(package); L37: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 24, "package(libmem): need ndk api level >= 24 for android"); L46: on_install("windows", "linux&#124;!arm64", "bsd", "mingw", "msys", "android", function (package) |
| [libmetalink](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmetalink/xmake.lua) | 含 Android 逻辑 | L12: on_install("windows", "linux", "macosx", "android", "mingw", "cross", function (package) |
| [libmill](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmill/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libminc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libminc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmng/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmobi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmobi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmodbus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmodbus/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmodplug](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmodplug/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmorton](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmorton/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmpdclient](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmpdclient/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmspack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmspack/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libmysofa](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libmysofa/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libnest2d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libnest2d/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libnet](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libnet/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libnfc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libnfc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libnl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libnl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libnpy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libnpy/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libnpy-matajoh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libnpy-matajoh/xmake.lua) | 含 Android 逻辑 | L22: if package:is_plat("android") and package:version() and package:version():ge("2.1.0") then |
| [libntl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libntl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libnyquist](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libnyquist/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [liboai](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/liboai/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libogg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libogg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libomp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libomp/xmake.lua) | 含 Android 逻辑 | L42: on_check("android", function (package); L55: on_install("macosx", "linux", "cross", "android", "mingw", "msys", "bsd", function (package) |
| [libopenmpt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libopenmpt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libopus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libopus/xmake.lua) | 含 Android 逻辑 | L57: if (package:is_plat("android") and package:is_arch("armeabi-v7a")) or package:is_plat("wasm") then; L80: elseif package:is_plat("android") then |
| [libopusenc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libopusenc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libopusfile](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libopusfile/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [liboqs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/liboqs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libp11](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libp11/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libp2p](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libp2p/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpam](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpam/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpaper](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpaper/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libparserutils](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libparserutils/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpcap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpcap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpciaccess](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpciaccess/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpcsclite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpcsclite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpeconv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpeconv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpfm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpfm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpg_query](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpg_query/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libplist](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libplist/xmake.lua) | 含 Android 逻辑 | L31: if not (is_subhost("windows") or package:is_plat("windows", "android", "wasm")) then; L43: if is_subhost("windows") or package:is_plat("windows", "android", "wasm") then |
| [libpng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpng/xmake.lua) | 含 Android 逻辑 | L50: if package:is_plat("android") and package:is_arch("armeabi-v7a") then |
| [libpopcnt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpopcnt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpq](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpq/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpqxx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpqxx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpsl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpsl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libpthread-stubs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libpthread-stubs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libqrencode](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libqrencode/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libraqm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libraqm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [librats](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/librats/xmake.lua) | 含 Android 逻辑 | L25: on_check("android", function (package); L71: if package:is_plat("android", "cross") then |
| [libraw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libraw/xmake.lua) | 含 Android 逻辑 | L27: on_check("android", function (package) |
| [librdkafka](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/librdkafka/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [librealsense](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/librealsense/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libredwg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libredwg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libremidi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libremidi/xmake.lua) | 含 Android 逻辑 | L38: on_check("android", function (package); L42: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 31, "package(libremidi): need ndk api level >= 31 for android") |
| [libressl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libressl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [librime](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/librime/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [librttopo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/librttopo/xmake.lua) | 含 Android 逻辑 | L21: on_check("android", function (package) |
| [libsais](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsais/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsamplerate](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsamplerate/xmake.lua) | 含 Android 逻辑 | L14: on_install("windows", "linux", "macosx", "iphoneos", "mingw", "android", function (package) |
| [libsdl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl2/xmake.lua) | 含 Android 逻辑 | L96: if is_plat("android") then; L115: if package:is_plat("linux", "android", "cross") then; L164: elseif package:is_plat("android") then |
| [libsdl2_gfx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl2_gfx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl2_image](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl2_image/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl2_mixer](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl2_mixer/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl2_mixer_x](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl2_mixer_x/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl2_net](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl2_net/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl2_ttf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl2_ttf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl3/xmake.lua) | 含 Android 逻辑 | L67: if package:is_plat("linux", "android", "cross") then; L104: elseif package:is_plat("android") then; L105: package:add("syslinks", "dl", "log", "android", "GLESv1_CM", "GLESv2", "OpenSLES") |
| [libsdl3_image](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl3_image/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl3_mixer](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl3_mixer/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl3_ttf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl3_ttf/xmake.lua) | 含 Android 逻辑 | L37: on_check("android", function (package) |
| [libsdl_gfx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl_gfx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl_image](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl_image/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl_mixer](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl_mixer/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl_net](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl_net/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsdl_ttf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsdl_ttf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libseccomp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libseccomp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libselinux](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libselinux/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsemanage](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsemanage/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsepol](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsepol/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsigc++](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsigc++/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsigcplusplus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsigcplusplus/xmake.lua) | 含 Android 逻辑 | L28: on_install("!android", function (package) |
| [libsimdpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsimdpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsmb2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsmb2/xmake.lua) | 含 Android 逻辑 | L20: on_check("android", function (package); L23: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 26, "package(libsmb2): need ndk api level >= 26 for android") |
| [libsndfile](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsndfile/xmake.lua) | 含 Android 逻辑 | L22: on_load("windows", "linux", "macosx", "iphoneos", "mingw", "android", function (package); L28: on_install("windows", "linux", "macosx", "iphoneos", "mingw", "android", function (package) |
| [libsndio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsndio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsodium](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsodium/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsolv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsolv/xmake.lua) | 含 Android 逻辑 | L174: if package:is_plat("android") and package:is_arch("armeabi-v7a") then |
| [libsoundio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsoundio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libspectre](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libspectre/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libspng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libspng/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsquish](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsquish/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libssh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libssh/xmake.lua) | 含 Android 逻辑 | L43: on_install("!android", function (package) |
| [libssh2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libssh2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libstatgrab](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libstatgrab/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsvgtiny](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsvgtiny/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsvm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsvm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libsystemd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libsystemd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libtask](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libtask/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libtasn1](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libtasn1/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libtcod](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libtcod/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libthai](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libthai/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libtiff](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libtiff/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libtins](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libtins/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libtomcrypt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libtomcrypt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libtommath](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libtommath/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libtool](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libtool/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libtorch](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libtorch/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libudev](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libudev/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libui/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libultrahdr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libultrahdr/xmake.lua) | 含 Android 逻辑 | L26: on_install("windows", "macosx", "linux", "mingw", "android", function (package) |
| [libunifex](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libunifex/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libunistring](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libunistring/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libunwind](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libunwind/xmake.lua) | 含 Android 逻辑 | L35: on_load("android", "linux", "bsd", "cross", function (package); L44: on_install("android&#124;arm64@linux,macosx", "linux", "bsd", "cross", function (package) |
| [liburing](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/liburing/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libusb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libusb/xmake.lua) | 含 Android 逻辑 | L31: elseif is_plat("android") then; L32: add_syslinks("android", "log") |
| [libusb-compat](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libusb-compat/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libusb-win32](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libusb-win32/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libusbmuxd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libusbmuxd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libuuid](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libuuid/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libuv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libuv/xmake.lua) | 含 Android 逻辑 | L48: on_check("android", function (package) |
| [libuvc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libuvc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libva](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libva/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libverto](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libverto/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libvips](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libvips/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libvorbis](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libvorbis/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libvpx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libvpx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libwapcaplet](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libwapcaplet/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libwebm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libwebm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libwebp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libwebp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libwebsockets](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libwebsockets/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libwfkafka](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libwfkafka/xmake.lua) | 含 Android 逻辑 | L29: on_install("linux", "macosx", "android", function (package) |
| [libx11](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libx11/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxau](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxau/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxaw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxaw/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxcb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxcb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxcomposite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxcomposite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxcrypt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxcrypt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxcursor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxcursor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxdamage](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxdamage/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxdmcp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxdmcp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxext](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxext/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxfixes](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxfixes/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxft](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxft/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxinerama](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxinerama/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxkbcommon](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxkbcommon/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxls](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxls/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxlsxwriter](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxlsxwriter/xmake.lua) | 含 Android 逻辑 | L29: on_check("android", function (package); L32: assert(ndk_sdkver and tonumber(ndk_sdkver) > 21, "package(libxlsxwriter): need ndk api level > 21 for android") |
| [libxmake](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxmake/xmake.lua) | 含 Android 逻辑 | L33: elseif is_plat("android") then |
| [libxml2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxml2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxmu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxmu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxnvctrl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxnvctrl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxpm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxpm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxrandr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxrandr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxrender](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxrender/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxshmfence](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxshmfence/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxslt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxslt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxss](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxss/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxtst](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxtst/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxvmc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxvmc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libxxf86vm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libxxf86vm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libyaml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libyaml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libyuv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libyuv/xmake.lua) | 含 Android 逻辑 | L29: on_check("android", function (package) |
| [libzchunk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libzchunk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [libzen](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libzen/xmake.lua) | 含 Android 逻辑 | L21: on_check("android", function (package); L25: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 24, "package(libzen/armeabi-v7a): need ndk api level >= 24 for android") |
| [libzip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libzip/xmake.lua) | 含 Android 逻辑 | L40: on_check("android", function (package) |
| [libzippp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/libzippp/xmake.lua) | 含 Android 逻辑 | L24: on_check("android", function (package) |
| [licensecc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/licensecc/xmake.lua) | 含 Android 逻辑 | L30: on_check("android", function (package); L32: raise("package(licensecc): does not support android build without freeifaddrs function.") |
| [lief](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lief/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lightgbm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lightgbm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lighthook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lighthook/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lightmapper](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lightmapper/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lightningscanner](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lightningscanner/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lilv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lilv/xmake.lua) | 含 Android 逻辑 | L44: on_install("!android", function (package) |
| [limonp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/limonp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [linalg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/linalg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [linenoise](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/linenoise/xmake.lua) | 含 Android 逻辑 | L11: on_install("linux", "macosx", "bsd", "wasm", "android", "cross", "iphoneos", function (package) |
| [linmath.h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/linmath.h/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [linux-headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/linux-headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [linux-syscall-support](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/linux-syscall-support/xmake.lua) | 含 Android 逻辑 | L12: on_install("android", "linux", "cross",  function (package) |
| [linux-tools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/linux-tools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [liquid-dsp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/liquid-dsp/xmake.lua) | 含 Android 逻辑 | L15: elseif is_plat("android") then; L21: on_check("android", function (package) |
| [litehtml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/litehtml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [littlefs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/littlefs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [llama.cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/llama.cpp/xmake.lua) | 含 Android 逻辑 | L28: on_check("android", function (package) |
| [llfio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/llfio/xmake.lua) | 含 Android 逻辑 | L26: if is_plat("android") then; L35: on_load("macosx", "iphoneos", "android", "linux", "windows", function(package); L62: on_install("macosx", "iphoneos", "android", "linux", "windows", function (package) |
| [llgl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/llgl/xmake.lua) | 含 Android 逻辑 | L11: if not is_plat("android", "iphoneos", "wasm", "bsd", "cross") then; L14: if is_plat("android", "iphoneos") then; L35: on_check("android", function (package) |
| [llhttp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/llhttp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [llvm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/llvm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [llvm-arm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/llvm-arm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [llvm-mingw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/llvm-mingw/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lmdb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lmdb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lockfree](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lockfree/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lodepng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lodepng/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [log4cplus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/log4cplus/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [loguru](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/loguru/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lolly](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lolly/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lrdf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lrdf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ls-hpack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/ls-hpack/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ls-qpack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/ls-qpack/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lsp-framework](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lsp-framework/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lsplt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lsplt/xmake.lua) | 含 Android 逻辑 | L3: set_description("Simple PLT hook for Android"); L27: on_install("android", function (package) |
| [lsquic](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lsquic/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lua](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lua/xmake.lua) | 含 Android 逻辑 | L45: if is_plat("iphoneos", "android") then |
| [lua-format](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lua-format/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [luabridge3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/luabridge3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [luajit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/luajit/xmake.lua) | 含 Android 逻辑 | L33: if package:is_plat("android") and package:is_arch("arm.*") and package:check_sizeof("void*") == "4" and is_host("windows") then; L34: raise("package(luajit/armeabi-v7a): Windows OS host is unsupported for android cross-compilation"); L48: on_install("windows", "mingw", "linux", "macosx", "bsd", "android", "iphoneos", function (package) |
| [luasocket](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/luasocket/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [luau](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/luau/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [luisa-compute](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/luisa-compute/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lunasvg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lunasvg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lunzip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lunzip/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lv2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lv2/xmake.lua) | 含 Android 逻辑 | L16: on_install("!android", function (package) |
| [lvgl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lvgl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lwlog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lwlog/xmake.lua) | 含 Android 逻辑 | L28: on_install("!android and !wasm and !bsd", function (package) |
| [lyra](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lyra/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lz4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lz4/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lzav](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lzav/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lzham_codec](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lzham_codec/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lzma](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lzma/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [lzo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/l/lzo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [m4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/m4/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [macdylibbundler](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/macdylibbundler/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [maddy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/maddy/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [magic_enum](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/magic_enum/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [magma](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/magma/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [magnum](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/magnum/xmake.lua) | 含 Android 逻辑 | L20: local applicationlibs = {"android", "emscripten", "glfw", "glx", "sdl2", "xegl", "windowlesscgl", "windowlessegl", "windowlessglx", "windowlessios", "windowlesswgl", "windowlesswindowsegl"}; L67: table.join2(links, {"MagnumAndroidApplication", "MagnumEmscriptenApplication", "MagnumGlfwApplication", "MagnumGlxApplication", "MagnumSdl2Application", "MagnumXEglApplication", "MagnumWindowlessCglApplication", "MagnumWindowlessEglApplication", "MagnumWindowlessGlxApplication", "MagnumWindowlessIosApplication", "MagnumWindowlessWglApplication", "MagnumWindowlessWindowsEglApplication"}) |
| [magnum-extras](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/magnum-extras/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [magnum-integration](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/magnum-integration/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [magnum-plugins](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/magnum-plugins/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mailio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mailio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [make](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/make/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [makeself](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/makeself/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mallocvis](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mallocvis/xmake.lua) | 含 Android 逻辑 | L18: on_install("!android and !wasm and !macosx and !iphoneos", function (package) |
| [managedc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/managedc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [manif](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/manif/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [manifold](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/manifold/xmake.lua) | 含 Android 逻辑 | L28: on_check("android", function (package); L31: assert(ndk_sdkver and tonumber(ndk_sdkver) >= 26, "package(manifold): need ndk api level >= 26 for android") |
| [mapbox_earcut](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mapbox_earcut/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mapbox_eternal](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mapbox_eternal/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mapbox_geometry](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mapbox_geometry/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mapbox_polylabel](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mapbox_polylabel/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mapbox_variant](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mapbox_variant/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [marchingcubecpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/marchingcubecpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mariadb-connector-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mariadb-connector-c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [marisa](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/marisa/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [marl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/marl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [matchit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/matchit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [materialx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/materialx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mathfu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mathfu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mathter](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mathter/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [matio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/matio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [matlab](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/matlab/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [matplotplusplus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/matplotplusplus/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mbedtls](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mbedtls/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mcfgthread](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mcfgthread/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mcut](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mcut/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [md4c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/md4c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [md4qt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/md4qt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mdns](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mdns/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mdspan](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mdspan/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mecab](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mecab/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [meet](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/meet/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [melon](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/melon/xmake.lua) | 含 Android 逻辑 | L25: on_install("!android", function (package) |
| [mem](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mem/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [memorymapping](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/memorymapping/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [memorymodulepp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/memorymodulepp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [memplumber](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/memplumber/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [meowhash](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/meowhash/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [meshoptimizer](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/meshoptimizer/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [meson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/meson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [metal-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/metal-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [metalang99](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/metalang99/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [metall](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/metall/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [metis](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/metis/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mfast](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mfast/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mhook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mhook/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [micro-gl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/micro-gl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [microprofile](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/microprofile/xmake.lua) | 含 Android 逻辑 | L20: on_install("windows", "linux", "macosx", "bsd", "android", "iphoneos", function (package) |
| [microsoft-apsi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/microsoft-apsi/xmake.lua) | 含 Android 逻辑 | L43: on_install("windows", "linux", "macosx", "bsd", "android", function (package) |
| [microsoft-detours](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/microsoft-detours/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [microsoft-gsl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/microsoft-gsl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [microsoft-kuku](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/microsoft-kuku/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [microsoft-proxy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/microsoft-proxy/xmake.lua) | 含 Android 逻辑 | L34: elseif package:is_plat("android") then |
| [microsoft-seal](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/microsoft-seal/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [microsoft-wtl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/microsoft-wtl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [microstl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/microstl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mikktspace](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mikktspace/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mimalloc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mimalloc/xmake.lua) | 含 Android 逻辑 | L50: elseif is_plat("android") then |
| [mingw-w64](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mingw-w64/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [minhook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/minhook/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mini](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mini/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [miniaudio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/miniaudio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [miniball](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/miniball/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [minifb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/minifb/xmake.lua) | 含 Android 逻辑 | L33: on_install("!android and !cross and !bsd", function (package) |
| [minilzo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/minilzo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [minimp3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/minimp3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [minio-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/minio-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [minitrace](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/minitrace/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [miniz](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/miniz/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [minizip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/minizip/xmake.lua) | 含 Android 逻辑 | L27: on_check("android", function (package) |
| [minizip-ng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/minizip-ng/xmake.lua) | 含 Android 逻辑 | L47: if package:is_plat("linux", "bsd", "android", "cross", "macosx", "iphoneos") then |
| [minja](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/minja/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mint](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mint/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mio/xmake.lua) | 含 Android 逻辑 | L13: on_install("windows", "linux", "macosx", "bsd", "iphoneos", "android", function (package) |
| [mir](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mir/xmake.lua) | 含 Android 逻辑 | L18: on_install("linux", "macosx", "android&#124;arm64-v8a", function (package) |
| [mjson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mjson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mkl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mkl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mlpack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mlpack/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mma](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mma/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mman_win32](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mman_win32/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mmeter](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mmeter/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mmkv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mmkv/xmake.lua) | 含 Android 逻辑 | L3: set_description("An efficient, small mobile key-value storage framework developed by WeChat. Works on Android, iOS, macOS, Windows, POSIX, and OHOS."); L17: elseif is_plat("android") then; L24: on_check("android", function (package) |
| [mmloader](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mmloader/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mnn](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mnn/xmake.lua) | 含 Android 逻辑 | L31: on_load("windows&#124;!arm*", "linux", "macosx", "android", "iphoneos&#124;!x86_64", function (package); L38: if package:is_plat("linux", "android", "cross") then; L68: on_install("windows&#124;!arm*", "linux", "macosx", "android", "iphoneos&#124;!x86_64", function (package) |
| [mold](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mold/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [moltenvk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/moltenvk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mongo-c-driver](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mongo-c-driver/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mongo-cxx-driver](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mongo-cxx-driver/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mongoose](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mongoose/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mono](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mono/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [moonjit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/moonjit/xmake.lua) | 含 Android 逻辑 | L26: on_install("windows", "linux", "macosx", "bsd", "android", "iphoneos", function (package) |
| [morton-nd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/morton-nd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mosquitto](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mosquitto/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mpc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mpc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mpdecimal](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mpdecimal/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mpfr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mpfr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mpg123](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mpg123/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mpich](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mpich/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mplib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mplib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mpmcqueue](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mpmcqueue/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mquickjs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mquickjs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mscharconv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mscharconv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msdf-atlas-gen](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msdf-atlas-gen/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msdfgen](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msdfgen/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msgpack-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msgpack-c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msgpack-cxx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msgpack-cxx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msgpack23](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msgpack23/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msmpi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msmpi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msquic](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msquic/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msvc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msvc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msvc-wine](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msvc-wine/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msys2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msys2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [msys2-base](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/msys2-base/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [muda](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/muda/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [muduo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/muduo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mujoco](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mujoco/xmake.lua) | 含 Android 逻辑 | L29: if package:is_plat("android") then; L189: if package:is_plat("android", "bsd", "mingw") then |
| [mujs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mujs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mumps](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mumps/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [munkres-algorithm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/munkres-algorithm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [muparserx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/muparserx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [muslcc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/muslcc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mustache](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mustache/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mvfst](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mvfst/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mxml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mxml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mysql](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mysql/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mysql-build-tools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mysql-build-tools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [mysqlpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/m/mysqlpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nam-core](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nam-core/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [named_type](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/named_type/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nameof](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nameof/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nana](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nana/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nanoarrow](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nanoarrow/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nanobench](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nanobench/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nanobind](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nanobind/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nanoflann](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nanoflann/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nanogui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nanogui/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nanomsg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nanomsg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nanopb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nanopb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nanosvg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nanosvg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nanovdb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nanovdb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nanovg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nanovg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nasm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nasm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nativefiledialog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nativefiledialog/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nativefiledialog-extended](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nativefiledialog-extended/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nazarautils](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nazarautils/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ncnn](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/ncnn/xmake.lua) | 含 Android 逻辑 | L33: if is_plat("android") then; L34: add_syslinks("android"); L38: on_check("android", function (package) |
| [ncurses](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/ncurses/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ndarray](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/ndarray/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ndicapi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/ndicapi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ndk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/ndk/xmake.lua) | 含 Android 逻辑 | L3: set_homepage("https://developer.android.com/ndk"); L4: set_description("Android NDK toolchain."); L7: set_urls("https://dl.google.com/android/repository/android-ndk-$(version).zip", {version = function(version) |
| [neargye-scope_guard](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/neargye-scope_guard/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [neco](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/neco/xmake.lua) | 含 Android 逻辑 | L24: on_install("linux", "mingw&#124;x86_64", "windows", "bsd", "android", "iphoneos", function (package); L26: "#if defined(__linux__) && !defined(_GNU_SOURCE) && !defined(__ANDROID__)", {plain = true}) |
| [netcdf-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/netcdf-c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nettle](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nettle/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [newtondynamics](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/newtondynamics/xmake.lua) | 含 Android 逻辑 | L16: if is_plat("linux", "android") then; L32: if not package:config("shared") and package:is_plat("linux", "android") and package:config("pic") ~= false then |
| [newtondynamics3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/newtondynamics3/xmake.lua) | 含 Android 逻辑 | L16: if is_plat("linux", "android") then; L31: if not package:config("shared") and package:is_plat("linux", "android") and package:config("pic") ~= false then |
| [newtondynamics4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/newtondynamics4/xmake.lua) | 含 Android 逻辑 | L20: if is_plat("linux", "android") then |
| [ng-log](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/ng-log/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nghttp2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nghttp2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nghttp3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nghttp3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ngtcp2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/ngtcp2/xmake.lua) | 含 Android 逻辑 | L39: on_install("macosx", "linux", "windows", "android", "mingw", function (package) |
| [nifly](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nifly/xmake.lua) | 含 Android 逻辑 | L13: on_install("windows", "linux", "bsd", "macos", "android", "iphoneos", function (package) |
| [nifti](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nifti/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [niftiheader](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/niftiheader/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nim](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nim/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ninja](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/ninja/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nlohmann_json](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nlohmann_json/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nlopt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nlopt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nmd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nmd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nng/xmake.lua) | 含 Android 逻辑 | L61: on_install("windows", "linux", "macosx", "android", "iphoneos", "cross", function(package) |
| [nngpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nngpp/xmake.lua) | 含 Android 逻辑 | L11: on_install("windows", "linux", "macosx", "android", "iphoneos", "cross", function (package) |
| [nod](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nod/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [node-addon-api](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/node-addon-api/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [node-api-headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/node-api-headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [node-api-stub](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/node-api-stub/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [node_crunch2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/node_crunch2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nodeeditor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nodeeditor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nodesoup](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nodesoup/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [noise-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/noise-c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [noisy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/noisy/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nowide_standalone](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nowide_standalone/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [npcap_sdk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/npcap_sdk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nri](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nri/xmake.lua) | 含 Android 逻辑 | L36: on_check("android", function (package); L37: assert(package:version() and package:version():lt("180"), "package(nri >=v180): unsupport android"); L69: on_install("!wasm and !bsd and (!windows or windows&#124;!x86) and (!android or android&#124;!armeabi-v7a)", function(package) |
| [nsis](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nsis/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nsync](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nsync/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ntkernel-error-category](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/ntkernel-error-category/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nuklear](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nuklear/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [numactl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/numactl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [numcpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/numcpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nv-codec-headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nv-codec-headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nvapi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nvapi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nvtt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nvtt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nvtx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nvtx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [nzsl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/n/nzsl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [oatpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/oatpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [oatpp-openssl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/oatpp-openssl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [oatpp-websocket](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/oatpp-websocket/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [obfuscate](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/obfuscate/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [obfusheader.h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/obfusheader.h/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [objfw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/objfw/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [oboe](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/oboe/xmake.lua) | 含 Android 逻辑 | L3: set_description("Oboe is a C++ library that makes it easy to build high-performance audio apps on Android."); L19: on_install("android", function (package); L21: io.replace("CMakeLists.txt", "LIBRARY DESTINATION lib/${ANDROID_ABI}", "LIBRARY DESTINATION lib", {plain = true}) |
| [observer-ptr-lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/observer-ptr-lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ocilib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/ocilib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [octomap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/octomap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [octree](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/octree/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ode](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/ode/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [offsetallocator](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/offsetallocator/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ogre-next](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/ogre-next/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ois](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/ois/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [olive.c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/olive.c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [omath](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/omath/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ompl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/ompl/xmake.lua) | 含 Android 逻辑 | L34: on_check("android", function (package); L36: raise("package(ompl >= 2.0.0): unsupport android") |
| [onednn](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/onednn/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [onedpl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/onedpl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [oneshot](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/oneshot/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [oniguruma](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/oniguruma/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [onnx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/onnx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [onnxruntime](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/onnxruntime/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [open3d](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/open3d/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openai-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openai-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openal-soft](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openal-soft/xmake.lua) | 含 Android 逻辑 | L40: elseif is_plat("android") then; L52: on_install("windows", "linux", "mingw", "macosx", "android", "iphoneos", "cross", "bsd" , function (package) |
| [openblas](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openblas/xmake.lua) | 含 Android 逻辑 | L92: on_check("android", function (package) |
| [opencascade](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opencascade/xmake.lua) | 含 Android 逻辑 | L160: ["CSF_androidlog"]    = package:is_plat("android")   and { syslinks = {"log"} } or nil, |
| [opencc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opencc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [opencl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opencl/xmake.lua) | 含 Android 逻辑 | L91: on_install("linux", "macosx", "android", function (package) |
| [opencl-clhpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opencl-clhpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [opencl-headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opencl-headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [opencolorio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opencolorio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [opencore-amr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opencore-amr/xmake.lua) | 含 Android 逻辑 | L9: on_install("linux", "macosx", "android", "iphoneos", "bsd", "cross", "mingw", function (package) |
| [opencv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opencv/xmake.lua) | 含 Android 逻辑 | L98: on_load("android", "linux", "macosx", "windows", "mingw@windows,msys", function (package); L113: elseif package:is_plat("android") then; L164: on_install("android", "linux", "macosx", "windows", "mingw@windows,msys", function (package) |
| [opencv-mobile](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opencv-mobile/xmake.lua) | 含 Android 逻辑 | L3: set_description("The minimal opencv for Android, iOS, ARM Linux, Windows, Linux, MacOS, WebAssembly"); L75: if not is_plat("android", "iphoneos") then; L80: on_check("android", function (package) |
| [openexr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openexr/xmake.lua) | 含 Android 逻辑 | L61: on_check("android", function (package) |
| [openfbx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openfbx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [opengl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opengl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [opengl-headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opengl-headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openh264](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openh264/xmake.lua) | 含 Android 逻辑 | L21: on_check("android", function (package) |
| [openimagedenoise](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openimagedenoise/xmake.lua) | 含 Android 逻辑 | L75: on_install("!android and !wasm", function (package) |
| [openimageio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openimageio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openjdk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openjdk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openjpeg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openjpeg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openjph](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openjph/xmake.lua) | 含 Android 逻辑 | L31: on_check("android", function (package) |
| [openldap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openldap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openmesh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openmesh/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openmp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openmp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openmvg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openmvg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openmvs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openmvs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openpgl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openpgl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openrestry-luajit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openrestry-luajit/xmake.lua) | 含 Android 逻辑 | L28: on_install("windows", "linux", "macosx", "bsd", "android", "iphoneos", function (package) |
| [openscenegraph](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openscenegraph/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openssh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openssh/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openssl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openssl/xmake.lua) | 含 Android 逻辑 | L32: if package:is_plat("android") and is_subhost("windows") and os.arch() == "x64" then; L117: on_install("linux", "macosx", "bsd", "cross", "android", "iphoneos", "mingw", "harmony", function (package); L181: if package:is_plat("cross", "android") then |
| [openssl3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openssl3/xmake.lua) | 含 Android 逻辑 | L83: elseif package:is_plat("android", "wasm") and is_host("windows") and os.arch() == "x64" then; L236: on_install("macosx", "linux", "cross", "android", "iphoneos", "wasm", "harmony", function (package); L297: if (package:is_plat("android") and is_host("windows")) or |
| [openssl4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openssl4/xmake.lua) | 含 Android 逻辑 | L44: elseif package:is_plat("android", "wasm") and is_host("windows") and os.arch() == "x64" then; L132: on_install("macosx", "bsd", "linux", "cross", "android", "iphoneos", "wasm", "harmony", function (package); L185: if (package:is_plat("android") and is_host("windows")) or |
| [opensubdiv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opensubdiv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [opentelemetry-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/opentelemetry-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openvdb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openvdb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openvpn3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openvpn3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openvr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openvr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openxlsx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openxlsx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [openxr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/openxr/xmake.lua) | 含 Android 逻辑 | L29: elseif is_plat("android") then; L37: elseif is_plat("android") then; L38: add_syslinks("log", "android") |
| [optick](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/optick/xmake.lua) | 含 Android 逻辑 | L22: on_install("windows&#124;x86", "windows&#124;x64", "linux", "macosx", "android", "cross", function (package) |
| [optional-lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/optional-lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [optix](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/optix/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [or-tools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/or-tools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [orangeduck_mpc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/orangeduck_mpc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [orc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/orc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ordered_map](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/ordered_map/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ormpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/ormpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [orocos-kdl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/orocos-kdl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [osip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/osip/xmake.lua) | 含 Android 逻辑 | L85: on_install("linux", "macosx", "bsd", "android@linux,macosx", "iphoneos", "cross", "wasm", function (package); L92: if package:is_plat("android") then |
| [osmanip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/osmanip/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [osqp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/osqp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [out_ptr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/out_ptr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [outcome](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/outcome/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ozz-animation](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/o/ozz-animation/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [p11-kit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/p11-kit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pagmo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pagmo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pahomqttc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pahomqttc/xmake.lua) | 含 Android 逻辑 | L23: elseif is_plat("android") then |
| [pahomqttcpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pahomqttcpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pango](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pango/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pangomm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pangomm/xmake.lua) | 含 Android 逻辑 | L42: on_install("!android and !bsd and !iphoneos and !wasm and (!windows or windows&#124;!arm*)", function (package) |
| [papi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/papi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [par](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/par/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [parallel-hashmap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/parallel-hashmap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [partio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/partio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [patch](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/patch/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [patchelf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/patchelf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [paul_thread_pool](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/paul_thread_pool/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pca9685](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pca9685/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pcapplusplus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pcapplusplus/xmake.lua) | 含 Android 逻辑 | L44: elseif package:is_plat("linux", "macosx", "android", "bsd") then; L51: on_install("windows", "mingw", "linux", "macosx", "android", "bsd", function (package) |
| [pcg-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pcg-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pcg32](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pcg32/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pciutils](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pciutils/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pcl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pcl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pcre](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pcre/xmake.lua) | 含 Android 逻辑 | L23: on_install("android", "windows", function (package); L30: if package:is_plat("android") then |
| [pcre2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pcre2/xmake.lua) | 含 Android 逻辑 | L24: on_check("android", function (package) |
| [pdcurses](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pdcurses/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pdcursesmod](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pdcursesmod/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pdfhummus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pdfhummus/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pdfio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pdfio/xmake.lua) | 含 Android 逻辑 | L31: on_check("android", function (package) |
| [pe-parse](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pe-parse/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pedeps](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pedeps/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pegtl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pegtl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [peloader](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/peloader/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [perlinnoise](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/perlinnoise/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pffft](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pffft/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [phnt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/phnt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [physfs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/physfs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [picobench](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/picobench/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [picojson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/picojson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [picosha2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/picosha2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [piex](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/piex/xmake.lua) | 含 Android 逻辑 | L13: on_install("macosx", "linux", "windows", "mingw", "android", "iphoneos", function (package) |
| [pigpio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pigpio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pigz](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pigz/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pine](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pine/xmake.lua) | 含 Android 逻辑 | L11: on_install("android", function (package); L36: "android.cpp", |
| [pinocchio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pinocchio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pipewire](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pipewire/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pixman](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pixman/xmake.lua) | 含 Android 逻辑 | L51: if package:is_plat("android") then; L54: local cpu_features = path.join(ndk, "sources", "android", "cpufeatures") |
| [pkg-config](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pkg-config/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pkgconf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pkgconf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pl_mpeg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pl_mpeg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [platformfolders](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/platformfolders/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plf_colony](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plf_colony/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plf_hive](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plf_hive/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plf_indiesort](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plf_indiesort/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plf_list](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plf_list/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plf_nanotimer](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plf_nanotimer/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plf_queue](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plf_queue/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plf_rand](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plf_rand/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plf_reorderase](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plf_reorderase/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plf_stack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plf_stack/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plfit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plfit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plog/xmake.lua) | 含 Android 逻辑 | L16: if is_plat("android") then |
| [plotlypp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plotlypp/xmake.lua) | 含 Android 逻辑 | L14: on_check("android", function (package) |
| [plusaes](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plusaes/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plutosvg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plutosvg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [plutovg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/plutovg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pmp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pmp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pocketfft](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pocketfft/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pocketpy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pocketpy/xmake.lua) | 含 Android 逻辑 | L24: on_install("windows&#124;x64", "linux", "macosx", "android", function (package); L31: on_test("linux", "macosx", "android", function (package) |
| [poco](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/poco/xmake.lua) | 含 Android 逻辑 | L111: elseif package:is_plat("android") then |
| [policycoreutils](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/policycoreutils/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [poly2tri](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/poly2tri/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [polyclipping](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/polyclipping/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [polyhook2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/polyhook2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [polyscope](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/polyscope/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [poppler](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/poppler/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [popt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/popt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [portable_build_tools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/portable_build_tools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [portaudio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/portaudio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [portmidi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/portmidi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [poselib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/poselib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [postgresql](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/postgresql/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ppqsort](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/ppqsort/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pprint](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pprint/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pqp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pqp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [premake5](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/premake5/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [process-dump](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/process-dump/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [proj](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/proj/xmake.lua) | 含 Android 逻辑 | L51: on_install("!wasm and (!android or android@!windows)", function (package) |
| [prometheus-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/prometheus-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [promise-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/promise-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [protobuf-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/protobuf-c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [protobuf-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/protobuf-cpp/xmake.lua) | 含 Android 逻辑 | L56: add_configs("upb", {description = "Build upb", default = not is_plat("android"), type = "boolean"}); L57: add_configs("tools", {description = "Build libprotoc and protoc compiler", default = not is_plat("android"), type = "boolean"}); L84: if package:is_plat("android") and is_host("windows") then |
| [protoc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/protoc/xmake.lua) | 含 Android 逻辑 | L6: if is_plat("android") then |
| [proxygen](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/proxygen/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [prvhash](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/prvhash/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pseudo-double-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pseudo-double-c/xmake.lua) | 含 Android 逻辑 | L13: on_install("windows&#124;x64", "linux&#124;x86_64", "macosx", "bsd", "android&#124;arm64*", "wasm", function (package) |
| [pseudo-double-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pseudo-double-cpp/xmake.lua) | 含 Android 逻辑 | L17: on_install("windows&#124;x64", "linux&#124;x86_64", "bsd", "android&#124;arm64*", function (package) |
| [psimd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/psimd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ptex](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/ptex/xmake.lua) | 含 Android 逻辑 | L23: on_check("android", function (package); L26: assert(ndk_sdkver and tonumber(ndk_sdkver) > 21, "package(ptex): need ndk api level > 21 for android") |
| [pthreadpool](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pthreadpool/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pthreads4w](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pthreads4w/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ptl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/ptl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pugixml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pugixml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pulsar](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pulsar/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pulseaudio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pulseaudio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pupnp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pupnp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pybind11](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pybind11/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pycdc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pycdc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pyincpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pyincpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [pystring](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/pystring/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [python](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/python/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [python-launcher](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/python-launcher/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [python2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/p/python2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qbdi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qbdi/xmake.lua) | 含 Android 逻辑 | L14: if is_plat("android", "iphoneos") then; L26: add_patches("v0.12.0", "patches/v0.12.0/fix-build-android-x86-64.patch", "69cc15efa38fd36547d4f5261a5e1aac6dd02aa183e2c13552dbce140ef4ad2f"); L30: android = "android", |
| [qcbor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qcbor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qdcae](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qdcae/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qdldl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qdldl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qengine](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qengine/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qhull](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qhull/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qjson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qjson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qmsetup](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qmsetup/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qoa](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qoa/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qoi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qoi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qpoases](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qpoases/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qr-code-generator-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qr-code-generator-c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qr-code-generator-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qr-code-generator-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qt-tools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt-tools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qt5base](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt5base/xmake.lua) | 含 Android 逻辑 | L8: on_install("windows&#124;x86", "windows&#124;x64", "linux", "macosx", "mingw", "android", "iphoneos", function (package, opt) |
| [qt5core](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt5core/xmake.lua) | 含 Android 逻辑 | L7: if package:is_plat("android") then |
| [qt5gui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt5gui/xmake.lua) | 含 Android 逻辑 | L9: if package:is_plat("android") then |
| [qt5lib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt5lib/xmake.lua) | 含 Android 逻辑 | L35: elseif package:is_plat("android") then; L74: on_install("windows&#124;x86", "windows&#124;x64", "linux", "macosx", "mingw", "android", "iphoneos", function (package) |
| [qt5network](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt5network/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qt5webview](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt5webview/xmake.lua) | 含 Android 逻辑 | L12: on_install("windows&#124;x86", "windows&#124;x64", "linux", "macosx", "android", "iphoneos", function (package) |
| [qt5widgets](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt5widgets/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qt6base](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt6base/xmake.lua) | 含 Android 逻辑 | L35: on_install("android&#124;arm64-v8a,armeabi-v7a,armeabi,x86_64,x86@windows,linux,macosx", function (package) |
| [qt6core](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt6core/xmake.lua) | 含 Android 逻辑 | L7: if package:is_plat("android") then |
| [qt6gui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt6gui/xmake.lua) | 含 Android 逻辑 | L11: elseif package:is_plat("android") then |
| [qt6lib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt6lib/xmake.lua) | 含 Android 逻辑 | L64: elseif package:is_plat("android") then; L108: on_install("android&#124;arm64-v8a,armeabi-v7a,armeabi,x86_64,x86@windows,linux,macosx", function (package) |
| [qt6network](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt6network/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qt6qml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt6qml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qt6quick](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt6quick/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qt6widgets](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qt6widgets/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qtawesome](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qtawesome/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qtbase](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qtbase/xmake.lua) | 含 Android 逻辑 | L151: elseif package:is_plat("android") then; L171: elseif package:is_plat("android") then; L172: target = "android" |
| [qtifw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qtifw/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qtpromise](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qtpromise/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [quadsort](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/quadsort/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [quake_triangle](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/quake_triangle/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [quantlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/quantlib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [quickcpplib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/quickcpplib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [quickjs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/quickjs/xmake.lua) | 含 Android 逻辑 | L18: elseif is_plat("android") then; L30: on_install("linux", "macosx", "iphoneos", "android", "mingw", "cross", function (package) |
| [quickjs-ng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/quickjs-ng/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [quickjspp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/quickjspp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [quill](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/quill/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [quirc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/quirc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [qwindowkit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/q/qwindowkit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [radeonrays](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/radeonrays/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ragel](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/ragel/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [randx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/randx/xmake.lua) | 含 Android 逻辑 | L21: #if defined(__ANDROID__) && __ANDROID_API__ < 28 |
| [rang](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rang/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [range-v3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/range-v3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rapidcsv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rapidcsv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rapidfuzz](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rapidfuzz/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rapidhash](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rapidhash/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rapidjson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rapidjson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rapidobj](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rapidobj/xmake.lua) | 含 Android 逻辑 | L17: on_check("android", function (package); L20: assert(ndk_sdkver and tonumber(ndk_sdkver) > 21, "package(rapidobj): need ndk api level  > 21 for android") |
| [rapidxml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rapidxml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [raptor2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/raptor2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [raw_pdb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/raw_pdb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [raygui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/raygui/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [raylib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/raylib/xmake.lua) | 含 Android 逻辑 | L52: elseif is_plat("android") then; L53: add_syslinks("log", "android", "EGL", "GLESv2", "OpenSLES", "m"); L63: on_install("windows", "linux", "macosx&#124;arm64", "mingw", "wasm", "android", function (package) |
| [raylib-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/raylib-cpp/xmake.lua) | 含 Android 逻辑 | L27: on_install("windows", "linux", "macosx", "mingw", "wasm", "android", function (package) |
| [rcmp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rcmp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [re-flex](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/re-flex/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [re-spirv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/re-spirv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [re2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/re2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [re2c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/re2c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [reaction](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/reaction/xmake.lua) | 含 Android 逻辑 | L13: if package:is_plat("android") then |
| [reactiveplusplus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/reactiveplusplus/xmake.lua) | 含 Android 逻辑 | L21: if package:is_plat("android") then; L36: if package:is_plat("android") then |
| [readerwriterqueue](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/readerwriterqueue/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [readline](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/readline/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [recastnavigation](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/recastnavigation/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [reckless](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/reckless/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [redex](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/redex/xmake.lua) | 含 Android 逻辑 | L3: set_description("A bytecode optimizer for Android apps") |
| [redis-plus-plus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/redis-plus-plus/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [reflect-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/reflect-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [remotery](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/remotery/xmake.lua) | 含 Android 逻辑 | L21: on_install("windows&#124;x64", "linux", "macosx", "bsd", "mingw&#124;x86_64", "msys", "android", "iphoneos", "cross", function (package) |
| [rendergraph](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rendergraph/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [replxx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/replxx/xmake.lua) | 含 Android 逻辑 | L12: on_check("android", function (package) |
| [reproc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/reproc/xmake.lua) | 含 Android 逻辑 | L33: if package:config("multithreaded") and not package:is_plat("windows", "android") then |
| [resiprocate](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/resiprocate/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rest_rpc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rest_rpc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [restinio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/restinio/xmake.lua) | 含 Android 逻辑 | L34: on_install("windows", "linux", "macosx", "bsd", "mingw", "msys", "android", "iphoneos", "cross", function (package) |
| [rewolf-wow64ext](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rewolf-wow64ext/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rgfw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rgfw/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rhash](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rhash/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ricab-scope_guard](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/ricab-scope_guard/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ring-span-lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/ring-span-lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [riscv32-esp-elf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/riscv32-esp-elf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rlimgui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rlimgui/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rlottie](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rlottie/xmake.lua) | 含 Android 逻辑 | L26: on_install("windows", "linux", "macosx", "android&#124;arm64*", "wasm", function (package) |
| [rmlui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rmlui/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [robin-hood-hashing](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/robin-hood-hashing/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [robin-map](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/robin-map/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [robotstxt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/robotstxt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rocket](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rocket/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rocksdb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rocksdb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rpclib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rpclib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rply](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rply/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rpm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rpm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rpmalloc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rpmalloc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rsm-autotoml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rsm-autotoml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rsm-binary-io](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rsm-binary-io/xmake.lua) | 含 Android 逻辑 | L11: on_install("windows", "linux", "macosx", "iphoneos", "android", "bsd", "wasm", "cross", function (package) |
| [rsm-bsa](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rsm-bsa/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rsm-mmio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rsm-mmio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rsync](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rsync/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rtaudio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rtaudio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rtm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rtm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rtmidi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rtmidi/xmake.lua) | 含 Android 逻辑 | L25: elseif is_plat("android") then |
| [rttr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rttr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ruapu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/ruapu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rubberband](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rubberband/xmake.lua) | 含 Android 逻辑 | L59: on_install("!android", function (package) |
| [rust](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rust/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rustlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rustlib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [rustup](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rustup/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ruy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/ruy/xmake.lua) | 含 Android 逻辑 | L17: on_install("windows", "linux", "macosx", "android", function (package) |
| [rxcpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/r/rxcpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [s2n-tls](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/s2n-tls/xmake.lua) | 含 Android 逻辑 | L44: on_install("linux", "bsd", "cross", "android", "macosx&#124;arm64", function (package) |
| [s7](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/s7/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [safetyhook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/safetyhook/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sailormoon_flags](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sailormoon_flags/xmake.lua) | 含 Android 逻辑 | L12: on_check("android", function (package) |
| [samurai](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/samurai/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [scnlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/scnlib/xmake.lua) | 含 Android 逻辑 | L56: on_install("!android and !iphoneos and !wasm", function (package) |
| [scons](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/scons/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [scotch](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/scotch/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [screen_capture_lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/screen_capture_lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sdformat](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sdformat/xmake.lua) | 含 Android 逻辑 | L22: on_check("android&#124;armeabi-v7a", function (package) |
| [sdl2webgpu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sdl2webgpu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sdl3webgpu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sdl3webgpu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sdsl-lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sdsl-lite/xmake.lua) | 含 Android 逻辑 | L21: on_install("linux", "macosx", "bsd", "android", "iphoneos", "cross", function (package) |
| [seacas](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/seacas/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [seasocks](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/seasocks/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [secilc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/secilc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [semi-static-conditions](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/semi-static-conditions/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [semver](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/semver/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sentencepiece](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sentencepiece/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sentry-native](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sentry-native/xmake.lua) | 含 Android 逻辑 | L60: elseif is_plat("android") then; L107: on_install("windows&#124;x86", "windows&#124;x64", "linux", "macosx&#124;x86_64", function (package) -- TODO: to enable android you will need to figure out the order of libs |
| [seqan3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/seqan3/xmake.lua) | 含 Android 逻辑 | L47: if package:is_plat("android") then; L76: on_install("linux", "macosx", "bsd", "android", "iphoneos", "cross", function (package) |
| [serd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/serd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [serial](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/serial/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sfgui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sfgui/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sfl-library](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sfl-library/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sfml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sfml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sfntly](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sfntly/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sfparse](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sfparse/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sha2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sha2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [shaderc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/shaderc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [shaderwriter](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/shaderwriter/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [shadowhook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/shadowhook/xmake.lua) | 含 Android 逻辑 | L2: set_homepage("https://github.com/bytedance/android-inline-hook/tree/main/doc"); L3: set_description("ShadowHook is an Android inline hook library which supports thumb, arm32 and arm64."); L6: add_urls("https://github.com/bytedance/android-inline-hook/archive/refs/tags/$(version).tar.gz", |
| [shared-mime-info](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/shared-mime-info/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sheenbidi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sheenbidi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sigslot](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sigslot/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simage](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simage/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simbody](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simbody/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simdcomp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simdcomp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simde](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simde/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simdjson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simdjson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simdutf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simdutf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simple_http](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simple_http/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simplecpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simplecpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simpleini](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simpleini/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simplethreadpool](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simplethreadpool/xmake.lua) | 含 Android 逻辑 | L20: on_install("linux", "macosx", "windows", "bsd", "android", "iphoneos", "cross", function (package) |
| [simplewindow](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simplewindow/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [simsimd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/simsimd/xmake.lua) | 含 Android 逻辑 | L31: on_check("android", function (package) |
| [sjpeg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sjpeg/xmake.lua) | 含 Android 逻辑 | L24: if package:is_plat("android") then; L26: table.insert(configs, "-DSJPEG_ANDROID_NDK_PATH=" .. ndk) |
| [skia](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/skia/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [slang](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/slang/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sleef](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sleef/xmake.lua) | 含 Android 逻辑 | L73: if package:is_cross() and package:is_plat("android") and package:arch():find("^arm") and not package:arch():find("arm64") then; L76: 'set(CLANG_FLAGS_ENABLE_NEON32 "--target=arm-linux-gnueabihf;-mcpu=cortex-a8")\nif(ANDROID)\n  list(FILTER CLANG_FLAGS_ENABLE_NEON32 EXCLUDE REGEX "^--target")\nendif()', |
| [slikenet](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/slikenet/xmake.lua) | 含 Android 逻辑 | L29: on_check("android", function (package); L43: elseif package:is_plat("android") then |
| [smoothcpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/smoothcpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [snappy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/snappy/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [snitch](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/snitch/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [snmalloc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/snmalloc/xmake.lua) | 含 Android 逻辑 | L31: on_check("android", function (package) |
| [snowhouse](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/snowhouse/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sobjectizer](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sobjectizer/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [soci](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/soci/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [socket-io-client](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/socket-io-client/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sockpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sockpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [soil2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/soil2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sokol](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sokol/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sokol-tools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sokol-tools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sol2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sol2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [soloud](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/soloud/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sonic-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sonic-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sophus](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sophus/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [soplex](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/soplex/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sord](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sord/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [soundtouch](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/soundtouch/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [soxr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/soxr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [span-lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/span-lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sparse-map](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sparse-map/xmake.lua) | 含 Android 逻辑 | L14: on_install("windows&#124;x86", "windows&#124;x64", "linux", "macosx", "bsd", "mingw", "msys", "android", "iphoneos", "cross", function (package) |
| [sparsepp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sparsepp/xmake.lua) | 含 Android 逻辑 | L10: on_install("linux", "macosx", "bsd", "windows", "android", "iphoneos", "cross", "mingw", function (package) |
| [spdlog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/spdlog/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [spectra](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/spectra/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [speex](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/speex/xmake.lua) | 含 Android 逻辑 | L16: on_install("linux", "macosx", "bsd", "mingw", "wasm", "cross", "iphoneos", "android@linux,macosx", function (package) |
| [spine-runtimes](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/spine-runtimes/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [spirv-cross](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/spirv-cross/xmake.lua) | 含 Android 逻辑 | L33: on_install("windows", "linux", "macosx", "mingw", "android", "wasm", function (package) |
| [spirv-headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/spirv-headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [spirv-reflect](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/spirv-reflect/xmake.lua) | 含 Android 逻辑 | L27: on_install("windows", "linux", "macosx", "mingw", "android", function (package) |
| [spirv-tools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/spirv-tools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [spot](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/spot/xmake.lua) | 含 Android 逻辑 | L19: on_check("android", function (package); L24: on_install("linux", "macosx", "android@linux,macosx", "cross", "bsd", "mingw", "msys", function (package) |
| [sqlcipher](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sqlcipher/xmake.lua) | 含 Android 逻辑 | L39: elseif is_plat("android") then |
| [sqlgen](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sqlgen/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sqlite-vec](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sqlite-vec/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sqlite3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sqlite3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sqlite3-lemon](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sqlite3-lemon/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sqlite_orm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sqlite_orm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sqlitecpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sqlitecpp/xmake.lua) | 含 Android 逻辑 | L15: if is_plat("android", "wasm") then |
| [sqlpp11](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sqlpp11/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sqlpp23](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sqlpp23/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sqrat](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sqrat/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [squirrel](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/squirrel/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sratom](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sratom/xmake.lua) | 含 Android 逻辑 | L32: on_install("!android", function (package) |
| [srell](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/srell/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [srpc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/srpc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [srt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/srt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [srtp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/srtp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sse2neon](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sse2neon/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sse2rvv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sse2rvv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ssp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/ssp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [stackwalker](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stackwalker/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [standardlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/standardlib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [starpu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/starpu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [status-code](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/status-code/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [stb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [stc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [stdexec](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stdexec/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [stduuid](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stduuid/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [steam-audio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/steam-audio/xmake.lua) | 含 Android 逻辑 | L29: elseif is_plat("android") then; L30: add_syslinks("log", "android") |
| [step20](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/step20/xmake.lua) | 含 Android 逻辑 | L11: on_check("android", function (package) |
| [stfl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stfl/xmake.lua) | 含 Android 逻辑 | L18: on_check("android", function (package) |
| [stlab](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stlab/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [strawberry-perl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/strawberry-perl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [streamvbyte](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/streamvbyte/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [string-view-lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/string-view-lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [stringbuilder](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stringbuilder/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [strings_h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/strings_h/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [stringzilla](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stringzilla/xmake.lua) | 含 Android 逻辑 | L76: on_install("android&#124;!armeabi-v7a or (!android and !cross)", function (package); L90: if not package:is_plat("android", "iphoneos", "wasm") and package:config("stringzillas") then |
| [strong_type](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/strong_type/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [strtk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/strtk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [stv](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stv/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [stx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/stx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [subhook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/subhook/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [subprocess.h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/subprocess.h/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [suitesparse](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/suitesparse/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [superlu](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/superlu/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [svector](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/svector/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [svt-av1](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/svt-av1/xmake.lua) | 含 Android 逻辑 | L21: if is_plat("android") and is_host("linux") then; L88: elseif package:is_plat("android") then |
| [swig](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/swig/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [swisseph](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/swisseph/xmake.lua) | 含 Android 逻辑 | L22: if package:is_plat("android") and package:is_arch("armeabi-v7a") then |
| [swxjson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/swxjson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [symengine](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/symengine/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sys_time_h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sys_time_h/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [sys_wait_h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/sys_wait_h/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [syscmdline](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/syscmdline/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [systemc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/systemc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [szip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/s/szip/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ta-lib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/ta-lib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tabulate](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tabulate/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [taglib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/taglib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [talloc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/talloc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tao_idl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tao_idl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [taocpp-json](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/taocpp-json/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [taskflow](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/taskflow/xmake.lua) | 含 Android 逻辑 | L32: on_check("android", function (package); L40: on_install("linux", "macosx", "windows", "iphoneos", "android", "cross", "mingw", "bsd", function (package) |
| [taywee_args](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/taywee_args/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tbb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tbb/xmake.lua) | 含 Android 逻辑 | L81: on_install("macosx", "linux", "mingw@windows", "mingw@msys", "android", "wasm", function (package); L95: if package:is_plat("android") then |
| [tbox](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tbox/xmake.lua) | 含 Android 逻辑 | L48: elseif not is_plat("android") then |
| [tcb-span](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tcb-span/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tclap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tclap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tclsh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tclsh/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [td](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/td/xmake.lua) | 含 Android 逻辑 | L30: elseif package:is_plat("android") then |
| [tdtl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tdtl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [teascript](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/teascript/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [telebot](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/telebot/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [telegram-bot-api](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/telegram-bot-api/xmake.lua) | 含 Android 逻辑 | L46: elseif is_plat("android") then |
| [termcap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/termcap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [termcolor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/termcolor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tesseract](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tesseract/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tetgen](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tetgen/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [texinfo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/texinfo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tf_workstealingqueue](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tf_workstealingqueue/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tgbot-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tgbot-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [theora](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/theora/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [think-cell-library](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/think-cell-library/xmake.lua) | 含 Android 逻辑 | L14: on_check("android", function (package) |
| [thorvg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/thorvg/xmake.lua) | 含 Android 逻辑 | L46: on_check("android", function (package) |
| [thread-pool](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/thread-pool/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [thrift](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/thrift/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [thrust](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/thrust/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ti-cgt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/ti-cgt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tidy-html5](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tidy-html5/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tiltedcore](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tiltedcore/xmake.lua) | 含 Android 逻辑 | L37: on_install("windows", "mingw", "linux", "cross", "android", "macosx&#124;!arm*", function (package) |
| [timeh](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/timeh/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinjector](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinjector/xmake.lua) | 含 Android 逻辑 | L12: on_install("android", function (package) |
| [tiny-aes-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tiny-aes-c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tiny-optional](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tiny-optional/xmake.lua) | 含 Android 逻辑 | L17: on_install("windows&#124;!arm*", "linux&#124;!arm*", "macosx&#124;!arm*", "bsd&#124;!arm*", "mingw&#124;!arm*", "msys&#124;!arm*", "android&#124;!arm*", function (package) |
| [tiny-process-library](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tiny-process-library/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinyalloc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyalloc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinycbor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinycbor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinycc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinycc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinycolormap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinycolormap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinycrypt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinycrypt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinycthread](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinycthread/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinydir](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinydir/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinyexpr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyexpr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinyexr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyexr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinyfiledialogs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyfiledialogs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinyformat](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyformat/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinygltf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinygltf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinyjpeg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyjpeg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinymcp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinymcp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinyobjloader](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyobjloader/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinyply](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyply/xmake.lua) | 含 Android 逻辑 | L11: on_install("macosx", "linux", "windows", "mingw", "android", "iphoneos", function (package) |
| [tinyspline](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyspline/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinytiff](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinytiff/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinyxml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyxml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tinyxml2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tinyxml2/xmake.lua) | 含 Android 逻辑 | L24: if package:is_plat("android") and package:is_arch("armeabi-v7a", "x86") then |
| [tl_expected](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tl_expected/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tl_function_ref](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tl_function_ref/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tl_optional](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tl_optional/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tlsf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tlsf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tmx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tmx/xmake.lua) | 含 Android 逻辑 | L46: elseif package:is_plat("android") then |
| [tmxlite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tmxlite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tmxparser](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tmxparser/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tobiaslocker_base64](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tobiaslocker_base64/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [token](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/token/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [toml++](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/toml++/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [toml11](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/toml11/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tomlc17](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tomlc17/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tomlc99](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tomlc99/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tomlcpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tomlcpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [toojpeg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/toojpeg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [toomanycooks](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/toomanycooks/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [toppra](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/toppra/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tracy](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tracy/xmake.lua) | 含 Android 逻辑 | L67: on_check("android", function (package); L94: #      define TLS_MODEL __attribute__((tls_model("initial-exec")))]], [[#    elif !defined(__HAIKU__) && !defined(__ANDROID__); L96: if package:is_plat("android") then |
| [transwarp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/transwarp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [trantor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/trantor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tree-sitter](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tree-sitter/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [trianglemeshdistance](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/trianglemeshdistance/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [trompeloeil](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/trompeloeil/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tuplet](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tuplet/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [turbobase64](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/turbobase64/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [tvision](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tvision/xmake.lua) | 含 Android 逻辑 | L34: on_install("!wasm and !iphoneos and (!android or android@!windows)", function (package) |
| [tweeny](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/tweeny/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [type_safe](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/t/type_safe/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [uasm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/uasm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [uchardet](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/uchardet/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ucx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/ucx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [udis86](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/udis86/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [udt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/udt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ufbx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/ufbx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [ultralight](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/ultralight/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [uni_algo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/uni_algo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [unicorn](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/unicorn/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [unistd_h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/unistd_h/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [units](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/units/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [unity_test](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/unity_test/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [universal_stacktrace](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/universal_stacktrace/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [unordered_dense](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/unordered_dense/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [unqlite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/unqlite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [unzip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/unzip/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [upa-url](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/upa-url/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [urdfdom](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/urdfdom/xmake.lua) | 含 Android 逻辑 | L26: on_check("android&#124;armeabi-v7a", function (package) |
| [urdfdom-headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/urdfdom-headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [uriparser](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/uriparser/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [usd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/usd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [usockets](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/usockets/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [usrsctp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/usrsctp/xmake.lua) | 含 Android 逻辑 | L32: on_check("android", function (package) |
| [utest.h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/utest.h/xmake.lua) | 含 Android 逻辑 | L9: on_install("windows", "linux", "bsd", "macosx", "mingw", "android", "iphoneos", "cross", function (package) |
| [utf8.h](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/utf8.h/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [utf8_range](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/utf8_range/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [utf8proc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/utf8proc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [utfcpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/utfcpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [uthash](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/uthash/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [util-linux](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/util-linux/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [util-macros](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/util-macros/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [uuid_v4](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/uuid_v4/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [uvatlas](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/uvatlas/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [uvw](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/uvw/xmake.lua) | 含 Android 逻辑 | L37: on_check("android", function (package) |
| [uvwasi](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/uvwasi/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [uwebsockets](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/u/uwebsockets/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [v8](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/v8/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [valgrind](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/valgrind/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [valgrind-macos](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/valgrind-macos/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [valijson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/valijson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vamp-plugin-sdk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vamp-plugin-sdk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vapoursynth](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vapoursynth/xmake.lua) | 含 Android 逻辑 | L37: on_check("android", function (package); L90: if package:is_plat("android") and package:check_sizeof("void*") == "4" then; L139: elseif package:is_plat("android") and package:check_sizeof("void*") == "4" then |
| [variant-lite](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/variant-lite/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vc/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vc-ltl5](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vc-ltl5/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vcglib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vcglib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vcpkg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vcpkg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vectorial](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vectorial/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vectorscan](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vectorscan/xmake.lua) | 含 Android 逻辑 | L30: on_install("linux", "macosx", "android&#124;arm64-v8a", function(package) |
| [veil](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/veil/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [verdict](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/verdict/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [verilator](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/verilator/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vexcl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vexcl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [viennacl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/viennacl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [visit_struct](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/visit_struct/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [visp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/visp/xmake.lua) | 含 Android 逻辑 | L53: "-DBUILD_ANDROID_SERVICE=OFF",; L54: "-DBUILD_ANDROID_PROJECTS=OFF",; L55: "-DBUILD_ANDROID_EXAMPLES=OFF", |
| [vk-bootstrap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vk-bootstrap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vladimirshaleev-ipaddress](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vladimirshaleev-ipaddress/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vld](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vld/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vmaf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vmaf/xmake.lua) | 含 Android 逻辑 | L39: on_check("android", function (package) |
| [volk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/volk/xmake.lua) | 含 Android 逻辑 | L62: on_install("windows", "linux", "macosx", "mingw", "iphoneos", "android", function (package); L77: if package:is_plat("android") and (package:gitref() or package:version():lt("1.3.261")) then |
| [vtk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vtk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vulkan-headers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vulkan-headers/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vulkan-hpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vulkan-hpp/xmake.lua) | 含 Android 逻辑 | L47: on_install("windows&#124;x86", "windows&#124;x64", "linux", "macosx", "mingw", "android", "iphoneos", function (package) |
| [vulkan-loader](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vulkan-loader/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vulkan-memory-allocator](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vulkan-memory-allocator/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vulkan-memory-allocator-hpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vulkan-memory-allocator-hpp/xmake.lua) | 含 Android 逻辑 | L23: on_install("windows&#124;x86", "windows&#124;x64", "linux", "macosx", "mingw", "android", "iphoneos", function (package) |
| [vulkan-tools](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vulkan-tools/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vulkan-utility-libraries](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vulkan-utility-libraries/xmake.lua) | 含 Android 逻辑 | L51: on_install("windows", "linux", "macosx", "android", "bsd", "mingw", "msys", "cross", function (package) |
| [vulkan-validationlayers](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vulkan-validationlayers/xmake.lua) | 含 Android 逻辑 | L8: if is_plat("android") then; L12: return "vulkan-sdk-" .. versionLoc .. "/android-binaries-" .. versionLoc; L14: return "vulkan-sdk-" .. versionLoc .. "/android-binaries-vulkan-sdk-" .. versionLoc |
| [vulkanscenegraph](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vulkanscenegraph/xmake.lua) | 含 Android 逻辑 | L32: on_install("windows", "macosx", "linux", "android", function (package) |
| [vulkansdk](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vulkansdk/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [vvenc](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vvenc/xmake.lua) | 含 Android 逻辑 | L81: if (package:is_plat("android") and package:is_arch("armeabi-v7a")) or package:is_plat("wasm") then |
| [vxl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/v/vxl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [w64devkit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/w64devkit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wangle](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wangle/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wasm-micro-runtime](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wasm-micro-runtime/xmake.lua) | 含 Android 逻辑 | L25: if is_plat("android") then; L26: add_patches("2.2.0", path.join(os.scriptdir(), "patches", "2.2.0", "log-link-android.patch"), "66644a9b86fa26368c029c670f2c5529ba03fba3f5ed6f2aa11f6c359c293cab"); L49: elseif is_plat("android") then |
| [watcher](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/watcher/xmake.lua) | 含 Android 逻辑 | L28: on_check("android", function (package) |
| [wavpack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wavpack/xmake.lua) | 含 Android 逻辑 | L30: on_install("windows", "linux", "bsd", "macosx", "mingw", "android", "wasm", function (package); L31: if package:is_plat("android") and package:is_arch("armeabi-v7a") then |
| [wayland](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wayland/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wayland-protocols](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wayland-protocols/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [webdriverxx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/webdriverxx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [websocketpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/websocketpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [webthing-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/webthing-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [webui](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/webui/xmake.lua) | 含 Android 逻辑 | L22: on_install("windows", "linux", "macosx", "mingw&#124;x86_64", "msys", "android", "cross", function (package); L23: if package:is_plat("android") and package:is_arch("armeabi-v7a") then |
| [wfrest](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wfrest/xmake.lua) | 含 Android 逻辑 | L23: on_install("linux", "macosx", "android", function (package) |
| [wgpu-native](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wgpu-native/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wgsl-validator](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wgsl-validator/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [whereami](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/whereami/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [which](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/which/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [whisper.cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/whisper.cpp/xmake.lua) | 含 Android 逻辑 | L34: on_install("windows", "linux", "mingw", "msys", "android", "wasm", function (package) |
| [wigxjpf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wigxjpf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wil](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wil/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wineditline](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wineditline/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [winflexbison](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/winflexbison/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wingetopt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wingetopt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [winlamb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/winlamb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [winpcap](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/winpcap/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [winpixevent](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/winpixevent/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [winreg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/winreg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wintoast](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wintoast/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wirehair](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wirehair/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wixtoolset](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wixtoolset/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wjakob_filesystem](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wjakob_filesystem/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [woff2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/woff2/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wolfssl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wolfssl/xmake.lua) | 含 Android 逻辑 | L58: if package:is_plat("android") then |
| [workflow](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/workflow/xmake.lua) | 含 Android 逻辑 | L41: on_install("linux", "macosx", "android", function (package) |
| [workspace_hanya](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/workspace_hanya/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wren](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wren/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wxwidgets](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wxwidgets/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [wyhash](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/w/wyhash/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [x264](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/x264/xmake.lua) | 含 Android 逻辑 | L67: if package:is_plat("android") and package:is_arch("armeabi-v7a") then; L85: elseif package:is_plat("android") then |
| [x265](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/x265/xmake.lua) | 含 Android 逻辑 | L73: if package:is_plat("android") then; L99: or package:is_plat("android", "iphoneos", "wasm") then |
| [xapian-core](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xapian-core/xmake.lua) | 含 Android 逻辑 | L29: on_check("android", function (package); L37: on_install("linux", "macosx", "bsd", "mingw", "msys", "android@linux,macosx", "cross", "wasm", function (package) |
| [xaudio2redist](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xaudio2redist/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xbyak](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xbyak/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xcb-proto](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xcb-proto/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xcb-util](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xcb-util/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xcb-util-cursor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xcb-util-cursor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xcb-util-errors](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xcb-util-errors/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xcb-util-image](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xcb-util-image/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xcb-util-keysyms](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xcb-util-keysyms/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xcb-util-renderutil](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xcb-util-renderutil/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xcb-util-wm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xcb-util-wm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xclang](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xclang/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xdl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xdl/xmake.lua) | 含 Android 逻辑 | L3: set_description("xDL is an enhanced implementation of the Android DL series functions."); L13: on_install("android", function (package) |
| [xege](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xege/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xent-core](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xent-core/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xerces-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xerces-c/xmake.lua) | 含 Android 逻辑 | L19: if is_plat("android") then; L22: path.join(os.scriptdir(), "patches", "patch-android.diff"),; L26: on_check("android&#124;armeabi-v7a", function (package) |
| [xframe](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xframe/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xgrammar](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xgrammar/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xhook](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xhook/xmake.lua) | 含 Android 逻辑 | L3: set_description("PLT (Procedure Linkage Table) hook library for Android native ELF (executable and shared libraries)"); L9: on_install("android", function (package) |
| [xlnt](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xlnt/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xlsxio](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xlsxio/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xmlto](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xmlto/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xor_singleheader](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xor_singleheader/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xorgproto](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xorgproto/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xorstr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xorstr/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xoshiro-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xoshiro-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xpack](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xpack/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xproperty](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xproperty/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xquic](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xquic/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xrefl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xrefl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xsimd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xsimd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xtd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xtd/xmake.lua) | 含 Android 逻辑 | L3: set_description("xtd is a modern C++17/20 framework to create console, GUI (forms like WinForms) and unit test applications on Microsoft Windows, Apple macOS, Linux, iOS and android (*).") |
| [xtensa-esp-elf](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xtensa-esp-elf/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xtensor](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xtensor/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xtensor-blas](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xtensor-blas/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xtensor-io](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xtensor-io/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xtl](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xtl/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xtrans](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xtrans/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xunwind](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xunwind/xmake.lua) | 含 Android 逻辑 | L3: set_description(":fire: xUnwind is a collection of Android native stack unwinding solutions."); L13: on_install("android", function (package) |
| [xxhash](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xxhash/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xxmlxx](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xxmlxx/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xz](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xz/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [xz-embedded](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/x/xz-embedded/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yalantinglibs](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yalantinglibs/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yaml-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yaml-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yaml_cpp_struct](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yaml_cpp_struct/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yara](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yara/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yas](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yas/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yasm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yasm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yoga](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yoga/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yojimbo](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yojimbo/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yolos-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yolos-cpp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yomm2](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yomm2/xmake.lua) | 含 Android 逻辑 | L19: on_check("android", function (package) |
| [yxml](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yxml/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yy-thunks](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yy-thunks/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [yyjson](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/y/yyjson/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [z3](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/z3/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zasm](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zasm/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zbar](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zbar/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zeromq](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zeromq/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zeus_expected](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zeus_expected/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zfp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zfp/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zig](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zig/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zimg](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zimg/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zint](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zint/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zip](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zip/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zix](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zix/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zlib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zlib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zlib-ng](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zlib-ng/xmake.lua) | 含 Android 逻辑 | L42: on_check("android", function (package); L44: assert(false, "package(zlib-ng/android >= 2.1.5): Unsupported android and arm"); L49: on_install("windows", "macosx", "linux", "cross", "android", "mingw", function (package) |
| [zlibcomplete](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zlibcomplete/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zlmediakit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zlmediakit/xmake.lua) | 含 Android 逻辑 | L14: add_configs("server_lib", {description = "Enable server as android static library.", default = false, type = "boolean"}) |
| [zlog](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zlog/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zltoolkit](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zltoolkit/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zmij](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zmij/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zmqpb](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zmqpb/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zoe](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zoe/xmake.lua) | 含 Android 逻辑 | L31: if package:is_plat("cross", "android") then; L32: if package:is_plat("android") then |
| [zopfli](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zopfli/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zpp_bits](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zpp_bits/xmake.lua) | 含 Android 逻辑 | L19: on_check("android", function (package) |
| [zpp_throwing](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zpp_throwing/xmake.lua) | 含 Android 逻辑 | L12: on_install("linux", "macosx", "bsd", "mingw", "msys", "android", "iphoneos", "cross", "wasm", function (package) |
| [zstd](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zstd/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zstr](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zstr/xmake.lua) | 含 Android 逻辑 | L13: add_patches("v1.0.7", "patches/fix-build-on-android-ndksdk-21.patch", "66468d9aab3443c488b7fadde7fb2547f1501c73d89e00c672834652ce61a047") |
| [zxing-cpp](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zxing-cpp/xmake.lua) | 含 Android 逻辑 | L29: if package:is_plat("android") and version and version:ge("3.0.2") then |
| [zycore-c](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zycore-c/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
| [zydis](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zydis/xmake.lua) | 含 Android 逻辑 | L43: if package:is_plat("android") then |
| [zziplib](https://github.com/xmake-io/xmake-repo/blob/58f6e9c1bd2e930aadb332fec7c37281edd798b3/packages/z/zziplib/xmake.lua) | 待验证 | 无显式 Android 字符串；通用 on_install 仍可能支持 Android |
