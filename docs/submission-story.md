# Evidence Trail

**OpenAIRE AI Hackathon 2026 — Theme B: Build**

**Participant:** Dan Lowry, independent

**Artifact:** a provenance-first OpenAIRE evidence map and exportable decision brief

## The problem

Research programme managers, funders, and policy analysts often need a practical answer rather than
a reading list: is a field ready for action, can its results be reused, and where should the next
investment go? Conventional search surfaces papers, but reconstructing the trail from publications
to datasets, software, funded projects, and organisations is slow. A fluent AI summary can make the
problem worse if it quietly fills missing links with plausible claims.

Evidence Trail makes provenance and absence visible. It turns a plain-language question into a
source-linked map of OpenAIRE entities and their recorded relationships. Every factual item links to
a public source. Missing artifact links are labelled as deterministic observations about a bounded
snapshot—not as proof that the artifact does not exist.

The demonstration asks:

> Which heat-pump flexibility research is connected to funded projects and reusable open artifacts?

Residential heat-pump flexibility is a useful test case: it matters for a decarbonised electricity
system, spans UK and EU funding, and has publications, datasets, and software in OpenAIRE.

## What I built

Evidence Trail is a small, dependency-free Python application with three outputs:

1. A JSON evidence map for reuse by other tools.
2. A concise Markdown decision brief.
3. A standalone, accessible HTML view for a first-time evaluator.

The mapper deduplicates entities by their OpenAIRE identifier, preserves public source links, records
only returned relationships, and runs explicit evidence-gap rules for publication records. A missing
dataset or software edge is displayed as a “rule-derived observation” with its source publication.
The report explains the crucial limitation: absence in the retrieved snapshot is not universal
absence.

This is intentionally not another paper summariser. It does not claim consensus, research quality,
causality, or funding impact from metadata. It does not retrieve or redistribute paywalled full text.

## How the OpenAIRE MCP is used

I authenticated to the official Alien Intelligence MCP gateway and queried the OpenAIRE Graph API
V3 through its live MCP tools. The bounded smoke used read-only calls and recorded tool schemas,
latency, pagination, identifiers, relationships, attribution, and failure behaviour. The Codex client
also disables the gateway's write-capable profile tool.

For `heat pump flexibility`, the live MCP returned:

- 5 of 135 page-one publications with funded-project relationships;
- 5 of 16 page-one datasets, including a CC BY dataset linked to two UKRI projects;
- all 4 matching software records, including MIT, CC BY, and BSD-3-Clause examples;
- EU project relationships including AURES II, PUMP-HEAT, and O-CEI.

The generated demo contains ten deduplicated, source-linked entities and five returned project
relationships. The two publications show four visible gaps because neither record returned a linked
dataset or software. Separate dataset and software search results remain separate: Evidence Trail
does not invent publication-to-artifact edges.

The integration work also surfaced useful implementation evidence. A sort value of `relevance`
failed with HTTP 400; the live API required `relevance DESC`. Two generated tool descriptions did not
match their observed endpoints. The project records these discrepancies and relies on verified
responses and fixed fixtures rather than trusting names or descriptions blindly.

## Responsible and reproducible by design

Responsible data use is part of the product, not a final disclaimer:

- source URLs and OpenAIRE IDs are mandatory;
- related entities without a public source link are rejected;
- duplicate entities are consolidated deterministically;
- inferred relationships are prohibited;
- negative claims are bounded to the retrieved snapshot;
- credentials, private invitations, mailbox content, and private configuration links are excluded;
- no paid feature, wallet, or write-capable MCP tool is required.

The core has no runtime dependency outside Python 3.11+. A clean user can install the package, run
the fixture, regenerate JSON/Markdown/HTML, and run the tests without MCP credentials. The live MCP
smoke document explains exactly which sanitized identifiers and relationships produced the example.
Code is MIT licensed; documentation and submitted materials are CC BY 4.0.

## Evaluation and reuse

The focused test suite covers provenance rejection, entity deduplication, relationship preservation,
type-aware gap rules, Markdown reporting, HTML escaping, and command-line export. Generated demo
outputs are checked from the sanitized live ledger. The submission contains no unsupported scientific
claim: it reports only metadata and relationships returned by OpenAIRE, plus explicitly labelled
rules about missing links.

The pattern is reusable beyond heat pumps. Any team can supply a source-backed OpenAIRE ledger for a
new research question and receive the same auditable outputs. A next pilot would add bounded live
pagination and compare artifact-linkage profiles across funders without changing the provenance
contract.

## AI assistance disclosure

OpenAI Codex 5.6 Sol at Ultra effort helped inspect the live MCP schemas, run bounded read-only
queries, implement and test the mapper and reports, and draft this story. Deterministic tests and an
independent pointwise review checked the outputs. Dan Lowry remains responsible for the entry and
must approve any publication or submission.
