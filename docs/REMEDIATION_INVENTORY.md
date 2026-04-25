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
