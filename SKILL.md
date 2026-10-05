---
name: job-application-engine
description: |
  Universal end-to-end job application system for any candidate, from intern
  to C-suite, any industry, any country. This skill should be used whenever someone wants
  to apply for a job, find jobs, build or tailor a CV or resume, make a CV pass
  ATS screening, fill a job application, or write a cover letter — even if they
  only paste a job ad or upload a CV. Mode A finds and ranks roles across 10
  platforms. Mode B applies to a specific role from a CV (or a short intake
  questionnaire) plus a job link. Runs scored phases from company research and
  fit analysis through CV building, an ATS test on the real CV file, the
  application package, a combined final check and post-submission tracking,
  with consent-gated automations. Triggers on "apply for this role", "find me
  jobs", "tailor my CV", "make my resume ATS-friendly", "fill this application",
  "write my cover letter", an uploaded CV, or any job URL or job ad text.
compatibility: Claude.ai, Claude CoWork, Manus. Tools - web_search, web_fetch, bash_tool, create_file, present_files. Optional - image viewing and browser or computer control (ATS Gate visual review), job board and ATS MCPs, email, cloud storage, calendar.
metadata:
  version: 2.2.0
  edition: generic-universal
  author: Ahmed Ossama | Product Leader, Builder & Venture Management Architect
  built_on: job-application-engine 2.1.1 (generic-universal)
  design_record: docs/CV_ATS_REQUIREMENTS_SPEC_v0.11.0.md
  last_verified: "2026-10-05"
  freshness_window: 6 months
  freshness_category: procedural
  verified_against: []
  verification_note: Built from CV & ATS Requirements Spec v0.11.0. Country profiles are conventions pending a local check (references/country-profiles.md).
  license: MIT
  owner: job-application-engine maintainers (generic edition)
  review_trigger: every 6 months, any country-profile check, or a GATE-17 outcome review that changes a Default value
  changelog: CHANGELOG.md
---

# Job Application Engine — Generic Universal Edition v2.2.0

A complete job application system with two session entry modes. Core workflow
is in this file. Detailed protocols load on demand from `references/` (see the
Reference Map). The design record is `docs/CV_ATS_REQUIREMENTS_SPEC_v0.11.0.md`.

**What v2.2.0 adds:** the engine now builds and tests the CV itself. A person
fills a short intake form once (or uploads a CV), the engine writes a tailored
CV for each job, tests the real file the way an ATS and a recruiter would, and
uploads only the file that passed.

**What stays the same:** every v2.1.1 phase number, the 5/5 gate format, the
consent tiers and exact approval phrases, automations A01–A16, execution modes
and all 12 invariants.

---

## Session Start Sequence

Run in this order before any phase:

1. **Execution mode gate** — below.
2. **A0 Capability Detection** — `references/automation-layer.md` § A0. Also
   check for a document tool (CV export), text readers (read test) and, when
   available, image viewing plus browser or computer control (visual review).
3. **Profile check** — if a profile exists, run First-Use **Step 4** staleness
   check (`references/first-use-protocol.md`). If none exists, run First-Use
   Steps 0–3 with the intake questionnaire.
4. **Session Entry Gate** — detect Mode A or Mode B and route.

