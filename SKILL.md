---
name: job-application-engine
version: 1.0.0
edition: generic-universal
author: Ahmed Ossama | Product Leader, Builder & Venture Management Architect
description: |
  Universal end-to-end job application system. Works for any candidate, any
  role, any industry. Supports two session entry modes. Mode A — Job
  Discovery: the user wants to find matching roles; the skill searches 10
  platforms, ranks results, and guides the full application workflow.
  Mode B — Direct Application: the user already has a specific role; they
  upload their CV and provide the job URL, and the skill runs the full
  workflow from Phase 1 onward, skipping discovery entirely. A Session Entry
  Gate detects the mode automatically from uploaded files and URLs, or
  presents both options explicitly if the mode is ambiguous. All agent logic
  is embedded inline — no external dependencies. Triggers when a user uploads
  a CV, pastes a job URL, says "find me jobs", "apply for this role", "I
  want to apply to [company]", "fill this application", or provides any job
  posting URL or job description text.
compatibility:
  tools: [web_search, web_fetch, bash_tool, create_file, present_files]
  platforms: [Claude.ai, Claude CoWork, Manus]
  external_dependencies: none
changelog:
  - version: 1.0.0
    date: 2026-04-24
    notes: |
      Initial generic release. All agent logic nativized: fit analysis,
      writing quality (25 patterns across 5 families), governance gate,
      checklist system, and hiring manager protocol embedded inline.
      7-level job classification framework embedded with auto-detection
      and self-identification logic. Dynamic applicant profile with full
      field taxonomy, salary architecture, dependency map, conflict
      resolution rules, per-field review cycles, equity fields, first-use
      setup protocol, data persistence format, and multi-currency handling.
      Both canonical cover letter templates incorporated with mixing guide
      and 10 quality rules. Rules.json for machine-readable execution.
      README for platform onboarding. MIT licence.
---

# Job Application Engine — Generic Universal Edition

A complete, standalone job application system with two session entry modes.
No external agents, skills, or frameworks required. All logic is embedded
in this file and the reference files in the references/ directory.

All 8 phases are mandatory and sequential. Every phase ends with a user
scoring gate. A score of 5 out of 5 is required to proceed. A score below 5
triggers a revision loop within the same phase before advancing.

---

## First-Use Setup Protocol

Run this protocol when no applicant profile exists, or when the user explicitly
asks to rebuild or update their profile. Execute the four steps in order. Never
skip Step 0 — document detection must always run first.

---

### STEP 0 — Document and Link Detection (always runs first)

Before presenting any questions, check the current session for available data
sources. The skill must attempt to extract profile fields from every available
source before asking the user to type anything manually.

**Check for uploaded files:**
If any file is attached to the session (PDF, DOCX, image of a CV, LinkedIn
export, or any text file), read it immediately using the appropriate tool.
Documents to look for and what to extract from each:

CV or resume (PDF or DOCX):
Extract → [CANDIDATE_NAME], [PRIMARY_EMAIL], [PRIMARY_PHONE], [LINKEDIN_URL],
[PORTFOLIO_URL], [CURRENT_CITY], [CURRENT_COUNTRY], [NATIONALITY],
education history (institution, degree, graduation year), certifications,
work history (company, role, dates, key outcomes — feeds [KEY_EVIDENCE]),
tools and technologies mentioned (feeds [TOOLS_STACK]),
languages listed (feeds [LANGUAGE_PROFICIENCY]),
professional headline or summary (feeds [POSITIONING_HEADLINE]).

LinkedIn PDF export or profile screenshot:
Extract → same fields as CV above, plus connection count as a signal of
network strength, and any published articles or recommendations.

Portfolio document or project list:
Extract → project names, outcomes, tools used, URLs — feed into
[KEY_EVIDENCE] and [PORTFOLIO_ASSETS].

**Check for URLs or links in the user's opening message:**
If the user has pasted any URLs, fetch and parse each one:

LinkedIn public profile URL (`linkedin.com/in/[handle]`):
Fetch with web_fetch → extract name, headline, current role, work history,
education, skills, certifications, and contact information.

GitHub profile URL (`github.com/[handle]`):
Fetch with web_fetch → extract repositories, languages, top projects,
README content for project context — feeds [TOOLS_STACK] and [PORTFOLIO_ASSETS].

Personal website or portfolio URL:
Fetch with web_fetch → extract professional bio, project descriptions,
contact information — feeds [POSITIONING_HEADLINE] and [KEY_EVIDENCE].

Behance, Dribbble, or similar creative portfolio URL:
Fetch with web_fetch → extract project names, descriptions, tools — feeds
[KEY_EVIDENCE] and [PORTFOLIO_ASSETS].

**Check for inline text:**
If the user's opening message describes their background, role, or situation
in any way, extract every usable data point from it before asking questions.

After extraction, build a preliminary field map showing:
- Fields successfully extracted with their extracted values
- Fields partially extracted (value found but needs confirmation)
- Fields not found (will require a question)

---

### STEP 1 — Present Extraction Results

Present what was extracted in this format:

```
── PROFILE EXTRACTION RESULTS ──────────────────────────────────────
Source(s) used: [list each document or URL that was read]

EXTRACTED — confirm or correct each:
  Full name           : [extracted value]
  Email               : [extracted value]
  Phone               : [extracted value]
  LinkedIn            : [extracted value]
  Portfolio           : [extracted value]
  Current location    : [extracted value]
  ...

PARTIALLY EXTRACTED — review needed:
  [field]             : [extracted value] — is this current?

NOT FOUND — will ask below:
  [list of fields that could not be extracted]

Review the extracted values above. Reply with:
  - CONFIRM to accept all extracted values as shown
  - Any corrections in the format: [FIELD]: [corrected value]
  - Or a numbered list of corrections if multiple fields need updating
────────────────────────────────────────────────────────────────────
```

If no documents or links were provided, skip Step 1 and go directly to Step 2
with all fields in the NOT FOUND category.

---

### STEP 2 — Gap-Fill Questions

Ask only for fields that were not extracted or were flagged as needing
confirmation. Group by section. Do not re-ask for confirmed fields.

Present only the applicable questions from this master list:

STATIC FIELDS (if not extracted):
  — Full name
  — Primary email address
  — Primary phone number with country code
  — LinkedIn profile URL
  — Portfolio URL (GitHub, Behance, Dribbble, personal site, or similar)
  — Nationality and passport country
  — Current city and country of residence
  — Education history (institution, degree, graduation year — most recent first)
  — Certifications relevant to your target roles
  — Any geography you will never apply to (hard exclusions — countries or regions)

