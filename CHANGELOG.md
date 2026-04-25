# Changelog — Job Application Engine

All notable changes to this project are documented in this file.
Format: [Version] — Date | Summary of changes

---

## [2.0.0] — 2026-04-24 | Automation Layer Added — Additive to v1.0

### Architecture
All v1.0 workflow phases, gates, and invariants unchanged. The automation
layer is purely additive — mapped onto the existing 8-phase structure at
specific trigger points within each phase.

### Added — Core automation infrastructure
- Capability Detection Protocol (A0): runs at session start before Phase 0,
  probes all tools and MCP connections, builds and presents a live Capability
  Map. User acknowledges before Phase 0 begins.
- Automation Recommendation Protocol: inline recommendations at 7 phase
  trigger points (Phases 0, 1, 3, 4, 6, 7). Max 2 recommendations per phase.
  Always shows manual fallback alongside every automation option.
  Inactive automation recommendations include MCP connection instructions.
- Consent Gate Protocol: three tiers — Tier 1 (read-only, auto-execute),
  Tier 2 (reversible write, APPROVE [ACTION_NAME]), Tier 3 (irreversible
  write, APPROVE [SPECIFIC_PHRASE]). Approval and scoring are explicitly
  separate systems and must never be conflated.
- Browser Automation Protocol: BrowserBase MCP as primary path, Playwright
  MCP as secondary with user disclosure and complexity explanation for
  non-technical users. Fallback to pre-staged manual answers when both
  unavailable. Failure handling stops immediately and switches to manual.
- Email Selection Protocol: always ask user which email MCP to use, never
  assume, never hardcode. Store SESSION_EMAIL_CHOICE for current session only.
  Ask fresh each session.
- Document Storage Protocol: local download via present_files always first.
  Cloud save offered separately after local download. User selects provider.
  Folder path suggested and confirmed before save.
- Platform-aware execution routing: Tier 1 actions parallel in CoWork,
  all Tier 2 and Tier 3 actions sequential in main thread on all platforms.
  Irreversible actions never dispatched to subagents.

### Added — New files
- automation-registry.json: 11 declared automations (A01–A11) with scope,
  tool requirements, consent tier, approval phrase, reversibility, fallback,
  and boundary conditions. Scope lock — only registered automations may fire.
- references/automation-playbooks/job-board-access.md: platform-specific
  fetch strategies for 9 job boards, search query construction, top-5 fetch
  protocol, exclusion filter application.
- references/automation-playbooks/application-filling.md: 3-stage protocol
  (form fetch, browser field fill, submission). Platform strategies, field
  map construction, BrowserBase/Playwright selection, failure handling,
  pre-staged manual fallback, Playwright complexity disclosure for
  non-technical users.
- references/automation-playbooks/email-actions.md: external email to
  hiring manager (A08, Tier 3 APPROVE SEND) and confirmation email to self
  (A11, Tier 2 APPROVE SEND). Email selection protocol, draft construction
  rules, scope boundary.
- references/automation-playbooks/document-creation.md: cover letter DOCX
  (A06), full package document (A07), cloud save (A09). Mandatory local-first
  storage sequence, provider selection, folder path protocol, naming convention.

### Modified — Existing files (additive only)
- SKILL.md: Automation Layer section appended before Invariants. Six inline
  modules added: Capability Detection, Automation Recommendations per phase,
  Consent Gate Protocol, Browser Automation Protocol, Email Selection,
  Document Storage, Platform-Aware Routing.
- rules.json: automation_layer block appended. Contains capability_detection,
  consent_tiers, browser_automation, email_selection, document_storage,
  automation_recommendations, platform_routing, and automation invariants.

### Automation invariants added
- Never trigger automation outside automation-registry.json scope
- Never conflate approval with scoring
- Never store credentials across sessions
- Never auto-resubmit after browser failure
- Never save to cloud without Tier 2 consent
- Never send external email without Tier 3 approval
- Never submit application without Tier 3 approval
- Never assume email provider — always ask
- Always present local download before cloud save option
- Always show Capability Map at session start
- Always provide manual fallback alongside automation option

---

## [1.0.0] — 2026-04-24 | Generic Universal Edition — Initial Release

### Added
- Full 8-phase workflow: Job Discovery, Company Intelligence, Fit Analysis,
  Clarifying Intake, Application Package Production, Writing Quality Pass,
  Governance Gate, Post-Submission Loop.
- 7-level Job Classification Framework with auto-detection from JD scope,
  self-identification prompt, startup and enterprise calibration rules, and
  level-to-strategy mapping for salary, tone, and evidence selection.
- Dynamic session checklist with live status board, scoring gates at every
  phase, and revision loop for scores below 5.
- Fit Analysis module (Phase 2): adversarial two-column gap mapping, three
  verdicts (Clean Fit / Honest Stretch / Mismatch), Mismatch hard halt,
  compensating evidence protocol, session gap statement to log only.
- Writing Quality module (Phase 5): 25 AI-writing pattern categories across
  five families — significance inflation, promotional language, structural
  AI patterns, voice and attribution patterns, technical AI tells. Two-pass
  internal audit loop. Final version only — draft never presented.
- Governance Gate module (Phase 6): eight sequential checks covering field
  completeness, claim traceability, salary format, gap acknowledgment, token
  resolution, word count, portfolio URL validity, and salary field type.
