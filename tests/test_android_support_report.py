import importlib.util
from pathlib import Path
import unittest


spec = importlib.util.spec_from_file_location(
    "report", Path(__file__).resolve().parents[1] / "scripts/android-support-report.py")
report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(report)


class SupportsExpressionTests(unittest.TestCase):
    def test_platform_arch_and_precedence(self):
        cases = [
            ("", "arm64", True),
            ("android & (arm64 | x64)", "arm64", True),
            ("android & (arm64 | x64)", "arm", False),
            ("!android", "arm64", False),
            ("windows | android & arm64", "x86", False),
            ("static & !staticcrt", "x64", True),
            ("future-platform", "arm64", None),
            ("android | future-platform", "arm64", True),
            ("windows & future-platform", "arm64", False),
            ("android &", "arm64", None),
            ("android + arm64", "arm64", None),
        ]
        for expression, arch, expected in cases:
            with self.subTest(expression=expression, arch=arch):
                self.assertIs(report.supports(expression, arch), expected)


if __name__ == "__main__":
    unittest.main()