DYNAMIC FIELDS (if not extracted or inferred):
  — Your primary professional title as you currently present it
  — Your target role types (e.g. Product Manager, UX Designer, Data Analyst)
  — Your target seniority level (see Level Classification Framework — state
    your primary target level and acceptable range)
  — Your target sectors (e.g. SaaS, FinTech, Healthcare, EdTech)
  — Your preferred cities or regions for new roles
  — Are you open to relocation? If yes, which cities are preferred?
  — Your current availability (days or weeks from an offer to your start date)
  — Any active notice period or engagement that affects your start date
  — Your tools and technology stack (every tool you use professionally)
  — Your top 3–5 career achievements with company name, metric, and context
  — Language proficiency (list each language and your current level)

COMPENSATION FIELDS:
  — Your target gross annual salary for your primary target market
  — Currency for each market you are targeting
  — Are you open to equity? If yes, minimum acceptable vesting schedule?
  — Any compensation structure you will not accept

If the user provided a CV or LinkedIn profile and all fields were successfully
extracted, Step 2 may have zero questions. Proceed directly to Step 3.

---

### STEP 3 — Profile Confirmation and Sign-Off

Present the complete populated profile — all extracted and gap-filled values
together — as a single readable summary. Ask the user to review the full
profile and confirm it is accurate before the first session begins.

Apply the scoring gate:
```
── PROFILE SETUP REVIEW GATE ──────────────────────────────────────
Your Applicant Profile is ready. Review the full profile above and respond:
  1. What was correct
  2. Your score from 1 to 5  (5 required to proceed)
  3. What needs correcting before we begin
If score < 5, apply corrections and re-present the profile.
───────────────────────────────────────────────────────────────────
```

After score of 5: write all confirmed values into
references/applicant-profile-template.md and proceed to Phase 0.

---

### STEP 4 — Returning Session Profile Staleness Check

When a profile already exists, run this check at every session start before
Phase 0 begins. Do not run the full First-Use Protocol — only check the
fields listed below.

Time-sensitive fields that decay and must be re-confirmed if stale:

Availability and notice period: re-confirm at every session. This field
can change weekly. Do not use a value more than 2 weeks old without
re-confirming.

Salary anchors: flag any market entry whose source date is older than
6 months. Ask the user to confirm whether the anchor is still accurate
before Phase 3 salary research runs.

Active engagement or constraint: if the profile shows an active engagement,
confirm at session start whether it is still active and whether the end date
or notice period has changed.

Present stale fields in this format:

```
── PROFILE STALENESS CHECK ─────────────────────────────────────────
The following profile fields may be out of date:

  Availability     : [current value] — last confirmed [date]
  Salary anchor    : [market] — sourced [date], refresh due [date]
  Active engagement: [current value] — still active?

Confirm each or provide an update. Type CONFIRM to accept all as-is,
or correct the specific fields that have changed.
────────────────────────────────────────────────────────────────────
```

---

### STEP 5 — Per-Application Profile Update Protocol

This step runs automatically at specific points during the workflow —
not just at first use. It is the mechanism that keeps the profile current
across applications.

**After Phase 3 (Clarifying Intake):**
If any of the following were collected or confirmed during Phase 3 and differ
from the current profile values, flag them for update:
- Portfolio URL (if a new or updated link was provided)
- Salary figure confirmed for a new market (update salary anchors)
- Availability or notice period change
- Language level updated (e.g. user mentioned they passed an assessment)
- New tool added to the stack (user mentioned using a tool not in the profile)

Present as:

```
── PROFILE UPDATE OPPORTUNITY ──────────────────────────────────────
New information from this session differs from your profile:
  [field]  : current → [current profile value]
             new     → [value from this session]

Update your profile with this new information?
Type APPROVE UPDATE to apply, or SKIP to continue without updating.
────────────────────────────────────────────────────────────────────
```

Tier 2 action — requires APPROVE UPDATE before writing to the profile.

**After Phase 7 (Post-Submission Loop):**
After every session close, run this update check regardless of branch:

Branch A (submitted): update the excluded-companies-log with outcome
"Submitted" and date. If an interview or offer follows in a later session,
update the salary anchors with ground-truth offer data.

Branch B (withdrawn): update excluded-companies-log with outcome "Withdrawn"
and the reason. If the reason reveals a recurring gap (e.g. always too design-
heavy), flag this to the user as a potential profile adjustment — perhaps the
target role type or sector emphasis needs updating.

Branch C (rejected): update excluded-companies-log with outcome "Rejected".
Identify which profile field the rejection most likely traces to (using Phase 2
gap analysis). Ask whether to adjust the target seniority level, sector
emphasis, or positioning headline to reduce this gap in future applications.

All post-Phase 7 updates require APPROVE UPDATE (Tier 2) before writing
to the profile.

**Document upload mid-session:**
If the user uploads a document or provides a new URL at any point during an
active session (not just at first-use), run Step 0 extraction immediately
on the new source. Surface any fields that differ from the current profile
and offer to update them via APPROVE UPDATE before continuing.

---

## Dynamic Session Checklist

Print this board at the start of every phase. Update status and score after
each gate. Replace bracketed tokens with live session values.

```
╔════════════════════════════════════════════════════════════════════╗
║          JOB APPLICATION ENGINE — SESSION STATUS BOARD            ║
╠════════════════════════════════════════════════════════════════════╣
║  Phase 0 │ Job Discovery          │ [STATUS] │ Score: [ /5]       ║
║  Phase 1 │ Company Intelligence   │ [STATUS] │ Score: [ /5]       ║
║  Phase 2 │ Fit Analysis           │ [STATUS] │ Score: [ /5]       ║
║  Phase 3 │ Clarifying Intake      │ [STATUS] │ Score: [ /5]       ║
║  Phase 4 │ Application Package    │ [STATUS] │ Score: [ /5]       ║
║  Phase 5 │ Writing Quality Pass   │ [STATUS] │ Score: [ /5]       ║
║  Phase 6 │ Governance Gate        │ [STATUS] │ Score: [ /5]       ║
║  Phase 7 │ Post-Submission Loop   │ [STATUS] │ Score: [ /5]       ║
╠════════════════════════════════════════════════════════════════════╣
║  Active Phase : [PHASE NAME]                                      ║
║  Current Gate : [GATE DESCRIPTION]                                ║
║  Awaiting     : [WHAT IS NEEDED FROM USER]                        ║
║  Candidate    : [CANDIDATE_NAME]                                  ║
║  Session Role : [ROLE_TITLE]     Company: [COMPANY_NAME]          ║
╚════════════════════════════════════════════════════════════════════╝

Status codes: ⏳ Pending | 🔄 Active | 🔁 Revision | ✅ Complete | 🚫 Blocked
```

