# Changelog — Job Application Engine

All notable changes to this project are documented in this file.
Format: Most recent changes listed first within each version.

---

## [2.0.0] — 2026-04-24 | Current version — all patches below are additive

---

### Patch — Job Board MCP Detection + Diagram (latest)

**Added — Job Board and ATS Platform MCP Detection (SKILL.md, A0)**

STEP 1B added to A0: dedicated probe for 10 job board and ATS platform MCPs —
LinkedIn, Indeed, Greenhouse, Lever, Workday, Ashby, Wellfound, SmartRecruiters,
Breezy HR, Recruitee. Each reported as ACTIVE / LIMITED / INACTIVE in the
Capability Map, which now has a dedicated JOB BOARD & ATS PLATFORM MCPs section.

STEP 1C added: MCP Discovery Search fires automatically when all job board MCPs
are INACTIVE. Runs three targeted web_search queries to find available MCPs on
GitHub and npm. Presents results as RECOMMENDED CONNECTIONS below the Capability
Map. Notes clearly that web_search and web_fetch provide full discovery capability
without these MCPs — job board MCPs unlock authenticated features (saved jobs,
Easy Apply, application status tracking) as an enhancement, not a requirement.

STEP 4 updated: prompt changed from "Shall we begin Phase 0?" to "Shall we begin?"
to handle both Mode A and Mode B entry correctly.

**Added — Automations A12 and A13 (automation-registry.json)**

A12 — Job Board MCP Authenticated Search: Tier 1 auto-execute. Uses an active job
board or ATS MCP for authenticated searches, saved jobs, Easy Apply. Fires only when
at least one job board MCP is ACTIVE. Fallback: web_search and web_fetch.

A13 — Job Board MCP Discovery Search: Tier 1 auto-execute. Runs in A0 STEP 1C when
all job board MCPs are INACTIVE. Search and recommendation only — no install or
connection. User action required to connect any recommended MCP.

Out-of-scope additions: auto-installing MCPs; using job board MCPs for submission
(submission always routes through A05 — BrowserBase/Playwright).

**Updated — Workflow Diagram (README.md)**

Removed `%%{init: {'theme': 'dark', ...}}%%`. Diagram renders in GitHub's default
light mode. Changed `flowchart LR` to `flowchart TB` — phases stack vertically,
each displaying as a horizontal row internally. All classDef fills converted to
light-mode colors. Session Entry Gate subgraph added. Job Board MCP Probe and
Recommend MCPs nodes added to A0. Job Board MCP node added to Phase 0. Mode B
direct path from Session Entry Gate to Phase 1 shown explicitly.

---

### Patch — Session Entry Gate (Mode A / Mode B)

**Problem resolved**

The skill had a single linear entry path (discovery only). Users arriving with a
CV and a job URL were forced through Phase 0 discovery even when they already had
a specific role in mind. The cold-start branch asked "what role and geography?" even
when a job URL was already present in the session.

**Added — Session Entry Gate (SKILL.md)**

A routing gate runs after A0 and before any phase. Detects session mode from signals
(uploaded files, URLs, message content). Routes Mode A to Phase 0. Routes Mode B
directly to Phase 1 with Phase 0 marked Skipped. Presents both options explicitly
when the mode cannot be determined from signals alone.

Mode A — Job Discovery: user states a target role, sector, geography, or seniority.
Proceeds to Phase 0. All subsequent phases run as before.

Mode B — Direct Application: user provides a CV and job URL or JD text. Phase 0
skipped entirely. CV fed into First-Use Protocol Step 0 extraction. Job URL fed into
Phase 1 Company Intelligence simultaneously. Phases 1–7 run identically to Mode A.

**Added — Mode B intake prompt and checklist display (SKILL.md)**

Structured prompt requesting CV and job URL if either is absent in Mode B. Phase 0
shows ✅ Skipped with "Mode B" label in the session status board.

**Updated — Phase 0 (SKILL.md)**

Section opens with "MODE A ONLY" constraint. Cold-start branch explicitly restricted
to Mode A — does not fire when a job URL is already present.

**Updated — SKILL.md description block and body title**

Both session modes documented as triggers. Stale "v1.0" label removed from body title.

**Updated — rules.json**

session_entry_gate block added with mode_a and mode_b signal arrays, entry_phase
routing, parallel_intake spec for Mode B, and ambiguous_signal handling.

**Updated — README.md Quick Start**

Shows both modes with concrete example triggers and CV upload instruction for Mode B.

---

### Patch — Document-Aware First-Use Setup Protocol + Per-Application Profile Updates

**Problem resolved**

The First-Use Protocol presented 25 questions with no awareness of uploaded CVs,
LinkedIn URLs, or other documents. Users with a resume in hand were asked to re-type
information that already existed in structured form.

**Rewritten — First-Use Setup Protocol (SKILL.md)**

Five steps replace the single 25-question block.

