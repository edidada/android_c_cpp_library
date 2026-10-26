# Android C/C++ 库构建

## 全量 Android 包支持报告

[自动生成的 Markdown 报告](docs/android-support/README.md)扫描 **vcpkg、Conan Center（Conan 2）、xmake-repo** 的全量包元数据，保留上游快照与配方链接。
在 Actions 中运行 **Android Package Support Report**，即可生成报告并由机器人提交回当前分支；每周一也会自动更新。
该工作流只扫描，不编译。vcpkg 按 Android 四种 ABI 计算顶层 `supports`；Conan/xmake 的动态配方标明 Android 线索或待验证，不将候选库当作已编译支持。
下方的 55 库 manifest 是本仓库的构建选集，不是三个包管理器的全量清单。

使用 **xmake** 与 **Conan 2** 在 Linux / macOS / Windows(Git Bash) 上交叉编译常用 C/C++ 库，
生成 Android 各 ABI 的头文件与静态库。仓库本身不包含这些库的源码，只维护「要构建哪些库」的
清单和构建脚本。

- 库清单：`libraries/manifest.json`
- 常用库集合：`presets.core`（libevent、zlib、openssl、sqlite3、libcurl、libuv、libssh2、c-ares）
- 平台入口：`scripts/linux/`、`scripts/mac/`、`scripts/win/`
- 专用后端入口：`scripts/android/xmake/`、`scripts/android/conan2/`
- CI：`.github/workflows/`（只负责调用脚本，不包含库列表和编译命令）

## 平台入口脚本

三个平台目录都只做「宿主环境 + Android 交叉编译」，目标平台固定为 Android：

```bash
# Linux 宿主
bash scripts/linux/build.sh

# macOS 宿主
bash scripts/mac/build.sh

# Windows 宿主（Git Bash）
"C:\Program Files\Git\bin\bash.exe" scripts/win/build.sh
```

默认编译 `presets.core`，也可以指定库、ABI 和后端：

```bash
bash scripts/linux/build.sh --libs all --abis arm64-v8a,armeabi-v7a
bash scripts/mac/build.sh --libs core --backends conan
bash scripts/linux/build.sh --libs libevent --skip-setup   # 已手动执行过 setup
```

## 独立的 xmake / Conan 2 入口

如果只需要某一种后端，可以直接使用：

```bash
# xmake，target = Android，默认 presets.core
bash scripts/android/xmake/build.sh --libs libevent,zlib --abis arm64-v8a

# Conan 2，target = Android，默认 presets.core
bash scripts/android/conan2/build.sh --libs libevent,zlib --abis arm64-v8a
```

xmake 侧的 `libevent` 使用项目内包覆盖：
`scripts/android/xmake/repo/packages/l/libevent/xmake.lua`。
xmake-repo 上游的 libevent 包显式排除了 Android（`on_install("!android and ...")`），
该本地包保留相同的源码地址和校验值，只增加 Android 的 CMake 交叉编译配置。

## 支持的 Android 库

```bash
bash scripts/list-libraries.sh            # 终端表格
bash scripts/list-libraries.sh --markdown # Markdown 表格
bash scripts/list-libraries.sh --json     # 完整 JSON
bash scripts/list-libraries.sh --names    # 只输出库名
```

当前清单覆盖压缩、图像、字体、密码学、网络、序列化、音视频、XML/文本、数学、测试等方向的
Android 可用库。常用示例：

```bash
# 核心常用库（libevent 等）
bash scripts/list-libraries.sh --libs core

# 只看指定库
bash scripts/list-libraries.sh --libs zlib,openssl,libcurl

# 只看 Conan 2 能构建的库
bash scripts/list-libraries.sh --backends conan

# 只看非实验库
bash scripts/list-libraries.sh --experimental stable
```

`libraries/manifest.json` 中同时给出 xmake 包名和 Conan 2 引用；两者名称不一致的库（例如
Opus、FLAC、SDL3、protobuf）已分别配置。标记为 `"experimental": true` 的库通常是体积大、
依赖多或 Android 适配仍不稳定的库，CI 允许它们失败而不影响整个工作流。
`--libs` 除库名外也接受 `presets` 中的集合名，例如 `core`，也可以与库名混用：`core,ffmpeg`。