Example (Alex M., fictional mock candidate):
```
║  Candidate    : Alex M.                                           ║
║  Session Role : Senior Product Manager    Company: CloudBase Inc  ║
║  Phase 2      : Fit Analysis    │ ✅ Complete │ Score: 5/5        ║
```

Scoring gate format — present after every phase output:

```
── PHASE [N] REVIEW GATE ──────────────────────────────────────────
Please respond with:
  1. What was correct
  2. Your score from 1 to 5  (5 required to proceed)
  3. What you expected for a perfect result at this phase
If score < 5, state what to revise. This phase reruns before advancing.
───────────────────────────────────────────────────────────────────
```

---

## Inline Module 1 — Job Level Classification Framework

This framework is used in Phase 0 (discovery filtering), Phase 2 (fit
analysis — role level detection), Phase 3 (salary research anchoring),
and Phase 4 (positioning headline and summary selection).

Auto-detection: read the JD title, scope, reporting line, and team size
to assign a level. Do not rely on the title alone — a startup "Head of"
may carry Level 4 scope; an enterprise "Senior Manager" may carry Level 6
scope. Read the responsibilities to confirm.

Self-identification: if the user has not stated a target level, ask them
to identify their primary target and acceptable range before Phase 0 runs.

```
LEVEL 0 — NOVICE
  Titles:    Intern
  Scope:     Learning under supervision, no independent ownership
  Salary:    Stipend or entry-level band; varies widely by market

LEVEL 1 — ENTRY
  Titles:    Junior [Role], Associate [Role], Graduate [Role]
  Scope:     Defined tasks with guidance; limited independent decision-making
  Salary:    Market entry band; 0–3 years experience typical

LEVEL 2 — MID
  Titles:    [Role] (no qualifier), Associate [Role] with full responsibility
  Scope:     Independent execution on defined scope; some cross-functional work
  Salary:    Mid-market band; 3–6 years experience typical

LEVEL 3 — SENIOR
  Titles:    Senior [Role], Team Lead [Role], Staff [Role]
  Scope:     Independent ownership of a product area or function; mentors
             junior team members; influences roadmap or direction
  Salary:    Upper-market band; 6–10 years experience typical

LEVEL 4 — MANAGER
  Titles:    Manager, Principal, Group [Role]
  Scope:     Manages a team or significant product area; owns budget or
             headcount; accountable for team output
  Salary:    Management band; 8–12 years experience typical

LEVEL 5 — DIRECTOR
  Titles:    Director, Senior Director
  Scope:     Owns a department or major product line; sets strategy within
             a business unit; reports to VP or C-Suite
  Salary:    Director band; 12–18 years experience typical

LEVEL 6 — HEAD / VP
  Titles:    Head of [Function], VP of [Function], VP
  Scope:     Owns an entire function across the organisation; sets strategy;
             hires and structures the team; board-level visibility
  Salary:    VP band; 15+ years experience typical

LEVEL 7 — EXECUTIVE
  Titles:    C-Suite (CPO, CTO, CEO, CFO, COO), Managing Director, President
  Scope:     Full organisational or company-wide accountability; owns P&L or
             equivalent; reports to board or investors
  Salary:    Executive band; equity is a significant component at this level
```

Startup title calibration rule: at companies under 50 people, subtract one
level from the title to estimate true scope. A "Head of Product" at a 15-
person startup is typically Level 4–5 scope. At a 500-person company, the
same title is Level 6 scope.

Level-to-strategy mapping:

  Levels 0–2: Cover letter leads with potential and learning velocity.
    Evidence emphasises growth, adaptability, and early impact.
    Salary: use the floor-to-midpoint of the market band.

  Levels 3–4: Cover letter leads with delivery track record.
    Evidence emphasises owned outcomes, team collaboration, metrics.
    Salary: use the midpoint-to-75th percentile of the market band.

  Levels 5–6: Cover letter leads with strategic impact and organisational
    influence. Evidence emphasises direction-setting, stakeholder management,
    business outcomes, and team-building at scale.
    Salary: use the 75th percentile to stretch of the market band.

  Level 7: Cover letter leads with vision, governance, and systemic impact.
    Evidence emphasises P&L ownership, board relationships, market positioning.
    Salary: custom negotiation; benchmark against public comp data and equity.

---

## Session Entry Gate

This gate runs after A0 Capability Detection and before any phase begins.
It determines which of the two session modes the user is in and routes
the session accordingly. Never skip this gate. Never assume the mode.

---

### Detecting the Session Mode

Before presenting any phase, scan the session for the following signals:

**Signals for Mode B — Direct Application (skip Phase 0):**
- A file is uploaded to the session (CV, resume, portfolio)
- A URL is pasted that resolves to a job posting, job description, or
  application form (e.g. linkedin.com/jobs, boards.greenhouse.io, lever.co,
  breezy.hr, company careers page, or any URL with job-related path)
- The user's opening message contains any of: "apply for this", "I found a
  job", "here is the job", "I want to apply to", "this role", "help me apply",
  "fill in this application", a job title + company name together, or pastes
  a JD or application form text directly

**Signals for Mode A — Discovery (proceed to Phase 0):**
- No file uploaded and no job URL provided
- User asks to "find me jobs", "search for roles", "what jobs match my CV",
  or describes a general target (role type, sector, city) without a specific
  company or URL
- User says "continue" or "next" from a previous Phase 7 Branch A session

**If signals are ambiguous** (e.g. a CV is uploaded but no job URL):
Present the mode selection to the user explicitly (see below).

---

### Mode Selection Prompt

If the session mode cannot be determined from signals alone, present this:

```
── SESSION START ────────────────────────────────────────────────────
How would you like to begin?

  MODE A — Job Discovery
  I will search 10 platforms for roles matching your profile,
  rank the results, and then guide you through the full
  application workflow for whichever role you select.
  → Say "Discover" or describe a target role/city/sector.

  MODE B — Apply to a Specific Role
  You already have a job in mind. Provide your CV (upload the
  file) and the job description URL or application link, and I
  will run the full application workflow for that specific role —
  skipping the discovery phase entirely.
  → Upload your CV and paste the job URL, or say "Apply" and
    I will ask you for both.

Which would you like to do?
────────────────────────────────────────────────────────────────────
```

