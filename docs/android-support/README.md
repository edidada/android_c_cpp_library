# Android 库支持信息

生成时间：2026-11-16 09:11 UTC

全量扫描三个包仓库的元数据，不执行配方、不编译。**本报告不等于编译通过清单。**

- vcpkg：按默认静态库、动态 CRT 的 Android triplet 计算顶层 supports；不求解依赖、默认 features 或 portfile 条件。
- Conan 2：Conan Center 是配方仓库，存在配方不代表支持 Android；Android 字符串可能表示支持或排除。每个配方目录单列，版本见上游 config.yml。
- xmake：Lua 安装回调、宿主条件及依赖需要运行时求解；Android 字符串仅作为人工核对入口。
- 待验证并不表示不支持。要确认可用，需指定版本、宿主、ABI、API、选项并在 Actions 编译。
- Android 目标 ABI：arm64-v8a、armeabi-v7a、x86_64、x86；宿主 Linux/macOS/Windows 的支持不能直接互换。

| 包管理器 | 扫描条目 | 元数据允许 | 检出 Android 信号 | 待验证 | 元数据排除 | 上游快照 |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| [vcpkg](vcpkg.md) | 2915 | 2507 | 0 | 21 | 387 | [8f363bdc1135](https://github.com/microsoft/vcpkg/tree/8f363bdc11359ede4bc51e5eb32a2617538049c8) |
| [conan](conan.md) | 2030 | 0 | 118 | 1912 | 0 | [6f3abb462bd7](https://github.com/conan-io/conan-center-index/tree/6f3abb462bd77f361754da844ab7137ff1d3a567) |
| [xmake](xmake.md) | 2035 | 0 | 381 | 1654 | 0 | [0d4d4ef2fcac](https://github.com/xmake-io/xmake-repo/tree/0d4d4ef2fcaced81971e1a480c61ffa979c9fd93) |

## 实际编译结果

现有 Android C/C++ Libraries 与 Android Cross-Platform Build 工作流负责实际编译 xmake/Conan 库，详见各次运行的 Summary 与 dist artifact。
本报告尚不含 vcpkg 编译结果，也不将既有手工 manifest 视为全量支持清单。
