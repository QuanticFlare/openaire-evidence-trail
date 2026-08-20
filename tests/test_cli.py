import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class EvidenceTrailCliTests(unittest.TestCase):
    def test_json_evidence_ledger_can_be_mapped_from_the_command_line(self):
        ledger = {
            "question": "What evidence exists?",
            "records": [
                {
                    "id": "openaire:publication:1",
                    "type": "publication",
                    "title": "Heat-pump flexibility",
                    "source_url": "https://explore.openaire.eu/search/publication?pid=1",
                    "projects": [],
                    "datasets": [],
                    "software": [],
                }
            ],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = Path(temp_dir) / "ledger.json"
            input_path.write_text(json.dumps(ledger))
            result = subprocess.run(
                [sys.executable, "-m", "evidence_trail", "--input", str(input_path)],
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        rendered = json.loads(result.stdout)
        self.assertEqual(rendered["question"], "What evidence exists?")
        self.assertEqual(len(rendered["nodes"]), 1)
        self.assertEqual(len(rendered["observations"]), 2)

    def test_markdown_report_can_be_written_to_a_file(self):
        ledger = {
            "question": "What evidence exists?",
            "records": [
                {
                    "id": "openaire:publication:1",
                    "type": "publication",
                    "title": "Heat-pump flexibility",
                    "source_url": "https://doi.org/10.0000/example",
                    "projects": [],
                    "datasets": [],
                    "software": [],
                }
            ],
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = Path(temp_dir) / "ledger.json"
            output_path = Path(temp_dir) / "report.md"
            input_path.write_text(json.dumps(ledger))
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "evidence_trail",
                    "--input",
                    str(input_path),
                    "--format",
                    "markdown",
                    "--output",
                    str(output_path),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

            rendered = output_path.read_text() if output_path.exists() else ""

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("# Evidence Trail", rendered)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