---

### Mode A — Job Discovery Entry

Proceed to Phase 0 as defined below. The cold-start branch in Phase 0
handles the case where no prior anchor role exists.

---

### Mode B — Direct Application Entry

**Step 1 — Collect required inputs:**
The user must provide two things before Phase 1 can begin:
  (a) CV or resume — uploaded as PDF or DOCX, or pasted as text
  (b) Job URL — the posting URL, application form URL, or a paste of the JD

If either is missing, prompt for it specifically:

```
── MODE B INTAKE ────────────────────────────────────────────────────
To apply to a specific role I need:

  1. Your CV or resume — upload the file (PDF or DOCX) or paste
     the text directly into this conversation.

  2. The job URL — paste the link to the job posting or application
     form. If the company sent you the JD by email, paste the text
     of the JD here instead.

Provide both and I will begin immediately.
────────────────────────────────────────────────────────────────────
```

**Step 2 — Process inputs in parallel:**
Run these two operations simultaneously:
  (a) Feed the CV into the First-Use Setup Protocol Step 0 extraction.
      If a profile already exists, run the staleness check and note any
      fields the CV updates.
  (b) Feed the job URL into Phase 1 (Company Intelligence) directly.
      web_fetch the URL. If the URL is an application form, also extract
      the form fields as per the platform-aware form-fetch strategy.

**Step 3 — Skip Phase 0 entirely.**
Phase 0 (Job Discovery) is not relevant in Mode B. Update the session
checklist to mark Phase 0 as ✅ Skipped and proceed directly to Phase 1.

Do not ask the user "what role type, sector, geography are you targeting?"
in Mode B. That question belongs to Mode A cold-start only.

**Step 4 — Proceed from Phase 1 onward.**
The session now follows the standard workflow from Phase 1 through Phase 7.
All phases, scoring gates, automation recommendations, and consent gates
operate identically in both modes from Phase 1 onward.

---

### Dynamic Checklist — Mode B Display

In Mode B sessions, update the checklist header to reflect the skipped phase:

```
╔════════════════════════════════════════════════════════════════════╗
║          JOB APPLICATION ENGINE — SESSION STATUS BOARD            ║
╠════════════════════════════════════════════════════════════════════╣
║  Phase 0 │ Job Discovery          │ ✅ Skipped  │ Mode B          ║
║  Phase 1 │ Company Intelligence   │ [STATUS]    │ Score: [ /5]   ║
...
```

---

## Phase 0 — Job Discovery

MODE A ONLY. This phase does not run in Mode B sessions. If the session
is Mode B, Phase 0 is marked ✅ Skipped in the checklist and the workflow
proceeds directly from Phase 1.

Print checklist with Phase 0 set to 🔄 Active before running any searches.

COLD-START BRANCH (Mode A, no prior anchor): If no prior application exists
as a similarity anchor and the user has not stated a target role, prompt:
"What role type, seniority level, sector, and preferred geography are you
targeting?" Collect all four inputs. Use the Level Classification above to
confirm the seniority target before building queries. Do NOT run this branch
in Mode B — Mode B users have already defined their target via the job URL.

Read references/applicant-profile-template.md to extract:
  [TARGET_ROLE_TYPES], [TARGET_SENIORITY_LEVEL], [TARGET_SECTORS],
  [PREFERRED_CITIES], [HARD_EXCLUSION_GEOGRAPHIES]

Search platforms — run in parallel, apply exclusion filter before presenting:
LinkedIn Jobs | Indeed | Wellfound / AngelList | Relocate.me | EuroTechJobs |
Greenhouse (boards.greenhouse.io) | Lever (jobs.lever.co) | Breezy HR |
Welcome to the Jungle / Otta | RemoteOK

Pass 1 — Similarity anchor (adapt to stated role and level):
  "[ROLE_TITLE]" [CITY] relocation visa sponsorship [SECTOR]
  "[ROLE_TITLE]" OR "[ALTERNATIVE_TITLE]" [REGION] relocation SaaS FinTech
  senior [ROLE_FUNCTION] [SECTOR] remote Europe visa sponsorship

