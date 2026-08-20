# Delivery tickets

Tick a ticket only after its acceptance evidence exists. Operational submission cutoff:
**20 August 2026, 22:59 BST**, using the earlier interpretation of the email's 23:59 CEST and the
official page/template's 23:59 CET wording.

## [x] OA-001 — Register and lock the rules

- **Progress:** Registration, rules, attached template, Alien organization membership, OAuth status,
  official endpoint, submission recipient, and deadline conflict are recorded. No credential value is in Git.
- **Owner:** Dan (external actions), Codex (rules audit)
- **Effort / due:** light / 15 Aug
- **Depends on:** none
- **Work:** Register for the hackathon and Alien Gateway; capture the accepted rules, confirmed deadline, submission form fields, Build-track criteria, MCP access instructions, and permitted AI/tool use. Store credentials outside Git.
- **Done when:** Registration and MCP-access confirmation exist; rules checklist records no eligibility or licensing blocker.

## [x] OA-002 — Freeze the winning proposition

- **Progress:** The provenance-first heat-pump-flexibility proposition and non-goals were frozen after
  live MCP results supported the intended publication/dataset/software/project workflow.
- **Owner:** Codex; Dan approves only if the proposition materially changes
- **Effort / due:** deep / 15 Aug
- **Depends on:** OA-001
- **Work:** Define **Evidence Trail**: a provenance-first tool that turns a research question into a linked map of publications, datasets, software, funders, projects, supporting evidence, contradictions, and gaps.
- **Done when:** One-page brief names the user, painful job, differentiator, three demo questions, non-goals, judging hypothesis, and measurable success criteria.

## [x] OA-003 — Prove OpenAIRE MCP access

- **Progress:** OAuth-authenticated Alien MCP tool discovery and 12 bounded read-only calls passed.
  Exact schemas, failures, latency, counts, identifiers, relationships, safety controls, and judge
  outcome are recorded in `docs/spikes/mcp-live-smoke-2026-08-20.md`.
- **Owner:** Codex
- **Effort / due:** standard / 15 Aug
- **Depends on:** OA-001
- **Work:** Run bounded queries for research products, datasets/software, projects, organizations, and links; record schemas, latency, paging, attribution, and failure behaviour.
- **Done when:** A repeatable smoke test returns source identifiers and relationships for all three demo questions without leaking credentials.

## [x] OA-004 — Establish the application skeleton and verifier

- **Progress:** Dependency-free Python 3.11 package, installed console command, CLI, live fixture,
  eleven focused tests, clean-install smoke, and registered workspace verifier are complete.
- **Owner:** Codex
- **Effort / due:** standard / 16 Aug
- **Depends on:** OA-002, OA-003
- **Work:** Choose the smallest deployable stack, create the package/app/test structure, configuration boundary, sample environment file, and focused verifier; update the development profile and workspace verifier registry.
- **Done when:** Fresh setup starts the app; one deterministic test passes; no secrets are committed.

## [ ] OA-005 — Build the OpenAIRE retrieval adapter

- **Progress:** Live retrieval was completed through Codex's official Alien MCP connection and exported
  to a sanitized ledger. A reusable in-app pagination/retry/rate-limit adapter remains intentionally open.

- **Owner:** Codex
- **Effort / due:** standard / 16 Aug
- **Depends on:** OA-003, OA-004
- **Work:** Implement typed MCP retrieval, pagination limits, retries, caching, attribution, and normalized entities/relationships.
- **Done when:** Fixture and live smoke tests prove stable retrieval with explicit empty, partial, rate-limit, and timeout states.

## [ ] OA-006 — Build the evidence-map engine

- **Progress:** Provenance validation, deterministic entity deduplication, returned relationship
  preservation, and publication-only missing-artifact observations are complete. Ranking and
  contradiction logic remain out of the bounded submission scope.

- **Owner:** Codex
- **Effort / due:** deep / 17 Aug
- **Depends on:** OA-005
- **Work:** Rank results, connect claims to products/projects/funders/datasets/software, identify missing links and contradictory signals, and preserve every source identifier.
- **Done when:** Every displayed claim has a traceable OpenAIRE source; deterministic fixtures cover ranking, gaps, contradictions, and deduplication.

## [x] OA-007 — Build the judge-facing experience

- **Progress:** One command produces JSON, Markdown, or a responsive standalone HTML evidence map;
  checked-in live outputs and screenshots are generated from the sanitized MCP ledger.

