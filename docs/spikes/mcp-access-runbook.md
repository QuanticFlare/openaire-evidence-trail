# Official MCP access runbook

Run only after the registration email supplies the official Alien/OpenAIRE access route. Do not substitute an unofficial connector and do not copy credentials into this repository.

## Access evidence

1. Record the confirmation date, official hostname/package identity, supplied client configuration shape, terms link, and whether access is free for the hackathon.
2. Store secrets in the host credential mechanism or untracked environment only. Record presence and expiry, never values.
3. Enumerate the server's exposed tool names, descriptions, input schemas, read/write annotations, authentication behaviour, and documented limits.
4. Fail closed if the connector exposes unrelated write, destructive, financial, execution, or credential-management tools; allow only the OpenAIRE read tools needed by the artifact.

## Three-query smoke

Run one bounded query for each prepared question in `docs/product-brief.md`. For every call record:

- UTC timestamp and official tool name;
- redacted request parameters and result count;
- latency and any usage/cost indication;
- entity identifiers and relationship fields returned;
- pagination/truncation indicators;
- empty, partial, rate-limit, and timeout behaviour;
- whether the result can be transformed into the source-backed ledger consumed by `python3 -m evidence_trail`.

## Pass condition

OA-003 passes only when the official MCP returns enough source identifiers and public links to build the three evidence trails, the responses contain no unresolved credential or tool-scope risk, and the resulting ledgers pass the focused project verifier. Public Graph API success alone is insufficient.