Pass 2 — CV-fit broadened (use candidate's top skills and sectors):
  [TOP_SKILL_1] [TOP_SKILL_2] [SECTOR] [REGION] relocation visa
  [ROLE_FUNCTION] [YEARS_EXPERIENCE] [SECTOR] [CITY] sponsorship remote

Present results as ranked table:
`Rank | Company | Role | Level | Location | Relocation | Fit Signal | URL`

Add Level column using the Level Classification framework to assign a level
to each discovered role based on the title and available JD snippet.

Rank by: (1) relocation explicitly offered, (2) level match to candidate
target, (3) role title match, (4) sector alignment. Cap at 20. Flag top 5.

Example row (Alex M., fictional):
`3 | CloudBase Inc | Sr. Product Manager | L3 | Berlin, DE | Yes | SaaS, 0-to-1 match | [URL]`

Present Phase 0 scoring gate.

---

## Phase 1 — Company Intelligence

Print updated checklist with Phase 1 set to 🔄 Active.

Run four operations in parallel:

OPERATION 1 — Job posting fetch:
web_fetch the provided URL. Follow redirects. Note incomplete rendering.

OPERATION 2 — Application form fetch (platform-aware):
  Breezy HR: append /apply. If {{ question.text }} appears, flag to user.
  Greenhouse: fetch embed URL or append to posting path. Usually needs
    manual paste for custom questions.
  Lever: append /apply. Usually renders fully.
  LinkedIn / Indeed: behind authentication — flag to user, paste manually.
  Fallback: if template variables detected, instruct user to paste all
    custom question text into the conversation before proceeding.

OPERATION 3 — Hiring manager identification:
  Search: [COMPANY_NAME] [ROLE_TITLE] recruiter OR "hiring manager" LinkedIn
  Use result to address the cover letter to a named person.
  If no name found: use title. Never use "To Whom It May Concern."

OPERATION 4 — Company and product research:
  Search: [COMPANY_NAME] funding team culture [CITY] [current year]
  Search: [COMPANY_NAME] tech stack product philosophy [current year]

Compile Company Intelligence Brief: what the company does (one paragraph,
no promotional language), funding stage and investors, team size, tech stack,
culture signals, competitive market position, hiring manager name if found,
and any product gap or opportunity visible from public information.

Example (Alex M., fictional):
  CloudBase Inc: B2B SaaS platform for cloud cost optimisation, Series B
  ($42M), 120 employees, HQ Berlin. Stack: React, Node.js, AWS.
  Culture signals: "move fast, own the outcome, no hand-offs." Hiring
  manager: Sarah K., Head of Product (identified via LinkedIn).

Present Phase 1 scoring gate.

---

## Phase 2 — Fit Analysis (Inline Module)

Print updated checklist with Phase 2 set to 🔄 Active.

Hard gate. No application text is produced until a verdict is returned.

STEP 1 — Role level detection:
Assign a level from the Level Classification Framework based on JD scope,
reporting line, and responsibilities — not title alone. Record this level
as [DETECTED_LEVEL]. Compare to [TARGET_SENIORITY_LEVEL] in the applicant
profile. If there is a gap of more than one level in either direction,
flag this to the user before proceeding.

STEP 2 — Requirements extraction:
Extract every stated requirement. Separate mandatory (must-have) from
preferred (nice-to-have). Number them for reference.

STEP 3 — Two-column evidence mapping:
  Column A — Strong alignment: specific evidence from the applicant profile.
    Must be traceable: company name, role, outcome, or metric.
    General claims do not qualify. Only confirmed evidence counts.
  Column B — Honest gaps: requirements not covered or only partially covered.
    State plainly. No softening. No reframing as growth opportunities
    unless the JD itself uses that language.

STEP 4 — Compensating evidence:
For every gap in Column B, identify whether any related capability exists
that partially offsets it. State both gap and offset explicitly. An offset
is not a denial of the gap — both must appear in the output.

STEP 5 — Verdict:
  Clean Fit: all mandatory requirements covered by direct evidence.
  Honest Stretch: one or two mandatory gaps offset by compensating evidence.
    Application viable. Gap must appear in cover letter and "why suitable."
  Mismatch: two or more mandatory gaps with no compensating evidence.
    HALT. Inform user. Do not produce application materials.

STEP 6 — Session gap statement (to session log, not applicant profile):
One paragraph: name the gap directly in one sentence, name the compensating
evidence in one to two sentences. No hedging. No apologetic framing.

Example (Alex M., fictional — Honest Stretch):
  Gap: the JD requires hands-on React development experience; Alex's
  profile shows product management of React-based teams but no direct
  coding. Offset: Alex has prototyped front-end features using AI-assisted
  coding tools and has shipped working UIs into production environments
  in close collaboration with engineering leads, demonstrating practical
  understanding of the constraints and patterns the role requires.

Present Phase 2 scoring gate.

---

## Phase 3 — Clarifying Questions Intake

Print updated checklist with Phase 3 set to 🔄 Active.

Present all questions in a single block. Label each Critical or Important.

CRITICAL GATES:
  Portfolio: most relevant URL for this specific role. What is it?
  Salary: read applicant profile for [SALARY_TARGET_[MARKET]]. If no anchor
    exists for this market, run salary research protocol below.
  Availability: start date and any notice period constraint.
  Relocation: open to relocating for this role? In-office days required?
  Custom questions: paste any that the form rendered as template variables.

IMPORTANT GATES (ask when role-relevant):
  Specific project: project or prototype that maps to this JD's primary
    requirement. Two sentences: tool used and measurable outcome.
  Language level: confirm actual level if the JD lists a language requirement.
  Product trial: if the company has a public product, ask the user to spend
    10–15 minutes using it and return with one specific observation.
    Do not write the cover letter before receiving this observation.

SALARY RESEARCH PROTOCOL:
  When no anchor exists for the target market, run:
    [CITY] [ROLE_TITLE] salary [current year] gross Glassdoor
    [CITY] [ROLE_TITLE] [LEVEL] salary [current year] Handpicked OR Levels.fyi
  Extract floor (25th pct), target (50–75th pct midpoint), stretch (90th pct).
  Apply market take-home rate from references/salary-anchors-template.md.
  Present as single gross figure for form entry.

  Level adjustment: apply the level-to-strategy mapping from the Level
  Classification Framework when selecting the percentile range:
    Levels 0–2: floor to midpoint.
    Levels 3–4: midpoint to 75th percentile.
    Levels 5–7: 75th percentile to stretch.

  Fractional or consulting roles: day rate = (annual FTE target ÷ 220) × 1.4

  Multi-currency roles: store both currency figures separately. Flag exchange
  rate risk as a user decision point. Do not convert on the user's behalf.

Present Phase 3 scoring gate.

---

## Phase 4 — Application Package Production

Print updated checklist with Phase 4 set to 🔄 Active.
Confirm all Phase 3 critical gates cleared before writing anything.

Produce all deliverables in one response, clearly labelled for copy-paste.

STANDARD FORM FIELDS:
Pull from references/applicant-profile-template.md:
[CANDIDATE_NAME], [EMAIL], [PHONE], [LINKEDIN_URL], [SALARY_TARGET_GROSS],
[PORTFOLIO_URL]. Flag any missing confirmed value.

EXPERIENCE SUMMARY (3–4 sentences):
Select the appropriate Professional Summary version from the applicant
profile based on the JD's primary requirement and [DETECTED_LEVEL].
Tailor to this specific role. Do not restate the full CV.
Route through Phase 5 before presenting.

COVER LETTER — follow references/cover-letter-templates.md:
Mix Template A and Template B elements per the mixing guide.

  Address: to [HIRING_MANAGER_NAME] identified in Phase 1.
    Fallback: "Dear [HIRING_MANAGER_TITLE]:" or "Dear Hiring Team:"
    Never use: "To Whom It May Concern"

  Opening paragraph: why this role, why this company, what makes the
    candidate a fit — specific to the JD requirements.

  Evidence paragraph: one or two examples. [COMPANY_A], [ROLE_AT_COMPANY_A],
    [OUTCOME_A], [METRIC_A]. Action verbs. Explicit connection to JD.

  Product observation: the user's specific observation from the Phase 3 trial.
    Cannot be written before the trial answer is received.

  Gap acknowledgment: one sentence naming the gap. One to two sentences
    naming the compensating evidence. Required for Honest Stretch verdicts.

  Strong close: commits to a follow-up action. Confirms relocation.
    Prohibited: "I look forward to your reply", "please call me at your
    earliest convenience."

  Sign-off: [CANDIDATE_NAME] | [PHONE] | [EMAIL] | [LINKEDIN_URL]

  Word limits: text box 450; online/email 250; document 500.

Level-specific tone guidance:
  Levels 0–2: enthusiastic, specific about learning pace and early wins.
  Levels 3–4: direct, evidence-led, delivery-focused.
  Levels 5–7: strategic, organisational, outcome-at-scale language.

CUSTOM QUESTION ANSWERS:
Print the exact question text above each answer.
Every claim traces to the applicant profile or a Phase 3 answer.
No fabricated metrics. No generic phrases.

Route all written output through Phase 5 before presenting.

Example field tokens in use (Alex M., fictional):
  [CANDIDATE_NAME] = Alex M.
  [COMPANY_A] = DataFlow GmbH
  [ROLE_AT_COMPANY_A] = Senior Product Manager
  [OUTCOME_A] = Reduced churn by 18% in 6 months through a
    friction-audit-led onboarding redesign
  [METRIC_A] = 18% churn reduction, 6-month timeline

Present Phase 4 scoring gate.

---

## Phase 5 — Writing Quality Pass (Inline Module)

Print updated checklist with Phase 5 set to 🔄 Active.
Two passes run internally. Present only the final version — never the draft.

PASS 1 — Remove all instances of the following 25 pattern categories:

Family 1 — Significance inflation (10 patterns):
  "stands as", "serves as", "is a testament to", "marks a pivotal moment",
  "underscores", "highlights its importance", "reflects broader", "evolving
  landscape", "indelible mark", "setting the stage for", "key turning point",
  "shaping the future of", "deeply rooted", "contributing to the."

Family 2 — Promotional language (8 patterns):
  "boasts", "vibrant", "groundbreaking", "renowned", "breathtaking",
  "nestled", "in the heart of", "showcasing", "exemplifies", "commitment
  to excellence", "rich experience", "stunning", "dynamic" (used vaguely).

Family 3 — Structural AI patterns (5 patterns):
  Rule of three used for rhetorical effect rather than genuine enumeration.
  Em dashes used more than once per paragraph for stylistic effect.
  Negative parallelism: "not just X, but Y."
  Synonym cycling: three different words for the same thing in sequence.
  False ranges: "from X to Y, from A to B."

Family 4 — Voice and attribution patterns (7 patterns):
  Vague attributions: "experts argue", "industry reports suggest",
    "observers have noted."
  Copula avoidance: "serves as" or "functions as" instead of "is."
  Superficial -ing phrases tacked onto sentence endings.
  Chatbot artifacts: "Great question!", "I hope this helps!", "Let me know if."
  Excessive hedging: "could potentially possibly", "might arguably be."
  Knowledge cutoff hedging: "based on available information."
  Overuse of "I" beginning consecutive sentences.

Family 5 — Technical AI tells (5 patterns):
  Hyphenated word pairs with perfect consistency: "cross-functional",
    "data-driven", "end-to-end", "client-facing" used uniformly throughout.
  Filler openers: "In order to", "It is important to note", "At its core."
  Generic positive conclusions: "The future looks bright", "exciting times."
  Over-formatted output: excessive bold, bullets, headers where prose fits.
  Passive voice in evidence sections where active voice is stronger.

PASS 2 — Internal audit loop:
Ask internally: "What still makes this obviously AI-generated?" List remaining
tells. Resolve each. Vary sentence length and rhythm. Add specificity where
vague claims remain. Match the voice to the candidate's level and sector:
direct and delivery-focused for mid-level; strategic and systems-oriented
for senior and executive levels.

Present Phase 5 scoring gate.

---

## Phase 6 — Governance Gate (Inline Module)

Print updated checklist with Phase 6 set to 🔄 Active.
Fix all failures before presenting. Do not present with any open check.

Check 1: Can a third party complete this application without asking any
  questions? Every required field has a value or an explicit flag.
Check 2: Every factual claim traces to the applicant profile or a
  Phase 3 answer. No unconfirmed metrics or tool names.
Check 3: Salary is a single gross figure in the correct local currency.
  Not a range in prose unless the form explicitly requires a range.
Check 4: Any gap identified in Phase 2 is acknowledged in both the cover
  letter and the "why suitable" answer. Not hidden. Not softened.
Check 5: All placeholder tokens ([CANDIDATE_NAME], [COMPANY_A], etc.) are
  replaced with real values or explicitly flagged for user completion.
Check 6: Cover letter is within the word limit for its submission format.
  (Text box: 450. Online/email: 250. Document: 500.)
Check 7: Portfolio field is a valid URL, not placeholder text or description.
Check 8: Salary field is a numeric value in currency format, not prose.

Present Phase 6 scoring gate.

---

## Phase 7 — Post-Submission Loop

Print updated checklist with Phase 7 set to 🔄 Active.

BRANCH A — Successful submission:
  Use submitted role as anchor. Return to Phase 0. Present next 5 ranked
  recommendations from a fresh filtered discovery pass.

BRANCH B — Candidate withdrawal before submission:
  Log role as withdrawn. Ask: "What was the reason?" Use the answer to
  refine the next discovery pass weighting (e.g. if too design-heavy,
  downweight design-primary roles in the next pass).

BRANCH C — Rejection after submission:
  Log outcome. Identify which mandatory JD requirement the rejection most
  likely reflects based on Phase 2 gaps. Ask the user whether to adjust
  seniority target, sector, or emphasis for the next search cycle.

Post-session updates required in all branches:
  Append outcome to references/excluded-companies-log.md.
  Update references/salary-anchors-template.md if offer data was received.

Present Phase 7 scoring gate.

---

## Platform Execution Notes

Claude.ai: Sequential phases. Wait for scoring gate before advancing.
  Confirm explicitly before Phase 4. Present status board each phase.

Claude CoWork: Phases 0, 1, and Phase 3 salary research run as parallel
  subagents. Phase 2 must return a verdict before Phase 4 begins. Phases
  5 and 6 run sequentially as final passes. Package output as downloadable
  file on request. Status board as a static artifact updated per gate.

Using both together: Run Phases 0 and 1 in CoWork for parallel speed.
  Transfer the Company Intelligence Brief into a Claude.ai session.
  Run Phases 2 through 7 in Claude.ai for sequential gate control.

Manus: Paste rules.json into the Manus project as a .json or .md file at
  session start. Manus treats it as session-scope instructions and executes
  the phase sequence. Maintain the status board as a text artifact.
  All 8 phase outputs must be confirmed by the user before advancing.

---

## Automation Layer — v2.0 Addition

This section is purely additive to the v1.0 workflow. All 8 phases and their
gates remain unchanged. The automation layer adds a capability detection
protocol at session start, inline automation recommendations at relevant
phase steps, consent gates before any real-world action fires, and execution
routing per platform. Read automation-registry.json for the full declared
scope of permitted automations.

---

### A0 — Capability Detection Protocol

Run this protocol at the very start of every session, before Phase 0 begins.
Do not proceed to Phase 0 until the Capability Map is presented and the user
has acknowledged it.

STEP 1 — Probe available tools and MCP connections:
Check which of the following are active in the current session environment:
  web_search, web_fetch, bash_tool, create_file, present_files (native tools)
  BrowserBase MCP (browser automation — primary path for form filling)
  Playwright MCP (browser automation — secondary path)
  Gmail MCP (email send and draft)
  Outlook / MS365 MCP (email alternative)
  Google Drive MCP (cloud document storage)
  OneDrive MCP (cloud document storage alternative)
  Google Calendar MCP (reminder creation)
  Any other MCP detected in the session environment

STEP 2 — Build and present the Capability Map:
Print the map using this exact format. Replace [STATUS] with one of:
  ✅ ACTIVE — tool confirmed available and callable
  ⚠ LIMITED — tool present but with known constraints (note the constraint)
  ❌ INACTIVE — tool not connected (show what connection would enable it)

```
╔══════════════════════════════════════════════════════════════════════════╗
║                 JAE — AUTOMATION CAPABILITY MAP                         ║
╠═══════════════════════════════╦══════════════════╦══════════╦═══════════╣
║  AUTOMATION                   ║ TOOL / MCP       ║ STATUS   ║ FALLBACK  ║
╠═══════════════════════════════╬══════════════════╬══════════╬═══════════╣
║  Job board access & search    ║ web_fetch/search  ║ [STATUS] ║ —        ║
║  Form fetch & parse           ║ web_fetch         ║ [STATUS] ║ Manual   ║
║  Browser form filling         ║ BrowserBase MCP   ║ [STATUS] ║ Playwright║
║  Application submission       ║ BrowserBase MCP   ║ [STATUS] ║ Manual   ║
║  Document creation (DOCX/PDF) ║ bash_tool         ║ [STATUS] ║ —        ║
║  File download (local)        ║ present_files     ║ [STATUS] ║ —        ║
║  Cloud save (Drive/OneDrive)  ║ Drive / OneDrive  ║ [STATUS] ║ Ask user ║
║  Email draft & send           ║ Gmail / Outlook   ║ [STATUS] ║ Manual   ║
║  Calendar reminders           ║ Calendar MCP      ║ [STATUS] ║ Manual   ║
╚═══════════════════════════════╩══════════════════╩══════════╩═══════════╝

INACTIVE AUTOMATIONS — what would enable them:
  [List each ❌ item with the MCP name and how to connect it]
```

STEP 3 — Browser automation disclosure:
If BrowserBase MCP is ACTIVE: note it as the primary path for form filling
and submission. No further explanation needed unless the user asks.

If BrowserBase is INACTIVE but Playwright MCP is ACTIVE: present this
disclosure to the user before Phase 0:

  "Playwright MCP is available for browser automation (form filling and
  application submission). This is a technical tool — it controls a real
  browser programmatically. It works reliably on most job platforms but
  requires that the target site does not use aggressive bot detection.
  If a site blocks it, the fallback is pre-staged answers for manual paste.
  Do you want to use Playwright automation where available?"

