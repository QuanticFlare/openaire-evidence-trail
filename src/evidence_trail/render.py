"""Deterministic, source-linked reports for an Evidence Trail map."""

from __future__ import annotations

from html import escape
from typing import Any, Mapping


OBSERVATION_LABELS = {
    "missing_dataset_link": "No linked dataset is present in the retrieved OpenAIRE record.",
    "missing_software_link": "No linked software is present in the retrieved OpenAIRE record.",
}


def render_markdown(evidence_map: Mapping[str, Any]) -> str:
    """Render a compact, auditable Markdown decision brief."""
    nodes = list(evidence_map.get("nodes", []))
    edges = list(evidence_map.get("edges", []))
    observations = list(evidence_map.get("observations", []))
    nodes_by_id = {node["id"]: node for node in nodes}

    lines = [
        "# Evidence Trail",
        "",
        f"**Question:** {evidence_map['question']}",
        "",
        f"**Snapshot:** {len(nodes)} source-linked entities, {len(edges)} relationships, "
        f"{len(observations)} rule-derived observations.",
        "",
        "## Source-linked entities",
        "",
    ]
    for node in nodes:
        lines.append(
            f"- **{str(node['type']).title()}:** "
            f"[{node['title']}]({node['source_url']}) — `{node['id']}`"
        )

    lines.extend(["", "## Relationships", ""])
    if edges:
        for edge in edges:
            source = nodes_by_id[edge["source_id"]]
            target = nodes_by_id[edge["target_id"]]
            relationship = str(edge["relationship"]).replace("_", " ")
            lines.append(
                f"- [{source['title']}]({source['source_url']}) "
                f"**{relationship}** [{target['title']}]({target['source_url']})"
            )
    else:
        lines.append("- No source-backed relationships were returned in this snapshot.")

    lines.extend(["", "## Evidence gaps", ""])
    if observations:
        for observation in observations:
            source = nodes_by_id[observation["source_ids"][0]]
            label = OBSERVATION_LABELS.get(
                observation["rule_id"], str(observation["rule_id"]).replace("_", " ")
            )
            lines.append(
                f"- **Rule-derived observation — {label}** "
                f"Source: [{source['title']}]({source['source_url']})."
            )
    else:
        lines.append("- No evidence-gap rules fired for this snapshot.")

    lines.extend(
        [
            "",
            "## Method and limits",
            "",
            "Every entity and relationship above comes from the supplied OpenAIRE evidence ledger. "
            "Gap statements are deterministic observations about absent links in that retrieved "
            "snapshot; they do not prove that an artifact does not exist elsewhere.",
            "",
        ]
    )
    return "\n".join(lines)