## GitHub Actions

包含两份工作流，均只调用 `scripts/`，不硬编码库列表：

1. `.github/workflows/android-libraries.yml`
   - Linux runner，按库展开矩阵，构建清单中的全部/指定库，上传单库 artifact
2. `.github/workflows/android-cross-platform.yml`
   - 矩阵：Ubuntu / macOS / Windows(Git Bash) 三种宿主
   - 默认编译 `presets.core`，验证三个平台入口脚本
   - 上传各平台的 `dist/` artifact

触发方式（两份工作流相同）：

- push 到 `main`（仅当 `libraries/`、`scripts/`、工作流或 README 变化时）
- pull request
- `workflow_dispatch` 手动触发

`android-libraries.yml` 参数：

| 参数 | 默认值 | 说明 |
| --- | --- | --- |
| `libraries` | `all` | `all` / `core` / 逗号分隔的库名（push/PR 默认跑 `core`） |
| `abis` | `arm64-v8a` | 逗号分隔：`arm64-v8a`、`armeabi-v7a`、`x86_64`、`x86` |
| `backends` | `all` | `all`、`xmake` 或 `conan` |
| `api_level` | `21` | Android API level（minSdkVersion） |
| `include_experimental` | `true` | 是否构建 experimental 库 |

`android-libraries.yml` 流水线包含两个阶段：

1. **查看支持的 Android 库列表**：安装 xmake 与 Conan 2，校验清单，输出库列表到 job summary，
   并把库列表展开为构建矩阵。
2. **构建**：每个库一个 job，按所选后端和 ABI 编译，上传 `dist/<库名>/` 作为 artifact，
   并把每个库的构建结果写入 job summary。

CI 使用 GitHub 托管 runner 自带的 Android NDK（通过 `ANDROID_NDK_HOME` /
`ANDROID_NDK_LATEST_HOME` / `$ANDROID_HOME/ndk` 自动定位）。

## 本地构建

需要 Bash、Python 3、curl。Linux / macOS 直接使用对应平台脚本；Windows 使用 Git Bash。
Windows 原生 PowerShell 不是目标环境。

```bash
# 方式一：平台入口（自动安装 xmake / Conan 2 / 生成 profiles）
bash scripts/linux/build.sh --libs core --abis arm64-v8a
bash scripts/mac/build.sh   --libs core --abis arm64-v8a
# Windows:
# "C:\Program Files\Git\bin\bash.exe" scripts/win/build.sh --libs core --abis arm64-v8a

# 方式二：手动分步
bash scripts/setup.sh --abis arm64-v8a --api 21
bash scripts/list-libraries.sh
bash scripts/android/xmake/build.sh  --libs libevent,zlib
bash scripts/android/conan2/build.sh --libs libevent,zlib
```

常用参数：

```bash
# 全部库、两种后端
bash scripts/build.sh

# 只构建一个库的 Conan 包
bash scripts/build.sh --libs libcurl --backends conan

# 多个 ABI
bash scripts/build.sh --libs ffmpeg --abis arm64-v8a,armeabi-v7a

# 指定 NDK，清理后重建
bash scripts/build.sh --ndk /opt/android-ndk-r27c --clean

# 构建失败立即停止
bash scripts/build.sh --fail-fast
```

### 环境变量

| 变量 | 作用 |
| --- | --- |
| `ANDROID_NDK` / `ANDROID_NDK_HOME` / `ANDROID_NDK_ROOT` / `ANDROID_NDK_LATEST_HOME` | 定位 NDK |
| `ANDROID_HOME` / `ANDROID_SDK_ROOT` | 在 `$SDK/ndk/*` 下查找 NDK |
| `CONAN_HOME` | Conan 2 缓存目录，默认 `~/.conan2` |
| `CONAN_VENV` | 自动安装 Conan 时使用的 Python venv |
| `CONAN_ANDROID_STL` | Android C++ STL，默认 `c++_static` |
| `DIST_DIR` / `WORK_DIR` | 自定义产物目录 / 临时构建目录 |

