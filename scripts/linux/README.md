# Linux 宿主的 Android 库入口

每个库对应一个脚本：`libevent.sh`、`zlib.sh`、`zstd.sh`、`libpng.sh`、`openssl.sh`、`sqlite3.sh`、`libcurl.sh`、`libuv.sh`、`libssh2.sh`、`c-ares.sh`。

```bash
# 默认使用 vcpkg、Conan 2、xmake 三个后端，只构建 libevent
bash scripts/linux/libevent.sh

# 只使用指定后端
bash scripts/linux/libevent.sh --backend conan
bash scripts/linux/zlib.sh --backend vcpkg --jobs 4
bash scripts/linux/libpng.sh --backend xmake --ndk /opt/android-ndk
```

脚本可从任意工作目录运行，固定选择文件名对应的库，其他参数透传公共实现 `scripts/android-smoke.py`。默认 Android ABI/API 与库映射来自 `libraries/android-smoke.json`。

逐库产物和日志位于 `dist/smoke/<backend>/<library>/`，`results.json` 供汇总报告使用。`android-common10.yml` 的矩阵由公共脚本读取清单生成；构建步骤直接调用 `scripts/linux/<library>.sh`，不包含库构建命令。

原有 `build.sh` 仍为基于 manifest 的多库 xmake/Conan 构建入口。