**First turn (one message, so the person isn't stopped twice):**
1. A 3–5 line plain summary of what works in this session (A0). Show the full
   Capability Map only when asked, or when a tool this application needs is missing.
2. What was extracted from any CV, link or text (First-Use Step 1), for confirmation.
3. **At most 10 questions**, only those needed to start this application
   (see "Ask in small batches" below), as one numbered list under the heading
   **Questions for you (N)**, where N is the number of questions, followed by
   "about M more later".
Replying to that message counts as "Begin" for A0 Step 4.

**Phase loop rule:** at the start of every phase, print the status board and
check that phase's automation trigger points in `references/automation-layer.md`.

---

## Reference Map — read only when needed

| File | Read when |
|---|---|
| `references/first-use-protocol.md` | No profile, new CV or link (Steps 0–3); session start (Step 4); after Phases 3 and 7 (Step 5) |
| `references/intake-questionnaire.md` | First-Use Step 2; a new target; an expired field |
| `references/applicant-profile-template.md` | Every session — profile fields and tokens |
| `references/workflow-integration.md` | Scoring model; handoffs between phases; Phase 6 verdict; upload; logs |
| `references/cv-build.md` | Phase 3B; Phase 4 summary |
| `references/ats-gate.md` | Phase 3C |
| `references/country-profiles.md` | Phase 3 profile choice; Phases 3B and 3C |
| `references/job-level-framework.md` | Phase 0 ranking; Phase 2 level; Phase 3 salary; CV and letter tone |
| `references/skill-instructions/*.md` | Status board; Phase 2, 5, 6 detail |
| `references/cover-letter-templates.md` | Phase 4 |
| `references/salary-anchors-template.md`, `references/excluded-companies-log.md` | Phase 3 salary; Phase 0 filtering; Phase 7 logging |
| `references/automation-layer.md`, `references/automation-playbooks/*.md` | A0; before any automation A01–A18 fires |
| `references/automation-playbooks/vision-browser-computer-fallback.md` | A tool is missing or blocked; any visual audit (A18) |
| `references/platform-execution-notes.md` | Platform-specific behaviour |
| `scripts/ats_gate.py` | Phase 3C counted checks; records the PASS and verifies uploads |
| `scripts/selftest.py`, `evals/`, `hooks/` | Maintenance: self-test harness, test cases and grader, optional enforcement hooks |
| `rules.json`, `automation-registry.json` | Machine-readable workflow and automation scope |

---

## Fallback ladder and visual audits (A18)

Never stop just because one tool is missing. Detail:
`references/automation-playbooks/vision-browser-computer-fallback.md`.

1. Connector (MCP) → 2. native tool (web search or fetch, bash) → 3. **browser
use** (read the page in a browser) → 4. **computer use** (open the file or page
in a desktop app on the linked computer) → 5. **vision** (screenshot or render
to an image and read it) → 6. ask the person to paste or upload.

Use the same three abilities on purpose to audit: read a scanned CV, capture
a form that won't fetch, view every CV page as ATS and recruiter (GATE-18),
screenshot filled form pages before submit, and check the portal's preview of
the uploaded CV. Falling back never lowers a consent tier. The person logs in
themselves; never type or store credentials. Each grade line names the rung
used when it isn't 1 or 2.

**Capability wording (what the person is told).** Promise only what this
session can do:

1. **No brand names:** don't name a browser, browser-automation product or
   desktop-app brand to the person. Say "browser control", "a document app",
   "a PDF viewer".
2. **No promises beyond the map:** don't say "on your computer", and don't
   promise an action, unless the A0 Capability Map shows the tool for it as
   ACTIVE. Otherwise say what you will do instead.
3. **Form filling:** say "I can fill the form if you approve each step" only when
   browser control is ACTIVE. Otherwise say "I'll give you answers to paste",
   and don't offer filling as a later or "if connected" option either.

---

## Execution mode gate (run once per session — before A0)

Record the mode on the status board (e.g. `Execution mode: agent_supported`).

- **Claude.ai and Manus:** `agent_supported` only.
- **Claude CoWork:** offer Mode 1 `agent_supported` (default) and Mode 2
  `cowork_autonomous` (opt-in phrase exactly as in `rules.json` →
  `execution_modes.cowork_autonomous.opt_in_phrases_exact`). `JAE MODE:
  AGENT_SUPPORTED` switches back.
- **Mode 2 rule (non-negotiable):** after every autonomous chunk (A14), run
  A15 governance re-anchor and A16 drift check before the next chunk or phase.
  Phases 3B and 3C are covered like every other phase. Details:
  `docs/EXECUTION_MODES.md`.

---

## Scoring, approval and visible grades

Full rules: `references/workflow-integration.md` (RES-11, INT-05).

**Five mandatory gates per application.** Each uses the unchanged v2.1.1 gate
format and needs 5/5. Below 5 reruns the phases that gate covers.

| Gate | After | Covers |
|---|---|---|
| M1 Company brief | Phase 1 | Phase 1 |
| M2 Fit | Phase 2 | Step 2A job analysis + fit analysis |
| M3 Facts | Phase 3 | Phase 3 |
| M4 CV text | Phase 3B | CV build, critique, style pass |
| M5 Package | Phase 5 | Phase 4 package + Phase 5 package pass |

Plus the **one-time setup sign-off** (First-Use Step 3), once per person.

**Complementary scores** for every other phase (0, 2A, CV critique, 3C ATS
Gate, 6 combined verdict, 7): each scores itself 1–5 from its own checks
(5 all pass · 4 Should-level issues only · 3 three or more waivers or warnings
· 1–2 a Must check failed). The person may add a score and a one-line "what
would perfect look like" note at any time before the next mandatory gate.

**Escalation:** a complementary phase becomes a blocking 5/5 gate when its
automatic score is 3 or lower, or when the person scores it below 5.

**Visible grades:** every complementary phase prints one line the moment it
finishes, and the next mandatory gate repeats all lines since the last gate:

```
ATS Gate: 4/5 · 2 warnings: file is 2.4 MB (limit 2 MB), skim test missed the job title. Not stopping.
```

**Side-effects line:** every reply that finishes Phase 3C, 4, 5 or 6, or runs
any automation, ends with one plain line saying what left the session, for
example "Nothing was uploaded, sent or submitted." or "Sent: cover letter to
jobs@example.com (APPROVE SEND given)." The person never has to guess.

**Confidence:** when a fact is uncertain (partly extracted, an unchecked
country-profile rule, a salary from thin data), label it "unconfirmed", say
why, and ask before relying on it. Never present a guess as a fact.

**Approval is separate from scoring.** A score never authorises an action.
Tier 1 runs read-only. Tier 2 needs `APPROVE [ACTION]`. Tier 3 needs the exact
phrase (`APPROVE SUBMIT`, `APPROVE FILL`, `APPROVE SEND`) after a full data
preview. All scores and notes go to the application log (Phase 7).

---

## Status board

Print at the start of every phase. Update after each gate or grade line.

```
╔════════════════════════════════════════════════════════════════════╗
║          JOB APPLICATION ENGINE — SESSION STATUS BOARD            ║
╠════════════════════════════════════════════════════════════════════╣
║  Setup    │ Profile + intake        │ [STATUS] │ Readiness [ /5]  ║
║  Phase 0  │ Job Discovery           │ [STATUS] │ Grade [ /5]      ║
║  Phase 1  │ Company Intelligence    │ [STATUS] │ M1 Score [ /5]   ║
║  Phase 2A │ Job Analysis            │ [STATUS] │ Grade [ /5]      ║
║  Phase 2  │ Fit Analysis            │ [STATUS] │ M2 Score [ /5]   ║
║  Phase 3  │ Clarifying Intake       │ [STATUS] │ M3 Score [ /5]   ║
║  Phase 3B │ CV Build                │ [STATUS] │ M4 Score [ /5]   ║
║  Phase 3C │ ATS Gate                │ [STATUS] │ Grade [ /5]      ║
║  Phase 4  │ Application Package     │ [STATUS] │ —                ║
║  Phase 5  │ Writing Quality Pass    │ [STATUS] │ M5 Score [ /5]   ║
║  Phase 6  │ Combined Final Verdict  │ [STATUS] │ Grade [ /5]      ║
║  Phase 7  │ Post-Submission Loop    │ [STATUS] │ Grade [ /5]      ║
╠════════════════════════════════════════════════════════════════════╣
║  Execution mode : [MODE]        Session mode: [A / B]              ║
║  Awaiting       : [WHAT IS NEEDED FROM THE USER]                   ║
║  Candidate      : [CANDIDATE_NAME]                                 ║
║  Role / Company : [ROLE_TITLE] / [COMPANY_NAME]                    ║
╚════════════════════════════════════════════════════════════════════╝
Status: ⏳ Pending | 🔄 Active | 🔁 Revision | ✅ Complete | ✅ Skipped | 🚫 Blocked
```

Mode B marks Phase 0 `✅ Skipped`. More board rules: `references/skill-instructions/checklist-templates.md`.

---

## First-Use Setup and the intake questionnaire

Follow `references/first-use-protocol.md` exactly. In v2.2.0, Step 2 asks its
questions through the intake questionnaire v4 (`references/intake-questionnaire.md`):

1. **Extract first** (Step 0) from any CV, LinkedIn export, link or pasted text.
2. **Show what was found** (Step 1).
3. **Ask only the gaps** (Step 2), using the questionnaire path chosen by Q0.1:
   first job · career change · returning · experienced · executive. "N/A" is
   always accepted. Never guess a value.
4. **Ask in small batches** (INQ-09): never more than 10 questions in one
   message. First batch = what this application needs now (target, contact,
   eligibility and start date). Ask the rest where it is used: pay and
   format preferences in Phase 3, missing role details and results in Phase
   3B. Experienced people are asked only for gaps their CV leaves.
5. **Sign off once** (Step 3, 5/5) and print the readiness grade.
6. **Keep fresh** (Step 4) using each field's expiry; **update with approval**
   (Step 5, `APPROVE UPDATE`).

Each filled Section 1 (Target) becomes one positioning track with its own base
CV: 2 per person recommended, a 3rd only when targets truly differ. Every
result gets an evidence ID. Fields marked *Private* are never printed on a CV.
Government ID numbers are never collected. Any language other than English or
Arabic is auto-translated from the English master; the person confirms the
English copy of key fields at sign-off.

---

## Session Entry Gate

Runs after A0 and before any phase. Never skip it. Never assume the mode.

**Mode B signals (skip Phase 0):** an uploaded CV, resume or portfolio; a URL
to a job posting or application form (linkedin.com/jobs, boards.greenhouse.io,
lever.co, breezy.hr, careers pages); phrases such as "apply for this", "I found
a job", "help me apply", "fill in this application", a job title plus company,
or a pasted job ad or form.

**Mode A signals (Phase 0):** no file and no job URL; "find me jobs", "search
for roles", "what jobs match my CV", or a general target without a specific
company; "continue" or "next" after a Phase 7 Branch A session.

**No CV and no job link, but "help me apply":** treat as Mode A (discovery)
after setup, and say that pasting a job link switches to Mode B.

**Ambiguous** (for example a CV but no job URL): present this choice.

```
── SESSION START ────────────────────────────────────────────────────
How would you like to begin?

  MODE A — Job Discovery
  I will search 10 platforms for roles matching your profile, rank
  them, and guide the full application for the role you pick.
  → Say "Discover" or describe a target role, city or sector.

  MODE B — Apply to a Specific Role
  Give me your CV (or fill the short intake form) and the job link,
  and I will run the full application for that role.
  → Upload your CV and paste the job URL, or say "Apply".
────────────────────────────────────────────────────────────────────
```

**Mode B intake:** collect (a) a CV as PDF, DOCX or text — or, when the person
has no CV, the intake questionnaire — and (b) the job URL or pasted job ad.
Ask specifically for whichever is missing. Then in parallel: feed (a) into
First-Use Step 0 (or the staleness check if a profile exists), and feed (b)
into Phase 1. Mark Phase 0 `✅ Skipped`. Do not ask Mode A cold-start
questions in Mode B. From Phase 1 onward both modes run identically.

---

## Phase 0 — Job Discovery (Mode A only)

Cold start (no anchor, no stated target): ask for role type, seniority level,
sector and geography; confirm the level with `references/job-level-framework.md`.

Read from the profile: `[TARGET_ROLE_TYPES]`, `[TARGET_SENIORITY_LEVEL]`,
`[TARGET_SECTORS]`, `[PREFERRED_CITIES]`, `[HARD_EXCLUSION_GEOGRAPHIES]`, and
the intake answers Q1.7–Q1.9 and Q3.2 (relocation, sponsorship need).

Search in parallel, applying exclusions before presenting: LinkedIn Jobs |
Indeed | Wellfound | Relocate.me | EuroTechJobs | Greenhouse | Lever |
Breezy HR | Welcome to the Jungle / Otta | RemoteOK. Pass 1: similarity anchor
(role, city, relocation, sector). Pass 2: CV-fit broadened (top skills,
sectors, years, region). Use job board MCPs when A0 found them (A12).

Present `Rank | Company | Role | Level | Location | Relocation | Fit Signal | URL`.
Rank by relocation offered, level match, title match, sector fit. Cap at 20,
flag the top 5. Print the Phase 0 grade line (complementary score).

---

## Phase 1 — Company Intelligence

Run four operations in parallel:

1. **Job posting fetch:** web_fetch the URL, follow redirects, note incomplete rendering.
2. **Application form fetch:** Breezy HR append `/apply` (flag `{{ question.text }}`);
   Greenhouse embed URL or path (custom questions often need pasting); Lever
   append `/apply`; LinkedIn / Indeed are behind login — ask the person to paste.
   Detect the ATS platform for REQ-30 profiles.
3. **Hiring manager:** search `[COMPANY_NAME] [ROLE_TITLE] recruiter OR "hiring manager"`.
   Never use "To Whom It May Concern".
4. **Company and product research:** funding, team, stack, culture, market
   position, a visible product gap. Every fact gets a source and date.

Save the post text, form questions and platform to the handoff record
(`references/workflow-integration.md`, INT-02). Present the brief, then **M1**.

---

## Phase 2 — Fit Analysis (with Step 2A)

Hard gate: no application text before a verdict. Detail:
`references/skill-instructions/fit-analysis.md`.

**Step 2A — Job analysis** (complementary score):
1. Number every requirement; mark must-have or nice-to-have.
2. Build the **locked keyword list**: exact wording, weight by repetition,
   variants and acronym pairs. Every keyword links to its requirement number.
3. Detect the role level (scope and reporting line, not title alone). Flag a
   gap of more than one level from the target.
4. Compare with the track's base keyword list and print the Step 2A grade
   line, for example: "6 of this job's 12 must-have terms are not in your base CV."

**Fit analysis** on the same numbered list (INT-06):
1. Two columns: strong alignment (evidence ID: company + role + outcome) and
   honest gaps. General claims never count.
2. Compensating evidence for each gap, stated next to it, never replacing it.
3. Verdict: **Clean Fit** · **Honest Stretch** (1–2 mandatory gaps with offsets;
   proceed, gap must be acknowledged) · **Mismatch** (2+ mandatory gaps without
   offsets: HALT, inform the person, produce nothing).
4. Start the **gap log** (REQ-39): unproven must-haves and unmet knockouts,
   each under its requirement number, logged once.

Show the Step 2A line and the verdict side by side, then **M2**.

---

## Phase 3 — Clarifying Intake (before any writing)

Present all questions in one block, labelled Critical or Important. Pre-fill
every answer the profile already holds; the person only confirms. Ask again
only for expired or missing fields.

**Critical:** portfolio URL for this role · salary (read `[SALARY_TARGET_[MARKET]]`;
if missing or "prefer not to say", run the salary research below) ·
availability and notice · relocation and in-office days · work permit, visa
and other knockout criteria (REQ-29) · custom questions the form rendered as
template variables · **country profile** for this job
(`references/country-profiles.md`; General International when no profile fits) ·
**positioning source** (RES-10: matching track, else level version, else master).

**Important (when role-relevant):** a project that maps to the main
requirement (tool + measurable outcome) · language level if the ad requires
one · product trial: if the company has a public product, ask the person to
use it for 10–15 minutes and return one specific observation (needed before
the cover letter).

**Salary research protocol:** search `[CITY] [ROLE_TITLE] salary [year] gross`
on Glassdoor, Levels.fyi or similar; take floor (25th), target (50–75th
midpoint) and stretch (90th); apply the market take-home rate from
`references/salary-anchors-template.md`. Levels 0–2 floor to midpoint; 3–4
midpoint to 75th; 5–7 75th to stretch. Fractional day rate = (annual FTE
target ÷ 220) × 1.4. Store multi-currency figures separately and flag the
exchange-rate decision to the person.

Then **M3**. After M3, run First-Use Step 5 (profile update check).

---

## Phase 3B — CV Build

Rules: `references/cv-build.md`. Preconditions (INT-01): fit verdict, gap log,
knockout facts, country profile, positioning source and locked keyword list.

1. **Write** from the chosen base CV: headline mirroring the job title
   (truthful), summary of 3 sentences and at most 60 words, bullets as outcome
   + metric + method (a 4th clause only when it carries a locked keyword),
   bullets ordered by relevance, 8–12 skills in the ad's exact wording (each
   proven in a bullet), length and section order from the country profile.
   Add a keyword only when the record proves it; otherwise it stays in the gap log.
