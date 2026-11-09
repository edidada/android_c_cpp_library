# Android 库支持信息

生成时间：2026-11-09 09:23 UTC

全量扫描三个包仓库的元数据，不执行配方、不编译。**本报告不等于编译通过清单。**

- vcpkg：按默认静态库、动态 CRT 的 Android triplet 计算顶层 supports；不求解依赖、默认 features 或 portfile 条件。
- Conan 2：Conan Center 是配方仓库，存在配方不代表支持 Android；Android 字符串可能表示支持或排除。每个配方目录单列，版本见上游 config.yml。
- xmake：Lua 安装回调、宿主条件及依赖需要运行时求解；Android 字符串仅作为人工核对入口。
- 待验证并不表示不支持。要确认可用，需指定版本、宿主、ABI、API、选项并在 Actions 编译。
- Android 目标 ABI：arm64-v8a、armeabi-v7a、x86_64、x86；宿主 Linux/macOS/Windows 的支持不能直接互换。

| 包管理器 | 扫描条目 | 元数据允许 | 检出 Android 信号 | 待验证 | 元数据排除 | 上游快照 |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| [vcpkg](vcpkg.md) | 2910 | 2504 | 0 | 20 | 386 | [ec48c11eae94](https://github.com/microsoft/vcpkg/tree/ec48c11eae9448c8c6e7739d93e06fa2433aa95f) |
| [conan](conan.md) | 2028 | 0 | 118 | 1910 | 0 | [08d9ba53fce3](https://github.com/conan-io/conan-center-index/tree/08d9ba53fce3cf3d5a9157da1fdecd32371c452a) |
| [xmake](xmake.md) | 2033 | 0 | 380 | 1653 | 0 | [511a3c4536a1](https://github.com/xmake-io/xmake-repo/tree/511a3c4536a12318e7c1effa012dc8d7b5637526) |

## 实际编译结果

现有 Android C/C++ Libraries 与 Android Cross-Platform Build 工作流负责实际编译 xmake/Conan 库，详见各次运行的 Summary 与 dist artifact。
本报告尚不含 vcpkg 编译结果，也不将既有手工 manifest 视为全量支持清单。
