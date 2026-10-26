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


if __name__ == "__main__":
    unittest.main()