- Dynamic Applicant Profile template with full field taxonomy: static fields,
  dynamic fields (positioning headline, professional summary, tools stack, key
  evidence catalogue, language proficiency, availability, relocation status,
  compensation preferences, portfolio assets, sector targeting, target seniority
  level), salary architecture (multi-market, multi-currency, day rate model,
  equity fields, offer history log), field dependency map, conflict resolution
  rules, and per-field review cycles.
- Both canonical cover letter templates reproduced in full with structural
  annotations, a mixing guide, level-specific tone adjustments, and ten
  quality rules enforced at Phases 5 and 6.
- Salary anchors template with confirmed market entry format, regional
  take-home reference rates for eight markets, multi-currency handling rules,
  fractional day rate conversion, and offer history log.
- Excluded companies and application outcomes log with exclusion protocol and
  update instructions.
- Job Level Classification Framework as a standalone reference file.
- Four skill-instruction reference files: fit-analysis.md, writing-quality.md,
  governance-gate.md, checklist-templates.md.
- rules.json: machine-readable workflow encoding compatible with Claude.ai,
  Claude CoWork, and Manus.
- README.md: platform-specific setup and usage instructions for Claude.ai,
  CoWork, combined workflow, and Manus.
- First-Use Setup Protocol for candidates initialising the profile for the
  first time.
- Phase 0 cold-start branch for sessions without a prior anchor role.
- Phase 1 platform-aware form-fetch strategy with per-platform instructions
  and fallback for template-variable rendering.
- Hiring manager identification step in Phase 1 — cover letters always
  addressed to a named person where one can be found.
- Phase 7 three-branch post-submission handling: successful submission,
  withdrawal before submission, rejection after submission.
- All invariants are structural (no candidate-specific data in the invariants
  section).
- MIT licence.

### Architecture decisions
- All agent logic nativized: no external skill files, agents, or frameworks
  required. The skill operates as a standalone package.
- Placeholder tokens ([CANDIDATE_NAME], [COMPANY_A], [ROLE_TITLE], etc.)
  used throughout alongside fictional Alex M. examples to constrain LLM
  output and prevent hallucination in unfilled fields.
- Session log is separate from the Applicant Profile. Gap statements, cover
  letter drafts, and application outcomes are session outputs — they do not
  overwrite the candidate's permanent profile data.

---

## Session Entry Gate — Additive patch to v2.0.0

### Problem resolved
The skill previously had a single linear entry path (Mode A — discovery)
with no mechanism to detect or handle the most common real-world session
start: a user uploading their CV and providing a specific job URL. Phase 0
(discovery) would run even when the user already had a role in mind. The
cold-start branch asked "what role type and geography?" even when a job
URL was already in the session.

### Added — Session Entry Gate (SKILL.md)
A routing gate that runs after A0 Capability Detection and before any phase.
Detects the session mode automatically from session signals. Routes Mode A
sessions to Phase 0. Routes Mode B sessions directly to Phase 1 with Phase 0
marked as Skipped.

Mode A — Job Discovery: triggered when no file is uploaded and no job URL
is provided. User states a target role, sector, geography, or seniority.
Proceeds to Phase 0 as before.

Mode B — Direct Application: triggered when the user uploads a CV and
provides a job URL or JD text, or when any of: "apply for this", "I found
a job", "I want to apply to [role/company]", a job URL, or JD text appears
in the opening message. Phase 0 is skipped entirely. The CV is fed into
the First-Use Setup Protocol Step 0 extraction and the job URL is fed into
Phase 1 Company Intelligence simultaneously. All subsequent phases run
identically in both modes.

Ambiguous signal handling: if the mode cannot be determined from session
signals, the skill presents both options explicitly and waits for the user
to choose before proceeding.

### Added — Mode B intake prompt (SKILL.md)
Structured prompt requesting CV upload and job URL if either is absent when
Mode B is detected but one of the two required inputs is missing.

### Added — Mode B checklist display (SKILL.md)
Phase 0 shows ✅ Skipped with "Mode B" label in Mode B sessions.

### Updated — Phase 0 (SKILL.md)
Section now opens with "MODE A ONLY" constraint. Cold-start branch updated
to include explicit instruction not to fire in Mode B sessions.

### Updated — SKILL.md description block
Now describes both session modes. Trigger language updated to include CV
upload, job URL paste, and "I want to apply to [company]" as explicit
triggers alongside the existing discovery-mode triggers.

### Updated — SKILL.md body title
Removed stale "v1.0" version label from the document body title.

### Updated — rules.json
session_entry_gate block added with mode_a and mode_b signal arrays,
entry_phase routing, parallel_intake spec for Mode B, and ambiguous_signal
handling. Phase 0 trigger updated to session_entry_gate_routes_mode_a and
mode field set to mode_a_only. cold_start note updated to include Mode A only constraint.

### Updated — README.md Quick Start
Now shows both entry modes with concrete example phrases and file upload
instruction for Mode B.

---

## Planned

- Application tracking dashboard (multi-role session management).
- Interview preparation module triggered from Phase 7 Branch A.
- Offer evaluation module — structured comparison of competing offers.
- Additional salary market anchors: USA (by state), Canada, Singapore, Australia.
- Mode B enhancement: structured resume parser returning a scored diff
  against the JD before Phase 2 runs, surfacing gaps earlier.
- Multi-role Mode B: user uploads one CV and provides multiple job URLs
  in one session, skill queues them and runs each through Phases 1–7 sequentially.
