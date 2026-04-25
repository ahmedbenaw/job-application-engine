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

**SHA256 (git archive, tag `v2.1.0`, last computed):** `6d28fa7e351194637cddb710da63db6e952330f2dd06fc654fe062cadb066b5b` — the digest changes if this file is edited; verify with `git archive v2.1.0` and `certutil -hashfile` (Windows) or `shasum -a 256` (Unix), or use GitHub’s digest on the release asset.
