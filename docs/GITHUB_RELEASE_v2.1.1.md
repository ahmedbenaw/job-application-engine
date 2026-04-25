## v2.1.1 — Repo audit reconciliation and release alignment

See [CHANGELOG.md](https://github.com/ahmedbenaw/job-application-engine/blob/master/CHANGELOG.md) section **[2.1.1]** for the full list.

### Highlights

- **Full repo audit pass:** cross-file invariants re-checked across `README.md`, `SKILL.md`, `rules.json`, `automation-registry.json`, and docs.
- **Diagram reconciliation:** README legend now matches runtime node semantics (automation/runtime nodes include MCP discovery and fallback nodes, not only Tier 3 actions).
- **Metadata normalization:** version fields aligned to **2.1.1** across skill/rules/registry/readme.
- **Release alignment:** clean patch release to keep tag, notes, and asset synchronized.

### Install

**Claude.ai / Claude CoWork** — **Customize → Skills → Create Skill → Upload ZIP**.  
**Manus** — **Skills** upload or **Import from GitHub** → `https://github.com/ahmedbenaw/job-application-engine`

### Asset

Download **`JAE-v2.1.1-Generic-Universal-2026-04-25.zip`** from Assets (flat repo root for Skills upload). Built with `git archive` from tag `v2.1.1`.

**SHA256:** Use the digest shown on the uploaded GitHub release asset, or reproduce locally with `git archive --format=zip v2.1.1` and `certutil -hashfile` / `shasum -a 256`.