If both are INACTIVE: note that form filling and submission will use
pre-staged answers for manual paste. No further action needed.

STEP 4 — Acknowledge and proceed:
After presenting the Capability Map, ask: "Shall we begin Phase 0?"
Do not proceed until the user confirms.

---

### Automation Recommendation Protocol

At each phase where an automation is relevant, present a recommendation
block AFTER the phase's main output and BEFORE the scoring gate.

Use this format:

```
── AUTOMATION AVAILABLE ────────────────────────────────────────────
  ACTION    : [What the automation will do]
  TOOL      : [Which tool or MCP will execute it]
  CONSENT   : [Tier 1 auto / Tier 2 APPROVE / Tier 3 APPROVE + phrase]
  RELEVANCE : [Why this is useful at this exact step]
  → Type APPROVE [ACTION] to execute, or skip to continue manually.
────────────────────────────────────────────────────────────────────
```

Additionally, if the Capability Map shows an INACTIVE automation that would
be highly useful at the current step, present a recommendation to connect it:

```
── AUTOMATION RECOMMENDED (NOT YET CONNECTED) ──────────────────────
  MISSING   : [Automation name]
  WOULD DO  : [What it would do at this step]
  REQUIRES  : [MCP name and how to connect]
  BENEFIT   : [Why connecting it would improve this step]
────────────────────────────────────────────────────────────────────
```

