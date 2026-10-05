# Remediation inventory — files and patterns (mandatory traceability)

This list documents the **mandatory** doc and code touch surfaces for the platform-accuracy release.

## New files (mandatory)

| Path | Role |
|------|------|
| `docs/MANDATORY_EXCLUSIONS.md` | Explicit non-features + reasons |
| `docs/platform-capabilities.md` | Canonical Claude / CoWork / Manus / hybrid |
| `docs/REMEDIATION_INVENTORY.md` | This file |
| `docs/EXECUTION_MODES.md` | Dual execution modes; re-anchor; opt-in strings (v2.1.0) |

## Modified files (mandatory)

| Path | Change class |
|------|----------------|
| `SKILL.md` | Manus Skills-first; hybrid labels; A0 `present_files` fallback; CoWork scope; front matter 2.0.x; link exclusions + platform doc |
| `rules.json` | `platform_notes` extended; hybrid keys; exclusions pointer |
| `README.md` | Platform sections; remove brittle file count; Manus Skills; soften claims; link docs |
| `automation-registry.json` | `artifact_policy` / registry-level notes for `present_files` |
| `references/automation-playbooks/document-creation.md` | Fallback pointer to SKILL A0 |
| `references/skill-instructions/checklist-templates.md` | Links to canonical docs |
| `CHANGELOG.md` | Patch entry |

## Grep verification patterns (mandatory post-change)

- Must **not** remain as sole primary: `Manus does not currently support` (unless qualified with Skills primary above it)
- Must **not** overclaim: `full agentic execution capability` without chat-bound qualifier
- Must **not** unqualified: `CoWork routes parallel phases automatically` without skill-authored wording
- Must **not** brittle: `all 20 files`
- `present_files` in `references/` must reference A0 fallback or registry `artifact_policy`

---

## v2.2.0 — CV build, ATS Gate, fallback ladder, hooks, release harness

Design record: `docs/CV_ATS_REQUIREMENTS_SPEC_v0.11.0.md` (Part 7.9 maps every v2.1.1 component to kept / extended / changed / new).

### New files

| Path | Role |
|------|------|
| `references/intake-questionnaire.md` · `cv-build.md` · `ats-gate.md` · `country-profiles.md` · `workflow-integration.md` · `application-log-template.md` | Intake v4, Phase 3B, Phase 3C, country profiles, gates and grades, logs |
| `references/first-use-protocol.md` · `automation-layer.md` · `platform-execution-notes.md` | Moved out of `SKILL.md` (content unchanged unless marked v2.2.0) |
| `references/automation-playbooks/vision-browser-computer-fallback.md` | A18 fallback ladder and visual audits |
| `scripts/ats_gate.py` | Phase 3C counted checks; PASS freeze, upload verify, stale check |
| `scripts/selftest.py` | Release harness (structure, gate, PASS state, hooks, evals, regression checks) |
| `evals/` | 6 test cases, fixtures, `grade.py`, stored test replies (`results/latest/`), README |
| `hooks/` | Opt-in Claude Code hooks, settings snippet, README |
| `docs/CV_ATS_REQUIREMENTS_SPEC_v0.11.0.md` · `docs/REVIEW_v2.2.0.md` · `docs/GITHUB_RELEASE_v2.2.0.md` | Design record, build review, release note |

### Modified files

| Path | Change class |
|------|----------------|
| `SKILL.md` | v2.2.0 workflow (2A, 3B, 3C, M1–M5, combined verdict), 19 invariants, A18, progressive disclosure |
| `rules.json` | `skill.version` and `automation_layer.version` 2.2.0; phase map, gates, invariants, fallback ladder, country profiles, intake |
| `automation-registry.json` | `registry_version` 2.2.0; A04 upload rule; A17; A18 |
| `references/` (10 existing files) | Additive "v2.2.0" sections only |
| `docs/platform-capabilities.md` · `docs/EXECUTION_MODES.md` · `docs/MANDATORY_EXCLUSIONS.md` | Sub-phases and scoring model, A18 scope (section B/C), hooks (section F), Claude Code section |
| `README.md` · `CHANGELOG.md` | v2.2.0 narrative, diagram, tables, structure, install links |

### Grep verification patterns (mandatory post-change)

- Must **not** remain outside history (`CHANGELOG.md`, old release notes) and compatibility statements ("A01–A16 … still work"): `A01–A16` as the full automation list, `16 declared`, `16 Registered`, `releases/tag/v2.1.1` in install links
- Must **not** appear in `SKILL.md`, `rules.json`, `automation-registry.json`, `references/`: a vendor browser brand as an execution path (`Chrome`) — checked by `scripts/selftest.py`
- All version fields must agree (`SKILL.md` metadata, `rules.json` `skill.version` and `automation_layer.version`, `automation-registry.json` `registry_version`) — checked by `scripts/selftest.py`
- `python3 scripts/selftest.py` must pass 100%; `python3 evals/grade.py <iteration>` must report `with_skill` 100%
- Test replies (`evals/results/latest/`, or a fresh run with `selftest.py --replies <iteration>`) must not name a browser or app brand or say "on your computer" — checked by `scripts/selftest.py`
- Frontmatter `name` and `version` are read as values, so quotes added by an installer don't fail the self-test
