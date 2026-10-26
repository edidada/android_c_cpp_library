# 常用 10 库 Android 编译验证

目标：Linux → Android `arm64-v8a` / API 28 / Release。

[GitHub Actions 运行与日志](https://github.com/edidada/android_c_cpp_library/actions/runs/40326079514)

验证的是选定配置下包的实际构建与产物导出；不是 Android 设备运行测试，也不证明所有 ABI/选项可用。
xmake 会编译头文件探针；Conan/vcpkg 构建包。各后端版本及默认功能可能不同。

所有成功项还需通过 NDK llvm-readelf 的静态库架构检查；arm64 目标必须为 AArch64。

| 库 | vcpkg | Conan 2 | xmake |
| --- | --- | --- | --- |
| zlib | ✅ 编译通过 | ✅ 编译通过 | ✅ 编译通过 |
| zstd | ✅ 编译通过 | ✅ 编译通过 | ✅ 编译通过 |
| libpng | ✅ 编译通过 | ✅ 编译通过 | ✅ 编译通过 |
| openssl | ✅ 编译通过 | ✅ 编译通过 | ✅ 编译通过 |
| sqlite3 | ✅ 编译通过 | ✅ 编译通过 | ✅ 编译通过 |
| libcurl | ✅ 编译通过 | ✅ 编译通过 | ✅ 编译通过 |
| libuv | ✅ 编译通过 | ✅ 编译通过 | ✅ 编译通过 |
| libssh2 | ✅ 编译通过 | ✅ 编译通过 | ✅ 编译通过 |
| c-ares | ✅ 编译通过 | ✅ 编译通过 | ✅ 编译通过 |
| libevent | ✅ 编译通过 | ✅ 编译通过 | ✅ 编译通过 |

通过 **30/30** 个组合。

## 环境与证据

- vcpkg：源码 `68c4da551aebac0908028d26b1bf2e8355bd1494`；NDK `/usr/local/lib/android/sdk/ndk/27.3.13750724`；时间 2026-10-26T12:54:09.687532+00:00。
  vcpkg 快照：`817892b0ecbc6af994dd6df999c73faf795adbf2`。
- conan：源码 `68c4da551aebac0908028d26b1bf2e8355bd1494`；NDK `/usr/local/lib/android/sdk/ndk/27.3.13750724`；时间 2026-10-26T12:54:09.787307+00:00。
- xmake：源码 `68c4da551aebac0908028d26b1bf2e8355bd1494`；NDK `/usr/local/lib/android/sdk/ndk/27.3.13750724`；时间 2026-10-26T12:56:50.426852+00:00。

每个后端的 artifact 含 results.json、build.log、安装产物及可取得的单库日志；vcpkg 版本见 installed-versions.txt，Conan/xmake 版本见构建日志。

## 独立使用

```bash
bash scripts/linux/libevent.sh # 默认使用三个后端
bash scripts/linux/libevent.sh --backend conan
bash scripts/linux/zlib.sh --backend vcpkg
python scripts/android-smoke.py report
```

库选择与 vcpkg 映射位于 libraries/android-smoke.json；Conan/xmake 包信息复用 libraries/manifest.json。脚本不读取 YAML 或依赖 GitHub 环境变量。
