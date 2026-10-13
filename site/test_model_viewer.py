# SPDX-License-Identifier: Apache-2.0
"""Synthetic reference-wall acceptance smoke tests, not engineering verification."""
import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "model-verification" / "stud-wall.html"


class ReferenceWall(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = HTML.read_text(encoding="utf-8")
        match = re.search(r'<script type="application/json" id="assembly">([\s\S]*?)</script>', cls.page)
        if not match:
            raise AssertionError("missing embedded, versioned assembly source")
        cls.assembly = json.loads(match.group(1))

    def test_stud_layout_and_panel_coverage(self):
        src = self.assembly
        self.assertEqual(src["units"], "in")
        wall, framing, panels = src["wall"], src["framing"], src["sheathing"]
        self.assertEqual((wall["width"], wall["height"]), (96, 96))
        centers = framing["stud_centers"]
        self.assertEqual(len(centers), 7)
        self.assertEqual(centers, sorted(set(centers)))
        self.assertEqual(centers[0] - framing["stud_width"] / 2, 0)
        self.assertEqual(centers[-1] + framing["stud_width"] / 2, wall["width"])
        self.assertGreater(wall["height"] - framing["bottom_plate_height"] -
                           framing["top_plate_count"] * framing["top_plate_height"], 0)
        self.assertEqual(panels["width"] * panels["panels"], wall["width"])
        self.assertEqual(panels["height"], wall["height"])
        self.assertGreater(panels["thickness"], 0)

    def test_stable_part_identity_and_known_counts(self):
        src = self.assembly
        n_studs = len(src["framing"]["stud_centers"])
        n_plates = src["framing"]["top_plate_count"] + 1
        n_panels = src["sheathing"]["panels"]
        n_markers = n_studs * len(src["fasteners"]["row_heights"])
        self.assertEqual((n_studs, n_plates, n_panels, n_markers), (7, 3, 2, 56))
        self.assertEqual(len(set(src["fasteners"]["row_heights"])),
                         len(src["fasteners"]["row_heights"]))
        self.assertIn("revision", src)
        self.assertIn("urn:ori:synthetic:", self.page)
        self.assertIn("e.id===selected", self.page)
        self.assertIn("elements.filter", self.page)
        self.assertIn("project(", self.page)

    def test_unverified_not_approved(self):
        self.assertEqual(self.assembly["verification"]["status"], "unknown")
        self.assertIsNone(self.assembly["reviewer_decision"])
        self.assertIn("not a building-code check", self.page)
        self.assertIn("fastening schedule", self.page)
        self.assertNotIn('verification:"pass"', self.page)
        self.assertNotIn("https://cdn.", self.page)

    @unittest.skipUnless(shutil.which("node"), "node executable not installed")
    def test_inline_javascript_syntax(self):
        scripts = re.findall(r"<script(?:\s[^>]*)?>([\s\S]*?)</script>", self.page)
        self.assertEqual(len(scripts), 2)
        result = subprocess.run(
            ["node", "--check", "-"], input=scripts[-1], text=True,
            capture_output=True, timeout=15, check=False
        )
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