2. **Critique** against one rubric (REQ-38): each rule pass or fail with a
   quote and a fix. Score = rules passed. Print the critique grade line.
3. **Style pass** (Phase 5 rules, `references/skill-instructions/writing-quality.md`)
   with the locked keywords protected: those terms never change (INT-03).

Present the CV text and the critique, then **M4**. At M4, ask for
`APPROVE CREATE` (A17). One approval per application covers every export and
re-test for this job, unless the person chose to approve every export.

---

## Phase 3C — ATS Gate

Rules and order: `references/ats-gate.md`. Countable checks:
`python scripts/ats_gate.py --help`.

1. **Export** DOCX (main) and text-based PDF from the same text, single column,
   no tables, text boxes, images or header/footer text (A17).
2. **Layout lint** — counts must be zero.
3. **Read test** — 2 text readers as standard (1 minimum, flagged): every
   critical field (name, contact, titles, companies, dates, headings) must
   come out exactly right.
4. **Visual review as ATS and recruiter** (GATE-18) — view each page as an
   image; check reading order, overlaps, cut-off text; do the 6–10 second skim.
   When tools allow, open the file in a CV-parsing preview read-only. Uploading
   to any outside site is Tier 2 and needs approval; never use an employer's
   live form for testing.
5. **Locked-keyword integrity**, **coverage** (must-have ≥ 90%, each keyword at
   most 4 times, about 3 normally), **evidence trace**, **knockout alignment**,
   **content hygiene**, **platform profile** (2 MB max when unknown),
   **country profile**, **skim test**.
