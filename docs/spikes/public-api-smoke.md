# Public Graph API schema smoke

Run on 15 August 2026 to reduce integration uncertainty while Alien MCP access remains gated. This is **not** evidence of OA-003 completion because the competition explicitly requires MCP use.

## Research products

Request: `GET https://api.openaire.eu/graph/v3/research-products` with `search=heat pump demand response`, `type=publication`, and `pageSize=3`.

- HTTP request succeeded unauthenticated.
- Header reported 488 matches, 291 ms query time, and three returned records.
- Records exposed stable identifiers, titles, publication dates, type, and linked projects where present.
- One returned publication linked two UKRI projects; missing dataset/software relationships remained absent rather than fabricated.

## Projects

Request: `GET https://api.openaire.eu/graph/v3/projects` with `search=heat pump` and `pageSize=3`.

- HTTP request succeeded unauthenticated.
- Header reported 162 matches, 54 ms query time, and three returned records.
- Records exposed identifiers, codes, acronyms, titles, funders, funding streams, and dates.

## Implication

The chosen demonstration domain has enough public OpenAIRE coverage to support a useful trail. OA-003 must still verify the equivalent workflow through the supplied Alien/OpenAIRE MCP, including tool schemas, relationship coverage, authentication, latency, and failure modes.

