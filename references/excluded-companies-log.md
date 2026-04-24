# Excluded Companies and Application Outcomes Log
# Version: 1.0.0 | Generic Universal Edition
# Append after every discovery run and every session close.

---
## Hard Exclusion Rules

These are set by the candidate in the Applicant Profile under
[HARD_EXCLUSION_GEOGRAPHIES]. Apply at every Phase 0 search and before
presenting any results table. No candidate should see a role from an excluded
geography in any output.

Current exclusions for this profile:
  [EXCLUDED_GEOGRAPHY_1]
  [EXCLUDED_GEOGRAPHY_2]

---
## Application Outcomes Log

Format: Date | Company | HQ | Role | Level | Outcome | Notes
Outcomes: Submitted | Withdrawn | Rejected | Offer-Accepted | Offer-Declined

(Append after every Phase 7 session close)

---
## Excluded Companies Encountered in Discovery

Format: Date | Company | HQ Location | Reason | Role Title Encountered

(Append after every Phase 0 discovery run for any company filtered out)

---
## Update Protocol

After every Phase 0 run: scan all results for excluded geographies before
presenting the ranked table. Log every filtered company here.

After every Phase 7 close: append the session outcome to the Application
Outcomes Log regardless of branch (submitted, withdrawn, or rejected).

After every offer received: update salary-anchors-template.md with the
offered figure, currency, and outcome (accepted or declined).
