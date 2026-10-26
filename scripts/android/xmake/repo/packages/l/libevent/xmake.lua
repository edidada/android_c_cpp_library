-- Project-local xmake package override for libevent.
--
-- xmake-repo 的 libevent 包使用 on_install("!android and ...") 显式排除了 Android，
-- 但 libevent 本身可以通过 NDK 的 CMake 工具链交叉编译。这里保留上游的下载/校验信息，
-- 只把 Android 加入 on_install，并关闭测试、示例、benchmark 和不使用的 SSL 后端。
package("libevent")
    set_homepage("https://libevent.org/")
    set_description("Event notification library (Android override)")
    set_license("BSD-3-Clause")

    add_urls("https://github.com/libevent/libevent/releases/download/release-$(version)-stable/libevent-$(version)-stable.tar.gz",
             "https://github.com/libevent/libevent.git")
    add_versions("2.1.12", "92e6de1be9ec176428fd2367677e61ceffc2ee1cb119035037a27d346b0403bb")

    add_deps("cmake")

    on_install("android", function (package)
        local configs = {
            "-DEVENT__DISABLE_TESTS=ON",
            "-DEVENT__DISABLE_REGRESS=ON",
            "-DEVENT__DISABLE_SAMPLES=ON",
            "-DEVENT__DISABLE_BENCHMARK=ON",
            "-DEVENT__DISABLE_OPENSSL=ON",
            "-DEVENT__DISABLE_MBEDTLS=ON",
            "-DEVENT__LIBRARY_TYPE=STATIC",
            "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
        }
        table.insert(configs, "-DCMAKE_BUILD_TYPE=" .. (package:debug() and "Debug" or "Release"))
        table.insert(configs, "-DEVENT__DISABLE_DEBUG_MODE=" .. (package:debug() and "OFF" or "ON"))
        import("package.tools.cmake").install(package, configs)
    end)

    on_test(function (package)
        assert(package:has_cfuncs("event_base_new", {includes = "event2/event.h"}))
    end)
