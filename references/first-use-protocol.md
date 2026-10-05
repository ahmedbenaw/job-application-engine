# First-Use Setup Protocol
# job-application-engine v2.2.0 (generic) | moved out of SKILL.md for progressive disclosure, content unchanged unless marked "v2.2.0"
# Read when: session start (Step 4 staleness); no profile or new CV/link (Steps 0–3); after Phase 3 and Phase 7 (Step 5)

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

> **v2.2.0:** ask these questions through the intake questionnaire v4
> (`references/intake-questionnaire.md`). It contains every field in the master
> list below plus eligibility, pay, evidence proof, tracks and market
> preferences. Q0.1 picks the path (first job · career change · returning ·
> experienced · executive) so only relevant questions appear. Pre-filled fields
> are shown for confirmation only. "N/A" is always accepted. The master list
> below stays valid as the minimum set.

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

> **v2.2.0:** print the intake readiness grade first (INQ-08), for example
> "Intake: 4/5 · missing: notice period, proof for 2 results. Not stopping."
> A grade of 3 or lower is raised here. This sign-off is a one-time setup
> check per person and is not one of the 5 per-application gates.

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

> **v2.2.0:** also re-confirm fields whose expiry has passed in the intake
> questionnaire: work permit or visa status and relocation (6 months), current
> city (6 months), certificate expiry dates (at expiry). Show the Phase 7 grade
> of the person's previous application at the start of the session.

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
