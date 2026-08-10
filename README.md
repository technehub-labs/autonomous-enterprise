# Autonomous Enterprise

> **Umbrella concept repository** for the Autonomous Enterprise pattern.
> Composes references, tools, and artifacts on top of the DEA catalogs and the
> four sibling concept repositories.

This is the **public, umbrella** concept repository in the Autonomous family.
It does not own a single layer — it owns the *cross-cutting* concern: how all
five concept repositories (and the catalogs beneath them) cohere into an
operating model that can run itself end-to-end.

## Relationship to other repos

```
         ┌──────────────────────────────────────────────┐
         │       autonomous-enterprise  (PUBLIC)        │  ← you are here
         │       umbrella / cross-cutting               │
         └────────────────────────┬─────────────────────┘
                                  │ composes
   ┌──────────────┌───────────────┌────────────────┌──────────────┐
   │              │                                               │
   ▼              ▼               ▼                ▼              ▼
autonomous-    autonomous-     autonomous-       autonomous-    dea-catalog-*
operations     networks        flow              agentic-       (catalogs)
(ops layer)    (network        (cross-system     workflows
               layer)          flow layer)       (agent task
                                               layer)
```

## What lives here

| Folder | Contents |
|---|---|
| [`references/`](./references) | Cross-cutting reference architectures and operating-model documents |
| [`tools/`](./tools) | Cross-cutting tooling — governance validators, autonomy maturity assessors, cross-repo dimension mappers |
| [`artifacts/`](./artifacts) | Cross-cutting deliverables — operating-model templates, autonomy maturity scorecards, adoption playbooks |
| [`ADRs/`](./ADRs) | Architecture decision records |

## Dimensions

Every artifact in this repo must declare at least one dimension from
[`ADRs/0001-dimension-taxonomy.md`](./ADRs/0001-dimension-taxonomy.md). The
four dimensions currently declared are:

- **`zoom`** — enterprise / domain / capability / system / task
- **`unit`** — decision / process / data / infrastructure / governance
- **`lifecycle`** — assisted / augmented / supervised / autonomous / self-evolving
- **`governance`** — strict / policy-bounded / open

New dimensions require a new ADR.

## Catalogs composed

This repo composes entries from, but does not own, these catalogs:

- `dea-metaframework` — the 7×7 ECF matrix
- `dea-catalog-strategic-objectives` — strategic intent
- `dea-catalog-value-streams` — value creation flows
- `dea-catalog-processes` — process decomposition
- `dea-catalog-business-capabilities` — capability mapping
- `dea-catalog-organizational-units` — accountability
- `dea-catalog-agent-foundry` — agent patterns
- `dea-catalog-application-components` — deployable units
- `dea-catalog-platform-services` — compute / data / network services
- `dea-catalog-reference-architecture` — the canonical blueprint

## Getting started

1. Read [`ADRs/0001-dimension-taxonomy.md`](./ADRs/0001-dimension-taxonomy.md)
2. Skim [`references/`](./references) for the cross-cutting reference docs
3. Use [`artifacts/autonomy-maturity-scorecard`](./artifacts/autonomy-maturity-scorecard)
   to assess where you are on the lifecycle axis

## License

Apache-2.0. See [`LICENSE`](./LICENSE).
