"""Provenance-first evidence mapping for OpenAIRE records."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any

from .render import render_html, render_markdown


def build_evidence_map(*, question: str, records: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    """Build rule-derived observations without inventing missing evidence."""

    observations: list[dict[str, Any]] = []
    nodes_by_id: dict[str, dict[str, str]] = {}
    edges: list[dict[str, str]] = []
    for record in records:
        if not record.get("source_url"):
            raise ValueError("record source_url is required for provenance")
        source_id = str(record["id"])
        nodes_by_id.setdefault(
            source_id,
            {
                "id": source_id,
                "type": str(record["type"]),
                "title": str(record["title"]),
                "source_url": str(record["source_url"]),
            },
        )
        for collection_name, entity_type in (
            ("projects", "project"),
            ("datasets", "dataset"),
            ("software", "software"),
        ):
            for related in record.get(collection_name, []):
                if not related.get("source_url"):
                    raise ValueError("related entity source_url is required for provenance")
                target_id = str(related["id"])
                nodes_by_id.setdefault(
                    target_id,
                    {
                        "id": target_id,
                        "type": str(related.get("type", entity_type)),
                        "title": str(related["title"]),
                        "source_url": str(related["source_url"]),
                    },
                )
                edges.append(
                    {
                        "source_id": source_id,
                        "relationship": f"linked_{entity_type}",
                        "target_id": target_id,
                    }
                )
        if record.get("type") == "publication" and not record.get("datasets"):
            observations.append(
                {
                    "rule_id": "missing_dataset_link",
                    "source_ids": [source_id],
                }
            )
        if record.get("type") == "publication" and not record.get("software"):
            observations.append(
                {
                    "rule_id": "missing_software_link",
                    "source_ids": [source_id],
                }
            )

    return {
        "question": question,
        "nodes": list(nodes_by_id.values()),
        "edges": edges,
        "observations": observations,
    }


__all__ = ["build_evidence_map", "render_html", "render_markdown"]
