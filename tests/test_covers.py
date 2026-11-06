import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / "scripts/checks/verify-covers.py"


class CoverCheck(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.output = Path(temporary.name)
        self.add_cover("rv-capitals-cover-light-1.png")
        self.add_cover("rv-capitals-cover-dark-1.png")

    def add_cover(self, name, size=(2010, 1340), mark=None):
        with Image.new("RGB", size, "#211e18") as image:
            if mark is not None:
                point, color = mark
                image.putpixel(point, color)
            image.save(self.output / name)

    def check(self):
        return subprocess.run(
            [sys.executable, str(CHECK), "--output", str(self.output)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )

    def test_shared_covers_supply_both_languages(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)

    def assert_rejected(self, message):
        result = self.check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn(message, result.stderr)

    def test_wrong_dimensions_are_rejected(self):
        self.add_cover("rv-capitals-cover-light-1.png", size=(2010, 1339))
        self.assert_rejected("must be a 2010 × 1340 PNG")

    def test_invalid_names_are_rejected(self):
        for name in (
            "rv-capitals-cover-LIGHT-2.png",
            "rv-capitals-cover-dark-0.png",
            "rv-capitals-de-cover-dark-2.png",
            "rv-capitals-cover-dark-2.PNG",
        ):
            with self.subTest(name=name):
                self.add_cover(name)
                self.assert_rejected(f"Invalid cover filename: {name}")
                (self.output / name).unlink()

    def test_missing_appearance_is_rejected(self):
        (self.output / "rv-capitals-cover-dark-1.png").unlink()
        self.assert_rejected("en missing cover appearances: dark")

    def test_worded_cover_requires_every_language_at_the_same_number_and_appearance(self):
        self.add_cover("rv-capitals-en-cover-dark-2.png")
        self.add_cover("rv-capitals-fr-cover-dark-3.png")
        self.add_cover("rv-capitals-fr-cover-light-2.png")
        self.assert_rejected("Worded cover dark-2 missing languages: fr")

    def test_fully_localized_set_supplies_both_appearances(self):
        for path in self.output.iterdir():
            path.unlink()
        for language in ("en", "fr"):
            for appearance in ("light", "dark"):
                self.add_cover(f"rv-capitals-{language}-cover-{appearance}-1.png")
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_artwork_at_the_inclusive_corner_boundary_is_rejected(self):
        self.add_cover(
            "rv-capitals-cover-dark-1.png", mark=((1608, 335), (237, 230, 216))
        )
        self.assert_rejected("has artwork in the language-pill corner")

    def test_minor_background_variation_and_art_outside_the_corner_are_allowed(self):
        self.add_cover(
            "rv-capitals-cover-light-1.png", mark=((1608, 335), (37, 26, 27))
        )
        self.add_cover(
            "rv-capitals-cover-dark-1.png", mark=((1608, 336), (237, 230, 216))
        )
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)
