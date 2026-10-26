# Android 库支持信息

生成时间：2026-10-26 11:42 UTC

全量扫描三个包仓库的元数据，不执行配方、不编译。**本报告不等于编译通过清单。**

- vcpkg：按默认静态库、动态 CRT 的 Android triplet 计算顶层 supports；不求解依赖、默认 features 或 portfile 条件。
- Conan 2：Conan Center 是配方仓库，存在配方不代表支持 Android；Android 字符串可能表示支持或排除。每个配方目录单列，版本见上游 config.yml。
- xmake：Lua 安装回调、宿主条件及依赖需要运行时求解；Android 字符串仅作为人工核对入口。
- 待验证并不表示不支持。要确认可用，需指定版本、宿主、ABI、API、选项并在 Actions 编译。
- Android 目标 ABI：arm64-v8a、armeabi-v7a、x86_64、x86；宿主 Linux/macOS/Windows 的支持不能直接互换。

| 包管理器 | 扫描条目 | 元数据允许 | 含 Android 逻辑 | 待验证 | 元数据排除 | 上游快照 |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| [vcpkg](vcpkg.md) | 2887 | 2485 | 0 | 20 | 382 | [817892b0ecbc](https://github.com/microsoft/vcpkg/tree/817892b0ecbc6af994dd6df999c73faf795adbf2) |
| [conan](conan.md) | 2027 | 0 | 116 | 1911 | 0 | [915064e52143](https://github.com/conan-io/conan-center-index/tree/915064e52143e583fba3a02511c9985bb0329fe0) |
| [xmake](xmake.md) | 2028 | 0 | 380 | 1648 | 0 | [58f6e9c1bd2e](https://github.com/xmake-io/xmake-repo/tree/58f6e9c1bd2e930aadb332fec7c37281edd798b3) |

## 实际编译结果

现有 Android C/C++ Libraries 与 Android Cross-Platform Build 工作流负责实际编译 xmake/Conan 库，详见各次运行的 Summary 与 dist artifact。
本报告尚不含 vcpkg 编译结果，也不将既有手工 manifest 视为全量支持清单。
