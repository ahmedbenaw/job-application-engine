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

## Planned for v1.1.0

- Application tracking dashboard (multi-role session management).
- Interview preparation module (Phase 8) triggered from Branch A of Phase 7.
- Offer evaluation module — structured comparison of competing offers across
  compensation dimensions.
- Additional market salary anchors: USA (by state), Canada, Singapore,
  Australia.
- Integration guide for uploading the skill to Claude Projects directly from
  the repository.