- **Owner:** Codex
- **Effort / due:** standard / 17 Aug
- **Depends on:** OA-006
- **Work:** Create a crisp question-to-map workflow, expandable evidence cards, filters, confidence/limitation labels, and downloadable Markdown/JSON brief.
- **Done when:** A first-time user completes a demo question in under three minutes without instruction.

## [ ] OA-008 — Run the three-question evaluation

- **Progress:** The live MCP smoke covered publication/project trails, artifact search, and the limits of
  funder filtering. The fixed judge-facing artifact currently presents one integrated question; a
  formal three-question scorecard is not complete.

- **Owner:** Codex
- **Effort / due:** deep / 18 Aug
- **Depends on:** OA-006, OA-007
- **Work:** Test one clear evidence trail, one sparse/gap-heavy topic, and one conflicting topic. Score provenance coverage, duplicate rate, unsupported claims, usefulness, latency, and repeatability.
- **Done when:** Zero unsupported claims; 100% source-link coverage; known failures are visible; focused verifier passes on a fresh run.

## [x] OA-009 — Harden and package the public artifact

- **Progress:** README, clean install, licences, secret scan, generated reports, screenshot, live MCP
  evidence, private submission workspace, and approved public GitHub release are complete.

- **Owner:** Codex
- **Effort / due:** standard / 18 Aug
- **Depends on:** OA-008
- **Work:** Add setup, architecture, limitations, attribution, CC-BY-compatible licensing, screenshots, sample outputs, and a one-command demo path. Remove secrets and private workspace dependencies.
- **Done when:** A clean clone reproduces the demo and license/attribution audit passes.

## [x] OA-010 — Produce the winning submission story

- **Progress:** `docs/submission-story.md` is complete. A six-page, visually verified Word submission
  matching the official template is generated privately with approved public links and consent declarations.

- **Owner:** Codex drafts; Dan reviews
- **Effort / due:** deep / 19 Aug
- **Depends on:** OA-008, OA-009
- **Work:** Write the required 1–2 page story around user pain, distinctive method, OpenAIRE value, evaluation evidence, limitations, reuse potential, and next pilot; capture a short demo video/GIF if permitted.
- **Done when:** Every judging claim points to runnable evidence and the narrative fits the official submission format.

## [x] OA-011 — Independent pre-submission audit

- **Progress:** Live MCP evidence received pointwise review; C2–C5 passed and C1 was resolved with
  deterministic OAuth evidence. Eleven local and clean-clone tests, DOCX validation, PDF proof,
  counts-only secret scans, the public repository, and the hosted demo all pass.

- **Owner:** Codex verifier/judge
- **Effort / due:** deep / 20 Aug, 12:00 BST
- **Depends on:** OA-010
- **Work:** Recheck live rules, eligibility, deadline, licensing, MCP use, links, clean-clone reproducibility, demo outputs, form completeness, and prohibited/private content.
- **Done when:** Signed checklist is green or the submission is explicitly stopped with the blocking evidence.

## [ ] OA-012 — Submit and preserve the receipt

- **Progress:** The completed, validated Word form is attached to a saved Gmail draft addressed to
  `innovation@openaire.eu`; recipient, subject, body, links, and attachment were verified. It has not been sent.
- **Owner:** Dan approves; Codex can perform the send only after action-time approval
- **Effort / due:** light / 20 Aug, 22:59 BST
- **Depends on:** OA-011
- **Work:** Review the final preview, submit through the official form, and save the confirmation/entry URL.
- **Done when:** Official submission receipt and immutable release/commit identifier are recorded in `HANDOFF.md`.

## [ ] OA-013 — Run the ethical community-vote campaign

- **Owner:** Dan approves messages; Codex drafts
- **Effort / due:** light / 21–29 Aug
- **Depends on:** OA-012
- **Work:** Share the genuine artifact through owned professional channels and relevant open-science communities; no purchased engagement, spam, duplicate accounts, or voting manipulation.
- **Done when:** One approved message set is posted and engagement evidence is recorded.

## [ ] OA-014 — Prepare finalist presentation

- **Owner:** Codex drafts; Dan presents
- **Effort / due:** standard / only if shortlisted
- **Depends on:** OA-012
- **Work:** Build a concise live narrative and fallback recording; rehearse the three-minute product flow and likely judge questions.
- **Done when:** Timed rehearsal fits the event slot and every answer is supported by project evidence.