6. **Report** one verdict: PASS · PASS WITH WAIVERS (only Should-level checks)
   · FAIL. Print the gate grade line, then the side-effects line. Save the
   report with `ats_gate.py all [CONFIG] --out gate_report.json` in the
   evidence pack (GATE-16).
7. **Retries:** normal issues get 1 automatic retry; major issues up to 5,
   decided by retry points (ats-gate.md, GATE-15). Stop and ask when a fix
   needs new facts or two tries make no progress. Rerun from check 0.
8. **Freeze** on PASS: run `scripts/ats_gate.py record-pass --job [JOB_ID]
   --config [gate config with "job": "[JOB_ID]"]`. It re-runs every counted
   check itself and saves the fingerprints only on PASS, so a report can't be
   typed in by hand. The PASS belongs to that job and its keyword list: a
   changed keyword list cancels it, and a CV passed for another job is refused. A PASS WITH WAIVERS is frozen only after the person accepts each
   waiver, by adding `--waived`. Any later edit cancels the PASS (the optional
   hooks in `hooks/` enforce this in Claude Code).

---

## Phase 4 — Application Package Production

Confirm Phase 3 critical gates and an ATS Gate PASS before writing.

**Standard form fields** from the profile: `[CANDIDATE_NAME]`, `[EMAIL]`,
`[PHONE]`, `[LINKEDIN_URL]`, `[SALARY_TARGET_GROSS]`, `[PORTFOLIO_URL]`. Flag
any missing confirmed value.

