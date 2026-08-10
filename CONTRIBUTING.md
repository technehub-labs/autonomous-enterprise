# Contributing

This repository is one of five **concept repositories** in the `technehub-labs`
organisation. Concept repositories assemble patterns, tools, and artifacts
*on top of* the DEA catalogs — they are not catalogs themselves.

## How this repo is organised

Every concept repository uses the same three-folder layout:

| Folder | Purpose |
|---|---|
| `references/` | Named reference architectures, pattern documents, and ADR-backed design notes |
| `tools/` | Reusable tooling — CLI scripts, validators, generators, accelerators |
| `artifacts/` | Concrete deliverables — templates, scaffolds, checklists, worked examples |

Each artifact is tagged with one or more **dimensions** declared in
[`ADRs/0001-dimension-taxonomy.md`](./ADRs/0001-dimension-taxonomy.md). Dimensions
are how this repo stays coherent when multiple valid classification axes apply
(zoom level, domain, automation unit, lifecycle stage).

## Contribution rules

1. **Foundation first.** New patterns, tools, and artifacts must reference an
   existing dimension declared in `ADRs/0001-dimension-taxonomy.md`. If a new
   dimension is needed, add an ADR before adding the artifact.
2. **No silent scope drift.** If a contribution does not fit any existing
   dimension, the contribution is rejected until either (a) the artifact is
   re-scoped to fit an existing dimension, or (b) a new ADR adds the dimension.
3. **Atomic commits.** One logical change per commit. Commit message format:
   `<type>: <imperative description>` (`feat:`, `fix:`, `refactor:`,
   `docs:`, `chore:`).
4. **Apache-2.0.** All contributions are under the Apache License, Version 2.0.
   Include the standard license header in new files where applicable.
5. **Provenance.** New references must cite the DEA catalog entries they
   compose (e.g. `dea-catalog-processes#<entry>`,
   `dea-catalog-agent-foundry#<entry>`).

## Pull request checklist

- [ ] Artifact is tagged with at least one declared dimension
- [ ] README/ADR updated if a new dimension or naming was introduced
- [ ] No secrets, credentials, or proprietary data included
- [ ] Commit messages follow `<type>: <description>`
- [ ] Branch name follows `feature/<scope>`, `fix/<scope>`, `refactor/<scope>`,
      or `docs/<scope>`
