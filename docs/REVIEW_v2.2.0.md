# v2.2.0 Build Review

How version 2.2.0 was built and checked, and what each review step changed.

## 1. Build guides (skill-creator, skill-development)

- Kept the skill name `job-application-engine` (this is an update, not a new skill).
- Moved long sections out of SKILL.md into `references/` so it loads less at once: first-use protocol, automation layer, platform notes. Their content is unchanged.
- Non-standard frontmatter keys moved under `metadata` so the package validates.
- Bundled `scripts/ats_gate.py` because the test runs showed models rewriting the same checker every time.
- Packaged with `evals/` inside, on request. (skill-creator's packager leaves `evals/` out by default, so the package was built with the same rules minus that one, then verified from a clean extract: self-test 45/45, 90/90 after the release audit in sections 8–9.)

## 2. Test runs (skill-creator)

4 test cases, run on v2.2.0 and on v2.1.1. Viewer: `jae-v2.2.0-eval-review.html`. Grader: `evals/grade.py`. Release bar: 100%.

| Test | v2.1.1 | v2.2.0 round 1 | v2.2.0 final (round 7) |
|---|---|---|---|
| CV + job ad, new person | 2 of 6 | 5 of 6 | 6 of 6 |
| Flawed CV file through the ATS test | 4 of 8 | 8 of 8 | 8 of 8 |
| Student with no CV | 2 of 5 | 4 of 5 | 5 of 5 |
| Job page that won't load (new) | 5 of 6 | — | 6 of 6 |
| **Total** | **17 of 25 (68%)** | **17 of 19 (89%)** | **25 of 25 (100%)** |

What each round fixed:

1. **Round 1–2:** first message asked 27–28 questions (now at most 10, INQ-09); "Shall we begin?" clashed with reading the CV at once; no CV and no link gave mixed signals (now Mode A).
2. **Round 3:** the ATS test was right but never said "nothing was uploaded". Added the side-effects line. Testers also found that a saved gate report couldn't be re-read to freeze a PASS.
3. **Round 4–6:** testers found 10 more gate-script bugs (entity decoding, fonts set by styles, white text, duplicate headings, verdict vs grade, exit code, missing inputs, size limit level, "I/O" as a pronoun, PDF alone hides tables). All fixed, each with a regression check in `scripts/selftest.py`.
4. **Round 7:** all 4 tests rerun on the final build: 25 of 25.

Self-test: 45 of 45 at round 7; 90 of 90 after the release audit (sections 8–9). One open design question went to the spec owner (Q-19: with few must-have keywords, one honest gap makes 90% impossible).

## 3. Skills QA (legal-builder-hub:skills-qa)

- **Injection scan:** nothing found. No override or authority text, no hidden Unicode, no encoded content, no config writes, no credential requests. URLs point only to the project repo and Anthropic product and docs pages.
- **Trust surface:** no MCP declarations. Two optional Claude Code hooks (section 5): each runs a local Python script, reads only the hook input and the PASS state file, writes only that state file, and makes no network calls. `scripts/ats_gate.py` runs only local document tools (pdftotext, pdffonts, pdfimages, pdftoppm) on files the person provides. The fallback ladder (A18) uses browser and computer control only under the existing consent tiers; the person logs in themselves.
- **Fixes applied:** freshness fields added (last_verified, freshness_window, freshness_category, verified_against); an owner and review trigger declared; a confidence rule added (label uncertain facts "unconfirmed" and ask).
- **Not legal advice:** the scope section says the skill gives no legal, immigration or tax advice. Privilege doesn't apply. The person decides at every gate.
- **Overlaps:** this skill shares triggers with the personal edition (if installed), pm-toolkit's review-resume and tailor-resume, and the Claude Project Kit's /resume. Install one engine edition per account to avoid both firing.
- **Verdict:** Ready for piloting. The only open item is checking the country profiles against local sources (GAP-07).

## 4. Kaizen

Small fixes, one at a time:

- The script refuses to start without files (fail fast, GATE-01).
- The read test and coverage no longer "pass" when they had nothing to compare; that now lowers the grade.
- The script exits quietly when its output is piped.

Nothing speculative was added.

## 5. Hooks (plugin-dev:hook-development, hookify:configure)

- **Added, opt-in.** `hooks/hooks.json` (plugin format) and `hooks/settings-snippet.json` (settings format).
  - **PreToolUse, upload tools:** `pre_upload_guard.py` blocks (exit 2) any CV file that isn't the fingerprinted file from the latest ATS Gate PASS for that job (GAP-11, GATE-14). Non-CV files pass through.
  - **PostToolUse, Write/Edit/Bash:** `post_change_stale.py` cancels a PASS whose file bytes changed and tells Claude why. Never blocks.
- **Where they run:** Claude Code only, installed as a plugin (`job-application-engine-plugin.zip`) or through the settings snippet. A `.skill` upload in Claude.ai, CoWork or Manus doesn't run hooks; there the same rules hold as instructions (invariant 15 and GATE-14).
- **Checked:** schema validation and hook linter passed; behaviour covered by 5 self-test checks.
- **hookify:** no hookify rules exist in this workspace, so there was nothing to configure.

## 6. Automation recommendations (claude-automation-recommender)

For people maintaining this skill in Claude Code (optional, not shipped):

| Type | Recommendation | Why |
|---|---|---|
| Hook | After edits to SKILL.md, rules.json, automation-registry.json or scripts: run `quick_validate.py`, a JSON check and `python -m py_compile scripts/ats_gate.py` | Catches broken packages before release |
| Subagent | A spec-sync reviewer that checks every spec ID used in SKILL.md and references still exists in the spec | Keeps the design record and the skill aligned |
| MCP | GitHub MCP | The project is a public GitHub repo with releases |
| MCP (for end users) | A browser automation MCP (Playwright) | Powers the optional ATS-parsing preview in GATE-18 |

## 7. Installer pre-check (legal-builder-hub:skill-installer)

Pre-install review only. Nothing was installed in the build environment.

- Allowlist: none configured; first-party build.
- License: MIT. The LICENSE file matches the frontmatter.
- Freshness fields: valid shapes. `verified_against` is empty on purpose, because the country profiles are still waiting on their local check.
- Hooks: 2, opt-in, Claude Code plugin only (section 5). MCP servers: none. Writes outside the skill folder: only the PASS state file (`jae-state/gate_pass.json`, or `$JAE_STATE_DIR`).
- Install: upload the `.skill` file in the Claude app (Customize → Skills). The app shows the full file before you confirm.

## 8. Release audit against the repo's own docs

Before publishing, the build was checked against the repo's normative docs (`docs/platform-capabilities.md`, `docs/MANDATORY_EXCLUSIONS.md`, `docs/EXECUTION_MODES.md`, `docs/REMEDIATION_INVENTORY.md`).

| Found | Fix | Now checked by |
|---|---|---|
| A18 named a vendor browser product as an execution path (MANDATORY_EXCLUSIONS section D) | Browser order follows the registry: BrowserBase, Playwright, then a host-reported browser tool from the Capability Map | `selftest.py` — no vendor browser brand in skill files |
| `rules.json` `automation_layer.version` still said 2.1.1 | Set to 2.2.0 | `selftest.py` — all four version fields agree |
| Platform and scope docs still described "a scoring gate every phase" and had no rule for A18 or hooks | Updated platform-capabilities, EXECUTION_MODES, MANDATORY_EXCLUSIONS (sections A, B, C, new F), REMEDIATION_INVENTORY | Grep patterns in REMEDIATION_INVENTORY |

| The release-build eval run found that `record-pass` could freeze a file without a gate report, or a file the PASS report never tested, which would let `verify-upload` approve an untested CV | First fix required the report; replaced by the stronger fix below (`record-pass` re-runs the gate itself) | `selftest.py` — 2 new checks |

| A second release-build run of test 2 found 4 more: line breaks inside a paragraph glued words and hid keywords; the read test passed with nothing to compare; `fingerprint` and `render` exited 1 on success; a missing approved CV text silently fell back to loose keyword matching | Fixed; the last one is now a visible warning | `selftest.py` — 4 new checks |

| A third run of test 2 and a dedicated adversarial review of the gate script found 5 + 12 more ways a bad CV could pass or the wrong file could be uploaded (renamed XML prefix, decoy document part, embedded documents, hand-written reports, unverifiable or oddly named CV paths, shell uploads, invisible PDF text, silent PDF checks, renamed header and comment parts, style inheritance, frames and moves, hygiene word gaps) | All fixed. `record-pass` now re-runs the gate itself from a config that names the job | `selftest.py` — one check per bypass |

Known limits, stated in `hooks/README.md` and the spec: PDF white or tiny text is caught by the DOCX/PDF word match and the visual review (GATE-18), not per character; a CV renamed without "CV"/"resume" in its name isn't recognised by the hook (A17 always names it); uploads through page scripts or computer-use dragging aren't intercepted by hooks.

| The final run of test 2 found 2 more: the upload hook accepted a CV that passed for a different job, and a changed keyword list didn't cancel a PASS | Uploads are checked against the job in progress; a changed keyword list cancels the job's PASS | `selftest.py` — 8 new checks |
| The eval password check flagged "I never type your passwords" as asking for one | The check now ignores negated statements | `evals.json` (verified against 5 sample sentences) |

| The last run of test 2 hit two usability snags: `all` crashed when keywords were given as a file path, and its saved output wasn't pure JSON | `all` accepts a keywords file; `--out` writes a pure-JSON report | `selftest.py` — 2 new checks |

All 4 evals were re-run on the final release build: 25 of 25 (100%). Self-test after the audit: 85 of 85.

## 9. Two late fixes (owner request)

| Fix | What changed | Checked by |
|---|---|---|
| Self-test read `name` and `version` as raw text | Installers add quotes (`name: "job-application-engine"`, `version: '2.2.0'`), which failed 2 checks. They are now read as values. SKILL.md quoting is unchanged | Self-test run on the build and on copies with double, single and mixed quotes (all pass); a new check parses quoted and unquoted samples |
| Capability wording (generic edition only) | Replies name no browser, browser-automation or desktop-app brand, never say "on your computer", and promise nothing the A0 Capability Map doesn't show as ACTIVE. Form filling: "I can fill the form if you approve each step" only with browser control; otherwise "I'll give you answers to paste" | 2 new evals (browser control inactive and active); every eval checks the wording; the self-test scans the stored replies. The first run caught the inactive reply offering filling "if browser control gets connected" — the rule now also bans that, and the rerun passed. The final run's form-filling reply ran the tested-file check and said so in plain words ("the exact one that passed the ATS Gate"); the eval's pattern was widened to accept that wording |

Final run on the release build: 6 tests, 40 of 40 (100%); v2.1.1 scores 24 of 40. Self-test: 90 of 90.