**Experience summary:** derive from the CV summary (GAP-12): shorten, never
add claims; keep locked keywords.

**Cover letter** — `references/cover-letter-templates.md`: addressed to the
named hiring manager (fallback "Dear [HIRING_MANAGER_TITLE]:" or "Dear Hiring
Team:"); why this role and company; 1–2 evidence examples with metrics; the
person's product observation; one gap sentence plus compensating evidence for
every Honest Stretch (from the gap log); a committed close with a dated
follow-up ("I'll follow up on [date]"). Prohibited: "To Whom It May Concern",
"I look forward to your reply", "I look forward to hearing from you". Word
limits: email or online 250 · text box 450 · document 500. Tone by level:
0–2 enthusiastic and specific; 3–4 direct and evidence-led; 5–7 strategic
and outcome-at-scale.

**Custom question answers:** print the exact question above each answer.
Every claim traces to the profile or a Phase 3 answer.

---

## Phase 5 — Writing Quality Pass

Apply `references/skill-instructions/writing-quality.md` (25 pattern families,
two internal passes) to the package. Present only the final version, never
the draft. The locked keyword list is passed in and those terms are never
changed (INT-03). Then **M5** (covers Phases 4 and 5).

---

## Phase 6 — Combined Final Verdict

Detail: `references/skill-instructions/governance-gate.md` and INT-04.
One report covering CV and application:

1. The eight governance checks (third-party completable · claims trace ·
   salary as one gross figure in local currency · gap acknowledged in the
   letter and the "why suitable" answer · no placeholders · word limit ·
   valid portfolio URL · numeric salary field).
2. **Check 9:** the ATS Gate verdict is PASS or PASS WITH WAIVERS for this job.
3. Public-profile consistency (titles, companies, dates match LinkedIn).
4. Every gap-log entry has a handling decision.

Claim tracing runs once (ATS Gate GATE-07) and is reused. Show the most
important failure first. Print the verdict grade line. On FAIL, return to
Phase 4 (or Phase 3B if the CV is the cause).

**Fill and submit** (A04 / A05, Tier 3): only after a PASS and the exact
phrase after a full preview. **Upload only the fingerprinted file(s) from the
latest ATS Gate PASS for this job**: run `scripts/ats_gate.py verify-upload
--job [JOB_ID] [FILE]`; stop on any mismatch (GAP-11). After upload, check
the portal's preview of the parsed CV by eye (A18). DOCX is the main file; add
the PDF when the portal accepts two files.

---

## Phase 7 — Post-Submission Loop

**Branch A — submitted:** use the role as the anchor and return to Phase 0
for the next 5 ranked roles.
**Branch B — withdrawn:** log it, ask the reason, re-weight the next search.
**Branch C — rejected:** log it, name the mandatory requirement it most likely
reflects (from Phase 2 gaps), ask whether to adjust level, sector or emphasis.

**In all branches:**
1. Write the **application log** (GAP-13): job, level, track, CV fingerprint,
   gate verdict, coverage, fit verdict, waivers, every score and note, date
   sent, outcome. Same `APPROVE UPDATE` rule as the excluded-companies log.
2. Set the **follow-up window** from the company research: 7 days (fast-moving
   employers), 14 (most companies), 21 (large corporate, public sector,
   government). 21 is the maximum; the person can shorten it.
3. **Interview prep** (GAP-14) when an interview is booked: honest answers for
   each gap, a 60–90 second story for each lead result, one-line answers for
   knockout facts. A short prep sheet at submission only on request and approval.
4. Append to `references/excluded-companies-log.md`; update salary anchors
   when offer data arrives; run First-Use Step 5 (`APPROVE UPDATE`).

Print the Phase 7 grade line. Its grade also shows at the start of the
person's next application.

---

## Worked Example — Mode B (fictional candidate, Alex M.)

**Input:** Alex uploads `AlexM_CV.pdf` and pastes `https://jobs.lever.co/acme/123` with "apply for this".

1. Execution mode recorded; A0 Capability Map shown, including CV export, text readers and visual-review tools.
2. Profile exists: staleness check flags availability. CV compared with the profile; differences offered via `APPROVE UPDATE`. The intake form asks only the 3 missing fields.
3. Entry gate detects Mode B; Phase 0 `✅ Skipped`.
4. Phase 1 brief → M1 5/5. Step 2A grade line: "11 must-have terms, 3 not in the base CV" → fit verdict Honest Stretch → M2 5/5.
5. Phase 3 confirms pre-filled facts, picks the Germany profile and the Product Delivery track → M3 5/5.
6. Phase 3B writes the CV, critique 18/19 rules fixed to 19/19 → M4 5/5 and `APPROVE CREATE`.
7. Phase 3C: "ATS Gate: 5/5 · all checks passed · must-have coverage 92% (was 64%). Not stopping." Files frozen.
8. Phases 4–5 → M5 5/5. Phase 6 combined verdict PASS. `APPROVE FILL` then `APPROVE SUBMIT` upload the frozen DOCX. Phase 7 logs everything; follow-up window 14 days.

---

## Scope — what this skill does not do

- Does not submit, fill, email, create or save anything without the required approval phrase.
- Does not invent metrics, tools, titles, companies or keywords the record can't prove.
- Does not install or connect MCPs — it detects and recommends them.
- Does not give legal, immigration or tax advice; visa and salary notes are inputs for the person's own decision.
- Does not apply in bulk or to hard-excluded geographies.
- Does not store credentials or government ID numbers.
- Does not upload a CV to any outside site for testing without approval, and never tests through an employer's live application form.

---

## Invariants — Structural Rules (All Candidates)

Unchanged from v2.1.1:

1. Never produce application text before all Phase 3 critical gates cleared. In v2.2.0 this includes the CV.
2. Never fabricate metrics, company details, or tool names not in the profile.
3. Never suggest a salary without running market research first.
4. Never apply to or recommend companies in hard-excluded geographies.
5. Never present a Writing Quality draft — only the final version.
6. Never hide or soften a Mismatch verdict.
7. Never use "To Whom It May Concern" in any cover letter.
8. Never use passive cover letter closes.
9. Always address the cover letter to a named person where one can be found.
10. Always update the excluded-companies-log after every discovery run.
11. Always update salary anchors after any offer data is received.
12. Always run the Level Classification framework before Phase 3 salary research.

Added in v2.2.0:

13. Never add a keyword to a CV unless the record proves it; otherwise log it as a gap.
14. Never change a locked keyword in any rewriting, translation or export step.
15. Never upload or attach a CV file that is not the fingerprinted file from the latest ATS Gate PASS for that job.
16. Never print a Private field (salary, permit status, sponsorship need, notes) on a CV, and never collect government ID numbers.
17. Never let a score authorise an action; scores and approval phrases stay separate.
18. Always show a grade with its reason for every phase that does not stop the person.
19. Never stop on a missing or blocked tool before trying the fallback ladder (A18), and never lower a consent tier when falling back.