Step 0 — Document and link detection: runs before any question is asked. Detects
uploaded CVs (PDF, DOCX), LinkedIn URLs, GitHub URLs, portfolio URLs, Behance/Dribbble
URLs, and inline text descriptions. Extracts all recognisable profile fields from each
source. Builds a field map: extracted / partial / not found.

Step 1 — Present extraction results: shows what was found for user confirmation.
User confirms or corrects rather than typing from scratch.

Step 2 — Gap-fill questions: asks only for fields that could not be extracted.
Minimum zero questions (if CV + LinkedIn URL covered everything), maximum 25.

Step 3 — Profile confirmation and scoring gate: complete profile presented for review.
Score of 5 required before the workflow begins. Writes to applicant-profile-template.md.

Step 4 — Returning session staleness check: runs at every session start for existing
profiles. Availability re-confirmed per session. Salary anchors flagged if source date
older than 6 months. Active engagements re-confirmed.

Step 5 — Per-application profile update protocol: runs at Phase 3 and Phase 7.
After Phase 3: flags portfolio URL, salary, availability, language level, and tool
stack differences for APPROVE UPDATE. After Phase 7: logs all outcomes, updates
salary anchors if offer data received, flags recurring rejection gaps for profile
review. Mid-session document uploads trigger Step 0 extraction on the new source.
All profile writes require APPROVE UPDATE (Tier 2).

**Updated — applicant-profile-template.md**

Header updated with HOW THIS PROFILE GETS POPULATED (recommended document sources
and what is extracted from each) and HOW THIS PROFILE GETS UPDATED (update triggers
and APPROVE UPDATE requirement).

**Updated — rules.json**

first_use block replaced with structured 5-step object encoding extraction sources,
stale field rules, and per-application update triggers.

---

## [2.0.0] — 2026-04-24 | Automation Layer — Initial v2.0 release

### Architecture
All v1.0 workflow phases, gates, and invariants unchanged. The automation layer is
purely additive — mapped onto the existing 8-phase structure at specific trigger
points within each phase.

### Added — Core automation infrastructure
- Capability Detection Protocol (A0): runs at session start before any phase begins,
  probes all tools and MCP connections, builds and presents a live Capability Map.
  User acknowledges before proceeding.
- Automation Recommendation Protocol: inline recommendations at 7 phase trigger points
  (Phases 0, 1, 3, 4, 6, 7). Max 2 per phase. Always shows manual fallback.
  Inactive automation recommendations include MCP connection instructions.
- Consent Gate Protocol: three tiers — Tier 1 (read-only, auto-execute), Tier 2
  (reversible write, APPROVE [ACTION_NAME]), Tier 3 (irreversible write, APPROVE
  [SPECIFIC_PHRASE]). Approval and scoring are explicitly separate systems.
- Browser Automation Protocol: BrowserBase MCP as primary, Playwright MCP as secondary
  with user disclosure. Fallback to pre-staged manual answers when both unavailable.
- Email Selection Protocol: always ask user which email MCP to use per session, never
  assume or hardcode. Store SESSION_EMAIL_CHOICE for current session only.
- Document Storage Protocol: local download via present_files always first. Cloud save
  offered separately. User selects provider and confirms folder path before save.
- Platform-aware execution routing: Tier 1 actions may run parallel in CoWork. All
  Tier 2 and Tier 3 actions sequential in main thread. Irreversible actions never
  dispatched to subagents.

### Added — New files
- automation-registry.json: 11 declared automations (A01–A11) with scope, tool
  requirements, consent tier, approval phrase, reversibility, fallback, and boundary
  conditions. Scope lock — only registered automations may fire.
- references/automation-playbooks/job-board-access.md
- references/automation-playbooks/application-filling.md
- references/automation-playbooks/email-actions.md
- references/automation-playbooks/document-creation.md

### Automation invariants
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
  five families. Two-pass internal audit loop. Final version only.
- Governance Gate module (Phase 6): eight sequential checks.
- Dynamic Applicant Profile template with full field taxonomy, salary architecture,
  field dependency map, conflict resolution rules, and per-field review cycles.
- Both canonical cover letter templates with mixing guide, level-specific tone
  adjustments, and ten quality rules.
- Salary anchors template, excluded companies log, job level framework.
- Four skill-instruction reference files.
- rules.json, README.md, MIT licence.
- Phase 0 cold-start branch, Phase 1 platform-aware form-fetch, hiring manager
  identification, Phase 7 three-branch post-submission handling.

### Architecture decisions
- All agent logic nativized — no external skill files or frameworks required.
- Placeholder tokens with fictional Alex M. examples to constrain LLM output.
- Session log separate from Applicant Profile.

---

## Planned

- Application tracking dashboard (multi-role session management).
- Interview preparation module triggered from Phase 7 Branch A.
- Offer evaluation module — structured comparison of competing offers.
- Additional salary market anchors: USA (by state), Canada, Singapore, Australia.
- Mode B enhancement: structured resume parser returning a scored diff against
  the JD before Phase 2, surfacing gaps earlier.
- Multi-role Mode B: one CV, multiple job URLs queued and run sequentially.
