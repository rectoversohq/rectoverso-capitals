import unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from source_data import inputs, read


class OwnerFeedback(unittest.TestCase):
    def test_geography_has_named_continent_and_region_resources(self):
        for language in ("en", "fr"):
            words = read(f"source/languages/{language}.json")["fields"]
            _, notes, models, _ = inputs(language)
            self.assertIn("region", words)
            for model in models.values():
                back = model["templates"][0]["afmt"]
                self.assertIn("{{" + words["continent"] + "}}", back)
                self.assertIn("{{" + words["region"] + "}}", back)
            for note in notes:
                self.assertTrue(note["fields"][words["continent"]])
                self.assertTrue(note["fields"][words["region"]])
                self.assertNotIn(note["fields"][words["region"]], note["fields"][words["details"]].split("<br>"))

