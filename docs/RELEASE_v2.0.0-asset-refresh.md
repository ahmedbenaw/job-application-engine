# v2.0.0 — Release asset refresh (in-repo copy)

The canonical GitHub [release v2.0.0](https://github.com/ahmedbenaw/job-application-engine/releases/tag/v2.0.0) describes the refreshed ZIP and full notes. This file is the same content kept in the tree for visibility when browsing the repository.

## v2.0.0 — Release asset refreshed (2026-04-25)

This download is a **rebuilt skill package** from `master` (see tag `v2.0.0`), aligned with [CHANGELOG.md](../CHANGELOG.md). The previous ZIP (`JAE-v2.0-Generic-Universal-2026-04-24.zip`, SHA256 `9911a625…`) matched an older tree and omitted several commits that were already on `master` before the asset was rebuilt.

### Verification summary

| Check | Result |
|-------|--------|
| Old release ZIP SHA256 | `9911a625b6be481b6053d7d0815de6e8637092d335cb12eb5dcb7bdea8fc05cd` |
| New ZIP (current asset) | See release Assets — SHA256 published in release notes for each build |
| Layout | **Flat repo root** (`SKILL.md` at zip root) — correct for **Customize → Skills → Create Skill → Upload ZIP**. The retired zip used a nested `job-application-engine/` folder. |

### What was missing from the 2026-04-24 zip (now included)

Tag **`v2.0.0`** matches the `master` commit at the time of the last asset publish. Compare from the first v2.0.0 code tip: [f950ff3…<current tag>](https://github.com/ahmedbenaw/job-application-engine/compare/f950ff387e63c4faaad3367ca8dc2409e6b6e1ba...e1f1697) (link uses known SHAs; update if tag moves again).

1. **40e0027** — Update release links to v2.0.0 tag URL
2. **c9f2a10** — Redesign workflow diagram (dark theme, PNG-matched palette)
3. **616f9b5** — Document-aware First-Use Setup Protocol + per-application profile updates
4. **e311f45** — Session Entry Gate — Mode A (discovery) and Mode B (direct apply)
5. **a364382** — Job board MCP detection + vertical light-mode diagram; automations **A12** and **A13**
6. **c94499f** — README and CHANGELOG audit (11 → **13** declared automations, structure fixes)
7. **4bde2be** — Fix diagram legend violations (five node class corrections)
8. **320c78b** — Revise author information in README.md
9. **e1f1697** — README Quick Start: name the dated release ZIP

### Product highlights (cross-reference with CHANGELOG)

- **13 automations (A01–A13)** including job-board MCP authenticated search (**A12**) and discovery search (**A13**).
- **Session Entry Gate**: Mode A (discovery through Phase 0) vs Mode B (CV + job URL, Phase 0 skipped).
- **First-Use Protocol**: five-step document extraction before gap-fill questions.
- **README** workflow diagram: light-mode vertical layout, legend fixes, Session Entry Gate and job-board nodes.

### Install

Primary: **Customize → Skills → Create Skill → Upload ZIP** — use the `JAE-v2.0-Generic-Universal-*.zip` from [Releases](https://github.com/ahmedbenaw/job-application-engine/releases).

### Full changelog

[CHANGELOG.md](../CHANGELOG.md) on `master`
