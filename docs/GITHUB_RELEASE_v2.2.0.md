## v2.2.0 — CV Build, ATS Gate, intake v4, fallback ladder

See [CHANGELOG.md](https://github.com/ahmedbenaw/job-application-engine/blob/master/CHANGELOG.md) section **[2.2.0]** for the full list. Design record: [docs/CV_ATS_REQUIREMENTS_SPEC_v0.11.0.md](https://github.com/ahmedbenaw/job-application-engine/blob/master/docs/CV_ATS_REQUIREMENTS_SPEC_v0.11.0.md).

### Highlights

- **The engine now builds and tests the CV:** Phase 2A job analysis, Phase 3B CV Build, Phase 3C ATS Gate on the real DOCX/PDF (2-reader read test, layout lint, visual review as ATS and recruiter, must-have coverage ≥ 90%, evidence trace, fingerprint freeze).
- **Only the tested file is uploaded:** Phase 6 combined verdict (Check 9: ATS Gate PASS); A04 verifies the fingerprint before any upload.
- **Fewer stops, nothing hidden:** 5 mandatory 5/5 gates (M1–M5) plus a visible grade with reasons for every other phase; a grade of 3 or lower stops you.
- **Intake questionnaire v4:** first job to executive, any country; at most 10 questions per message; private answers never printed; no government ID numbers.
- **A17 CV export** (Tier 2) and **A18 fallback ladder** (browser use → computer use → vision → ask you) — never lowers a consent tier.
- **Optional Claude Code hooks** that block an untested CV upload and cancel a PASS after an edit.
- **Promises only what the session can do:** no browser or app brand names, never "on your computer" unless that tool is active; "I can fill the form if you approve each step" only with browser control, otherwise "I'll give you answers to paste".
- **Tested:** `scripts/selftest.py` 90/90; evals 40/40 (100%) vs 24/40 for v2.1.1.
- **Fully compatible with v2.1.1:** phase numbers, gate format, consent tiers, A01–A16, execution modes, original invariants (spec Part 7.9).

### Install

**Claude.ai / Claude CoWork** — **Customize → Skills → Create Skill → Upload ZIP**.  
**Manus** — **Skills** upload or **Import from GitHub** → `https://github.com/ahmedbenaw/job-application-engine`  
**Claude Code (optional, hooks)** — install `job-application-engine-plugin.zip` as a plugin, then restart. Use the plugin **or** a Skills upload in one account, not both.

### Assets

1. **`JAE-v2.2.0-Generic-Universal-2026-10-05.zip`** — flat repo root for Skills upload. Built with `git archive` from tag `v2.2.0`.
2. **`job-application-engine-plugin.zip`** — Claude Code plugin: `.claude-plugin/plugin.json`, `hooks/hooks.json`, and the same skill under `skills/job-application-engine/`.

**SHA256:** Use the digest shown on each uploaded GitHub release asset, or reproduce the skill ZIP locally with `git archive --format=zip v2.2.0` and `certutil -hashfile` / `shasum -a 256`.

### Open item

- Spec Q-19 (open): with few must-have keywords, one honest gap makes the 90% coverage rule impossible. Current default: the role is a stop and the person decides.
