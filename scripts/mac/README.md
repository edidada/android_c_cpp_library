# macOS 单库入口

```bash
bash scripts/mac/libevent.sh
bash scripts/mac/libevent.sh --backend conan
bash scripts/mac/zlib.sh --backend vcpkg --jobs 4
bash scripts/mac/libpng.sh --backend xmake --ndk /opt/android-ndk
```

10 个库与 Linux 入口同名。默认运行三个后端，可使用 `--backend` 选择一个。
公共实现自动使用 NDK 的 darwin-x86_64 工具链；需 Python 3、Git、Android NDK 和 Xcode Command Line Tools。

Actions 的 **Android Common 10 Libraries** 可手动选择 `platform=mac`，逐库调用此目录下的脚本。参数、包映射和编译逻辑放在配置与公共脚本中，YAML 不包含库构建命令。
