# OA-003 live Alien/OpenAIRE MCP smoke

**Run:** 20 August 2026, 16:00–16:08 UTC

**Endpoint:** `https://mcp.alien.club/mcp`

**Client:** Codex CLI using OAuth; `auth_status` was `o_auth` before the smoke

**Scope:** read-only, page 1, at most five results per query

## Result

The official Alien Intelligence gateway was reachable through OAuth and returned live OpenAIRE
Graph records. Twelve MCP calls completed. No credential value, private configuration URL, raw
mailbox content, or private invitation detail is stored here.

The gateway exposed read tools for health, discovery, research-product search, project search,
person search, organization search, publication/dataset/software/project/organization lookup, and
Scholix links. The datasource tools were not enabled. A separate `set_profile` tool can change
gateway state; it was not called and is disabled in the Codex MCP configuration.

## Schema findings

- `search_5` reached `/research-products` and supported a `type` filter for publication, dataset,
  and software. `sortBy` required both a field and direction, for example `relevance DESC`.
- `search_6` reached `/projects`, despite its gateway description referring to datasets.
- `search_7` reached `/persons`, despite its gateway description referring to projects.
- `search_8` searched organizations.
- Direct lookup tools accepted a single OpenAIRE `id` for publication, dataset, software/project,
  and organization records. Some generated parameter descriptions do not match the live resource.
- `get_links` exposed bounded Scholix link filters including source/target PID, publisher, type,
  relation, date range, page, and page size.

These description mismatches are treated as integration risks: Evidence Trail relies on observed
responses and fixed fixtures, not tool names alone.

## Bounded query evidence

### Research publications

`search_5(search="heat pump flexibility", type="publication", hasProjectRel=true,
page=1, pageSize=5, sortBy="relevance DESC")` returned 5 of 135 records in 1,071 ms.

- `doi_________::41413068adb6fc05b2b2bfe294720212`, DOI
  `10.1007/s12053-024-10206-z`, linked to AURES II.
- `doi_dedup___::b48435b2a226ece3f0b16fac39ee13da`, DOI
  `10.1051/e3sconf/201911301007`, linked to PUMP-HEAT.
- Three further page-one publications had project links.

All five returned no dataset/software relationship and `codeRepositoryUrl: null`. This is a gap in
the retrieved page-one snapshot, not proof that artifacts do not exist elsewhere.

### Datasets

The same bounded query with `type="dataset"` returned 5 of 16 records in 683 ms. The leading result,
`doi_dedup___::3f1722337b77704550b638aed0432b50`, DOI
`10.25384/sage.c.6345957`, was CC BY and linked to two UKRI projects:
`EP/S021671/1` and `EP/R035288/1`. Both returned relationship trust `0.85`.

### Software

The same bounded query with `type="software"` returned all 4 records in 358 ms. Results included:

- MIT-licensed software at DOI `10.48420/23778021`.
- An open CC BY reproducible example at DOI `10.5281/zenodo.21196303`.
- A restricted CC BY-NC-ND record linked to Horizon Europe project O-CEI, relationship trust `0.9`.
- BSD-3-Clause SIMONA software with a GitHub repository at DOI `10.5281/zenodo.15376524`.

### Projects and failure behaviour

A general project search for the phrase returned 2 of 2 results. Adding literal `funder="UKRI"` or
`funder="EC"` returned zero results, so funder comparison must be derived from returned project
relationships rather than assumed to work as a direct text filter.

Three initial calls with `sortBy="relevance"` returned HTTP 400. Adding `DESC` resolved the error.
No call requested a paid feature and no response exposed a usage-cost signal.

## Reproducible artifacts

- Sanitized live ledger: `examples/mcp-heat-pump-live.json`
- Generated Markdown brief: `docs/demo/evidence-trail-live.md`
- Generated standalone HTML: `docs/demo/evidence-trail-live.html`

The local fixture preserves exact identifiers and returned project relationships. It deliberately
does not create edges between separate publication, dataset, and software search results.

## Acceptance judgment

The independent pointwise review passed tool discovery, live retrieval, three-question evidence,
and safety/reproducibility. Its only failure was that the model-written report did not itself show
authentication evidence. The parent resolved that deterministically with the pre-run OAuth status
and the successful authenticated calls above. OA-003 therefore passes for bounded live access;
pagination, timeout, and rate-limit handling remain future adapter work.
