import unittest

from evidence_trail import build_evidence_map


class EvidenceMapTests(unittest.TestCase):
    def test_missing_artifact_links_are_explicit_and_source_backed(self):
        evidence_map = build_evidence_map(
            question="Which heat-pump flexibility research has reusable artifacts?",
            records=[
                {
                    "id": "openaire:publication:1",
                    "type": "publication",
                    "title": "Demand response with heat pumps",
                    "source_url": "https://explore.openaire.eu/search/publication?pid=1",
                    "projects": [
                        {
                            "id": "openaire:project:1",
                            "title": "UK Centre for Research on Energy Demand",
                            "source_url": "https://explore.openaire.eu/search/project?pid=1",
                        }
                    ],
                    "datasets": [],
                    "software": [],
                }
            ],
        )

        self.assertEqual(evidence_map["question"], "Which heat-pump flexibility research has reusable artifacts?")
        self.assertEqual(
            {observation["rule_id"] for observation in evidence_map["observations"]},
            {"missing_dataset_link", "missing_software_link"},
        )
        for observation in evidence_map["observations"]:
            self.assertEqual(observation["source_ids"], ["openaire:publication:1"])

    def test_record_without_public_source_link_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "source_url"):
            build_evidence_map(
                question="What evidence exists?",
                records=[
                    {
                        "id": "openaire:publication:1",
                        "type": "publication",
                        "title": "Untraceable record",
                        "projects": [],
                        "datasets": [],
                        "software": [],
                    }
                ],
            )

    def test_related_entity_without_public_source_link_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "related entity source_url"):
            build_evidence_map(
                question="What evidence exists?",
                records=[
                    {
                        "id": "openaire:publication:1",
                        "type": "publication",
                        "title": "Traceable record",
                        "source_url": "https://explore.openaire.eu/search/publication?pid=1",
                        "projects": [
                            {
                                "id": "openaire:project:1",
                                "title": "Untraceable project",
                            }
                        ],
                        "datasets": [],
                        "software": [],
                    }
                ],
            )

    def test_shared_project_is_emitted_once_with_two_evidence_edges(self):
        shared_project = {
            "id": "openaire:project:1",
            "type": "project",
            "title": "Shared energy programme",
            "source_url": "https://explore.openaire.eu/search/project?pid=1",
        }
        evidence_map = build_evidence_map(
            question="Which work came from this programme?",
            records=[
                {
                    "id": "openaire:publication:1",
                    "type": "publication",
                    "title": "First result",
                    "source_url": "https://explore.openaire.eu/search/publication?pid=1",
                    "projects": [shared_project],
                    "datasets": [],
                    "software": [],
                },
                {
                    "id": "openaire:publication:2",
                    "type": "publication",
                    "title": "Second result",
                    "source_url": "https://explore.openaire.eu/search/publication?pid=2",
                    "projects": [shared_project],
                    "datasets": [],
                    "software": [],
                },
            ],
        )

        self.assertEqual(
            [node["id"] for node in evidence_map["nodes"]],
            ["openaire:publication:1", "openaire:project:1", "openaire:publication:2"],
        )
        self.assertEqual(
            evidence_map["edges"],
            [
                {
                    "source_id": "openaire:publication:1",
                    "relationship": "linked_project",
                    "target_id": "openaire:project:1",
                },
                {
                    "source_id": "openaire:publication:2",
                    "relationship": "linked_project",
                    "target_id": "openaire:project:1",
                },
            ],
        )

    def test_only_publications_receive_missing_artifact_observations(self):
        evidence_map = build_evidence_map(
            question="Which reusable artifacts have project links?",
            records=[
                {
                    "id": "openaire:dataset:1",
                    "type": "dataset",
                    "title": "Heat-pump demand-response data",
                    "source_url": "https://doi.org/10.0000/example-data",
                    "projects": [],
                    "datasets": [],
                    "software": [],
                },
                {
                    "id": "openaire:publication:1",
                    "type": "publication",
                    "title": "Heat-pump flexibility study",
                    "source_url": "https://doi.org/10.0000/example-paper",
                    "projects": [],
                    "datasets": [],
                    "software": [],
                },
            ],
        )

        self.assertEqual(
            evidence_map["observations"],
            [
                {
                    "rule_id": "missing_dataset_link",
                    "source_ids": ["openaire:publication:1"],
                },
                {
                    "rule_id": "missing_software_link",
                    "source_ids": ["openaire:publication:1"],
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
