# Application Filling Playbook
# Automation IDs: A03, A04, A05
# Version: 2.0.0 | Part of job-application-engine automation layer
# Consent tiers: A03=1, A04=3 (APPROVE FILL), A05=3 (APPROVE SUBMIT)

---
## Purpose

Covers the full protocol for fetching application forms, mapping confirmed
package answers to form fields, filling the form via browser automation,
and submitting after explicit consent. This playbook operates across Phase 1
(form fetch), Phase 6 (field fill after Governance Gate), and the transition
between Phase 6 and Phase 7 (submission).

---
## Stage 1 — Form Fetch (A03, Tier 1)

Executes as part of Phase 1 Company Intelligence — no separate consent gate.

STEP 1 — Identify the form URL:
  From the job posting fetched in Phase 1, find the apply link.
  Apply platform-specific strategy from the table below.

STEP 2 — Fetch and parse:
  web_fetch the form URL.
  Parse all visible form sections and field labels.
  Identify: standard fields, work history, education, custom questions,
    file upload requirements, and privacy consent checkboxes.

STEP 3 — Flag dynamic rendering:
  If custom questions appear as template variables (e.g. {{ question.text }}
  on Breezy HR, or are absent on LinkedIn), flag immediately:
  "The application form for [COMPANY] on [PLATFORM] renders custom questions
  dynamically and they cannot be fetched automatically. Please open the form
  at [URL] in your browser and paste all custom question text into this
  conversation before we proceed to Phase 3."

Platform-specific form fetch strategies:

  BREEZY HR:  Append /apply to job URL. Parse visible fields.
              Custom questions render as {{ question.text }} — flag to user.
  GREENHOUSE: Fetch embed URL or append to posting path.
              Custom questions often require manual paste.
  LEVER:      Append /apply to posting URL. Usually renders fully.
  LINKEDIN:   Form behind authentication. Flag to user — paste manually.
  INDEED:     Form behind authentication. Flag to user — paste manually.
  WORKDAY:    Dynamic JavaScript rendering. Flag to user — paste manually.
  OTHER:      Attempt direct fetch. If template variables detected, flag.

STEP 4 — Build field map:
  Create a numbered field map of every field in the form in order:
  [1] Full Name
  [2] Email Address
  [3] Phone Number
  [4] LinkedIn URL
  [5] Salary Expectation
  ... and so on for all visible fields.
  This field map is the reference for A04 field filling.

---
## Stage 2 — Browser Form Filling (A04, Tier 3 — APPROVE FILL)

Prerequisite: All 8 Governance Gate checks must pass at score 5 before
this action is offered. Do not offer A04 before Phase 6 completes.

STEP 1 — Tool selection:
  Check Capability Map for browser automation status.
  If BrowserBase ACTIVE: proceed with BrowserBase.
  If BrowserBase INACTIVE + Playwright ACTIVE: present Playwright disclosure
    if not shown this session. If user accepts, proceed with Playwright.
  If both INACTIVE: switch to pre-staged answers mode (see below).

STEP 2 — Present Tier 3 consent gate:

  "TIER 3 CONSENT GATE — BROWSER FORM FILLING
  ─────────────────────────────────────────────
  ACTION     : Fill all fields in the [COMPANY_NAME] application form
  PLATFORM   : [PLATFORM_NAME] at [FORM_URL]
  TOOL       : [BrowserBase or Playwright]
  DATA       : [list all field values from the confirmed package]
  NOTE       : This will fill but NOT submit the form.
               You will review the filled form before any submission.
  ⚠ Fields cannot be easily cleared on some platforms once filled.

  Type APPROVE FILL to proceed, or CANCEL to fill manually."

STEP 3 — Execute (only after exact APPROVE FILL received):
  Navigate to the form URL.
  Map each field from the field map (Stage 1 Step 4) to the confirmed
    answer from the application package.
  Fill each field in order.
  For file uploads (CV/resume): upload the file provided by the user.
    If no file is provided, skip the upload and flag to the user.
  For privacy consent checkboxes: check them only if the user has
    indicated consent during Phase 3 intake.
  Do NOT click Submit or any final submission button.
  Take a visual snapshot of the completed form if the tool supports it.
  Report: "All [N] fields filled. Please review the form before confirming
    submission. Type APPROVE SUBMIT when ready, or CANCEL to abort."

