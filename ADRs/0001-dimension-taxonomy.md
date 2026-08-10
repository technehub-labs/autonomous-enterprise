# ADR 0001: Dimension Taxonomy for the Autonomous Enterprise Concept Repository

- **Status:** Accepted
- **Date:** 2026-08-10
- **Deciders:** TechneHub Labs maintainers

## Context

This repository is the **umbrella concept repository** for the "Autonomous
Enterprise" pattern. It composes references, tools, and artifacts *on top of*
the DEA catalogs (`dea-catalog-*`) and the four sibling concept repositories
(`autonomous-operations`, `autonomous-networks`, `autonomous-flow`,
`agentic-workflows`).

Because the pattern spans the whole operating model, multiple valid
classification axes apply at once (zoom level, automation unit, lifecycle
stage, governance regime). We cannot enforce MECE on the repo name itself —
the name covers the whole enterprise. Instead, every artifact in this repo
must declare the dimension(s) it belongs to.

This ADR defines those dimensions. New dimensions require a new ADR.

## Decision

The Autonomous Enterprise concept repository uses the following dimensions.
Every artifact in `references/`, `tools/`, and `artifacts/` MUST be tagged
with at least one dimension.

### Dimension 1 — Zoom level (`zoom`)

What scope the artifact addresses.

| Value | Meaning |
|---|---|
| `zoom=enterprise` | Whole-enterprise operating model, governance, strategy execution |
| `zoom=domain` | A single business domain within the enterprise |
| `zoom=capability` | A single business capability and its automation |
| `zoom=system` | A single system of record or system of engagement |
| `zoom=task` | A single task or agent action |

### Dimension 2 — Automation unit (`unit`)

What the autonomy acts on.

| Value | Meaning |
|---|---|
| `unit=decision` | Decision-making (human-in-the-loop vs autonomous vs hybrid) |
| `unit=process` | End-to-end business process orchestration |
| `unit=data` | Data products, pipelines, and information lifecycles |
| `unit=infrastructure` | Infrastructure provisioning and runtime |
| `unit=governance` | Policy, risk, compliance, audit |

### Dimension 3 — Lifecycle stage (`lifecycle`)

Where the artifact sits on the autonomy maturity curve.

| Value | Meaning |
|---|---|
| `lifecycle=assisted` | Human does the work; AI/automation assists |
| `lifecycle=augmented` | Human and automation collaborate, human retains accountability |
| `lifecycle=supervised` | Automation does the work; human supervises and can intervene |
| `lifecycle=autonomous` | Automation does the work end-to-end with policy-bounded exception handling |
| `lifecycle=self-evolving` | Automation improves its own policies, models, or playbooks under guardrails |

### Dimension 4 — Governance regime (`governance`)

What control regime applies.

| Value | Meaning |
|---|---|
| `governance=strict` | Hard policy + approval gates before action |
| `governance=policy-bounded` | Soft policy with bounded exception handling |
| `governance=open` | Minimal gating, high observability |

## Consequences

- Every artifact carries a dimension tag (in its frontmatter or README header).
  New artifacts without a tag are rejected at PR review.
- Adding a new dimension value within an existing dimension is a minor change
  (PR with rationale). Adding a new dimension axis itself requires a new ADR
  that supersedes this one.
- Cross-repo references to sibling concept repos
  (`autonomous-operations`, `autonomous-networks`, `autonomous-flow`,
  `agentic-workflows`) are encouraged and must declare the corresponding
  dimension on both sides.

## Alternatives considered

- **Single flat enum on the repo name.** Rejected — collapses three axes and
  forces one of them to win. Loses the ability to keep multiple axes explicit
  over time.
- **Per-artifact free-form tags.** Rejected — drifts without reviewable
  governance.
- **No dimensions, just folders.** Rejected — hides the classification and
  makes drift invisible until it's too late.