Never present more than two automation recommendations per phase.
Always present the manual fallback path alongside any automation option.
Never suggest automations outside the scope declared in automation-registry.json.

Phase-by-phase automation trigger points:

Phase 0 (Job Discovery): after presenting the ranked table, offer to fetch
  full job posting content for top 5 results (Tier 1 auto via web_fetch).
  If BrowserBase or Playwright is active, offer to access job board dashboards
  that require login after user provides credentials within the session.

Phase 1 (Company Intelligence): after the Intelligence Brief, offer to
  fetch and map the full application form for the selected role (Tier 1).
  If form requires browser access and automation is available, trigger it.

Phase 3 (Clarifying Intake): if a follow-up email to the hiring manager
  would be appropriate (e.g. to ask for the application form name), offer
  to draft and send it via email automation (Tier 3 — requires APPROVAL).

Phase 4 (Application Package): after package is produced and scored 5,
  offer to create a DOCX version of the cover letter (Tier 2 — APPROVE CREATE).
  Offer to save the full package to local download immediately (Tier 1).

Phase 6 (Governance Gate): after all 8 checks pass, offer to fill the
  application form fields using browser automation if available (Tier 3).
  Offer to create a session record document for local download (Tier 2).

Phase 7 (Post-Submission): offer to create a calendar reminder for
  follow-up (Tier 2 — APPROVE CREATE). Offer to send a confirmation email
  to the user's own address with the application package (Tier 2).

---

### Consent Gate Protocol

Three tiers based on reversibility and risk. Approval and Scoring are
separate systems. Scoring gates evaluate phase quality. Consent gates
authorise real-world actions. They use different confirmation mechanisms
and must never be conflated.

