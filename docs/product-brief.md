# Evidence Trail — product brief

**Status:** Frozen on 20 August 2026 after authenticated live MCP schema and query smoke.

## User and painful job

Research programme managers, funders, and policy analysts need to decide whether a field is ready for action or needs more investment. Conventional literature search returns papers, but it rarely shows whether claims connect to open datasets, reusable software, funded projects, organisations, or obvious evidence gaps. Manually reconstructing that trail is slow and difficult to audit.

## Proposition

Evidence Trail converts one plain-language research question into a source-linked map of relevant OpenAIRE entities. It shows what evidence exists, who funded and produced it, which open datasets and software make it reusable, and where the graph contains missing or weak links. It then exports a concise Markdown and JSON decision brief.

The demonstration domain will be residential heat-pump flexibility: topical, decision-relevant, and rich enough to connect publications, UK/EU projects, organisations, datasets, and software. The method remains reusable for any domain.

## Differentiator

This is not another paper summariser. It treats provenance and absence as first-class outputs:

1. Every displayed statement links to an OpenAIRE entity or is explicitly labelled as a rule-derived observation.
2. Missing datasets, software, funding links, licences, or open-access signals remain visible rather than being filled by model inference.
3. The exported evidence ledger can be rerun, audited, and extended by another user.
4. The judge sees both a useful decision workflow and a reusable technical pattern for the OpenAIRE MCP.

## Three demo questions

1. **Clear trail:** Which research on residential heat-pump demand response is connected to funded projects and reusable open artifacts?
2. **Gap-heavy:** Where has heat-pump flexibility research produced publications but no linked open dataset or software in the OpenAIRE Graph?
3. **Comparison:** How do the openness and artifact-linkage profiles of UK- and EU-funded heat-pump flexibility projects differ?

## Success measures

- 100% of displayed factual claims have an OpenAIRE source identifier and public link.
- Zero unsupported generated claims in the fixed three-question evaluation.
- Duplicate entities are consolidated deterministically.
- Missing or partial evidence is labelled rather than silently inferred.
- A clean setup can rerun all three examples and export Markdown plus JSON.
- A first-time evaluator reaches a useful map in under three minutes.
- The submission demonstrates and documents actual Alien/OpenAIRE MCP use.

## Judging hypothesis

Evidence Trail can score at least 4/5 on all six criteria by combining mandatory MCP use with a concrete policy/research job, a provenance-first design, honest limitations, a reproducible public artifact, and a simple before/after story. The strongest originality claim is not generic AI search; it is an auditable evidence-gap workflow built from the relationships already present—or visibly absent—in OpenAIRE.

## Non-goals

- Claiming scientific consensus or contradiction from metadata alone.
- Reading or redistributing paywalled full text.
- Replacing systematic-review methodology or expert appraisal.
- Inferring causal effects, research quality, or funding impact without evidence.
- Building a broad autonomous research agent before the three-question path works.

## Scope guard

If MCP access cannot expose the required entity relationships by 16 August, reduce the artifact to a reproducible MCP-driven evidence ledger and gap report. Do not replace the required MCP with the public API and still claim compliance.
