## v2.1.0 — Dual execution modes, A14–A16, policy alignment

See [CHANGELOG.md](https://github.com/ahmedbenaw/job-application-engine/blob/master/CHANGELOG.md) section **[2.1.0]** for the full list.

### Highlights

- **Execution modes (Claude CoWork):** default **`agent_supported`**; optional **`cowork_autonomous`** with per-chunk **A14** (host execution, Tier 2, `APPROVE COCHUNK`) then **A15** re-anchor and **A16** drift/scope check — eight-phase law and Tier 3 submit/send are unchanged.
- **Docs:** [docs/EXECUTION_MODES.md](EXECUTION_MODES.md), reframed [MANDATORY_EXCLUSIONS.md](MANDATORY_EXCLUSIONS.md), [platform-capabilities.md](platform-capabilities.md) execution-mode section.
- **Machine-readable policy:** [rules.json](../rules.json) `execution_modes`; [automation-registry.json](../automation-registry.json) `registry_version` **2.1.0**; **16** automations **A01–A16**.
- **README:** workflow diagram includes execution-mode gate before A0; install links **v2.1.0**.

### Install

**Claude.ai / Claude CoWork** — **Customize → Skills → Create Skill → Upload ZIP**.  
**Manus** — **Skills** upload or **Import from GitHub** → `https://github.com/ahmedbenaw/job-application-engine`

### Asset

Download **`JAE-v2.1.0-Generic-Universal-2026-04-25.zip`** from Assets (flat repo root for Skills upload). Built with `git archive` from the tagged tree.

**SHA256:** Use the digest shown on the uploaded GitHub release asset, or rebuild the skill ZIP from tag `v2.1.0` and hash it:

```bash
TZ=UTC-3 git -c core.autocrlf=false archive --format=zip -o JAE-v2.1.0.zip v2.1.0
shasum -a 256 JAE-v2.1.0.zip    # Windows: certutil -hashfile JAE-v2.1.0.zip SHA256
```

The asset was replaced on 2026-10-10 with an LF-clean rebuild. The original upload came from a checkout with `core.autocrlf=true`, so every text file had CRLF line endings. Two settings change the digest: `git archive` stamps files with the build machine's local time (the asset was built in UTC+3), and `core.autocrlf` converts line endings. `TZ=UTC-3` is the POSIX spelling of UTC+3 and works without a timezone database. On Windows, set `TZ` for the shell only (`$env:TZ='UTC-3'` in PowerShell, `set TZ=UTC-3` in cmd). **SHA256 of the ZIP attached to this GitHub release:** `98401725508bd231fd17c6ca867565215e511a0d7da917b275562b0017e73ca1` (the original CRLF upload was `368f755e35faeea2297fe063423fca9d7ab9c504f2ee583a256595e3758a9d5e`).
