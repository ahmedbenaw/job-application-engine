# Application Log, Gap Log and Handoff Record — Templates
# job-application-engine v2.2.0 (generic)
# Read when: Phase 2 (start the gap log), any phase handoff (INT-02), Phase 7 (write the application log)

All three are written under `APPROVE UPDATE` (Tier 2), the same rule as the excluded-companies log.

## Handoff record (INT-02) — one per application, versioned

| Field | Written by |
|---|---|
| Job ID, post text, source, date | Phase 1 |
| Form questions, ATS platform | Phase 1 |
| Numbered requirements (must / nice) | Phase 2 Step 2A |
| Locked keyword list: term, requirement number, weight, variants | Phase 2 Step 2A |
| Seniority level and reasoning | Phase 2 Step 2A |
| Company brief | Phase 1 |
| Evidence map and fit verdict | Phase 2 |
| Gap log | Phase 2 onward |
| Knockout facts, country profile, positioning source | Phase 3 |
| CV version, fingerprint(s), gate report | Phase 3C |
| Combined verdict | Phase 6 |

A phase that changes a field writes a new version. Outputs built on the old version are marked stale and re-run.

## Gap log (REQ-39) — one per application

| Req # | Must / nice | What's missing | Offsetting evidence | Handled by (letter line · form answer · interview answer · skill to build) | Status |
|---|---|---|---|---|---|

Sources: fit mapping, keywords that couldn't be proven, unmet knockout criteria. Each gap appears once.

## Application log (GAP-13) — one row per application

| Field | Example |
|---|---|
| Job ID / company / role / level | ACME-123 / Acme / Senior PM / L3 |
| Positioning source | Track "Product Delivery" |
| CV fingerprint(s) | sha256 of DOCX (and PDF) |
| Gate verdict and grade | PASS · 5/5 |
| Must-have coverage before → after | 64% → 92% |
| Weighted coverage before → after | 58% → 88% |
| Fit verdict | Honest Stretch |
| Waivers | None |
| Scores and notes (M1–M5, complementary, the person's notes) | M1 5 · 2A 4 "missed one tool" · … |
| Date sent | 2026-10-05 |
| Follow-up window | 14 days |
| Outcome and date | No response / screen reject / interview / offer / withdrawn |

Phase 7 reviews read this log (GATE-17) to tune Default values, citing the outcome data behind each change.