STEP 4 — Failure handling:
  If the browser tool encounters an error (bot detection, DOM change,
    timeout, unexpected field type):
  Stop immediately.
  Report: "Browser automation stopped at field [N]: [FIELD_NAME].
    Reason: [ERROR]. Fields [1] through [N-1] have been filled.
    Here are the remaining answers for manual entry:"
  Display all remaining field values in copy-paste format.
  Switch to manual mode for remaining fields.
  Never attempt to resubmit, retry, or continue automatically.

---
## Pre-Staged Answers Mode (Fallback when automation unavailable)

When browser automation is not available or fails, produce this output:

  "Manual Field Entry — [COMPANY_NAME] Application
  ─────────────────────────────────────────────────
  All answers are ready. Open the form at [URL] and paste each answer
  into the corresponding field:

  [1] Full Name: [VALUE]
  [2] Email: [VALUE]
  [3] Phone: [VALUE]
  [4] LinkedIn: [VALUE]
  [5] Salary: [VALUE]
  [N] [FIELD_NAME]: [VALUE]
  ...

  [CUSTOM QUESTION TEXT]: [ANSWER]
  ...

  When complete, review the form before submitting."

---
## Stage 3 — Application Submission (A05, Tier 3 — APPROVE SUBMIT)

Offered only after A04 field fill is reviewed by the user.

STEP 1 — Present full Tier 3 consent gate:

  "TIER 3 CONSENT GATE — APPLICATION SUBMISSION
  ──────────────────────────────────────────────
  ACTION     : Submit the completed application to [COMPANY_NAME]
  ROLE       : [ROLE_TITLE]
  PLATFORM   : [PLATFORM_NAME]
  SUBMITTED BY: [TOOL — BrowserBase or Playwright]
  TIMESTAMP  : [CURRENT DATE AND TIME]
  DATA SENT  : All fields as filled in Stage 2

  ⚠ THIS CANNOT BE UNDONE AFTER CONFIRMATION.
  Once submitted, the application is received by the employer.

  To confirm, type exactly: APPROVE SUBMIT
  To abort, type CANCEL or anything else."

STEP 2 — Execute (only after exact APPROVE SUBMIT received):
  Click the form's Submit button.
  Wait for the confirmation page or success message.
  Capture the confirmation reference number or text if displayed.
  Report: "Application submitted to [COMPANY_NAME] for [ROLE_TITLE].
    Confirmation: [REFERENCE or 'no reference number shown'].
    Timestamp: [DATE AND TIME].
    Proceeding to Phase 7."

STEP 3 — Failure after submission click:
  If the form returns an error after the Submit button is clicked:
  Report the exact error message shown.
  Do not retry automatically.
  Ask the user: "The submission returned an error: [ERROR]. Would you like
    to attempt resubmission, or would you prefer to contact the employer
    directly to confirm receipt?"
  Wait for instruction. Never resubmit without explicit user direction.

---
## Playwright Complexity Disclosure

Present this explanation to any user who has not used Playwright before,
triggered on first Playwright use per session:

  "Playwright MCP controls a real web browser programmatically to fill and
  navigate forms on your behalf. A few things to know before we use it:

  What it does well: it can fill text fields, select dropdown options,
  check boxes, and navigate between form pages — reliably on most job
  platforms like Greenhouse, Lever, and Breezy HR.

  Where it may fail: some platforms (LinkedIn, Indeed, Workday) use bot
  detection systems that can block Playwright mid-form. If this happens,
  I will stop immediately and switch to manual mode — you will never lose
  data you have already entered, and I will stage the remaining answers
  for manual paste.

  What it cannot do: it cannot solve CAPTCHAs, log into accounts without
  your credentials, or handle multi-factor authentication automatically.

  If any of this makes you uncomfortable, we can skip browser automation
  entirely and I will pre-stage all answers for manual entry instead.

  Do you want to proceed with Playwright, or prefer manual entry?"