如果机器上没有 NDK，可以通过 Android SDK 安装：

```bash
bash scripts/setup.sh --ndk-version 27.2.12479018
```

## 产物结构

```text
dist/
├── summary.md                 # 总体构建摘要
├── summary.tsv
└── <库名>/
    ├── summary.md             # 单库摘要
    ├── summary.tsv
    ├── logs/
    │   ├── arm64-v8a-xmake.log
    │   └── arm64-v8a-conan.log
    └── arm64-v8a/
        ├── xmake/             # xmake require --export 导出的包（含依赖）
        └── conan/             # Conan full_deploy 部署的包（含依赖）
```

- xmake 产物来自 `xmake require --export`，按 `包名/版本/配置哈希` 组织。
- Conan 产物来自内置 `full_deploy` deployer，可以直接作为离线依赖目录使用。

## 添加新库

编辑 `libraries/manifest.json`，在 `libraries` 数组中加入条目：

```json
{
  "name": "mylib",
  "title": "MyLib",
  "category": "utility",
  "description": "示例库",
  "experimental": false,
  "minAndroidApi": 21,
  "headers": ["mylib.h"],
  "defines": [],
  "xmake": {
    "package": "mylib",
    "version": "1.2.3",
    "configs": { "shared": false }
  },
  "conan": {
    "reference": "mylib/1.2.3",
    "options": ["mylib:shared=False"]
  }
}
```

字段说明见 `libraries/manifest.schema.json`。

- `name` 必须唯一，用作目录名和 CI 参数。
- `xmake.package` 是 [xmake-repo](https://github.com/xmake-io/xmake-repo) 中的包名。
- `conan.reference` 是 ConanCenter 中的完整引用，必须带版本。
- `headers` 用于编译探针，校验头文件是否可用；不写则只验证包能编译。
- `defines` 会以 `#define` 形式加入探针，例如 PCRE2 需要 `PCRE2_CODE_UNIT_WIDTH=8`。
- `experimental: true` 时 CI 对该库使用 `continue-on-error`。

修改后先校验：

```bash
bash scripts/list-libraries.sh --validate
bash scripts/build.sh --libs mylib --abis arm64-v8a
```

## 构建方式说明

每个库、每个 ABI 都会创建一个最小探针工程：

- **xmake**：探针工程通过 `add_requires()` / `add_packages()` 拉取包，使用
  `xmake f -p android -a <abi> --ndk=<ndk> --ndk_sdkver=<api>` 配置，编译后
  `xmake require --export` 导出头文件与库。探针会注册项目内包仓库
  `scripts/android/xmake/repo`，用于覆盖 Android 支持不完整的包（当前为 libevent）。
- **Conan 2**：使用 `scripts/setup.sh` 生成的 `android-<abi>` host profile，
  `conan install --requires=<ref> --build=missing` 从源码构建，`full_deploy` deployer 收集产物。

探针默认会 include 清单中的头文件，从而同时验证编译参数和头文件可用性；可用
`--no-header-check` 关闭。

## 相关文件

```text
.github/workflows/android-libraries.yml       全库矩阵构建（Linux）
.github/workflows/android-cross-platform.yml  Linux / macOS / Windows 平台入口验证
libraries/manifest.json                       库清单 + presets
libraries/manifest.schema.json                清单 JSON Schema
scripts/setup.sh                              安装 xmake / Conan 2，生成 NDK / Conan profiles
scripts/list-libraries.sh                     查看支持的 Android 库列表
scripts/build.sh                              通用编译入口
scripts/linux/build.sh                        Linux 宿主入口
scripts/mac/build.sh                          macOS 宿主入口
scripts/win/build.sh                          Windows(Git Bash) 宿主入口
scripts/android/xmake/build.sh                xmake Android 专用入口
scripts/android/conan2/build.sh               Conan 2 Android 专用入口
scripts/android/xmake/repo/                   项目内 xmake 包覆盖（libevent）
scripts/lib/common.sh                         NDK / ABI / 工具链路径 / 日志等公共函数
scripts/lib/platform.sh                       平台入口公共实现
scripts/lib/manifest.py                       清单解析、校验、preset / matrix / TSV 输出
```
