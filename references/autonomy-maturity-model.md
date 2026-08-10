# Reference: Autonomy Maturity Model (Cross-Cutting)

<!--
Dimensions:
  zoom=enterprise
  unit=governance
  lifecycle=assisted,lifecycle=augmented,lifecycle=supervised,lifecycle=autonomous,lifecycle=self-evolving
  governance=policy-bounded
-->

## Purpose

A cross-cutting reference that defines the **five stages of autonomy** an
enterprise (or any unit within it) moves through as it adopts the patterns
in this repo family. Used by [`autonomous-enterprise/artifacts/autonomy-maturity-scorecard`](../artifacts/autonomy-maturity-scorecard)
to assess current state and to identify the next viable stage.

## Composed from

- `dea-catalog-strategic-objectives` — autonomy is pursued in service of objectives
- `dea-catalog-organizational-units` — maturity applies per unit, not just enterprise-wide
- `dea-catalog-agent-foundry` — the stages describe increasing agent autonomy

## The five stages

| Stage | What changes | What's required to move to the next stage |
|---|---|---|
| **L1 Assisted** | AI/automation assists a human doing the work | Telemetry that proves the assist is needed and useful |
| **L2 Augmented** | AI/automation and human collaborate; human retains accountability | Bounded scope, decision provenance, rollback |
| **L3 Supervised** | Automation does the work; human supervises and can intervene | Policy gates on side effects, intervention cost measured |
| **L4 Autonomous** | Automation does the work end-to-end with policy-bounded exception handling | Self-healing, exception budgets, observability |
| **L5 Self-Evolving** | Automation improves its own policies, models, or playbooks under guardrails | Change-management governance, model-update guardrails, kill-switches |

## Notes

- Maturity is **per unit × per capability**, not a single enterprise-wide score.
- Stage L4 and above require the cross-cutting governance regime from
  `governance=policy-bounded` or stricter.
- Stage L5 requires an ADR per new class of self-modification.