TIER 1 — Read-only actions:
Examples: fetching job listings, loading forms, researching companies.
Execution: auto-execute as part of the phase workflow. No separate gate.
The existing phase scoring gate is sufficient.

TIER 2 — Reversible write actions:
Examples: creating a DOCX, saving to Drive, creating a calendar event.
Present a preview before executing:

```
── TIER 2 CONSENT GATE ────────────────────────────────────────────
  ACTION    : [Exact description of what will be created or written]
  LOCATION  : [Where it will be saved — local / Drive folder / calendar]
  CONTENTS  : [Summary of what the file or event will contain]
  REVERSIBLE: Yes — [explain how to undo if needed]
  → Type APPROVE [ACTION_NAME] to execute.
  → Example: APPROVE CREATE to create the document.
  → Type SKIP to continue without this action.
────────────────────────────────────────────────────────────────────
```

Accept only exact APPROVE [ACTION_NAME] typed by the user. A score of 5,
"yes", "ok", or any other response does not constitute Tier 2 approval.

TIER 3 — Irreversible write actions:
Examples: submitting an application, sending an email to an external party.
These cannot be undone. Use the full consent gate:

```
── TIER 3 CONSENT GATE — IRREVERSIBLE ACTION ──────────────────────
  ACTION     : [Exact description — what will be sent or submitted]
  DESTINATION: [Exact recipient or platform receiving the action]
  DATA SENT  : [Full list of data fields or content being transmitted]
  TIMESTAMP  : [Current date and time of execution if confirmed]
  ⚠ THIS CANNOT BE UNDONE AFTER CONFIRMATION.

  To confirm, type the exact phrase:
  APPROVE [SPECIFIC_PHRASE]

  Examples:
    Application submission → APPROVE SUBMIT
    Email send             → APPROVE SEND
    Form field commit      → APPROVE FILL

  Type CANCEL or anything else to abort.
────────────────────────────────────────────────────────────────────
```

After receiving APPROVE [SPECIFIC_PHRASE]: read it back to confirm the
match is exact. Then execute. Never execute on a partial match.
Never proceed if the user types a score, "yes", or a paraphrase.

---

### Browser Automation Protocol

STEP 1 — Platform detection:
Before triggering browser automation for a specific job platform, check
automation-registry.json for the platform's known bot-detection level.
High bot-detection platforms (LinkedIn, Indeed) require special handling.
Low bot-detection platforms (Greenhouse, Lever, Breezy HR) are reliable.

STEP 2 — Tool selection:
If BrowserBase MCP is ACTIVE: use it as the primary execution path.
If BrowserBase is INACTIVE and Playwright MCP is ACTIVE: present the
Playwright disclosure (see A0 Step 3) if not already shown this session,
confirm the user accepts Playwright, then proceed.
If both are INACTIVE: switch to pre-staged answers mode — produce all
field values in a numbered copy-paste format matching the form structure,
and instruct the user to fill manually.

STEP 3 — Credential handling:
Never store credentials in any file. If a platform requires login for
form access, request credentials within the session only, use them for
the current action, and explicitly confirm to the user that they are
not retained after the session ends.

STEP 4 — Failure handling:
If browser automation fails mid-form (bot detection, timeout, DOM change):
immediately stop, report the failure to the user, show how far the form
was completed, and switch to pre-staged answers for the remaining fields.
Never attempt to resubmit automatically after a failure.

---

### Email Selection Protocol

Never assume which email system to use. Never hardcode a default.

When an email action is triggered for the first time in a session:
Present all active email MCPs detected in the Capability Map.
Ask the user which to use for this action.
Store the selection for this session only as [SESSION_EMAIL_CHOICE].
On subsequent email actions in the same session: show "Last used:
[SESSION_EMAIL_CHOICE]" and ask "Use the same, or switch?"
Do not carry the selection across sessions. Ask fresh each time.

Format for email selection prompt:

```
── EMAIL SYSTEM SELECTION ─────────────────────────────────────────
  Available email systems detected this session:
    [List each active email MCP]
  Last used this session: [SESSION_EMAIL_CHOICE or "None yet"]
  Which would you like to use for this action?
────────────────────────────────────────────────────────────────────
```

---

### Document Storage Protocol

When a document (DOCX, PDF, or package) is created:

STEP 1 — Always present for local download first using present_files.
Never ask about cloud storage before local download is presented.

STEP 2 — After local download is offered, ask:
"Would you also like to save this to cloud storage?"
If yes: present all active cloud storage MCPs detected in the Capability Map
  (Google Drive, OneDrive, or any other connected provider).
Ask which provider to use for this save.
Execute the cloud save as a Tier 2 action (APPROVE SAVE required).
If no: proceed without cloud save. Never save to cloud without consent.

STEP 3 — Folder suggestion:
When saving to cloud, suggest a logical folder path based on the current
session context (e.g. "Job Applications / [COMPANY_NAME] / [DATE]").
Present the suggested path and ask the user to confirm or modify it before
executing the save.

---

### Platform-Aware Automation Routing

Claude.ai:
All automations execute sequentially. Tier 1 actions fire inline as part
of the phase. Tier 2 and Tier 3 actions pause for consent before firing.
Browser automation and email MCPs execute in the same conversation thread.

Claude CoWork:
Tier 1 read-only automations (job board fetching, form parsing, company
research) may run as parallel subagents during Phases 0 and 1.
All Tier 2 and Tier 3 actions — regardless of phase — execute sequentially
after consent in the main coordination thread. Never dispatch an irreversible
action to a subagent.

Manus:
All automations follow the rules.json automation_layer block as session
instructions. Tier 1 actions execute inline. Tier 2 and Tier 3 actions
pause and surface the consent gate as a text prompt in the session.
Browser automation relies on Manus's native browser tools if BrowserBase
and Playwright MCPs are not available.

---

## Invariants — Structural Rules (All Candidates)

Never produce application text before all Phase 3 critical gates cleared.
Never fabricate metrics, company details, or tool names not in the profile.
Never suggest a salary without running market research first.
Never apply to or recommend companies in hard-excluded geographies.
Never present a Writing Quality draft — only the final version.
Never hide or soften a Mismatch verdict.
Never use "To Whom It May Concern" in any cover letter.
Never use passive cover letter closes.
Always address the cover letter to a named person where one can be found.
Always update the excluded-companies-log after every discovery run.
Always update salary anchors after any offer data is received.
Always run the Level Classification framework before Phase 3 salary research.
