import json
import unittest
from pathlib import Path

from evidence_trail import build_evidence_map, render_html, render_markdown


class LiveFixtureTests(unittest.TestCase):
    def test_sanitized_mcp_fixture_has_expected_provenance_coverage(self):
        fixture_path = Path(__file__).parents[1] / "examples" / "mcp-heat-pump-live.json"
        payload = json.loads(fixture_path.read_text())

        evidence_map = build_evidence_map(
            question=payload["question"], records=payload["records"]
        )

        self.assertEqual(len(evidence_map["nodes"]), 10)
        self.assertEqual(len(evidence_map["edges"]), 5)
        self.assertEqual(len(evidence_map["observations"]), 4)
        self.assertTrue(
            all(node["source_url"].startswith("https://") for node in evidence_map["nodes"])
        )

    def test_checked_in_reports_match_the_live_fixture(self):
        root = Path(__file__).parents[1]
        payload = json.loads((root / "examples" / "mcp-heat-pump-live.json").read_text())
        evidence_map = build_evidence_map(
            question=payload["question"], records=payload["records"]
        )

        self.assertEqual(
            (root / "docs" / "demo" / "evidence-trail-live.md").read_text(),
            render_markdown(evidence_map),
        )
        self.assertEqual(
            (root / "docs" / "demo" / "evidence-trail-live.html").read_text(),
            render_html(evidence_map),
        )


if __name__ == "__main__":
    unittest.main()
