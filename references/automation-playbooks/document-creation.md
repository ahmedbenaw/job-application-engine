# Document Creation Playbook
# Automation IDs: A06, A07, A09
# Version: 2.0.0 | Part of job-application-engine automation layer
# Consent tiers: A06=2 (APPROVE CREATE), A07=2 (APPROVE CREATE), A09=2 (APPROVE SAVE)

---
## Purpose

Covers all document creation and storage actions: cover letter DOCX (A06),
full application package document (A07), and cloud storage save (A09).
All document creation actions present the file for local download first.
Cloud save is always a separate, subsequent action requiring its own consent.

---
## Document Storage Sequence (mandatory for all document actions)

This sequence is invariant. It must be followed for every document created.

STEP 1 — Create the document using bash_tool and create_file.
STEP 2 — Present for local download using present_files.
          Do this immediately after creation, before any other action.
STEP 3 — After local download is offered, ask:
          "Would you also like to save this to cloud storage?"
STEP 4 — If yes: present cloud provider options, confirm folder path,
          execute Tier 2 cloud save (A09).
STEP 5 — If no: proceed. The file is available locally. Never save to cloud
          without explicit consent.

Never reverse this sequence. Never offer cloud save before local download.

---
## A06 — Cover Letter DOCX Creation

### When to Trigger

Phase 4 — after the Application Package scores 5 at the Phase 4 scoring gate.
Offer as an automation recommendation after the scoring gate confirmation.

### Consent Gate (Tier 2 — APPROVE CREATE)

  "TIER 2 CONSENT GATE — COVER LETTER DOCUMENT
  ──────────────────────────────────────────────
  ACTION    : Create a DOCX cover letter
  FILENAME  : CoverLetter_[CANDIDATE_NAME]_[COMPANY_NAME]_[DATE].docx
  CONTENTS  : The humanized cover letter from Phase 4 output
  FORMAT    : Professional DOCX — standard cover letter formatting
  REVERSIBLE: Yes — file can be deleted after download
  Type APPROVE CREATE to generate, or SKIP."

### Creation Specifications

Filename format: CoverLetter_[CANDIDATE_NAME]_[COMPANY_NAME]_[DATE].docx
Font: match the CV font specified in the applicant profile. If unknown,
  default to Calibri 11pt for body, 14pt for name header.
Margins: 1 inch (2.54cm) on all sides — standard professional format.
Header: Candidate name, email, phone, LinkedIn on separate lines (right or
  centred — match the profile's stated CV format preference).
Date: full date below the header.
Addressee block: hiring manager name and title if identified in Phase 1.
Body: the full humanized cover letter from Phase 4, no additions.
Signature: "Sincerely," followed by the candidate's typed name.
Footer: none — keep it clean.

### Fallback

If bash_tool is unavailable, present the cover letter text in a clearly
labelled code block formatted for copy-paste into a word processor.
Provide formatting instructions: "Paste this into a blank Word document.
  Set font to [FONT], margins to 1 inch, and format the header block
  with your name and contact details aligned to the right."

---
## A07 — Full Application Package Document

### When to Trigger

Phase 6 — after all 8 Governance Gate checks pass.
Offer as an automation recommendation with the governance pass report.
Purpose: a complete session record of everything submitted — for the
  candidate's own records and future reference.

### Consent Gate (Tier 2 — APPROVE CREATE)

  "TIER 2 CONSENT GATE — FULL APPLICATION PACKAGE DOCUMENT
  ──────────────────────────────────────────────────────────
  ACTION    : Create a complete application record document
  FILENAME  : AppPackage_[CANDIDATE_NAME]_[COMPANY_NAME]_[DATE].docx
  CONTENTS  : All items listed below
  FORMAT    : DOCX or PDF — which would you prefer?
  REVERSIBLE: Yes
  Type APPROVE CREATE to generate, or SKIP."

Ask the user for their format preference (DOCX or PDF) before generating.

### Document Contents (in this order)

Section 1 — Session Summary:
  Company name, role title, application date, platform submitted to,
  fit verdict from Phase 2, salary figure stated, start date stated.

Section 2 — Company Intelligence Brief:
  The full brief from Phase 1 — what the company does, funding stage,
  tech stack, culture signals, hiring manager name.

Section 3 — Fit Analysis:
  The verdict, evidence mapping summary, gap statement, and compensating
  evidence from Phase 2.

Section 4 — Cover Letter:
  The full humanized cover letter as submitted.

Section 5 — Custom Question Answers:
  Each question printed in full followed by the full answer.

Section 6 — Standard Form Fields:
  A complete record of all standard form field values used.

Section 7 — Next Actions:
  Follow-up date (if calendar reminder was created).
  Notes on any outstanding items.

### Fallback

If bash_tool is unavailable, present all sections as clearly labelled
conversation output with a note: "Copy and paste these sections into a
document for your records."

---
## A09 — Cloud Document Save

### When to Trigger

After any document creation action (A06 or A07) where the user responds
"yes" to the cloud save question. Never trigger independently.

### Provider Selection

Present all active cloud storage MCPs detected in the Capability Map.
Ask the user which to use for this specific save.
Never assume the same provider will be used across different saves.

  "CLOUD STORAGE SELECTION
  ─────────────────────────────────────────────
  Available cloud storage this session:
    [List each active cloud MCP]
  Which would you like to save to?"

### Folder Path Protocol

After provider selection, suggest a folder path based on session context:
  Suggested path: Job Applications / [COMPANY_NAME] / [DATE]

Present the suggestion and ask:
  "Save to: [SUGGESTED PATH]? Or type a different path."

Wait for confirmation or a modified path before executing the save.

### Consent Gate (Tier 2 — APPROVE SAVE)

  "TIER 2 CONSENT GATE — CLOUD DOCUMENT SAVE
  ──────────────────────────────────────────
  ACTION    : Save document to [PROVIDER_NAME]
  FILE      : [FILENAME]
  LOCATION  : [CONFIRMED_FOLDER_PATH]
  REVERSIBLE: Yes — file can be deleted from cloud storage
  Type APPROVE SAVE to save, or SKIP."

### Execution

After exact APPROVE SAVE received: execute the upload using the selected
cloud MCP. Confirm the save location to the user after completion.
  "Saved to [PROVIDER]: [FULL_PATH/FILENAME]"

### Fallback

If the selected cloud MCP fails or is unavailable:
  Report the failure.
  Confirm the file is already available locally from the present_files step.
  Offer to try an alternative cloud provider if one is active.
  Never retry the failed provider automatically.

---
## Document Naming Convention

All documents produced by this skill follow this naming format:
  [DOCTYPE]_[CANDIDATE_NAME]_[COMPANY_NAME]_[DATE].[EXT]
  Example: CoverLetter_AlexM_CloudBaseInc_2026-04-24.docx
  Example: AppPackage_AlexM_CloudBaseInc_2026-04-24.pdf

Spaces replaced with nothing (no underscores in company names with spaces —
use CamelCase): CloudBaseInc not Cloud_Base_Inc.
Date format: YYYY-MM-DD always.
