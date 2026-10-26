import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock


spec = importlib.util.spec_from_file_location(
    "smoke", Path(__file__).resolve().parents[1] / "scripts/android-smoke.py")
smoke = importlib.util.module_from_spec(spec)
spec.loader.exec_module(smoke)


class LibraryReportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        config, _ = smoke.read_config()
        for backend in config["backends"]:
            for item in config["libraries"]:
                directory = self.root / backend / item["name"]
                directory.mkdir(parents=True)
                result = dict(backend=backend, revision="test", abi=config["abi"], api=config["api"],
                              ndk="/ndk", generated="test", rows=[dict(name=item["name"], status="success")])
                (directory / "results.json").write_text(json.dumps(result), encoding="utf-8")
        self.destination = self.root / "report.md"

    def test_merge_thirty_library_results(self):
        self.assertEqual(smoke.report(self.root, self.destination, ""), 0)
        self.assertIn("30/30", self.destination.read_text(encoding="utf-8"))

    def test_missing_library_is_not_success(self):
        (self.root / "conan/libevent/results.json").unlink()
        self.assertEqual(smoke.report(self.root, self.destination, ""), 1)
        self.assertIn("29/30", self.destination.read_text(encoding="utf-8"))

    def test_duplicate_library_results_rejected(self):
        original = self.root / "conan/libevent/results.json"
        duplicate = self.root / "duplicate/results.json"
        duplicate.parent.mkdir()
        duplicate.write_bytes(original.read_bytes())
        with self.assertRaisesRegex(ValueError, "duplicate library"):
            smoke.report(self.root, self.destination, "")

    def test_ndk_lookup_preserves_sdk_junction_path(self):
        ndk = self.root / "short-sdk/ndk"
        toolchain = ndk / "build/cmake/android.toolchain.cmake"
        toolchain.parent.mkdir(parents=True)
        toolchain.write_text("", encoding="utf-8")
        with mock.patch.dict(os.environ, {"ANDROID_NDK_HOME": str(ndk)}, clear=True), \
                mock.patch.object(Path, "resolve", side_effect=AssertionError("must preserve junction path")):
            self.assertEqual(smoke.resolve_ndk(), ndk.absolute().as_posix())

    def test_xmake_host_tools_are_not_android_outputs(self):
        target = self.root / "exports/z/zlib/version/hash/lib/libz.a"
        host = self.root / "exports/m/msys2-base/version/hash/usr/lib/libalpm.a"
        for archive in (target, host):
            archive.parent.mkdir(parents=True)
            archive.write_bytes(b"test archive")
        (self.root / "exports/m/msys2-base/version/hash/manifest.txt").write_text(
            '{\n    kind = "toolchain",\n    plat = "windows",\n}\n', encoding="utf-8")
        with mock.patch.object(smoke.subprocess, "check_output", return_value="Machine: AArch64\n") as readelf:
            self.assertEqual(smoke.verify_archives(self.root / "exports", "/ndk", "arm64-v8a"), 1)
            self.assertEqual(Path(readelf.call_args.args[0][-1]), target)

    def test_wrong_architecture_target_library_still_fails(self):
        library = self.root / "exports/z/zlib/version/hash/lib/libz.a"
        library.parent.mkdir(parents=True)
        library.write_bytes(b"test archive")
        (library.parent.parent / "manifest.txt").write_text(
            '{\n    kind = "library",\n    plat = "windows",\n}\n', encoding="utf-8")
        with mock.patch.object(smoke.subprocess, "check_output", return_value="Machine: Intel 80386\n"):
            with self.assertRaisesRegex(RuntimeError, "ABI mismatch"):
                smoke.verify_archives(self.root / "exports", "/ndk", "arm64-v8a")


if __name__ == "__main__":
    unittest.main()
