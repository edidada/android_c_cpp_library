# Windows 原生单库入口

在 CMD 或 PowerShell 中直接调用 `.bat`，无需 Git Bash：

```bat
scripts\win\libevent.bat
scripts\win\libevent.bat --backend conan
scripts\win\zlib.bat --backend vcpkg --jobs 4
scripts\win\libpng.bat --backend xmake --ndk C:\Android\ndk\27.3.13750724
```

10 个库与 Linux 入口对应。默认运行 vcpkg、Conan 2、xmake；`--help` 查看参数。
需要 Python 3、Git 和 Android NDK，以及后端要求的宿主构建工具；Git 使用原生 git.exe。
公共实现通过原生命令初始化工具、构建包和检查架构，不调用 Bash 脚本。vcpkg 可以自行下载其端口需要的构建工具。

Actions 的 **Android Common 10 Libraries** 可手动选择 `platform=win`，YAML 使用 `shell: cmd` 调用相应 `.bat`。
`Android Library Entry Checks` 在真实 Windows runner 上检查所有批处理入口和公共结果汇总逻辑；入口检查不等于编译通过。

`build.sh` 是早期 Git Bash 多库入口；新的单库 `.bat` 不使用它。
