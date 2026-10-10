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

**SHA256:** Use the digest shown on the uploaded GitHub release asset, or rebuild the skill ZIP from tag `v2.1.1` and hash it:

```bash
TZ=UTC-3 git -c core.autocrlf=false archive --format=zip -o JAE-v2.1.1.zip v2.1.1
shasum -a 256 JAE-v2.1.1.zip    # Windows: certutil -hashfile JAE-v2.1.1.zip SHA256
```

The asset was replaced on 2026-10-10 with an LF-clean rebuild. The original upload came from a checkout with `core.autocrlf=true`, so every text file had CRLF line endings. Two settings change the digest: `git archive` stamps files with the build machine's local time (the asset was built in UTC+3), and `core.autocrlf` converts line endings. `TZ=UTC-3` is the POSIX spelling of UTC+3 and works without a timezone database. On Windows, set `TZ` for the shell only (`$env:TZ='UTC-3'` in PowerShell, `set TZ=UTC-3` in cmd).
