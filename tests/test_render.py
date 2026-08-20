import unittest

from evidence_trail import render_html, render_markdown


class EvidenceTrailRenderTests(unittest.TestCase):
    def setUp(self):
        self.evidence_map = {
            "question": "Which evidence is reusable?",
            "nodes": [
                {
                    "id": "openaire:publication:1",
                    "type": "publication",
                    "title": "Heat pumps & flexibility",
                    "source_url": "https://doi.org/10.0000/example",
                },
                {
                    "id": "openaire:project:1",
                    "type": "project",
                    "title": "Open energy project",
                    "source_url": "https://explore.openaire.eu/search/project?pid=1",
                },
            ],
            "edges": [
                {
                    "source_id": "openaire:publication:1",
                    "relationship": "linked_project",
                    "target_id": "openaire:project:1",
                }
            ],
            "observations": [
                {
                    "rule_id": "missing_dataset_link",
                    "source_ids": ["openaire:publication:1"],
                }
            ],
        }

    def test_markdown_keeps_sources_and_labels_observations(self):
        rendered = render_markdown(self.evidence_map)

        self.assertIn("[Heat pumps & flexibility](https://doi.org/10.0000/example)", rendered)
        self.assertIn("Rule-derived observation", rendered)
        self.assertIn("No linked dataset", rendered)

    def test_html_is_self_contained_and_escapes_source_text(self):
        rendered = render_html(self.evidence_map)

        self.assertIn("<!doctype html>", rendered.lower())
        self.assertIn("Heat pumps &amp; flexibility", rendered)
        self.assertIn('href="https://doi.org/10.0000/example"', rendered)
        self.assertIn("Rule-derived observation", rendered)


if __name__ == "__main__":
    unittest.main()