def render_html(evidence_map: Mapping[str, Any]) -> str:
    """Render a self-contained, accessible HTML evidence map."""
    nodes = list(evidence_map.get("nodes", []))
    edges = list(evidence_map.get("edges", []))
    observations = list(evidence_map.get("observations", []))
    nodes_by_id = {node["id"]: node for node in nodes}

    entity_cards = []
    for node in nodes:
        entity_cards.append(
            '<article class="card">'
            f'<span class="badge">{escape(str(node["type"]).title())}</span>'
            f'<h3><a href="{escape(str(node["source_url"]), quote=True)}">'
            f'{escape(str(node["title"]))}</a></h3>'
            f'<code>{escape(str(node["id"]))}</code>'
            "</article>"
        )

    relationship_items = []
    for edge in edges:
        source = nodes_by_id[edge["source_id"]]
        target = nodes_by_id[edge["target_id"]]
        relationship_items.append(
            "<li>"
            f'<a href="{escape(str(source["source_url"]), quote=True)}">'
            f'{escape(str(source["title"]))}</a> '
            f'<strong>{escape(str(edge["relationship"]).replace("_", " "))}</strong> '
            f'<a href="{escape(str(target["source_url"]), quote=True)}">'
            f'{escape(str(target["title"]))}</a>'
            "</li>"
        )
    if not relationship_items:
        relationship_items.append("<li>No source-backed relationships were returned.</li>")

    observation_items = []
    for observation in observations:
        source = nodes_by_id[observation["source_ids"][0]]
        label = OBSERVATION_LABELS.get(
            observation["rule_id"], str(observation["rule_id"]).replace("_", " ")
        )
        observation_items.append(
            "<li>"
            f'<span class="badge warning">Rule-derived observation</span> '
            f'{escape(label)} Source: '
            f'<a href="{escape(str(source["source_url"]), quote=True)}">'
            f'{escape(str(source["title"]))}</a>.'
            "</li>"
        )
    if not observation_items:
        observation_items.append("<li>No evidence-gap rules fired for this snapshot.</li>")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Evidence Trail</title>
  <style>
    :root {{ color-scheme: light; --ink:#17202a; --muted:#52606d; --paper:#f5f7f4;
      --card:#fff; --line:#d7ded8; --green:#126b55; --amber:#8a4b08; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; font:16px/1.55 system-ui,-apple-system,sans-serif; color:var(--ink);
      background:linear-gradient(135deg,#edf5ef,var(--paper) 45%,#eef2f7); }}
    main {{ max-width:1060px; margin:auto; padding:56px 24px 72px; }}
    header {{ border-left:7px solid var(--green); padding:8px 0 8px 22px; margin-bottom:32px; }}
    h1 {{ font-size:clamp(2.2rem,7vw,4.5rem); line-height:.95; margin:0 0 18px; letter-spacing:-.05em; }}
    h2 {{ margin-top:42px; font-size:1.45rem; }}
    .question {{ max-width:780px; font-size:1.2rem; color:var(--muted); }}
    .metrics {{ display:flex; flex-wrap:wrap; gap:10px; margin-top:24px; }}
    .metric {{ background:var(--ink); color:white; padding:8px 13px; border-radius:999px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:14px; }}
    .card {{ background:var(--card); border:1px solid var(--line); border-radius:12px;
      padding:18px; box-shadow:0 8px 24px #17202a0d; }}
    .card h3 {{ font-size:1.02rem; margin:10px 0; }}
    .badge {{ display:inline-block; background:#dcefe8; color:var(--green); border-radius:999px;
      padding:3px 8px; font-size:.73rem; font-weight:750; letter-spacing:.04em; text-transform:uppercase; }}
    .warning {{ color:var(--amber); background:#fff0d7; margin-right:5px; }}
    a {{ color:#075b9a; text-underline-offset:3px; }}
    code {{ color:var(--muted); overflow-wrap:anywhere; font-size:.76rem; }}
    li {{ margin:11px 0; }}
    .limits {{ padding:18px 20px; background:#fff; border:1px solid var(--line); border-radius:12px; }}
  </style>
</head>
<body>
<main>
  <header>
    <span class="badge">OpenAIRE provenance map</span>
    <h1>Evidence Trail</h1>
    <p class="question">{escape(str(evidence_map['question']))}</p>
    <div class="metrics">
      <span class="metric">{len(nodes)} source-linked entities</span>
      <span class="metric">{len(edges)} relationships</span>
      <span class="metric">{len(observations)} visible gaps</span>
    </div>
  </header>
  <section><h2>Source-linked entities</h2><div class="grid">{''.join(entity_cards)}</div></section>
  <section><h2>Relationships</h2><ul>{''.join(relationship_items)}</ul></section>
  <section><h2>Evidence gaps</h2><ul>{''.join(observation_items)}</ul></section>
  <section class="limits"><h2>Method and limits</h2><p>Every entity and relationship comes from
  the supplied OpenAIRE evidence ledger. Gap statements describe absent links in this retrieved
  snapshot; they do not prove that an artifact does not exist elsewhere.</p></section>
</main>
</body>
</html>
"""
