"""Command-line entry point for fixture and MCP-export evidence ledgers."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import build_evidence_map, render_html, render_markdown


def main() -> int:
    parser = argparse.ArgumentParser(prog="evidence-trail")
    parser.add_argument("--input", required=True, type=Path, help="JSON evidence ledger")
    parser.add_argument(
        "--format",
        choices=("json", "markdown", "html"),
        default="json",
        help="Output format (default: json)",
    )
    parser.add_argument("--output", type=Path, help="Write output to a file instead of stdout")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text())
    evidence_map = build_evidence_map(
        question=payload["question"],
        records=payload["records"],
    )
    if args.format == "markdown":
        rendered = render_markdown(evidence_map)
    elif args.format == "html":
        rendered = render_html(evidence_map)
    else:
        rendered = json.dumps(evidence_map, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="" if rendered.endswith("\n") else "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
