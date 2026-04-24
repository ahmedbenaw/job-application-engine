# Email Actions Playbook
# Automation IDs: A08, A11
# Version: 2.0.0 | Part of job-application-engine automation layer
# Consent tier: A08=3 (APPROVE SEND external), A11=2 (APPROVE SEND to self)

---
## Purpose

Covers all email actions within the skill's scope: follow-up and
clarification emails to hiring managers or recruiters (A08), and
confirmation emails to the user's own address as a personal record (A11).
No other email actions are permitted.

---
## Email Selection Protocol (applies to all email actions)

Never assume which email system to use. Never hardcode a default.
Never carry a selection across sessions.

On first email action in the session:
  Present all active email MCPs detected in the Capability Map.
  Example prompt:
  ─────────────────────────────────────────────────────────────
  EMAIL SYSTEM SELECTION
  Available this session: [list each active MCP]
  Last used this session: None yet
  Which would you like to use for this email?
  ─────────────────────────────────────────────────────────────
  Store the user's selection as [SESSION_EMAIL_CHOICE].

On subsequent email actions in the same session:
  Show: "Last used this session: [SESSION_EMAIL_CHOICE]"
  Ask: "Use the same system, or switch to another?"
  If switching: show the available options again.
  Do not assume the same system will be used for every email.

---
## A08 — Hiring Manager or Recruiter Email

### When to Trigger

Phase 3 (Clarifying Intake): if a critical piece of information cannot be
  found through web research and contacting the hiring manager directly
  would unblock Phase 4 — for example, if the application form is entirely
  inaccessible, if the deadline is not publicly listed, or if a role
  detail is ambiguous enough to affect how the candidate positions themselves.
  Offer this as an option — never trigger automatically.

Phase 7 (Post-Submission, Branch A): if the user wants to send a
  professional follow-up email after a defined interval (typically 5–7
  business days after submission). Offer this proactively as part of
  Branch A handling.

### Draft Construction Rules

Subject line: specific and professional. Format:
  "[ROLE_TITLE] Application — [CANDIDATE_NAME]" for follow-ups
  "[ROLE_TITLE] — Quick Question" for Phase 3 clarifications

Tone: professional, concise, respectful of the recipient's time.
  Maximum 3 short paragraphs. No flowery language. No AI-pattern language.
  Pass through Writing Quality module before presenting draft.

Content for Phase 3 clarification email:
  Para 1: Introduce the candidate and the application context. Name the role.
  Para 2: State the specific question — one question only per email.
  Para 3: Thank the recipient and offer availability for any further context.

Content for Phase 7 follow-up email:
  Para 1: Reference the submission date and role. Express continued interest.
  Para 2: Briefly restate the strongest fit signal — one sentence.
  Para 3: Offer to provide any additional information. State next contact intent.

### Consent Gate (Tier 3 — APPROVE SEND)

Present the full Tier 3 gate before sending any external email:

  "TIER 3 CONSENT GATE — EMAIL TO EXTERNAL RECIPIENT
  ─────────────────────────────────────────────────────
  RECIPIENT  : [HIRING_MANAGER_NAME] — [EMAIL_ADDRESS]
  SUBJECT    : [SUBJECT_LINE]
  SENDING FROM: [USER_EMAIL via SESSION_EMAIL_CHOICE]
  BODY PREVIEW: [Full email body]
  ⚠ THIS EMAIL CANNOT BE RECALLED AFTER SENDING.

  Type APPROVE SEND to send, or CANCEL to abort."

Exact match required: APPROVE SEND only.
Any other response cancels the action and presents the draft for manual use.

### Fallback

If no email MCP is active, present the full email draft in copy-paste
format with the recipient address, subject, and body clearly labelled.
Instruct the user to send it manually from their email client.

---
## A11 — Confirmation Email to Self

### When to Trigger

Phase 7 (Post-Submission, Branch A) only.
Offered as an optional action after the application is confirmed submitted.
Purpose: creates a personal email record of exactly what was submitted,
  to which company, on which date.

### Draft Construction Rules

Recipient: user's own email address only. No exceptions.
Subject: "Application Record — [ROLE_TITLE] at [COMPANY_NAME] — [DATE]"
Body: structured summary of:
  - Company and role
  - Date and time of submission
  - Platform submitted to
  - Salary figure stated
  - Cover letter (pasted in full)
  - All custom question answers
  - Fit verdict from Phase 2
  - Next follow-up date if a calendar reminder was set

### Consent Gate (Tier 2 — APPROVE SEND)

  "TIER 2 CONSENT GATE — CONFIRMATION EMAIL TO SELF
  ──────────────────────────────────────────────────
  RECIPIENT  : [USER'S OWN EMAIL ADDRESS]
  SUBJECT    : Application Record — [ROLE_TITLE] at [COMPANY_NAME]
  CONTENTS   : Full application package summary (see above)
  REVERSIBLE : Yes — email stays in your Sent folder
  Type APPROVE SEND to send, or SKIP to continue without."

### Fallback

Present the full application record inline in the conversation as a
formatted document. Offer A07 (Application Package DOCX) as an
alternative if the user wants a saved file instead.

---
## Scope Boundary

Email actions in this skill are strictly limited to:
  1. One email to the target company's hiring manager or recruiter (A08)
  2. One confirmation email to the user's own address (A11)

The following are explicitly out of scope and must not be triggered
regardless of user request:
  Mass or bulk email sends
  Emails to references, former employers, or third parties
  Marketing or networking emails
  Any email unrelated to the active application session
  Automated follow-up sequences without per-email consent
