# vcpkg Android 元数据清单

生成时间：2026-10-26 11:42 UTC

[判定方法与限制](README.md)。以下条目均未在本扫描工作流中编译验证。

上游：[固定快照 817892b0ecbc6af994dd6df999c73faf795adbf2](https://github.com/microsoft/vcpkg/tree/817892b0ecbc6af994dd6df999c73faf795adbf2)；共 2887 条。

ABI 列：允许 / 排除 / 未知；仅顶层 supports 条件，不保证依赖或 features 可构建。

| 库 | 判定 | arm64-v8a | armeabi-v7a | x86_64 | x86 | supports / 依据 |
| --- | --- | --- | --- | --- | --- | --- |
| [3fd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/3fd/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !static & !arm64 |
| [7zip](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/7zip/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [abcmake](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/abcmake/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ableton-link](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ableton-link/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [abseil](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/abseil/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [absent](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/absent/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [abumq-ripe](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/abumq-ripe/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [ace](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ace/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [acl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/acl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [activemq-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/activemq-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | (windows & !uwp & (x86 &#124; x64)) &#124; (!windows & !osx) |
| [ada-idna](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ada-idna/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ada-url](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ada-url/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ade](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ade/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [adios2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/adios2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [advobfuscator](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/advobfuscator/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aeron](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aeron/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !((x86 &#124; arm64) & windows) & !android & !uwp & !xbox |
| [air-ctl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/air-ctl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aixlog](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aixlog/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aklomp-base64](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aklomp-base64/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [alac](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/alac/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [alac-decoder](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/alac-decoder/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [alembic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/alembic/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & x86) & !uwp |
| [alibabacloud-oss-cpp-sdk-v2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/alibabacloud-oss-cpp-sdk-v2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aliyun-oss-c-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aliyun-oss-c-sdk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(uwp &#124; linux &#124; osx) |
| [aliyun-oss-cpp-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aliyun-oss-cpp-sdk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | linux &#124; osx &#124; android |
| [allegro5](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/allegro5/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [alpaca](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/alpaca/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [alpaka](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/alpaka/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [alsa](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/alsa/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | linux &#124; android |
| [amd-adl-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/amd-adl-sdk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !osx |
| [amd-amf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/amd-amf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !osx |
| [ampl-asl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ampl-asl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [ampl-mp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ampl-mp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [amqpcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/amqpcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [amsozzer1-plusweb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/amsozzer1-plusweb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [anari](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/anari/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [anax](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/anax/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [andytech-tiny-crc32c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/andytech-tiny-crc32c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [angelscript](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/angelscript/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [angle](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/angle/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ankurvdev-embedresource](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ankurvdev-embedresource/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [annoy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/annoy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [antlr4](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/antlr4/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [any-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/any-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [anyrpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/anyrpc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [anyxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/anyxx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aom](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aom/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [apache-datasketches](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/apache-datasketches/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [approval-tests-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/approval-tests-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [appstream](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/appstream/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [appstream-glib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/appstream-glib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [apr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/apr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !mingw |
| [apr-util](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/apr-util/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [apriltag](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/apriltag/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [apsi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/apsi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aravis](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aravis/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [arcticdb-sparrow](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arcticdb-sparrow/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [arcticdb-sparrow-extensions](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arcticdb-sparrow-extensions/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [arcus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arcus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [arg-router](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arg-router/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [argagg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/argagg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [argh](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/argh/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [argon2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/argon2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [argparse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/argparse/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [args](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/args/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [argtable2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/argtable2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [argtable3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/argtable3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [argumentum](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/argumentum/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [argus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/argus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & static) & !(windows & x86) |
| [aricpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aricpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [armadillo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/armadillo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [arp1it-minecraft-server-status](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arp1it-minecraft-server-status/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [arpack-ng](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arpack-ng/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [arrayfire](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arrayfire/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 排除 | x64 |
| [arrow](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arrow/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 排除 | x64 &#124; arm64 |
| [arrow-adbc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arrow-adbc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [arsenalgear](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arsenalgear/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [arun11299-cpp-subprocess](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/arun11299-cpp-subprocess/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ashes](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ashes/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !ios & !android & !uwp & !x86 & !arm32 & !static |
| [asio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/asio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [asio-grpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/asio-grpc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [asiochan](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/asiochan/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [asiosdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/asiosdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [asmjit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/asmjit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [asmtk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/asmtk/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm |
| [asock](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/asock/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; linux &#124; osx |
| [assimp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/assimp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [astr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/astr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [async-mqtt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/async-mqtt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [async-simple](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/async-simple/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [asynch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/asynch/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [asyncplusplus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/asyncplusplus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [at-spi2-atk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/at-spi2-atk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [at-spi2-core](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/at-spi2-core/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [atk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/atk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [atkmm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/atkmm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [atl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/atl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !xbox |
| [atliac-minitest](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/atliac-minitest/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [atlmfc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/atlmfc/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !xbox |
| [atomic-queue](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/atomic-queue/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [attica](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/attica/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [attr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/attr/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [aubio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aubio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [audioengine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/audioengine/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | x64 & (windows &#124; linux) |
| [audiofile](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/audiofile/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [audit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/audit/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [aui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aui-toolbox](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aui-toolbox/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native & !(linux & arm64) |
| [aurora](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aurora/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aurora-au](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aurora-au/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [autodiff](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/autodiff/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [autodock-vina](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/autodock-vina/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [avcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/avcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [avir](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/avir/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [avisynthplus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/avisynthplus/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm & !uwp & !xbox |
| [avro-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/avro-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [avro-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/avro-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [awlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/awlib/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [aws-c-auth](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-c-auth/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-c-cal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-c-cal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-c-common](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-c-common/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm32) & !uwp |
| [aws-c-compression](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-c-compression/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-c-event-stream](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-c-event-stream/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-c-http](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-c-http/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-c-io](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-c-io/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-c-mqtt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-c-mqtt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-c-s3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-c-s3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-c-sdkutils](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-c-sdkutils/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-checksums](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-checksums/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-crt-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-crt-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [aws-lambda-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-lambda-cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [aws-sdk-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/aws-sdk-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ayush272002-dotenv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ayush272002-dotenv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [azmq](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azmq/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-c-shared-utility](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-c-shared-utility/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [azure-core-amqp-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-core-amqp-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [azure-core-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-core-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-core-tracing-opentelemetry-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-core-tracing-opentelemetry-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & !static) |
| [azure-data-tables-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-data-tables-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-identity-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-identity-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-iot-sdk-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-iot-sdk-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-kinect-depth-engine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-kinect-depth-engine/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (linux & (x64 &#124; arm64)) &#124; (windows & (x64 &#124; x86)) |
| [azure-kinect-sensor-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-kinect-sensor-sdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (linux &#124; windows) & !(static & staticcrt) |
| [azure-macro-utils-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-macro-utils-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-messaging-eventhubs-checkpointstore-blob-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-messaging-eventhubs-checkpointstore-blob-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-messaging-eventhubs-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-messaging-eventhubs-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-security-attestation-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-security-attestation-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-security-keyvault-administration-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-security-keyvault-administration-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-security-keyvault-certificates-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-security-keyvault-certificates-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-security-keyvault-keys-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-security-keyvault-keys-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-security-keyvault-secrets-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-security-keyvault-secrets-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-storage-blobs-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-storage-blobs-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-storage-common-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-storage-common-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-storage-files-datalake-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-storage-files-datalake-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-storage-files-shares-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-storage-files-shares-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-storage-queues-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-storage-queues-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-uamqp-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-uamqp-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-uhttp-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-uhttp-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [azure-umqtt-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/azure-umqtt-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [b64](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/b64/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [babl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/babl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [backward-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/backward-cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [baresip-libre](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/baresip-libre/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [bark](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bark/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(uwp &#124; osx) |
| [barkeep](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/barkeep/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [basisu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/basisu/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [bbalouki-itch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bbalouki-itch/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bbstrader](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bbstrader/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bcg729](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bcg729/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bddisasm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bddisasm/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !osx & !android |
| [bde](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bde/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !(arm64 & windows) & !uwp |
| [bdwgc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bdwgc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [behaviortree-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/behaviortree-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [benchmark](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/benchmark/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [bento4](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bento4/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [berkeleydb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/berkeleydb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(uwp &#124; linux &#124; osx) |
| [better-enums](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/better-enums/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bext-di](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bext-di/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bext-mp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bext-mp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bext-sml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bext-sml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bext-sml2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bext-sml2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bext-text](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bext-text/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bext-ut](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bext-ut/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bext-wintls](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bext-wintls/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; mingw |
| [bfgroup-lyra](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bfgroup-lyra/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bgfx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bgfx/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !bsd |
| [bigint](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bigint/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [binlog](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/binlog/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm64 & windows) |
| [binn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/binn/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bit7z](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bit7z/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bitmagic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bitmagic/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bitserializer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bitserializer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bitsery](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bitsery/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [blake3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/blake3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [blas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/blas/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [blaze](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/blaze/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [blend2d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/blend2d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !wasm32 |
| [blickfeld-qb2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/blickfeld-qb2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [blingfire](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/blingfire/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !static |
| [blitz](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/blitz/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 允许 | !(arm &#124; arm64 &#124; uwp) |
| [bloomberg-quantum](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bloomberg-quantum/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [blosc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/blosc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [blosc2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/blosc2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [blpapi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/blpapi/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (linux &#124; (windows & !uwp)) & !static & (x86 &#124; x64) |
| [bluescarni-tanuki](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bluescarni-tanuki/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boinc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boinc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm) & !uwp & !xbox |
| [boolinq](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boolinq/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-accumulators](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-accumulators/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-algorithm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-algorithm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-align](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-align/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-any](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-any/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-array](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-array/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-asio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-asio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-assert](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-assert/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-assign](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-assign/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-atomic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-atomic/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-beast](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-beast/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !emscripten |
| [boost-bimap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-bimap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-bind](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-bind/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-bloom](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-bloom/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-build](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-build/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-callable-traits](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-callable-traits/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-charconv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-charconv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-chrono](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-chrono/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-circular-buffer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-circular-buffer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-cmake](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-cmake/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-cobalt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-cobalt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-compat](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-compat/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-compute](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-compute/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-concept-check](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-concept-check/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-config](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-config/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-container](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-container/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-container-hash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-container-hash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-context](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-context/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !emscripten |
| [boost-contract](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-contract/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-conversion](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-conversion/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-convert](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-convert/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-core](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-core/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-coroutine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-coroutine/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & windows) & !uwp & !emscripten |
| [boost-coroutine2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-coroutine2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-crc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-crc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-date-time](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-date-time/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-decimal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-decimal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-describe](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-describe/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-detail](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-detail/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-dll](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-dll/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-dynamic-bitset](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-dynamic-bitset/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-endian](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-endian/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-exception](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-exception/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-fiber](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-fiber/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm & windows) & !emscripten |
| [boost-filesystem](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-filesystem/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-flyweight](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-flyweight/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-foreach](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-foreach/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-format](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-format/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-function](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-function/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-function-types](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-function-types/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-functional](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-functional/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-fusion](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-fusion/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-geometry](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-geometry/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-gil](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-gil/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-graph](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-graph/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-graph-parallel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-graph-parallel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-hana](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-hana/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-hash2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-hash2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-headers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-headers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-heap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-heap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-histogram](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-histogram/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-hof](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-hof/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-icl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-icl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-integer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-integer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-interprocess](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-interprocess/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-interval](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-interval/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-intrusive](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-intrusive/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-io](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-io/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-iostreams](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-iostreams/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-iterator](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-iterator/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-json](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-json/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-lambda](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-lambda/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-lambda2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-lambda2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-leaf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-leaf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-lexical-cast](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-lexical-cast/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-local-function](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-local-function/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-locale](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-locale/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-lockfree](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-lockfree/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-log](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-log/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !emscripten |
| [boost-logic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-logic/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-math](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-math/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-metaparse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-metaparse/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-move](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-move/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-mp11](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-mp11/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-mpi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-mpi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-mpl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-mpl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-mqtt5](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-mqtt5/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-msm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-msm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-multi-array](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-multi-array/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-multi-index](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-multi-index/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-multiprecision](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-multiprecision/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-mysql](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-mysql/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-nowide](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-nowide/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-numeric-conversion](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-numeric-conversion/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-odeint](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-odeint/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-openmethod](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-openmethod/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-optional](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-optional/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-outcome](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-outcome/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-parameter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-parameter/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-parameter-python](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-parameter-python/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-parser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-parser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-pfr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-pfr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-phoenix](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-phoenix/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-poly-collection](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-poly-collection/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-polygon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-polygon/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-pool](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-pool/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-predef](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-predef/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-preprocessor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-preprocessor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-process](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-process/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !emscripten & !android |
| [boost-program-options](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-program-options/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-property-map](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-property-map/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-property-map-parallel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-property-map-parallel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-property-tree](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-property-tree/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-proto](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-proto/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-ptr-container](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-ptr-container/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-python](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-python/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !emscripten & !ios & !android |
| [boost-qvm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-qvm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-random](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-random/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-range](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-range/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-ratio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-ratio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-rational](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-rational/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-redis](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-redis/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-regex](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-regex/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-safe-numerics](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-safe-numerics/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-scope](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-scope/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-scope-exit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-scope-exit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-serialization](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-serialization/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-signals2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-signals2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-smart-ptr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-smart-ptr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-sort](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-sort/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-spirit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-spirit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-stacktrace](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-stacktrace/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-statechart](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-statechart/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-static-assert](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-static-assert/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-static-string](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-static-string/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-stl-interfaces](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-stl-interfaces/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-system](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-system/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-test](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-test/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-thread](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-thread/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-throw-exception](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-throw-exception/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-timer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-timer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-tokenizer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-tokenizer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-tti](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-tti/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-tuple](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-tuple/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-type-erasure](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-type-erasure/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-type-index](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-type-index/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-type-traits](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-type-traits/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-typeof](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-typeof/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-ublas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-ublas/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-uninstall](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-uninstall/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-units](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-units/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-unordered](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-unordered/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-url](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-url/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-utility](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-utility/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-uuid](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-uuid/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-variant](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-variant/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-variant2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-variant2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-vmd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-vmd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-wave](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-wave/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [boost-winapi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-winapi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-xpressive](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-xpressive/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boost-yap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boost-yap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [boringssl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/boringssl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [botan](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/botan/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [box2d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/box2d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !uwp & !x86 |
| [box3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/box3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [bqlog](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bqlog/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(windows & x86) & !android |
| [braft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/braft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [breakpad](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/breakpad/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & (!windows &#124; !arm) & (!windows &#124; !arm64) |
| [brigand](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/brigand/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [brotli](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/brotli/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [brpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/brpc/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !windows |
| [brunocodutra-metal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/brunocodutra-metal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [brynet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/brynet/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bshoshany-thread-pool](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bshoshany-thread-pool/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bsio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bsio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [buck-yeh-bux](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/buck-yeh-bux/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [buck-yeh-bux-sqlite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/buck-yeh-bux-sqlite/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(android &#124; linux &#124; osx &#124; uwp) |
| [bullet3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bullet3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bungee](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bungee/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bustache](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bustache/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [butteraugli](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/butteraugli/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bw-sqlitemap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bw-sqlitemap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bw-tempdir](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bw-tempdir/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bxzstr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bxzstr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [byte-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/byte-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bzip2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bzip2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [bzip3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/bzip3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [c-ares](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/c-ares/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [c4core](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/c4core/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(windows & arm) |
| [c89stringutils](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/c89stringutils/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [c9y](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/c9y/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cachelib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cachelib/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux & x64 & static |
| [cadons-ctus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cadons-ctus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [caf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/caf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cairo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cairo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox & !uwp |
| [cairomm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cairomm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [calceph](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/calceph/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [camport3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/camport3/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | ((windows & !uwp & !arm & !arm64 & !static) &#124; linux) & !wasm32 |
| [canvas-ity](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/canvas-ity/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [capnproto](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/capnproto/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; (!uwp & !arm32) |
| [capstone](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/capstone/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cargs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cargs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [casadi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/casadi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [casclib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/casclib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [catch2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/catch2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cblas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cblas/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cccapstone](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cccapstone/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ccd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ccd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ccfits](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ccfits/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cctag](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cctag/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(uwp &#124; arm &#124; arm64 &#124; android &#124; x86 &#124; xbox) |
| [cctz](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cctz/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cddlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cddlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cdt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cdt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [celero](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/celero/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cello](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cello/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cereal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cereal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ceres](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ceres/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cesnet-ndk-sw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cesnet-ndk-sw/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [cfitsio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cfitsio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cgal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cgal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [cgicc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cgicc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cglm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cglm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cgltf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cgltf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cgns](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cgns/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [chadwick](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/chadwick/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [chaiscript](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/chaiscript/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [chakracore](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/chakracore/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !osx & !uwp & (linux &#124; !static) |
| [charls](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/charls/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [chartdir](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/chartdir/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !uwp & (x86 &#124; x64)) &#124; osx &#124; linux |
| [check](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/check/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [chenjunfu2-nbt-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/chenjunfu2-nbt-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [chipmunk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/chipmunk/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm & !arm64 & android) |
| [chmlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/chmlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [chromaprint](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/chromaprint/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [chronoengine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/chronoengine/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !static & !uwp) &#124; linux &#124; osx |
| [cialloo-rcon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cialloo-rcon/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cimg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cimg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cinatra](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cinatra/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [cista](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cista/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cityhash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cityhash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [civetweb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/civetweb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [cjson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cjson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [clamav](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clamav/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !static |
| [clap-cleveraudio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clap-cleveraudio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [clapack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clapack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [clara](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clara/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [clay](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clay/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [clblas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clblas/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm) |
| [clblast](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clblast/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cld3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cld3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cleishm-frequency-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cleishm-frequency-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [cleishm-thermo-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cleishm-thermo-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [clfft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clfft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cli](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cli/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cli11](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cli11/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [clickhouse-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clickhouse-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [clipboardxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clipboardxx/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !osx & !android |
| [clipp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clipp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [clipper2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clipper2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [clockutils](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clockutils/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [clrng](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clrng/vcpkg.json) | 元数据允许 | 排除 | 允许 | 允许 | 允许 | !arm64 |
| [clue](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/clue/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cmakerc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cmakerc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cmark](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cmark/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cmark-gfm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cmark-gfm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cminpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cminpack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cmocka](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cmocka/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cnats](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cnats/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cnl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cnl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cocoyaxi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cocoyaxi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm & windows) |
| [cofetch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cofetch/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [coin](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coin/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp |
| [coin-or-buildtools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coin-or-buildtools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [coin-or-cbc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coin-or-cbc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [coin-or-cgl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coin-or-cgl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [coin-or-clp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coin-or-clp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [coin-or-ipopt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coin-or-ipopt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [coin-or-osi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coin-or-osi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [coinbase-advanced-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coinbase-advanced-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [coinutils](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coinutils/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [collada-dom](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/collada-dom/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [colmap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/colmap/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (linux &#124; (windows & !static) &#124; osx) & (x86 &#124; x64 &#124; arm64) |
| [color-console](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/color-console/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [commata](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/commata/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [comms](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/comms/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [comms-ublox](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/comms-ublox/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [commsdsl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/commsdsl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [compoundfilereader](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/compoundfilereader/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [concurrencpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/concurrencpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [concurrentqueue](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/concurrentqueue/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [configcat](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/configcat/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [conjure-enum](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/conjure-enum/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [console-bridge](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/console-bridge/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [consteig](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/consteig/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [constexpr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/constexpr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [constexpr-contracts](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/constexpr-contracts/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [continuable](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/continuable/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [convectionkernels](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/convectionkernels/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [coolprop](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coolprop/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [copypp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/copypp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [coroutine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/coroutine/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [corrade](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/corrade/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [correlation-vector-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/correlation-vector-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [countly-sdk-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/countly-sdk-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [cpp-async](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-async/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-base64](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-base64/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-channel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-channel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-client-telemetry](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-client-telemetry/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | ((windows & !mingw) &#124; linux &#124; osx &#124; ios &#124; android) & !uwp |
| [cpp-exiftool](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-exiftool/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [cpp-httplib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-httplib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-ipc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-ipc/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !osx & !android |
| [cpp-jwt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-jwt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-kana](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-kana/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-lazy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-lazy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-peglib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-peglib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-pinyin](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-pinyin/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-redis](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-redis/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-smtpclient-library](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-smtpclient-library/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [cpp-sort](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-sort/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-timsort](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-timsort/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpp-unicodelib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpp-unicodelib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cppad](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppad/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cppadcodegen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppadcodegen/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cppcms](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppcms/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [cppcodec](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppcodec/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cppduals](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppduals/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [cppfs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppfs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [cppgraphqlgen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppgraphqlgen/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cppitertools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppitertools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cppkafka](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppkafka/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cppmicroservices](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppmicroservices/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cppp-reiconv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppp-reiconv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpprealm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpprealm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !emscripten |
| [cppslippi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppslippi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpptoml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpptoml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpptrace](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpptrace/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(uwp &#124; android) |
| [cppunit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppunit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [cpputest](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpputest/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cppvrf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppvrf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cppwinrt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppwinrt/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [cppxaml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppxaml/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !xbox |
| [cppzmq](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cppzmq/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cpu-features](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpu-features/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [cpuid](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpuid/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(windows & arm) |
| [cpuinfo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cpuinfo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(uwp & arm32) |
| [cr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [crashcatch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/crashcatch/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [crashpad](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/crashpad/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | android &#124; linux &#124; osx &#124; (windows & !uwp) |
| [crashrpt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/crashrpt/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 允许 | !osx & !linux & !uwp & (x86 &#124; x64) |
| [crc32c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/crc32c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [crcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/crcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [crfsuite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/crfsuite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [croncpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/croncpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [crossdb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/crossdb/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (!windows &#124; mingw) & !android |
| [crossguid](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/crossguid/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [crow](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/crow/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cryptopp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cryptopp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cserialport](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cserialport/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [cspice](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cspice/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & windows) |
| [ctbench](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ctbench/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [ctbignum](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ctbignum/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ctemplate](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ctemplate/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !arm |
| [cthash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cthash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ctpg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ctpg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ctre](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ctre/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ctstraffic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ctstraffic/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [cubeb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cubeb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [cuda](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cuda/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !uwp & !xbox) &#124; (linux & x64) &#124; (linux & arm64) |
| [cuda-api-wrappers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cuda-api-wrappers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cudnn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cudnn/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !uwp) &#124; (linux & x64) &#124; (linux & arm64) |
| [cudnn-frontend](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cudnn-frontend/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cunit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cunit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [curl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/curl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [curlcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/curlcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [curlpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/curlpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [curve-coco](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/curve-coco/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [curve-eraser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/curve-eraser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [curve-ereignis](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/curve-ereignis/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [curve-flagpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/curve-flagpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [curve-lockpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/curve-lockpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [curve-poolparty](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/curve-poolparty/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [curve-rebind](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/curve-rebind/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cute-headers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cute-headers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cutelyst2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cutelyst2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cwalk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cwalk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cwapi3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cwapi3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cxxgraph](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cxxgraph/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cxxopts](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cxxopts/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cyclonedds](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cyclonedds/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm64 & windows) |
| [cyclonedds-cxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cyclonedds-cxx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [cyrus-sasl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/cyrus-sasl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx &#124; (windows & !uwp) |
| [czmq](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/czmq/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [d3d12-memory-allocator](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/d3d12-memory-allocator/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [d3dx12](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/d3dx12/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !xbox) &#124; linux |
| [dacap-clip](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dacap-clip/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp |
| [dagir](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dagir/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [darknet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/darknet/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp & !(static & staticcrt) |
| [darts-clone](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/darts-clone/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dartsim](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dartsim/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 排除 | !x86 & !arm32 |
| [dataframe](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dataframe/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [date](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/date/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [datraw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/datraw/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dav1d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dav1d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & x86 & !static) |
| [daw-header-libraries](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/daw-header-libraries/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [daw-json-link](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/daw-json-link/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [daw-utf-range](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/daw-utf-range/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dawn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dawn/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [daxa](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/daxa/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows &#124; linux) & !x86 |
| [dbg-macro](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dbg-macro/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dbghelp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dbghelp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [dbow2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dbow2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dbow3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dbow3/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [dbus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dbus/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !staticcrt & !android & !ios |
| [dbus-cxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dbus-cxx/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [dcmtk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dcmtk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [ddtdanilo-lmdb-wrapper](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ddtdanilo-lmdb-wrapper/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !uwp & !x86 |
| [debug-assert](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/debug-assert/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [decimal-for-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/decimal-for-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [delaunator-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/delaunator-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [deniskovalchuk-libftp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/deniskovalchuk-libftp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [detours](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/detours/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [devicenameresolver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/devicenameresolver/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [devil](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/devil/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [dimcli](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dimcli/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [dime](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dime/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dingo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dingo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [directfb2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/directfb2/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux & !android |
| [directx-dxc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/directx-dxc/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !arm32 & !uwp & !xbox) &#124; (linux & x64) |
| [directx-headers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/directx-headers/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !arm32 & !xbox) &#124; linux |
| [directx12-agility](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/directx12-agility/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !xbox & !arm32 |
| [directxmath](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/directxmath/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !arm32 |
| [directxmesh](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/directxmesh/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !arm32) &#124; linux |
| [directxsdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/directxsdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !xbox & !arm |
| [directxtex](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/directxtex/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !arm32) &#124; linux |
| [directxtk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/directxtk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !xbox & !arm32 |
| [directxtk12](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/directxtk12/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !arm32 |
| [dirent](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dirent/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [discord-game-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/discord-game-sdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | ((x64 & (windows &#124; osx &#124; linux)) &#124; (x86 & windows) &#124; (arm64 & osx)) & !uwp & !static |
| [discord-rpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/discord-rpc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [discount](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/discount/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [discreture](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/discreture/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dispenso](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dispenso/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [distorm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/distorm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dlfcn-win32](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dlfcn-win32/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [dlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [dlpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dlpack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dmlc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dmlc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [docopt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/docopt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [docraft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/docraft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [doctest](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/doctest/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [double-conversion](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/double-conversion/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dp-thread-pool](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dp-thread-pool/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dpdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dpdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | freebsd &#124; linux &#124; (windows & x64) |
| [dpetkov-semver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dpetkov-semver/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [dpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !static & !uwp) &#124; linux &#124; osx |
| [draco](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/draco/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [drekar-launch-process-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/drekar-launch-process-cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & (x86 &#124; x64) & !uwp) &#124; linux &#124; osx |
| [drlibs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/drlibs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [drogon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/drogon/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [dstorage](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dstorage/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !arm32 & !uwp & !xbox |
| [dtc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dtc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dtl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dtl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [duckdb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/duckdb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [duckx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/duckx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [duilib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/duilib/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [dukglue](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dukglue/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [duktape](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/duktape/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dumb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dumb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [duvc-ctl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/duvc-ctl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [dv-processing](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dv-processing/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [dxcam-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dxcam-cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [dxsdk-d3dx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dxsdk-d3dx/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !arm & !uwp & !xbox |
| [dxut](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dxut/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !xbox |
| [dylib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dylib/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp |
| [dyno](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/dyno/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [e-dant-watcher](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/e-dant-watcher/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [eabase](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/eabase/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [earcut-hpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/earcut-hpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [eastl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/eastl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [easy-profiler](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/easy-profiler/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [easycl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/easycl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [easyexif](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/easyexif/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [easyhook](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/easyhook/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !static & !uwp & (x86 &#124; x64) |
| [easyloggingpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/easyloggingpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [eathread](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/eathread/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 排除 | !uwp & x64 |
| [ebml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ebml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ecal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ecal/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !emscripten & !uwp & !android |
| [ecaludp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ecaludp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [ecbuild](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ecbuild/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [eccodes](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/eccodes/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !x86 & !android |
| [ecm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ecm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ecos](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ecos/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ed25519](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ed25519/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [edflib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/edflib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [edlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/edlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [effects11](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/effects11/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !xbox & !mingw |
| [effolkronium-random](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/effolkronium-random/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [efsw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/efsw/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [egl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/egl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [egl-registry](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/egl-registry/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [eigen3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/eigen3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [eipscanner](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/eipscanner/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [elements](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/elements/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & staticcrt) &#124; osx &#124; linux |
| [elfio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/elfio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [elfutils](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/elfutils/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [eljonny-testcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/eljonny-testcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [embree](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/embree/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx &#124; (windows & !uwp & !arm) |
| [enchantum](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/enchantum/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [enet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/enet/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [engitsdatalib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/engitsdatalib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [enkits](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/enkits/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ensmallen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ensmallen/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [entityx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/entityx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [entt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/entt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [epoll-shim](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/epoll-shim/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | osx &#124; freebsd &#124; openbsd |
| [esaxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/esaxx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ethindp-prism](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ethindp-prism/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [etl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/etl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [eve](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/eve/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !windows, mingw |
| [eventpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/eventpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [evpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/evpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [exiv2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/exiv2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [expat](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/expat/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [expected-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/expected-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [exprtk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/exprtk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ez8-co-yapi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ez8-co-yapi/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [ezc3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ezc3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ezfoundation](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ezfoundation/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [f3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/f3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & (arm &#124; uwp)) |
| [faad2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/faad2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fadbad](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fadbad/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [faiss](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/faiss/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !x86 & !uwp |
| [fakeit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fakeit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [faker-cxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/faker-cxx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fameta-counter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fameta-counter/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fancyargumentparser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fancyargumentparser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fann](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fann/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [farmhash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/farmhash/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm |
| [fast-cpp-csv-parser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fast-cpp-csv-parser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fast-double-parser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fast-double-parser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fast-float](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fast-float/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fast-obj](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fast-obj/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fastcdr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fastcdr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fastcgi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fastcgi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [fastdds](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fastdds/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [fastfeat](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fastfeat/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fastgltf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fastgltf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fastio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fastio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fastlz](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fastlz/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fastor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fastor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fastpfor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fastpfor/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm & !arm64) |
| [faudio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/faudio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [fawdlstty-libfv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fawdlstty-libfv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fbgemm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fbgemm/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 排除 | !arm & !x86 & !uwp |
| [fbthrift](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fbthrift/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 排除 | x64 & static |
| [fcftest](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fcftest/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fcl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fcl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fdk-aac](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fdk-aac/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fdlibm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fdlibm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fenster](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fenster/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ffmpeg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ffmpeg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ffmpeg-bin2c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ffmpeg-bin2c/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [ffnvcodec](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ffnvcodec/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | linux &#124; (!osx & !uwp & !(arm64 & windows)) |
| [fftw3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fftw3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fftwpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fftwpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fineftp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fineftp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [fins](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fins/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fixed-containers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fixed-containers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fixed-math](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fixed-math/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fixed-string](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fixed-string/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fizz](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fizz/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fkyaml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fkyaml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [flann](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flann/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [flash-runtime-extensions](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flash-runtime-extensions/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm &#124; uwp) |
| [flashlight-cpu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flashlight-cpu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows &#124; osx) |
| [flashlight-cuda](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flashlight-cuda/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows &#124; osx) |
| [flashlight-sequence](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flashlight-sequence/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [flashlight-text](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flashlight-text/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [flat](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flat/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [flatbuffers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flatbuffers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [flatbush](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flatbush/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [flatcc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flatcc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [flecs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flecs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [flint](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flint/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(windows & arm64) |
| [fltk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fltk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [fluidlite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fluidlite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fluidsynth](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fluidsynth/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(uwp &#124; xbox) |
| [flux](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/flux/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fmem](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fmem/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fmi4cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fmi4cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fmilib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fmilib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [fmt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fmt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [folly](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/folly/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !uwp & !mingw) &#124; (!windows & !android & (x64 &#124; arm64)) |
| [font-chef](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/font-chef/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [font-util](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/font-util/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fontconfig](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fontconfig/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [foonathan-lexy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/foonathan-lexy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [foonathan-memory](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/foonathan-memory/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [forge](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/forge/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & (arm &#124; uwp)) |
| [foxi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/foxi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [fp16](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fp16/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [freealut](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/freealut/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [freeglut](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/freeglut/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !ios |
| [freeimage](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/freeimage/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [freerdp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/freerdp/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !uwp & (!bsd &#124; freebsd) |
| [freetds](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/freetds/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !xbox |
| [freetype](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/freetype/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [freetype-gl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/freetype-gl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [freexl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/freexl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [frei0r](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/frei0r/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(static & windows) |
| [fribidi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fribidi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [frozen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/frozen/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [frugally-deep](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/frugally-deep/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fruit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fruit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ftgl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ftgl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ftxui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ftxui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [function2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/function2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [functionalplus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/functionalplus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [functions-framework-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/functions-framework-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [future-config](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/future-config/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fuzzylite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fuzzylite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [fxaudio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fxaudio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [fxdiv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/fxdiv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [g2o](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/g2o/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [g3log](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/g3log/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [gainput](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gainput/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [gamedev-framework](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gamedev-framework/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !arm & !android |
| [gameinput](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gameinput/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & (arm64 &#124; x64) & !uwp |
| [gamenetworkingsockets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gamenetworkingsockets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm64 & windows) |
| [gamma](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gamma/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gapp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gapp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gasol](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gasol/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !uwp & !arm |
| [gaussianlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gaussianlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gcem](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gcem/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gdal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gdal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [gdbm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gdbm/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [gdcm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gdcm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [gdk-pixbuf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gdk-pixbuf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [gegl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gegl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [gemmlowp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gemmlowp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [genann](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/genann/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [geo-utils-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/geo-utils-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [geogram](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/geogram/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [geographiclib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/geographiclib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [geos](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/geos/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [geotrans](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/geotrans/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !osx |
| [getdns](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/getdns/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [getopt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/getopt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [getopt-win32](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/getopt-win32/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !mingw |
| [gettext](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gettext/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [gettext-libintl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gettext-libintl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [gettimeofday](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gettimeofday/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gexiv2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gexiv2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gflags](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gflags/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [ggml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ggml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [ghc-filesystem](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ghc-filesystem/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gherkin-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gherkin-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gif-load](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gif-load/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [giflib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/giflib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ginkgo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ginkgo/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(x86 &#124; android) |
| [gklib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gklib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gl2ps](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gl2ps/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [gl3w](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gl3w/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [glad](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glad/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [glaze](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glaze/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [glbinding](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glbinding/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [glew](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glew/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [glfw3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glfw3/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [gli](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gli/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [glib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [glib-networking](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glib-networking/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !static |
| [glibmm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glibmm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox & !(windows & !mingw & static) |
| [glm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [globjects](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/globjects/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [glog](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glog/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gloo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gloo/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [glpk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glpk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [glslang](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glslang/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [glui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/glui/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [gmime](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gmime/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [gmmlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gmmlib/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [gmp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gmp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [gmsh](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gmsh/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [gobject-introspection](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gobject-introspection/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(static & staticcrt) |
| [godot-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/godot-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [goldy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/goldy/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(static & staticcrt) & !uwp & ((x64 & (windows &#124; linux)) &#124; osx) |
| [google-cloud-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/google-cloud-cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [gperf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gperf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [gperftools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gperftools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | ((x86 &#124; x64) & windows & !uwp) &#124; !windows &#124; mingw |
| [gpgme](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gpgme/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [gpgmepp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gpgmepp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gpgmm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gpgmm/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !(arm &#124; uwp) |
| [gppanel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gppanel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [graaf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/graaf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [grantlee](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/grantlee/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !staticcrt & !xbox |
| [graphene](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/graphene/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [graphicsmagick](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/graphicsmagick/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [graphite2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/graphite2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [graphviz](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/graphviz/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [greatest](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/greatest/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [grpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/grpc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [grppi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/grppi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gsasl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gsasl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [gsl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gsl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gsl-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gsl-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gst-rtsp-server](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gst-rtsp-server/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [gstreamer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gstreamer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [gtest](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gtest/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gtk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gtk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !xbox & !(arm64 & windows) |
| [gtk3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gtk3/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [gtkmm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gtkmm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [gtl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gtl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gts](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gts/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gtsam](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gtsam/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [guetzli](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/guetzli/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [guile](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/guile/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [guilite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/guilite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gul14](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gul14/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [gul17](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gul17/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [gumbo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gumbo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-cmake](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-cmake/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-common](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-common/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-fuel-tools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-fuel-tools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-gui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-gui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-math](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-math/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-msgs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-msgs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [gz-physics](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-physics/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-plugin](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-plugin/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !arm & !android |
| [gz-rendering](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-rendering/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-sensors](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-sensors/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-sim](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-sim/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-tools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-tools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & windows) & !uwp |
| [gz-transport](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-transport/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gz-utils](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gz-utils/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [gzip-hpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/gzip-hpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [h3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/h3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [h5py-lzf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/h5py-lzf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [half](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/half/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [halide](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/halide/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [hamlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hamlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [hanjingo-high-jump](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hanjingo-high-jump/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [happly](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/happly/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hareflow](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hareflow/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [harfbuzz](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/harfbuzz/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [hash-library](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hash-library/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hashids](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hashids/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hayai](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hayai/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hazelcast-cpp-client](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hazelcast-cpp-client/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [hdf5](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hdf5/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [hdr-histogram](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hdr-histogram/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [healpix](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/healpix/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [hedley](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hedley/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hello-imgui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hello-imgui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hesphoros-uniconv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hesphoros-uniconv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & windows) |
| [hexi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hexi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hexl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hexl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | x64 & !android |
| [hffix](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hffix/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hfsm2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hfsm2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hical61-hical](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hical61-hical/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !xbox & !android & !emscripten |
| [hidapi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hidapi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [highfive](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/highfive/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [highs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/highs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [highway](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/highway/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hikogui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hikogui/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & x64 |
| [hiredis](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hiredis/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hjson-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hjson-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hlslpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hlslpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !x86 |
| [hnswlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hnswlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hps](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hps/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hpx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hpx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm64) & !(windows & staticcrt) |
| [htscodecs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/htscodecs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [htslib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/htslib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [http-parser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/http-parser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [huira](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/huira/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp & !xbox |
| [hungarian](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hungarian/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hunspell](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hunspell/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [hwloc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hwloc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [hyperscan](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hyperscan/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm |
| [hypodermic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hypodermic/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [hypre](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/hypre/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [iausofa](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/iausofa/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [iceberg-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/iceberg-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [icecream-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/icecream-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [iceoryx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/iceoryx/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [icey](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/icey/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [icu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/icu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ideep](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ideep/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 排除 | x64 & !uwp |
| [ideviceinstaller](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ideviceinstaller/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android & !ios & !xbox |
| [idevicerestore](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/idevicerestore/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (!windows & !android & !ios) &#124; mingw |
| [idyntree](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/idyntree/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [if97](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/if97/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [igloo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/igloo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ignition-modularscripts](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ignition-modularscripts/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [igraph](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/igraph/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [iguana](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/iguana/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [iir1](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/iir1/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [im3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/im3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [imageinfo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/imageinfo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [imath](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/imath/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [imcce-openfa](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/imcce-openfa/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [imgui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/imgui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [imgui-node-editor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/imgui-node-editor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [imgui-sfml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/imgui-sfml/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [imguizmo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/imguizmo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [immer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/immer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [implot](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/implot/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [implot3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/implot3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [indicators](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/indicators/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [indirect-value](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/indirect-value/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [inflatelib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/inflatelib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [influxdb-cxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/influxdb-cxx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [infoware](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/infoware/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp & !(windows & arm) |
| [ini-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ini-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [inih](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/inih/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [iniparser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/iniparser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [inipp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/inipp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [inja](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/inja/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [intel-ipsec](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/intel-ipsec/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | x64 & (windows &#124; linux) & !uwp |
| [intel-mkl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/intel-mkl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows &#124; linux) & x64 |
| [intelrdfpmathlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/intelrdfpmathlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & windows) |
| [intrusive-shared-ptr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/intrusive-shared-ptr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [intx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/intx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [iowa-hills-dsp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/iowa-hills-dsp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ipgeolocation-cpp-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ipgeolocation-cpp-sdk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [irrlicht](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/irrlicht/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(android &#124; uwp) |
| [irsdkcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/irsdkcpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & x64 |
| [isal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/isal/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 排除 | !uwp & (x64 &#124; (arm64 & linux)) |
| [ismrmrd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ismrmrd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !(x86 &#124; wasm32) |
| [iso-codes](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/iso-codes/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [itay-grudev-singleapplication](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/itay-grudev-singleapplication/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [itk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/itk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [itlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/itlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [itpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/itpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [itsy-bitsy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/itsy-bitsy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ixwebsocket](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ixwebsocket/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jack2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jack2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [jaeger-client-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jaeger-client-cpp/vcpkg.json) | 元数据允许 | 排除 | 允许 | 允许 | 允许 | !arm64 |
| [jansson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jansson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jasper](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jasper/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jbcoe-value-types](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jbcoe-value-types/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jbig2dec](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jbig2dec/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jbigkit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jbigkit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jemalloc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jemalloc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jhasse-poly2tri](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jhasse-poly2tri/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jigson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jigson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jinja2cpplight](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jinja2cpplight/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [jkqtplotter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jkqtplotter/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [joltphysics](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/joltphysics/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [josuttis-jthread](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/josuttis-jthread/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jsmn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jsmn/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [json-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/json-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [json-dto](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/json-dto/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [json-glib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/json-glib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [json-rpc-cxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/json-rpc-cxx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [json-schema-validator](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/json-schema-validator/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [json11](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/json11/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [json5-parser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/json5-parser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jsoncons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jsoncons/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jsoncpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jsoncpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jsonfusion](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jsonfusion/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [jsonifier](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jsonifier/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !xbox) &#124; (linux & x64) &#124; (osx & x64) |
| [jsonnet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jsonnet/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jsonrpcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jsonrpcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [juce](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/juce/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [jwsung91-unilink](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jwsung91-unilink/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [jwt-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jwt-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [jxrlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/jxrlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kaitai-struct-cpp-stl-runtime](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kaitai-struct-cpp-stl-runtime/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kalshi-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kalshi-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [kangaru](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kangaru/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [karchive](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/karchive/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [kauth](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kauth/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !windows |
| [kbookmarks](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kbookmarks/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kbreezeicons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kbreezeicons/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !windows & !android |
| [kcenon-common-system](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kcenon-common-system/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [kcodecs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kcodecs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kcompletion](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kcompletion/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kconfig](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kconfig/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kcoreaddons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kcoreaddons/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kcp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kcp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kcrash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kcrash/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [kdalgorithms](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kdalgorithms/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kdbindings](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kdbindings/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kdbusaddons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kdbusaddons/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [kddockwidgets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kddockwidgets/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !ios |
| [kdgpu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kdgpu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [kdiagram](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kdiagram/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kdreports](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kdreports/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kdsingleapplication](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kdsingleapplication/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kdsoap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kdsoap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kdstatemachineeditor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kdstatemachineeditor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kdutils](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kdutils/vcpkg.json) | 元数据允许 | 排除 | 允许 | 允许 | 允许 | !uwp & (windows &#124; linux &#124; android &#124; osx) & (arm &#124; x86 &#124; x64) |
| [kealib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kealib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kedixa-coke](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kedixa-coke/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | osx &#124; linux &#124; freebsd |
| [kenlm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kenlm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm64 & windows) |
| [kerbal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kerbal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [keystone](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/keystone/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [kf5archive](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5archive/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [kf5attica](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5attica/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5auth](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5auth/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [kf5bookmarks](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5bookmarks/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5codecs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5codecs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5completion](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5completion/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5config](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5config/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5configwidgets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5configwidgets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5coreaddons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5coreaddons/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5crash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5crash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5dbusaddons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5dbusaddons/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5declarative](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5declarative/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5globalaccel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5globalaccel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [kf5guiaddons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5guiaddons/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5holidays](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5holidays/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5i18n](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5i18n/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5iconthemes](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5iconthemes/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5itemmodels](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5itemmodels/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5itemviews](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5itemviews/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5jobwidgets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5jobwidgets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5kcmutils](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5kcmutils/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5kio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5kio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5newstuff](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5newstuff/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5notifications](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5notifications/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5package](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5package/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5parts](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5parts/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5plotting](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5plotting/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5service](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5service/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5solid](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5solid/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5sonnet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5sonnet/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5syntaxhighlighting](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5syntaxhighlighting/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5texteditor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5texteditor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5textwidgets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5textwidgets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5wallet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5wallet/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5widgetsaddons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5widgetsaddons/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5windowsystem](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5windowsystem/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf5xmlgui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf5xmlgui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kf6-solid](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kf6-solid/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kfr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kfr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm64 & windows) & !xbox |
| [kglobalaccel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kglobalaccel/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !windows & !android & !osx |
| [kguiaddons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kguiaddons/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [ki18n](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ki18n/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [kinectsdk1](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kinectsdk1/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !arm & windows & !uwp & !xbox |
| [kinectsdk2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kinectsdk2/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !arm & windows & !uwp & !xbox |
| [kineto](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kineto/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kissfft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kissfft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kissnet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kissnet/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kitemmodels](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kitemmodels/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kitemviews](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kitemviews/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kleidiai](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kleidiai/vcpkg.json) | 元数据允许 | 允许 | 排除 | 排除 | 排除 | arm64 |
| [klein](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/klein/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [knet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/knet/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm &#124; uwp) |
| [knncolle](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/knncolle/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [knncolle-annoy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/knncolle-annoy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [knncolle-hnsw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/knncolle-hnsw/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [knncolle-kmknn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/knncolle-kmknn/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [knotifications](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/knotifications/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [komihash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/komihash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [krabsetw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/krabsetw/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [krb5](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/krb5/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx &#124; (x64 & windows & !static & !uwp) |
| [krpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/krpc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [krpc-cnano](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/krpc-cnano/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ktx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ktx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | arm64 &#124; x64 &#124; !windows |
| [kubazip](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kubazip/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kubernetes](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kubernetes/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [kuku](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kuku/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kvasir-mpl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kvasir-mpl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kvazaar](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kvazaar/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kwidgetsaddons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kwidgetsaddons/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kwindowsystem](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kwindowsystem/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [kwsys](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/kwsys/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [lager](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lager/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lapack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lapack/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [lapack-reference](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lapack-reference/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lastools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lastools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [laszip](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/laszip/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [launch-darkly-server](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/launch-darkly-server/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [lazy-importer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lazy-importer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lcm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lcm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !osx & !xbox |
| [lcms](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lcms/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lely-core](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lely-core/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [lemon-parser-generator](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lemon-parser-generator/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [lensfun](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lensfun/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm |
| [leptonica](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/leptonica/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lerc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lerc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lest](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lest/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [level-zero](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/level-zero/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | x64 & (linux &#124; (windows & !uwp)) |
| [leveldb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/leveldb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [levmar](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/levmar/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [lexbor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lexbor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [lexilla](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lexilla/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !mingw |
| [lfreist-hwinfo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lfreist-hwinfo/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(uwp &#124; android) |
| [lib3mf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lib3mf/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & (x86 &#124; x64)) &#124; (linux & x64) &#124; (osx & (x64 &#124; arm64)) |
| [libaaplus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libaaplus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libadlmidi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libadlmidi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libadwaita](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libadwaita/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libaec](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libaec/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libaes-siv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libaes-siv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libaiff](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libaiff/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libaio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libaio/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libalkimia](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libalkimia/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libao](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libao/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libarchive](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libarchive/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libaribcaption](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libaribcaption/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libass](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libass/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libassert](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libassert/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libassuan](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libassuan/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [libatomic-ops](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libatomic-ops/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libavif](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libavif/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libb2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libb2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libbacktrace](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libbacktrace/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libbluray](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libbluray/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libbpf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libbpf/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libbson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libbson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libcaer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcaer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & windows & !mingw) |
| [libcamera](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcamera/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libcanberra](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcanberra/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [libcap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcap/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libcbor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcbor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libcds](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcds/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & (osx &#124; windows)) & !uwp |
| [libcerf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcerf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libcgroup](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcgroup/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libcoap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcoap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libconfig](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libconfig/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libconfuse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libconfuse/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libcopp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcopp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm) |
| [libcoro](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcoro/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libcorrect](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcorrect/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libcpplocate](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcpplocate/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libcrafter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcrafter/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libcred](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcred/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !osx & !uwp & !arm & !(windows & staticcrt) & !android |
| [libcroco](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcroco/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libcsv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcsv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libcuckoo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcuckoo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libcurl-simple-https](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libcurl-simple-https/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libczi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libczi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libdaemon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdaemon/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx &#124; openbsd &#124; freebsd |
| [libdatachannel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdatachannel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libdatrie](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdatrie/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libdc1394](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdc1394/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libde265](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libde265/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libdeflate](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdeflate/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libdicom](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdicom/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libdisasm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdisasm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libdivide](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdivide/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libdjinterop](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdjinterop/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libdmtx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdmtx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libdmx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdmx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libdotconf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdotconf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libdshowcapture](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdshowcapture/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [libdvdcss](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdvdcss/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libdvdnav](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdvdnav/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libdvdread](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdvdread/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libdwarf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdwarf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libdxfrw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libdxfrw/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libe57format](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libe57format/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libebur128](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libebur128/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libedit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libedit/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (!windows &#124; mingw) & !android |
| [libenvpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libenvpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libepoxy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libepoxy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(windows & staticcrt) |
| [liberasurecode](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liberasurecode/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !windows |
| [libev](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libev/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libevdev](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libevdev/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libevent](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libevent/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libeventheader-decode](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libeventheader-decode/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; windows |
| [libeventheader-tracepoint](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libeventheader-tracepoint/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; windows |
| [libevhtp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libevhtp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libexif](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libexif/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libfabric](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libfabric/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | freebsd &#124; linux &#124; osx &#124; (windows & x64 & !mingw & !uwp & !(static & staticcrt)) |
| [libffi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libffi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libfido2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libfido2/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp |
| [libflac](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libflac/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libfn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libfn/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libfontenc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libfontenc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libfork](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libfork/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libfort](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libfort/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libfs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libfs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libftdi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libftdi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libftdi1](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libftdi1/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libfuse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libfuse/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; freebsd |
| [libgcrypt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgcrypt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [libgd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libgeotiff](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgeotiff/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libgig](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgig/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [libgit2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgit2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libgme](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgme/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libgnutls](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgnutls/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [libgo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgo/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm &#124; uwp) |
| [libgossip](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgossip/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libgpg-error](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgpg-error/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [libgpiod](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgpiod/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux & (x64 &#124; arm) |
| [libgta](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgta/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libguarded](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libguarded/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libgwenhywfar](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgwenhywfar/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [libgxps](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libgxps/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libharu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libharu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libhat](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libhat/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; linux |
| [libhdfs3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libhdfs3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libheif](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libheif/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libhsplasma](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libhsplasma/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm &#124; uwp &#124; xbox) |
| [libhv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libhv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libhydrogen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libhydrogen/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libical](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libical/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libice](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libice/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libiconv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libiconv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libics](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libics/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libid3tag](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libid3tag/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libideviceactivation](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libideviceactivation/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libidn2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libidn2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libigl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libigl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libilbc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libilbc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & uwp) |
| [libimobiledevice](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libimobiledevice/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libimobiledevice-glue](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libimobiledevice-glue/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libinterpolate](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libinterpolate/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libirecovery](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libirecovery/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libjpeg-turbo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libjpeg-turbo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libjuice](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libjuice/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libjxl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libjxl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libkeyfinder](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libkeyfinder/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libkml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libkml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [liblas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblas/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm & !staticcrt |
| [liblbfgs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblbfgs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libleidenalg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libleidenalg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [liblemon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblemon/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [liblinear](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblinear/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [liblo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [liblrc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblrc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !osx |
| [liblsl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblsl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [liblsquic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblsquic/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !x86 |
| [libltdl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libltdl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [liblttng-ust](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblttng-ust/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [liblzf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblzf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [liblzma](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liblzma/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmad](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmad/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmagic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmagic/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmariadb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmariadb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libmatio-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmatio-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmaxminddb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmaxminddb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmediainfo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmediainfo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmem](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmem/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | (!xbox & windows) &#124; linux &#124; freebsd &#124; android |
| [libmemcached-awesome](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmemcached-awesome/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libmicrodns](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmicrodns/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox & !uwp |
| [libmicrohttpd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmicrohttpd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & windows) & !uwp |
| [libmidi2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmidi2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmikmod](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmikmod/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(osx &#124; uwp &#124; xbox) |
| [libmodbus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmodbus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libmodman](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmodman/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libmodplug](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmodplug/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libmorton](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmorton/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmount](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmount/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libmpeg2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmpeg2/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(linux &#124; osx &#124; uwp &#124; android) |
| [libmspack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmspack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmt32emu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmt32emu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmtp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmtp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (!windows &#124; mingw) & !uwp & !android |
| [libmultisense](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmultisense/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmupdf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmupdf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmypaint](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmypaint/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmysofa](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmysofa/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libmysql](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libmysql/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !mingw & !uwp & !xbox |
| [libnatpmp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libnatpmp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libnfs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libnfs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libnice](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libnice/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libnice-gst](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libnice-gst/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libnick](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libnick/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; linux &#124; osx |
| [libnoise](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libnoise/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libnop](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libnop/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libnotify](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libnotify/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libnsgif](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libnsgif/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libobfuscate](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libobfuscate/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libodb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libodb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libodb-boost](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libodb-boost/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libodb-mysql](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libodb-mysql/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libodb-pgsql](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libodb-pgsql/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libodb-sqlite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libodb-sqlite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libofx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libofx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libogg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libogg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libopenmpt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libopenmpt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libopensp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libopensp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libopnmidi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libopnmidi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libopusenc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libopusenc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [liboqs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liboqs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(windows & static) |
| [liborigin](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liborigin/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libosdp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libosdp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libosip2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libosip2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm) & !uwp |
| [libosmium](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libosmium/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libosmscout](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libosmscout/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libp7client](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libp7client/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm &#124; uwp &#124; osx) |
| [libpcap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libpcap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libpff](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libpff/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !(static & windows) & !uwp & !xbox |
| [libpg-query](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libpg-query/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [libphonenumber](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libphonenumber/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libplist](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libplist/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libpmemobj-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libpmemobj-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libpng](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libpng/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libpopcnt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libpopcnt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libpopt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libpopt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libpq](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libpq/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !emscripten |
| [libpqxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libpqxx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libprotobuf-mutator](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libprotobuf-mutator/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libproxy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libproxy/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(uwp &#124; xbox &#124; android) |
| [libpsl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libpsl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libqcow](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libqcow/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libqglviewer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libqglviewer/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !xbox |
| [libqrencode](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libqrencode/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libqtrest](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libqtrest/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [librabbitmq](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/librabbitmq/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libraqm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libraqm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [librats](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/librats/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libraw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libraw/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [librdkafka](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/librdkafka/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libredwg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libredwg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libremidi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libremidi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libressl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libressl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [librsvg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/librsvg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [librsync](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/librsync/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [librtmp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/librtmp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [librtpi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/librtpi/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [librttopo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/librttopo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsamplerate](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsamplerate/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsass](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsass/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libsbml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsbml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libsbsms](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsbsms/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libscran-umappp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libscran-umappp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsecret](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsecret/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !ios & !osx & !windows |
| [libsercomm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsercomm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libserial](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libserial/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx |
| [libsersi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsersi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsharp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsharp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [libshout](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libshout/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libsigcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsigcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsl3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsl3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libslirp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libslirp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsmacker](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsmacker/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsmb2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsmb2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsndfile](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsndfile/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libsnoretoast](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsnoretoast/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [libsodium](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsodium/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsonic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsonic/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx |
| [libsoundio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsoundio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm64 & windows) |
| [libsoup](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsoup/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libspatialindex](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libspatialindex/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libspatialite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libspatialite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libspeechd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libspeechd/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !windows & !uwp & !xbox & !android & !osx & !ios & !mingw & !emscripten |
| [libspnav](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libspnav/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libspng](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libspng/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsquish](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsquish/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsrt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsrt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libsrtp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsrtp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libssh](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libssh/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [libssh2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libssh2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libstemmer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libstemmer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libstk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libstk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsvm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsvm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libsystemd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libsystemd/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libtar](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtar/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libtasn1](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtasn1/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libtcod](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtcod/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libtess2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtess2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libtheora](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtheora/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libtins](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtins/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libtomcrypt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtomcrypt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libtommath](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtommath/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libtorch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtorch/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !static) &#124; osx &#124; linux |
| [libtorrent](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtorrent/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libtracepoint](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtracepoint/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; windows |
| [libtracepoint-control](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtracepoint-control/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libtracepoint-decode](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtracepoint-decode/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; windows |
| [libtwolame](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libtwolame/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libu2f-server](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libu2f-server/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (x86 &#124; x64) & windows |
| [libudfread](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libudfread/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libudis86](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libudis86/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libudns](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libudns/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows & !osx |
| [libui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libui/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !emscripten & !ios & !uwp |
| [libunibreak](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libunibreak/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libunifex](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libunifex/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libunistring](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libunistring/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libunwind](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libunwind/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libupnp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libupnp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [liburcu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liburcu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [liburing](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liburing/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libusb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libusb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libusb-win32](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libusb-win32/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !xbox & !(static & staticcrt) |
| [libusbmuxd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libusbmuxd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libusbp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libusbp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp |
| [libuuid](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libuuid/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !osx & !windows |
| [libuv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libuv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libuvc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libuvc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !windows |
| [libva](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libva/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [libvault](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libvault/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libversion](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libversion/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & static) |
| [libvhdi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libvhdi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libvips](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libvips/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libvmaf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libvmaf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libvorbis](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libvorbis/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libvpl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libvpl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (x64 &#124; x86) & (windows &#124; linux) & !uwp |
| [libvpx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libvpx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libwandio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libwandio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libwebm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libwebm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libwebp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libwebp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libwebsockets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libwebsockets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libx11](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libx11/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxau](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxau/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxaw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxaw/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; !staticcrt |
| [libxcb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxcb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxchange](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxchange/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxcomposite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxcomposite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxcrypt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxcrypt/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx |
| [libxcvt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxcvt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [libxdamage](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxdamage/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxdf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxdf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxdiff](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxdiff/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libxdmcp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxdmcp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxext](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxext/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxfixes](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxfixes/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxfont](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxfont/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxinerama](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxinerama/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxkbcommon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxkbcommon/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxkbfile](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxkbfile/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxlsxwriter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxlsxwriter/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxml2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxml2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxmlb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxmlb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [libxmlmm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxmlmm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxmlpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxmlpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxmp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxmp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [libxmu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxmu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxpm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxpm/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; linux |
| [libxpresent](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxpresent/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxrandr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxrandr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxrender](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxrender/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxres](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxres/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxscrnsaver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxscrnsaver/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxslt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxslt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [libxt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm64 & windows) |
| [libxtst](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxtst/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libxxf86vm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libxxf86vm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libyaml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libyaml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libyuv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libyuv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libzen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libzen/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libzim](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libzim/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp & !xbox |
| [libzip](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libzip/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [libzippp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/libzippp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [licensepp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/licensepp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [lief](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lief/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lightgbm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lightgbm/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !osx & !uwp |
| [lightningscanner](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lightningscanner/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm |
| [lilv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lilv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [linalg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/linalg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [linmath](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/linmath/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [linux-dfl-uapi-headers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/linux-dfl-uapi-headers/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [lionkor-commandline](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lionkor-commandline/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [liquid-dsp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/liquid-dsp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx |
| [litehtml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/litehtml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [live555](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/live555/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [livepp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/livepp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [llama-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/llama-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [llfio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/llfio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [llgi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/llgi/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(uwp &#124; android) |
| [llgl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/llgl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [llhttp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/llhttp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [llnl-units](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/llnl-units/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lloyal-ai-inlined-vector](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lloyal-ai-inlined-vector/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [llvm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/llvm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm & windows) |
| [lmdb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lmdb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lodepng](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lodepng/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [log4cplus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/log4cplus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [log4cpp-log4cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/log4cpp-log4cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (linux &#124; windows) & !uwp |
| [log4cxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/log4cxx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [logme](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/logme/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [loguru](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/loguru/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lpeg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lpeg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ls-qpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ls-qpack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ltla-aarand](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ltla-aarand/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ltla-cppirlba](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ltla-cppirlba/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ltla-cppkmeans](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ltla-cppkmeans/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ltla-powerit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ltla-powerit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ltla-sanisizer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ltla-sanisizer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ltla-subpar](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ltla-subpar/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lttb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lttb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lua](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lua/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lua-compat53](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lua-compat53/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [luabridge](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/luabridge/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [luabridge3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/luabridge3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [luafilesystem](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/luafilesystem/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [luajit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/luajit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [luasec](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/luasec/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !staticcrt |
| [luasocket](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/luasocket/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [luau](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/luau/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lunarg-vulkantools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lunarg-vulkantools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !osx & !(static & staticcrt) |
| [lunasvg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lunasvg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [luv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/luv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [lv2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lv2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lwlog](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lwlog/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !(arm & windows) & !x86 |
| [lz4](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lz4/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lzav](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lzav/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lzfse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lzfse/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm |
| [lzo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lzo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [lzokay](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/lzokay/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mach](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mach/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [maddy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/maddy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [magic-args](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/magic-args/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [magic-enum](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/magic-enum/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [magma](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/magma/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [magnum](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/magnum/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [magnum-extras](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/magnum-extras/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [magnum-integration](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/magnum-integration/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [magnum-plugins](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/magnum-plugins/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mailio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mailio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [makeid](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/makeid/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [manif](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/manif/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [manifold](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/manifold/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mapbox-geojson-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mapbox-geojson-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mapbox-geojson-vt-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mapbox-geojson-vt-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mapbox-geometry](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mapbox-geometry/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mapbox-polylabel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mapbox-polylabel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mapbox-variant](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mapbox-variant/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mapbox-wagyu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mapbox-wagyu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mapnik](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mapnik/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [marble](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/marble/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & x64 & !static & !xbox |
| [marchingcubecpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/marchingcubecpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mariadb-connector-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mariadb-connector-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [marisa-trie](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/marisa-trie/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw &#124; (windows & static) |
| [marl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/marl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [marzbanpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/marzbanpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mas-bandwidth-netcode](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mas-bandwidth-netcode/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mas-bandwidth-reliable](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mas-bandwidth-reliable/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mas-bandwidth-serialize](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mas-bandwidth-serialize/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mas-bandwidth-yojimbo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mas-bandwidth-yojimbo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [matajoh-libnpy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/matajoh-libnpy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [matchit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/matchit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [materialx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/materialx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [mathc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mathc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mathgl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mathgl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !xbox & !android |
| [mathter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mathter/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [matio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/matio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [matplotlib-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/matplotlib-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [matplotplusplus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/matplotplusplus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(windows & arm) |
| [matroska](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/matroska/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mbedtls](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mbedtls/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mcap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mcap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mchehab-zbar](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mchehab-zbar/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [mcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [md4c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/md4c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mdl-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mdl-sdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !x86 & !(windows & (arm &#124; uwp)) & !(osx & arm) & !android |
| [mdns](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mdns/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mdnsresponder](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mdnsresponder/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !arm |
| [mdspan](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mdspan/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mecab](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mecab/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm & windows) |
| [meekrosoft-fff](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/meekrosoft-fff/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [memorymodule](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/memorymodule/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !linux & !osx & !uwp |
| [meojson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/meojson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mesa](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mesa/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm) & !staticcrt & !uwp |
| [meschach](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/meschach/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [meshoptimizer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/meshoptimizer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [metis](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/metis/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [metrohash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/metrohash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mexce](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mexce/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | ((windows &#124; linux) & (x86 &#124; x64)) &#124; (osx & (arm64 &#124; x64)) |
| [mfl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mfl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mfx-dispatch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mfx-dispatch/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 允许 | ((x86 &#124; x64) & (android &#124; linux)) &#124; (windows & !uwp) |
| [mgclient](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mgclient/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [mgnlibs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mgnlibs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mhook](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mhook/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !arm |
| [michaelmiller-sec21](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/michaelmiller-sec21/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [micro-gl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/micro-gl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [microlog](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/microlog/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [microsoft-windows-devices-midi2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/microsoft-windows-devices-midi2/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & (arm64 &#124; arm64ec &#124; x64) |
| [mikktspace](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mikktspace/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mimalloc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mimalloc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [mimicpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mimicpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [minc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/minc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [minhook](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/minhook/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !arm |
| [miniaudio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/miniaudio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [minifb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/minifb/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [minimp3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/minimp3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [minio-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/minio-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [miniply](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/miniply/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [minisat-master-keying](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/minisat-master-keying/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [minitrace](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/minitrace/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [miniupnpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/miniupnpc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [miniz](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/miniz/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [minizip](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/minizip/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [minizip-ng](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/minizip-ng/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [minmea](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/minmea/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mlpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mlpack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [mman](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mman/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [mmloader](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mmloader/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (x86 &#124; x64) & windows & !uwp |
| [mmx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mmx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mnn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mnn/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(arm &#124; uwp &#124; ios &#124; android) |
| [modern-cpp-kafka](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/modern-cpp-kafka/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [modp-base64](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/modp-base64/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mongo-c-driver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mongo-c-driver/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [mongo-cxx-driver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mongo-cxx-driver/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mongoose](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mongoose/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [monkeys-audio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/monkeys-audio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(uwp &#124; osx &#124; linux) |
| [moos-core](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/moos-core/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox & !uwp |
| [moos-essential](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/moos-essential/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [moos-ui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/moos-ui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [morcules-swiftnet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/morcules-swiftnet/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (osx & arm64) &#124; (linux & arm64) |
| [morphologica](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/morphologica/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [morton-nd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/morton-nd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mosquitto](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mosquitto/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [mp-units](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mp-units/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mp3lame](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mp3lame/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mpark-patterns](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mpark-patterns/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mpark-variant](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mpark-variant/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mpc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mpdecimal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mpdecimal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [mpfr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mpfr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [mpg123](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mpg123/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [mpi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mpi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [mpir](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mpir/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(uwp &#124; arm) |
| [mpmcqueue](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mpmcqueue/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mpss](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mpss/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !uwp & !bsd & !emscripten |
| [mqtt-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mqtt-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ms-gdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ms-gdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & (x64 &#124; arm64) & !uwp & !xbox & !staticcrt |
| [ms-gdkx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ms-gdkx/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & x64 & !uwp |
| [ms-gltf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ms-gltf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !linux |
| [ms-gsl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ms-gsl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ms-ifc-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ms-ifc-sdk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [msdfgen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/msdfgen/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [msgpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/msgpack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [msgpack-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/msgpack-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [msgpack11](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/msgpack11/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [msh3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/msh3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(static & staticcrt) |
| [msinttypes](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/msinttypes/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [msix](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/msix/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !static |
| [msmpi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/msmpi/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & (x64 &#124; x86) |
| [msolve](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/msolve/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [msquic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/msquic/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !mingw & !(static & staticcrt) |
| [mstch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mstch/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mtlt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mtlt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [muda](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/muda/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !uwp & !xbox) &#124; (linux & x64) &#124; (linux & arm64) |
| [mujoco](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mujoco/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & static) |
| [mujs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mujs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mumps-solver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mumps-solver/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !ios & !emscripten & !uwp & !(windows & arm) & !(windows & !mingw & static) |
| [munit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/munit/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm &#124; uwp) |
| [muparser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/muparser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [murmur3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/murmur3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [murmurhash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/murmurhash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [mvfst](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mvfst/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; static |
| [mxml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mxml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & (uwp &#124; static &#124; arm32)) |
| [mygui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mygui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [mypaint-brushes](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mypaint-brushes/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mysql-connector-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mysql-connector-cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp |
| [mysvac-jsonlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mysvac-jsonlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [mzying2001-sw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/mzying2001-sw/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [nameof](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nameof/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nana](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nana/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [nano-signal-slot](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nano-signal-slot/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [nanoarrow](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanoarrow/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nanobench](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanobench/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [nanobind](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanobind/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nanodbc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanodbc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [nanoflann](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanoflann/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nanogui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanogui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [nanojsonc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanojsonc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nanomsg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanomsg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nanopb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanopb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nanoprintf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanoprintf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nanorange](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanorange/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nanort](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanort/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nanosvg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanosvg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nanovg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nanovg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [nativefiledialog-extended](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nativefiledialog-extended/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !ios & !uwp |
| [nayuki-qr-code-generator](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nayuki-qr-code-generator/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nccl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nccl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux & x64 |
| [ncnn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ncnn/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm) |
| [ncurses](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ncurses/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [ndis-driver-library](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ndis-driver-library/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [neargye-semver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/neargye-semver/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ned14-internal-quickcpplib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ned14-internal-quickcpplib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [neko-event](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/neko-event/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [neko-function](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/neko-function/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [neko-log](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/neko-log/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [neko-network](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/neko-network/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [neko-schema](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/neko-schema/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [neko-system](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/neko-system/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; linux &#124; osx |
| [neko-threadpool](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/neko-threadpool/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [neon2sse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/neon2sse/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [neoslippi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/neoslippi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [netcdf-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/netcdf-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [netcdf-cxx4](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/netcdf-cxx4/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [netcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/netcpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; linux |
| [netgen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/netgen/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 排除 | arm64 &#124; x64 |
| [nethost](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nethost/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | (windows & !uwp), (linux, osx) |
| [nettle](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nettle/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [networkdirect-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/networkdirect-sdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & (x64 &#124; x86) & !uwp |
| [ng-log](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ng-log/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nghttp2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nghttp2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nghttp3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nghttp3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ngspice](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ngspice/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(linux &#124; osx &#124; arm &#124; uwp) |
| [ngtcp2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ngtcp2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nifly](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nifly/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [nifticlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nifticlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [nlohmann-fifo-map](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nlohmann-fifo-map/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nlohmann-json](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nlohmann-json/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nlopt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nlopt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nmslib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nmslib/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm &#124; uwp) |
| [nng](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nng/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [nngpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nngpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nnpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nnpack/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx |
| [node-addon-api](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/node-addon-api/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | ((windows & !arm) &#124; linux &#124; osx) & !uwp |
| [node-api-headers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/node-api-headers/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !arm & !uwp) &#124; linux &#124; osx |
| [nodesoup](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nodesoup/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nonius](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nonius/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nonstd-bit-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nonstd-bit-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nonstd-scope-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nonstd-scope-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nowide](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nowide/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nspr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nspr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox & !(windows & static & staticcrt) |
| [nss](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nss/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !arm32 & !(arm & windows) |
| [nsync](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nsync/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nt-wrapper](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nt-wrapper/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ntf-core](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ntf-core/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nu-book-zxing-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nu-book-zxing-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nuklear](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nuklear/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [numactl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/numactl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [numcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/numcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [numkong](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/numkong/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !((arm64 &#124; x86) & windows) |
| [nuraft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nuraft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [nuspell](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nuspell/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [nvidia-cutlass](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nvidia-cutlass/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [nvrhi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nvrhi/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !uwp & !xbox) &#124; (linux & (x64 &#124; arm64)) |
| [nvtt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nvtt/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp & !arm |
| [nyan-lang](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/nyan-lang/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !osx & !static & !uwp |
| [oatpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-consul](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-consul/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-curl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-curl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-libressl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-libressl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-mbedtls](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-mbedtls/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-mongo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-mongo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-openssl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-openssl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-postgresql](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-postgresql/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-sqlite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-sqlite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-ssdp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-ssdp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-swagger](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-swagger/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-websocket](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-websocket/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oatpp-zlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oatpp-zlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [obfuscxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/obfuscxx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oboe](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oboe/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | android |
| [observer-ptr-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/observer-ptr-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ocilib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ocilib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm & windows) |
| [octave](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/octave/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; mingw |
| [octomap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/octomap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [odbccpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/odbccpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [ode](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ode/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [offscale-libetcd-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/offscale-libetcd-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ogre](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ogre/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [ogre-next](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ogre-next/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !emscripten & !uwp & !xbox |
| [ois](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ois/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 允许 | !(arm &#124; arm64 &#124; uwp) |
| [omniorb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/omniorb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox & !((arm &#124; x86) & windows) & !osx |
| [ompl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ompl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(static & staticcrt) &#124; (windows & !mingw) |
| [omplapp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/omplapp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [onednn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/onednn/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 排除 | x64 & !uwp |
| [oniguruma](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oniguruma/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [onnx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/onnx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [onnx-optimizer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/onnx-optimizer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [onnxruntime](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/onnxruntime/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [onnxruntime-gpu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/onnxruntime-gpu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oof](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oof/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [open-dis-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/open-dis-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [open62541](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/open62541/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [open62541pp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/open62541pp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openal-soft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openal-soft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [openblas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openblas/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [opencascade](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opencascade/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [opencc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opencc/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm &#124; uwp) |
| [opencensus-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opencensus-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [opencl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opencl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [opencolorio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opencolorio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [opencsg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opencsg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openctm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openctm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [opencv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opencv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [opencv2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opencv2/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !(arm & windows) & !android |
| [opencv3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opencv3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [opencv4](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opencv4/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openexr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openexr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [openfbx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openfbx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openfx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openfx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [opengl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opengl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [opengl-registry](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opengl-registry/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [openh264](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openh264/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openigtlink](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openigtlink/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openimageio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openimageio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openjpeg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openjpeg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openjph](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openjph/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openldap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openldap/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !windows, (mingw & !x86) |
| [openmama](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openmama/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [openmesh](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openmesh/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openmpi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openmpi/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !windows & !android & !x86 & !arm32 |
| [openmvg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openmvg/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | (x86 &#124; x64 &#124; arm64) & !xbox |
| [openmvs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openmvs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [openni2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openni2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !staticcrt |
| [openpit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openpit/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | ((windows & x64 & !uwp) &#124; (osx & (arm64 &#124; x64)) &#124; (linux & (arm64 &#124; x64))) & !(static & staticcrt) |
| [openscap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openscap/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (linux &#124; windows) & !(static & staticcrt) |
| [openslide](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openslide/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [openssl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openssl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [opensubdiv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opensubdiv/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm & android) & !uwp |
| [opentelemetry-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opentelemetry-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [opentelemetry-cpp-contrib-version](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opentelemetry-cpp-contrib-version/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [opentracing](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opentracing/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [openturns](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openturns/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openvdb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openvdb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [openvino](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openvino/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 排除 | !uwp & !x86 & !(android & arm32) |
| [openvpn3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openvpn3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [openvr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openvr/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !uwp & (x64 &#124; x86)) &#124; (linux & (x64 &#124; x86 &#124; arm64)) |
| [openxlsx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openxlsx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [openxr-loader](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openxr-loader/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [openzl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/openzl/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 排除 | !uwp & !x86 & !arm32 |
| [optimus-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/optimus-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [optional-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/optional-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [opus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [opusfile](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/opusfile/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [orange-math](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/orange-math/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [orange-vmprotect-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/orange-vmprotect-sdk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | (windows &#124; linux &#124; osx &#124; android) & !(static & staticcrt) |
| [orc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/orc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [orefkov-simstr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/orefkov-simstr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ormpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ormpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx &#124; (windows & !uwp) |
| [orocos-kdl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/orocos-kdl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [oscpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/oscpack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & !static) |
| [osg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/osg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [osg-qt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/osg-qt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [osgearth](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/osgearth/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(arm &#124; x86 &#124; wasm32 &#124; android) |
| [osmanip](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/osmanip/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [osp-collection](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/osp-collection/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [osqp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/osqp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [osqp-eigen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/osqp-eigen/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [otl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/otl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [outcome](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/outcome/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [p-ranav-csv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/p-ranav-csv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [p-ranav-csv2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/p-ranav-csv2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [p-ranav-glob](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/p-ranav-glob/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pagmo2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pagmo2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [paho-mqtt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/paho-mqtt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [paho-mqttpp3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/paho-mqttpp3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [palsigslot](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/palsigslot/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pango](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pango/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [pangolin](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pangolin/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [pangomm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pangomm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [parallel-hashmap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/parallel-hashmap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [parallelstl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/parallelstl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [paraview](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/paraview/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [parmetis](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/parmetis/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [parsi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/parsi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [parson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/parson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [patternia](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/patternia/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pbc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pbc/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !uwp & !arm |
| [pcapplusplus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pcapplusplus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pcg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pcg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pciids](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pciids/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [pcl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pcl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pcre](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pcre/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pcre2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pcre2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pdal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pdal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(static & staticcrt) |
| [pdal-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pdal-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & staticcrt) |
| [pdal-dimbuilder](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pdal-dimbuilder/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [pdcurses](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pdcurses/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !mingw |
| [pdqsort](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pdqsort/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pe-parse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pe-parse/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [pegtl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pegtl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pegtl-2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pegtl-2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [perf-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/perf-cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [perfetto](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/perfetto/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !uwp & !x86 |
| [pffft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pffft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pfring](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pfring/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [pfultz2-linq](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pfultz2-linq/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [phnt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/phnt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [physac](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/physac/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [physfs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/physfs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [physx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/physx/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !mingw & !uwp) &#124; (linux & x64) &#124; (linux & arm64) |
| [picobench](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/picobench/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [picohttpparser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/picohttpparser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [picojson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/picojson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [picosha2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/picosha2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [piex](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/piex/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pipewire](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pipewire/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [pistache](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pistache/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !windows |
| [pixel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pixel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pixman](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pixman/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pkgconf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pkgconf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [plasma-wayland-protocols](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plasma-wayland-protocols/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [platform-folders](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/platform-folders/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plf-colony](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plf-colony/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plf-hive](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plf-hive/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plf-indiesort](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plf-indiesort/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plf-list](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plf-list/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plf-nanotimer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plf-nanotimer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plf-queue](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plf-queue/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plf-stack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plf-stack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plf-tools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plf-tools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(osx &#124; uwp &#124; xbox) |
| [plibsys](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plibsys/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [plog](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plog/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plplot](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plplot/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plustache](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plustache/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plutosvg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plutosvg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [plutovg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/plutovg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pmdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pmdk/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 排除 | !(linux &#124; arm &#124; x86) |
| [pmp-library](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pmp-library/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [pngpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pngpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pngwriter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pngwriter/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pocketfft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pocketfft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pocketpy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pocketpy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [poco](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/poco/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [podofo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/podofo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [poissonrecon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/poissonrecon/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [polkit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/polkit/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [polkit-qt-1](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/polkit-qt-1/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [polyclipping](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/polyclipping/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [polyhook2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/polyhook2/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 允许 | (x86 &#124; x64) & !(uwp &#124; osx) |
| [polymorphic-value](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/polymorphic-value/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ponder](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ponder/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [poolstl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/poolstl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [poppler](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/poppler/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [poppler-data](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/poppler-data/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [popsift](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/popsift/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(uwp &#124; arm &#124; arm64 &#124; android &#124; x86) |
| [portable-file-dialogs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/portable-file-dialogs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [portable-snippets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/portable-snippets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & osx) |
| [portaudio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/portaudio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [portmidi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/portmidi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [portsmf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/portsmf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [poselib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/poselib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ppconsul](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ppconsul/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ppqsort](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ppqsort/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pprint](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pprint/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pqp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pqp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pravila00-enum-string](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pravila00-enum-string/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pravila00-enumflag](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pravila00-enumflag/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pravila00-make-vector](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pravila00-make-vector/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [presentmon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/presentmon/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [proj](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/proj/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [projectm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/projectm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [projectm-eval](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/projectm-eval/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [prometheus-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/prometheus-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [promise-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/promise-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [protobuf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/protobuf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [protobuf-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/protobuf-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [protopuf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/protopuf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [protozero](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/protozero/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [proxsuite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/proxsuite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [proxy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/proxy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [proxygen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/proxygen/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [psimd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/psimd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ptc-print](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ptc-print/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ptex](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ptex/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [pthread](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pthread/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pthread-stubs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pthread-stubs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pthreadpool](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pthreadpool/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pthreads](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pthreads/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ptyqt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ptyqt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [pugixml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pugixml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pulsar-client-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pulsar-client-cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !((arm &#124; x86) & windows) & !android |
| [pulseaudio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pulseaudio/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !osx & !windows |
| [pulzed-mini](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pulzed-mini/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pxlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pxlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pybind11](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pybind11/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [pystring](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/pystring/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [python2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/python2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & osx) & !(arm & windows) & !uwp |
| [python3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/python3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !mingw |
| [qca](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qca/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qcbor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qcbor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qcoro](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qcoro/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qcustomplot](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qcustomplot/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [qdldl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qdldl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qe6502](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qe6502/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [qgis-o2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qgis-o2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qhttpengine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qhttpengine/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [qhull](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qhull/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qlementine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qlementine/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qlementine-icons](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qlementine-icons/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qmex](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qmex/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qoi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qoi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qoixx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qoixx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qpdf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qpdf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [qpid-proton](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qpid-proton/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(static & staticcrt) & !uwp |
| [qpoases](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qpoases/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qscintilla](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qscintilla/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [qt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt-advanced-docking-system](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt-advanced-docking-system/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [qt3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-activeqt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-activeqt/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [qt5-androidextras](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-androidextras/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | android |
| [qt5-base](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-base/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-charts](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-charts/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-connectivity](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-connectivity/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-datavis3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-datavis3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-declarative](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-declarative/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-doc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-doc/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [qt5-gamepad](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-gamepad/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-graphicaleffects](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-graphicaleffects/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-imageformats](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-imageformats/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-location](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-location/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-macextras](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-macextras/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | osx |
| [qt5-mqtt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-mqtt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-multimedia](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-multimedia/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-networkauth](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-networkauth/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-purchasing](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-purchasing/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-quick3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-quick3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-quickcontrols](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-quickcontrols/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-quickcontrols2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-quickcontrols2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-quicktimeline](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-quicktimeline/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-remoteobjects](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-remoteobjects/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-script](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-script/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-scxml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-scxml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-sensors](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-sensors/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-serialbus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-serialbus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-serialport](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-serialport/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-speech](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-speech/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-svg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-svg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-tools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-tools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-translations](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-translations/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-virtualkeyboard](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-virtualkeyboard/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-wayland](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-wayland/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [qt5-webchannel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-webchannel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-webengine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-webengine/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !static |
| [qt5-webglplugin](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-webglplugin/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-websockets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-websockets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-webview](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-webview/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5-winextras](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-winextras/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [qt5-x11extras](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-x11extras/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [qt5-xmlpatterns](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5-xmlpatterns/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qt5compat](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qt5compat/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtactiveqt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtactiveqt/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [qtapplicationmanager](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtapplicationmanager/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | android &#124; ios &#124; linux &#124; osx &#124; qnx &#124; (windows & !uwp & (arm64 &#124; x64)) |
| [qtbase](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtbase/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [qtcharts](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtcharts/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtcoap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtcoap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtconnectivity](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtconnectivity/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtdatavis3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtdatavis3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtdeclarative](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtdeclarative/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtdeviceutilities](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtdeviceutilities/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [qtdoc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtdoc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtgraphs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtgraphs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtgrpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtgrpc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qthttpserver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qthttpserver/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtimageformats](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtimageformats/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtinterfaceframework](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtinterfaceframework/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtkeychain](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtkeychain/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtkeychain-qt6](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtkeychain-qt6/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtlanguageserver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtlanguageserver/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtlocation](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtlocation/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtlottie](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtlottie/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtmqtt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtmqtt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtmultimedia](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtmultimedia/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtnetworkauth](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtnetworkauth/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtopcua](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtopcua/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtpositioning](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtpositioning/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtquick3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtquick3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtquick3dphysics](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtquick3dphysics/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtquickeffectmaker](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtquickeffectmaker/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [qtquicktimeline](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtquicktimeline/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtremoteobjects](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtremoteobjects/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtscxml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtscxml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtsensors](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtsensors/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtserialbus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtserialbus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtserialport](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtserialport/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !ios |
| [qtshadertools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtshadertools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtspeech](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtspeech/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & x86) |
| [qtsvg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtsvg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qttools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qttools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qttranslations](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qttranslations/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtvirtualkeyboard](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtvirtualkeyboard/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtwayland](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtwayland/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [qtwebchannel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtwebchannel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtwebengine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtwebengine/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtwebsockets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtwebsockets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qtwebview](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qtwebview/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 排除 | x64 &#124; arm64 |
| [quadtree](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/quadtree/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [quantlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/quantlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & !static) |
| [quarter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/quarter/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp |
| [quaternions](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/quaternions/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [quazip](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/quazip/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [quickfix](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/quickfix/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(osx & arm64) |
| [quickjs-ng](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/quickjs-ng/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [quill](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/quill/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [quirc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/quirc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qwt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qwt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [qwtw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qwtw/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & x64 & !static |
| [qzxing](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/qzxing/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rabit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rabit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [ragel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ragel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [random123](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/random123/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [randomstr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/randomstr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rang](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rang/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [range-v3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/range-v3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rapidcheck](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rapidcheck/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rapidcsv](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rapidcsv/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rapidfuzz-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rapidfuzz-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rapidhash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rapidhash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rapidjson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rapidjson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rapidobj](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rapidobj/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !linux |
| [rapidxml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rapidxml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rapidxml-ns](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rapidxml-ns/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rappture](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rappture/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [raygui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/raygui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [raylib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/raylib/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !arm32 & !uwp |
| [raylib-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/raylib-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rbdl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rbdl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rdma-core](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rdma-core/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [re2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/re2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [reaction](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/reaction/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [reactiveplusplus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/reactiveplusplus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [reactphysics3d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/reactphysics3d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [readerwriterqueue](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/readerwriterqueue/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [readline](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/readline/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [readline-unix](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/readline-unix/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [readline-win32](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/readline-win32/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [readosm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/readosm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [realm-core](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/realm-core/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !emscripten |
| [realsense2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/realsense2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(windows & arm) |
| [recastnavigation](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/recastnavigation/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rectpack2d](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rectpack2d/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [recycle](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/recycle/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [red0124-ssp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/red0124-ssp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [redis-plus-plus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/redis-plus-plus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [redisx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/redisx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [refl-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/refl-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [reflectcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/reflectcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [refprop-headers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/refprop-headers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rego-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rego-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !x86 |
| [rendergraph](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rendergraph/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [replxx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/replxx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [reproc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/reproc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [rerun-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rerun-sdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !staticcrt) &#124; (osx & arm64) &#124; (linux & (x64 &#124; arm64)) |
| [rest-rpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rest-rpc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [restbed](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/restbed/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [restc-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/restc-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [restclient-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/restclient-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [restinio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/restinio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [resultlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/resultlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [retropak](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/retropak/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [rewolf-wow64ext](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rewolf-wow64ext/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !mingw & x86 |
| [rexo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rexo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rgfw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rgfw/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rhash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rhash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [rhasheq](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rhasheq/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [riffcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/riffcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ring-span-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ring-span-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rioki-glow](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rioki-glow/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ripper37-libbase](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ripper37-libbase/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rivers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rivers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rkcommon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rkcommon/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 允许 | x86 &#124; x64 |
| [rlottie](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rlottie/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rmlui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rmlui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rmqcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rmqcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rnnoise](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rnnoise/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !windows & !arm |
| [roaring](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/roaring/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !(android & arm32) |
| [robin-hood-hashing](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/robin-hood-hashing/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [robin-map](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/robin-map/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [robotraconteur](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/robotraconteur/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & (x86 &#124; x64)) &#124; (linux & (x86 &#124; x64 &#124; arm64 &#124; arm32)) &#124; (osx & (x64 &#124; arm64)) |
| [robotraconteur-companion](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/robotraconteur-companion/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & (x86 &#124; x64)) &#124; (linux & (x86 &#124; x64 &#124; arm64 &#124; arm32)) &#124; (osx & (x64 &#124; arm64)) |
| [rocksdb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rocksdb/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !uwp & !(arm & !arm64 & android) |
| [rohit-singh-gautam-serializer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rohit-singh-gautam-serializer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [rp-ntuples](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rp-ntuples/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rpclib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rpclib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rply](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rply/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rsasynccpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rsasynccpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !arm |
| [rsig](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rsig/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rsm-binary-io](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rsm-binary-io/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !osx & !uwp |
| [rsm-bsa](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rsm-bsa/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !x86 & !osx & !uwp |
| [rsm-mmio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rsm-mmio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !osx & !uwp |
| [rsocket](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rsocket/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rtabmap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rtabmap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rtabmap-res-tool](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rtabmap-res-tool/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [rtaudio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rtaudio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [rtc-benchmarksuite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rtc-benchmarksuite/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !xbox) &#124; (linux & x64) &#124; (osx & x64) |
| [rtlsdr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rtlsdr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [rtmfp-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rtmfp-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rtmidi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rtmidi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [rttr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rttr/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (static & staticcrt) &#124; (!static & staticcrt) &#124; (!static & !staticcrt) |
| [ruapu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ruapu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rubberband](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rubberband/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(windows & static) & !xbox |
| [ruckig](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ruckig/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rxcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rxcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rxqt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rxqt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [rxspencer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/rxspencer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [ryml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ryml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ryu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ryu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [s2geometry](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/s2geometry/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [s2n](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/s2n/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !windows |
| [safeint](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/safeint/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [safetyhook](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/safetyhook/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows &#124; linux) & !arm & !uwp |
| [sail](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sail/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [sajson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sajson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [salome-configuration](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/salome-configuration/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; linux |
| [salome-med-fichier](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/salome-med-fichier/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [salome-medcoupling](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/salome-medcoupling/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & static) |
| [sassc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sassc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [saucer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/saucer/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp |
| [sbgecom](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sbgecom/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sbp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sbp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [scenepic](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/scenepic/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [scintilla](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/scintilla/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !mingw |
| [scinumtools3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/scinumtools3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sciplot](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sciplot/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [sciter-js](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sciter-js/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !arm & !static & !android & !freebsd & !openbsd & !netbsd & !(x86 & !windows) |
| [scnlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/scnlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [scope-guard](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/scope-guard/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [scotch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/scotch/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !arm & !uwp & !android & !osx |
| [scottt-debugbreak](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/scottt-debugbreak/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdbus-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdbus-cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux |
| [sdflib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdflib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdformat](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdformat/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [sdl2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl2-gfx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl2-gfx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl2-image](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl2-image/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl2-mixer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl2-mixer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl2-mixer-ext](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl2-mixer-ext/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl2-net](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl2-net/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl2-ttf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl2-ttf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl2pp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl2pp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [sdl3-image](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl3-image/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl3-mixer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl3-mixer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl3-net](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl3-net/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sdl3-shadercross](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl3-shadercross/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [sdl3-ttf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sdl3-ttf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [seacas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/seacas/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [seal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/seal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [seasocks](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/seasocks/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !osx & !android |
| [sebsjames-maths](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sebsjames-maths/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [secp256k1](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/secp256k1/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [selene](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/selene/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sentencepiece](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sentencepiece/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sentry-native](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sentry-native/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [septag-dmon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/septag-dmon/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [seqan](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/seqan/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [serd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/serd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [serdepp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/serdepp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(osx & arm) |
| [serf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/serf/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !uwp & !staticcrt & !arm |
| [sf2cute](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sf2cute/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sfcgal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sfcgal/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (x64 &#124; arm64) & (linux &#124; windows &#124; osx) |
| [sfgui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sfgui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sfl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sfl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sfml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sfml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [sfparse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sfparse/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sfsexp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sfsexp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [shader-slang](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/shader-slang/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (arm64 &#124; x64) & (linux &#124; osx &#124; windows) & !uwp & !(static & staticcrt) |
| [shaderc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/shaderc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [shaderwriter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/shaderwriter/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [shapelib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/shapelib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [shared-mime-info](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/shared-mime-info/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sheenbidi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sheenbidi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [shiftmedia-libgcrypt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/shiftmedia-libgcrypt/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !mingw |
| [shiftmedia-libgpg-error](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/shiftmedia-libgpg-error/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !mingw & !(arm &#124; arm64) |
| [si](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/si/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sigmatch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sigmatch/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [signalsmith-dsp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/signalsmith-dsp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [signalsmith-stretch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/signalsmith-stretch/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sigslot](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sigslot/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [simage](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simage/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [simbody](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simbody/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [simd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(uwp &#124; osx &#124; (arm64 & windows)) |
| [simde](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simde/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [simdjson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simdjson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [simdutf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simdutf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [simonbrunel-qtpromise](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simonbrunel-qtpromise/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [simple-fft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simple-fft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [simpleamqpclient](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simpleamqpclient/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !static |
| [simpleble](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simpleble/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp |
| [simpleini](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simpleini/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [simsimd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/simsimd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm64 & windows) |
| [sintra](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sintra/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sjpeg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sjpeg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [skcrypter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/skcrypter/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [skia](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/skia/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm32) & !mingw |
| [skyr-url](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/skyr-url/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [slang-verilog](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slang-verilog/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !arm32 & !(windows & !x64) |
| [sleef](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sleef/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & windows) |
| [sleepy-discord](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sleepy-discord/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [slick-dynamic-buffer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slick-dynamic-buffer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [slick-logger](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slick-logger/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [slick-net](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slick-net/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [slick-object-pool](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slick-object-pool/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [slick-perfmon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slick-perfmon/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [slick-queue](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slick-queue/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [slick-shm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slick-shm/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; linux &#124; osx |
| [slick-socket](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slick-socket/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; linux &#124; osx |
| [slick-stream-buffer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slick-stream-buffer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [slick-stream-buffer-multiplexer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slick-stream-buffer-multiplexer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [slickquant-alpaca-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slickquant-alpaca-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [slickquant-hyperliquid-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slickquant-hyperliquid-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [slikenet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/slikenet/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [sltbench](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sltbench/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [small-gicp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/small-gicp/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 排除 | !(x86 &#124; arm32) |
| [smax-clib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/smax-clib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [smf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/smf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [smpeg2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/smpeg2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [snap7](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/snap7/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp & !static |
| [snappy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/snappy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [snitch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/snitch/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [snmalloc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/snmalloc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [snowhouse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/snowhouse/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [so5extra](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/so5extra/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [soapysdr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/soapysdr/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !static |
| [sobjectizer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sobjectizer/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [soci](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/soci/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sockpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sockpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [soem](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/soem/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [soil](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/soil/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [soil2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/soil2/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [sokol](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sokol/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sol2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sol2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [solid3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/solid3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sonivox](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sonivox/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sophus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sophus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [soqt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/soqt/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 允许 | !(arm &#124; arm64 &#124; uwp) |
| [sord](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sord/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [soundtouch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/soundtouch/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [soxr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/soxr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spaceland](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spaceland/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [span-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/span-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sparrow-ipc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sparrow-ipc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [sparsehash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sparsehash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sparsepp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sparsepp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spatial-hash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spatial-hash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spatialite-tools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spatialite-tools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [spdlog](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spdlog/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spectra](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spectra/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [speex](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/speex/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [speexdsp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/speexdsp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spglib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spglib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spimpl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spimpl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spine-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spine-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spine-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spine-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spirit-po](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spirit-po/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spirv-cross](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spirv-cross/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spirv-headers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spirv-headers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spirv-reflect](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spirv-reflect/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spirv-tools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spirv-tools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spix](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spix/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [spout2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spout2/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !arm64 |
| [sproto](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sproto/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sprout](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sprout/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spscqueue](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spscqueue/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [spz](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/spz/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sqlcipher](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sqlcipher/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [sqlgen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sqlgen/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sqlite-flux](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sqlite-flux/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sqlite-modern-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sqlite-modern-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sqlite-orm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sqlite-orm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sqlite3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sqlite3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [sqlitecpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sqlitecpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sqlpp11](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sqlpp11/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sqlpp23](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sqlpp23/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [squirrel](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/squirrel/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sratom](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sratom/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [srell](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/srell/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [srpc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/srpc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sse2neon](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sse2neon/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [st-tree](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/st-tree/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stackwalker](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stackwalker/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [starlink-ast](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/starlink-ast/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [staticjson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/staticjson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [status-code](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/status-code/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [status-value-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/status-value-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stdexec](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stdexec/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stdgpu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stdgpu/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & x64 & !uwp & !xbox) &#124; (linux & x64) |
| [stduuid](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stduuid/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [steam-audio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/steam-audio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [stella-cv-fbow](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stella-cv-fbow/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stescobedo92-stellar](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stescobedo92-stellar/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [stftpitchshift](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stftpitchshift/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stillwater-universal](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stillwater-universal/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stlab](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stlab/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stlab-copy-on-write](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stlab-copy-on-write/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stlab-enum-ops](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stlab-enum-ops/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stormlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stormlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [str-view](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/str-view/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [strict-variant](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/strict-variant/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [string-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/string-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [string-theory](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/string-theory/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [string-view-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/string-view-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stringzilla](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stringzilla/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [strong-type](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/strong-type/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stronk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stronk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [strtk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/strtk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [structopt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/structopt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [stxxl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/stxxl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [subversion](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/subversion/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !mingw & !android |
| [suitesparse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-amd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-amd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-btf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-btf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-camd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-camd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-ccolamd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-ccolamd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-cholmod](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-cholmod/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-colamd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-colamd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-config](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-config/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-cxsparse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-cxsparse/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-graphblas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-graphblas/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-klu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-klu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-lagraph](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-lagraph/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-ldl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-ldl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-mongoose](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-mongoose/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-paru](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-paru/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-rbio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-rbio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-spex](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-spex/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-spqr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-spqr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [suitesparse-umfpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/suitesparse-umfpack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sundials](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sundials/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [superglu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/superglu/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [superlu](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/superlu/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [supernovas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/supernovas/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sushant-wayal-stringhash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sushant-wayal-stringhash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [svt-av1](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/svt-av1/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 排除 | !x86 & !arm32 & !uwp |
| [swaggercpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/swaggercpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [swenson-sort](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/swenson-sort/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [symengine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/symengine/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [syntax-highlighting](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/syntax-highlighting/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !(windows & arm64) |
| [syscalls-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/syscalls-cpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & (x64 &#124; x86) |
| [systemc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/systemc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [sz](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/sz/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tabulate](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tabulate/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tacopie](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tacopie/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [taglib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/taglib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [talib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/talib/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx &#124; (windows & !uwp) |
| [tanakh-cmdline](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tanakh-cmdline/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [taocpp-json](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/taocpp-json/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tap-windows6](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tap-windows6/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [task-thread-pool](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/task-thread-pool/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [taskflow](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/taskflow/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tbb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tbb/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tcb-span](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tcb-span/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tcl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tcl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tclap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tclap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tcp-pubsub](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tcp-pubsub/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tdlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tdlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tdscpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tdscpp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp & !osx |
| [telnetpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/telnetpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tensorpipe](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tensorpipe/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx |
| [termcolor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/termcolor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tesseract](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tesseract/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tesults-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tesults-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tesults-gtest](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tesults-gtest/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tevclient](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tevclient/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tfhe](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tfhe/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !windows & !arm |
| [tgbot-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tgbot-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tgc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tgc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tgui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tgui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [thermadiag-seq](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/thermadiag-seq/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [think-cell-range](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/think-cell-range/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [thomasmonkman-filewatch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/thomasmonkman-filewatch/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [thorvg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/thorvg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [threadweaver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/threadweaver/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [thrift](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/thrift/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tidy-html5](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tidy-html5/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tiff](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tiff/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tiledb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tiledb/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 排除 | !(x86 &#124; arm32 &#124; uwp) |
| [time-shield-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/time-shield-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinkerforge](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinkerforge/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tiny-aes-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tiny-aes-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tiny-bignum-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tiny-bignum-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tiny-dnn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tiny-dnn/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tiny-optional](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tiny-optional/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tiny-process-library](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tiny-process-library/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tiny-regex-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tiny-regex-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinycbor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinycbor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinycolormap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinycolormap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinycthread](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinycthread/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinydir](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinydir/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyexif](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyexif/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyexpr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyexpr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyexr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyexr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyfiledialogs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyfiledialogs/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tinyformat](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyformat/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyfsm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyfsm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinygltf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinygltf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinynpy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinynpy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyobjloader](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyobjloader/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyorm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyorm/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(uwp &#124; arm &#124; android &#124; emscripten &#124; osx &#124; ios &#124; xbox &#124; freebsd &#124; openbsd &#124; wasm32) |
| [tinyply](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyply/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyproto](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyproto/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyspline](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyspline/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinythread](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinythread/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinytiff](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinytiff/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinytoml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinytoml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyutf8](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyutf8/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyxml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyxml/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tinyxml2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tinyxml2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tl-expected](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tl-expected/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tl-function-ref](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tl-function-ref/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tl-generator](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tl-generator/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tl-optional](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tl-optional/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tl-ranges](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tl-ranges/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tlsf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tlsf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tlx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tlx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tmx](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tmx/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tmxlite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tmxlite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tobias-loew-flags](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tobias-loew-flags/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [toml11](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/toml11/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tomlplusplus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tomlplusplus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tomsolver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tomsolver/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [toomanycooks](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/toomanycooks/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [torch-th](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/torch-th/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tracy](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tracy/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & (arm &#124; uwp)) |
| [transwarp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/transwarp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [trantor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/trantor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tre](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tre/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tree-similarity](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tree-similarity/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tree-sitter](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tree-sitter/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tree-sitter-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tree-sitter-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tree-sitter-cli](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tree-sitter-cli/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [treehh](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/treehh/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [treehopper](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/treehopper/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(static & staticcrt) |
| [triangle](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/triangle/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [trianglemeshdistance](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/trianglemeshdistance/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [trieste](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/trieste/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !x86 |
| [triton](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/triton/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm |
| [trompeloeil](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/trompeloeil/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [try-catcher](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/try-catcher/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tsl-array-hash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tsl-array-hash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tsl-hat-trie](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tsl-hat-trie/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tsl-hopscotch-map](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tsl-hopscotch-map/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tsl-ordered-map](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tsl-ordered-map/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tsl-sparse-map](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tsl-sparse-map/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [tuplet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tuplet/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [turbobase64](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/turbobase64/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !(windows & arm) |
| [tvision](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tvision/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [tweeny](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/tweeny/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [type-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/type-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [type-safe](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/type-safe/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [typecast-ai](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/typecast-ai/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [uchardet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/uchardet/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ucoro](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ucoro/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [udt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/udt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [umock-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/umock-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [unarr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/unarr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows &#124; static |
| [uni-algo](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/uni-algo/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [unicorn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/unicorn/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(arm & windows) |
| [unicorn-lib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/unicorn-lib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [unimail-cpp-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/unimail-cpp-sdk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [units](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/units/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [unittest-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/unittest-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [unixodbc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/unixodbc/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; osx |
| [unleash-client-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/unleash-client-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [unordered-dense](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/unordered-dense/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [unqlite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/unqlite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [unrar](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/unrar/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !arm & !static |
| [upa-url](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/upa-url/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [urdfdom](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/urdfdom/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !staticcrt |
| [urdfdom-headers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/urdfdom-headers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [uriparser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/uriparser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [usbmuxd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/usbmuxd/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (!windows & !android & !ios) &#124; mingw |
| [usd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/usd/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !x86 & !(arm & windows) & !android |
| [usearch](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/usearch/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [usockets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/usockets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [usrsctp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/usrsctp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [utf8-range](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/utf8-range/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [utf8h](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/utf8h/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [utf8proc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/utf8proc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [utfcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/utfcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [utfz](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/utfz/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [uthash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/uthash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [uthenticode](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/uthenticode/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [uvatlas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/uvatlas/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !arm32) &#124; linux |
| [uvg266](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/uvg266/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !x86 |
| [uvw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/uvw/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [uwebsockets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/uwebsockets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [v-hacd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/v-hacd/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm |
| [valijson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/valijson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [value-ptr-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/value-ptr-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vamp-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vamp-sdk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [vanillapdf](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vanillapdf/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [variant-lite](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/variant-lite/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vbs-enclave-tooling-codegen](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vbs-enclave-tooling-codegen/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & arm64) &#124; (windows & x64) |
| [vc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vc/vcpkg.json) | 元数据允许 | 排除 | 允许 | 允许 | 允许 | !arm64 |
| [vcglib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcglib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vcpkg-boost](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-boost/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vcpkg-cmake](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-cmake/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vcpkg-cmake-config](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-cmake-config/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vcpkg-cmake-get-vars](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-cmake-get-vars/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vcpkg-get-python](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-get-python/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-get-python-packages](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-get-python-packages/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-gfortran](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-gfortran/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !arm & !uwp |
| [vcpkg-gn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-gn/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-make](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-make/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-msbuild](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-msbuild/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native & windows |
| [vcpkg-pkgconfig-get-modules](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-pkgconfig-get-modules/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-qmake](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-qmake/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-tool-castxml](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-tool-castxml/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-tool-gn](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-tool-gn/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-tool-gyp-next](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-tool-gyp-next/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-tool-lessmsi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-tool-lessmsi/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native & windows |
| [vcpkg-tool-meson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-tool-meson/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-tool-mozbuild](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-tool-mozbuild/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native & x64 & windows |
| [vcpkg-tool-ninja](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-tool-ninja/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-tool-nodejs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-tool-nodejs/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vcpkg-tool-python2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vcpkg-tool-python2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(arm & windows) |
| [vectorclass](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vectorclass/vcpkg.json) | 元数据允许 | 排除 | 排除 | 允许 | 允许 | !(arm &#124; arm64) |
| [vectorscan](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vectorscan/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !windows & !(x64 &#124; x86) & !android |
| [veigar](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/veigar/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | linux &#124; (windows & !uwp & !xbox) |
| [velodyne-decoder](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/velodyne-decoder/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [verdict](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/verdict/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vili](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vili/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vincentlaucsb-classify-scalar](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vincentlaucsb-classify-scalar/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vincentlaucsb-csv-parser](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vincentlaucsb-csv-parser/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [vins-z-backtesting-engine](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vins-z-backtesting-engine/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows & !(static & staticcrt) |
| [visit-struct](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/visit-struct/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vit-vit-ctpl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vit-vit-ctpl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vk-bootstrap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vk-bootstrap/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vkfft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vkfft/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vladimirshaleev-ipaddress](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vladimirshaleev-ipaddress/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vlfeat](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vlfeat/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vlpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vlpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [vmaware-vm-detection](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vmaware-vm-detection/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [void-numerics](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/void-numerics/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [volk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/volk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [voro](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/voro/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vowpal-wabbit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vowpal-wabbit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !x86 & !uwp & !(windows & arm) |
| [vs-yasm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vs-yasm/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !arm |
| [vsg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vsg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vsgimgui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vsgimgui/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vsgpoints](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vsgpoints/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vsgqt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vsgqt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vsgxchange](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vsgxchange/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vst3sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vst3sdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !uwp & !(arm64 & windows) & !staticcrt |
| [vtk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vtk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vtk-compile-tools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vtk-compile-tools/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | native |
| [vtk-dicom](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vtk-dicom/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vtk-m](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vtk-m/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 排除 | !x86 & !uwp |
| [vulkan](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vulkan/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [vulkan-extensionlayer](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vulkan-extensionlayer/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !static |
| [vulkan-headers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vulkan-headers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [vulkan-loader](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vulkan-loader/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [vulkan-memory-allocator](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vulkan-memory-allocator/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [vulkan-memory-allocator-hpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vulkan-memory-allocator-hpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [vulkan-sdk-components](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vulkan-sdk-components/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [vulkan-tools](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vulkan-tools/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !osx |
| [vulkan-utility-libraries](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vulkan-utility-libraries/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vulkan-validationlayers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vulkan-validationlayers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vvdec](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vvdec/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [vvenc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vvenc/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 排除 | !x86 & !arm32 |
| [vxl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/vxl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [wabt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wabt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wampcc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wampcc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm64) |
| [wangle](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wangle/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wasmedge](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wasmedge/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [wavelib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wavelib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wavpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wavpack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wayland](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wayland/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows &#124; osx) |
| [wayland-protocols](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wayland-protocols/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wcslib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wcslib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [webcraft](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/webcraft/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(uwp &#124; android &#124; emscripten) |
| [webrtc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/webrtc/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (linux & (arm64 &#124; x64)) &#124; (osx & (arm64 &#124; x64)) &#124; (windows & (arm64 &#124; x86 &#124; x64)) |
| [webthing-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/webthing-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [webui](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/webui/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !uwp & !(arm32 & android) |
| [webview2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/webview2/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & (x86 &#124; x64 &#124; arm64) |
| [wepoll](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wepoll/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [wg21-linear-algebra](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wg21-linear-algebra/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wg21-sg14](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wg21-sg14/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [whereami](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/whereami/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [whisper-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/whisper-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wiiuse](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wiiuse/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [wil](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wil/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wildcards](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wildcards/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [wildmidi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wildmidi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wincrypt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wincrypt/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [winlamb](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/winlamb/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [winpcap](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/winpcap/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp & !arm & !static |
| [winpixevent](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/winpixevent/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & (x64 &#124; arm64) & !staticcrt & !xbox |
| [winpty](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/winpty/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [winreg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/winreg/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [winsock2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/winsock2/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows |
| [winsparkle](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/winsparkle/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !(arm32 &#124; uwp) |
| [wintoast](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wintoast/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [wirestead](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wirestead/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [wmipp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wmipp/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !uwp |
| [woff2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/woff2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wolf-midi](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wolf-midi/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wolfmqtt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wolfmqtt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [wolfssl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wolfssl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [wolftpm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wolftpm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [wordnet](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wordnet/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [workflow](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/workflow/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [workflow-win](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/workflow-win/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !mingw |
| [wpilib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wpilib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wren](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wren/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wt/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [wtl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wtl/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !xbox |
| [wukong-easy-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wukong-easy-sdk/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android & !ios & !emscripten |
| [wxchartdir](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wxchartdir/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [wxcharts](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wxcharts/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [wxwidgets](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wxwidgets/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [wyhash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/wyhash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [x-plane](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/x-plane/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | (windows & !uwp & x64) &#124; (osx & (x64 &#124; arm64)) &#124; (linux & x64) |
| [x264](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/x264/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox |
| [x265](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/x265/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [x509cert-banned](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/x509cert-banned/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [x86-simd-sort](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/x86-simd-sort/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xapian](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xapian/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | (!arm &#124; arm64) & !uwp & !xbox |
| [xaudio2redist](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xaudio2redist/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows & !arm32 & !uwp & !xbox |
| [xbitmaps](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xbitmaps/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xbyak](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xbyak/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !(arm &#124; uwp) |
| [xcb-image](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xcb-image/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xcb-keysyms](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xcb-keysyms/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xcb-proto](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xcb-proto/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xcb-render-util](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xcb-render-util/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xcb-util](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xcb-util/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xcb-util-errors](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xcb-util-errors/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xcb-util-m4](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xcb-util-m4/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xcb-util-wm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xcb-util-wm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xdigest](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xdigest/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xerces-c](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xerces-c/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [xeus](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xeus/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xframe](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xframe/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xlnt](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xlnt/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | windows &#124; linux &#124; osx |
| [xlsxio](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xlsxio/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xmlsec](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xmlsec/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !xbox & !uwp |
| [xnnpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xnnpack/vcpkg.json) | 待验证 | 未知 | 未知 | 未知 | 未知 | !(arm & windows) & !uwp & !arm32 |
| [xorg-macros](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xorg-macros/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [xorstr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xorstr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xpack](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xpack/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xproperty](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xproperty/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xproto](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xproto/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xqilla](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xqilla/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xsimd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xsimd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xtensor](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xtensor/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xtensor-blas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xtensor-blas/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xtensor-fftw](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xtensor-fftw/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xtensor-io](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xtensor-io/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xtl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xtl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xtrans](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xtrans/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xxhash](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xxhash/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [xyo-sdk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/xyo-sdk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [yajl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yajl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [yalantinglibs](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yalantinglibs/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android |
| [yaml-cpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yaml-cpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [yandex-disk-cpp-client](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yandex-disk-cpp-client/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [yara](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yara/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [yas](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yas/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [yasm](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yasm/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [yasm-tool-helper](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yasm-tool-helper/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [yato](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yato/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !(windows & arm) |
| [yoctolib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yoctolib/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !(uwp &#124; android) |
| [yoga](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yoga/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [yomm2](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yomm2/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [yubico-piv-tool](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yubico-piv-tool/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !android & !ios |
| [yunsmall-usbipdcpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yunsmall-usbipdcpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [yyjson](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/yyjson/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [z3](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/z3/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [z4kn4fein-semver](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/z4kn4fein-semver/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [z85](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/z85/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zeroc-ice](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zeroc-ice/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !(windows & arm) & !wasm32 |
| [zeromq](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zeromq/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp & !xbox |
| [zfp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zfp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zimg](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zimg/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zimpl](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zimpl/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [zint](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zint/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !osx |
| [zix](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zix/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [zkpp](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zkpp/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !windows |
| [zlib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zlib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zlib-ng](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zlib-ng/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zlmediakit](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zlmediakit/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [zmij](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zmij/vcpkg.json) | 元数据允许 | 允许 | 排除 | 允许 | 允许 | !arm &#124; arm64 |
| [zoe](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zoe/vcpkg.json) | 元数据排除 | 排除 | 排除 | 排除 | 排除 | !uwp & !android |
| [zookeeper](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zookeeper/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zopfli](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zopfli/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zpp-bits](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zpp-bits/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zserge-webview](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zserge-webview/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zstd](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zstd/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zstr](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zstr/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ztd-cuneicode](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ztd-cuneicode/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ztd-encoding-tables](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ztd-encoding-tables/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ztd-idk](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ztd-idk/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ztd-platform](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ztd-platform/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ztd-static-containers](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ztd-static-containers/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [ztd-text](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/ztd-text/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | !uwp |
| [zug](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zug/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zxc](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zxc/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zycore](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zycore/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zydis](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zydis/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zyre](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zyre/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
| [zziplib](https://github.com/microsoft/vcpkg/blob/817892b0ecbc6af994dd6df999c73faf795adbf2/ports/zziplib/vcpkg.json) | 元数据允许 | 允许 | 允许 | 允许 | 允许 | 未设置 supports；未限制平台 |
