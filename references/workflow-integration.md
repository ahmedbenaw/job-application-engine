# Workflow Integration — order, handoffs, scores, logs
# job-application-engine v2.2.0 (generic)
# Read when: session start (scoring model); any phase handoff; Phase 6 combined verdict; A04 upload; Phase 7 logging

## Stage labels used in this file

The rules below use the spec's stage labels. In the engine they map to:

| Spec label | Engine phase |
|---|---|
| S1 | First-Use Setup (intake questionnaire) |
| S2 | Phase 0 Job Discovery |
| S3, M1 | Phase 1 Company Intelligence |
| S4 | Phase 2, Step 2A Job analysis |
| S5, M2 | Phase 2 Fit Analysis |
| S6, M3 | Phase 3 Clarifying Intake |
| S7, S8, S9, M4 | Phase 3B CV Build |
| S10 | Phase 3C ATS Gate |
| S11, M5 | Phase 4 Application Package |
| S12 | Phase 5 Writing Quality (package) |
| S13 | Phase 6 Governance (combined verdict) |
| S14 | A04 / A05 fill and submit |
| S15 | Phase 7 Post-Submission |

IDs (RES-, GAP-, REQ-, GATE-, INT-, INQ-, OUT-) point to docs/CV_ATS_REQUIREMENTS_SPEC_v0.11.0.md, the design record.

---

## Scoring and approval model

### RES-11 Hybrid approval model: 5 mandatory gates + complementary scores
- **Rule:** Five mandatory scored gates, each needing 5/5 to continue. A score below 5 opens a revision loop for the stages that gate covers:

  | Gate | Placed after | Covers | You judge |
  |---|---|---|---|
  | M1 Company brief | S3 | S3 | Is the company picture right? |
  | M2 Fit | S5 | S4–S5 | Is this role worth it, and is the evidence honest? |
  | M3 Facts | S6 | S6 | Are salary, availability, relocation and permit answers right? |
  | M4 CV text | S9 | S7–S9 | Does the CV represent you truthfully and sound like you? |
  | M5 Application package | S12 | S11–S12 | Are the cover letter, summary and answers right? |

  Every other stage gives a **complementary score**: S2 Discovery, S4 Job analysis, S8 CV critique, S10 ATS Gate, S13 Combined verdict, S15 After.
- **How complementary scores work:**
  1. **Automatic score (always):** each complementary stage scores itself 1–5 from its own checks. Default mapping: 5 = every check passes · 4 = Should-level issues only · 3 = 3 or more waivers or advisory warnings · 1–2 = a Must check failed (already blocking under that stage's own rules).
  2. **Your score (optional):** at any time before the next mandatory gate you can add a 1–5 score and one line on what a perfect result would have looked like. It never slows the flow unless it's below 5.
  3. **Roll-up:** each mandatory gate shows every complementary score since the previous gate (automatic, yours, and the notes). Your 5/5 at the mandatory gate confirms the whole stretch. Grades are also shown live, with reasons, as each step finishes (INT-05).
  4. **Escalation:** a complementary stage becomes a blocking gate when its automatic score is 3 or lower (confirmed by you, v0.4.1), or when you give it a score below 5. The 5/5 rule then applies to that stage until it's fixed.
  5. **Learning:** all scores and "perfect result" notes, mandatory and complementary, are saved to the application log (GAP-13) and reviewed against outcomes (GATE-17).
- **One-time setup check:** the engine's profile sign-off (first-use Step 3, see INQ-02) is a one-time check per person. It is not counted in the 5 per-application gates.
- **Separate from approval:** no score ever authorises an irreversible action. Submit, send, fill and changes to the master record keep their explicit approval (REQ-34).
- **Why:** Keeps 5/5 discipline where your judgment matters. Keeps the early warnings and feedback from every other stage without making each one a stop.
- **Acceptance:** Exactly 5 mandatory gates passed at 5/5 per application (Mode A and Mode B). 100% of complementary stages have an automatic score in the log. Every escalation is logged with its reason and resolved before the next mandatory gate. 0 irreversible actions without explicit approval.
- **No separate gate for S4:** the job-ad word list is reviewed at M2, together with the fit verdict (confirmed by you, v0.4.1).
- **Origin:** Your decision on Q-09 (hybrid) · **Basis:** Your decision (thresholds confirmed v0.4.1) · **Priority:** Must · **Status:** Accepted

### REQ-34 Approval gates
- **Requirement:** The candidate approves at the decisions that matter, without a gate at every step.
- **Spec:** Required approvals: fit verdict when it is a stretch or mismatch (REQ-10), any change to the master record (REQ-02), the final CV before export, and anything irreversible (submit, send, fill a live form) after a full preview of the data. Everything else runs without stopping.
- **Acceptance:** 0 irreversible actions without explicit approval. Routine steps don't block.
- **Best today:** Full (gates on every phase, which is heavy) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

## Integration rules

### INT-01 Stage preconditions (facts before writing)
- **Requirement:** No stage may produce CV or application text until its preconditions are met.
- **Spec:**

  | Stage produces | Requires first |
  |---|---|
  | Locked keyword list | Job post captured (REQ-04) · requirements classified (REQ-05) |
  | CV text | Fit verdict recorded (REQ-10) · gap log started (REQ-39) · knockout facts confirmed (REQ-29) · regional profile chosen (GAP-07) · positioning source chosen (RES-10) · keyword list locked (REQ-06) |
  | ATS Gate run | CV text passed at mandatory gate M4 (RES-11) · all GATE-01 inputs present |
  | Application package | ATS Gate PASS · salary and portfolio confirmed · a product observation, if the company has a public product |
  | Submission | Combined final verdict PASS (INT-04) · explicit approval (REQ-34) |

- **Acceptance:** 0 outputs produced with an unmet precondition. A blocked stage names the missing precondition and the stage that supplies it.
- **Origin:** Merge conflict "CV written before intake clears" · **Priority:** Must · **Status:** Proposed

### INT-02 Structured handoffs between stages
- **Requirement:** Stages pass defined data to each other instead of re-deriving it.
- **Spec:** One handoff record per application, with versioned fields:
  - job ID and post text (REQ-04)
  - numbered requirements with must/nice tags (REQ-05)
  - locked keyword list with weights and variants (REQ-06, GAP-05)
  - seniority level and reasoning (REQ-07)
  - company brief (REQ-08)
  - evidence map and fit verdict (REQ-09, REQ-10)
  - gap log (REQ-39)
  - knockout facts (REQ-29)
  - regional and platform profiles (GAP-07, REQ-30)
  - positioning source (RES-10)
  - CV version and fingerprint (GATE-14)
  - gate report (GATE-13)

  A stage that changes a field writes a new version of it. Every later output built on the old version is marked stale and must be re-run.
- **Acceptance:** Every stage reads its inputs from the handoff record. Changing an upstream field marks every dependent output as stale.
- **Origin:** Stage alignment "Fit": requirements weren't handed over · **Priority:** Must · **Status:** Proposed

### INT-03 Protected terms in every text-changing step
- **Requirement:** Every step that rewrites text receives the locked keyword list and leaves those terms unchanged (RES-02).
- **Spec:** Applies to style and AI-pattern passes (REQ-32), shortening for form limits (GAP-12), translation, and export (GATE-05). Each step reports a before/after check of the protected terms.
- **Acceptance:** The protected-term check shows no changes, for every step.
- **Origin:** Merge conflict "anti-AI pass rewrites locked keywords" · **Priority:** Must · **Status:** Proposed

### INT-04 One final verdict before submission
- **Requirement:** Submission requires one combined verdict covering both the CV and the application.
- **Spec:** The combined report contains the ATS Gate report (GATE-13), the application checklist (REQ-33), the public-profile consistency check (GAP-10) and confirmation that every gap-log entry has been handled (REQ-39). Verdict is PASS only if the gate is PASS or PASS WITH WAIVERS and every application Must check passes. Claim tracing runs once (GATE-07) and is reused, not repeated. The most important failure is shown first.
- **Acceptance:** 100% of submissions have one combined PASS report. 0 submissions where only one half passed.
- **Origin:** Merge conflict "two final gates, no combined verdict" · **Priority:** Must · **Status:** Proposed

### INT-05 Every grade is visible, with its reason
- **Requirement:** Every step that doesn't stop you shows its grade the moment it finishes, with the reason, and shows it again at the next stop.
- **Spec:**
  1. **Live line:** as each step finishes, show one line: step name · grade 1–5 · what failed or warned, in plain words · whether it is stopping you. Example: "ATS test: 4/5 · 2 warnings: file is 2.4 MB (limit 2 MB), skim test missed your job title. Not stopping."
  2. **Always a reason:** a grade below 5 always lists every check that failed or warned. A 5 says "all checks passed".
  3. **Roll-up:** each mandatory stop (M1–M5) repeats these lines for every step since the previous stop, before asking for your 5/5.
  4. **Where each grade shows:** Find jobs → M1 · Read the job ad → M2 · CV check → M4 · ATS test → M5 · Final check → just before APPROVE SUBMIT · After sending → at the start of your next application.
  5. **Wording:** steps of this kind are called "Doesn't stop you", never "background" or "hidden".
- **Acceptance:** 100% of these steps show a live line when they finish. 0 grades below 5 without a listed reason. Every grade appears again at its roll-up point.
- **Origin:** Your question on hidden grades (v0.5.0) · **Priority:** Must · **Status:** Accepted

### INT-06 Job analysis and fit check share one requirement list
- **Requirement:** Step 2A (S4, job analysis) and the fit check (S5) work from one shared, numbered requirement list, so they can never disagree.
- **Spec:**
  - Step 2A numbers every requirement (REQ-05). Every must-have keyword is linked to the requirement it came from.
  - The fit check uses the same numbers. Each requirement carries its keywords, its evidence (REQ-09) and its fit result.
  - Nothing exists in one and not the other: no keyword without a requirement, and no requirement without its keywords.
  - A keyword that can't be proven goes into the gap log once, under its requirement number. It is never logged twice.
  - At M2, the Step 2A grade line and the fit verdict are shown together, side by side.
- **Acceptance:** 0 keywords without a requirement number. 0 requirements in the fit check without their keywords. 0 duplicate gap-log entries.
- **Origin:** Your decision on Q-12 (keep Step 2A, zero conflict with the fit check) · **Priority:** Must · **Status:** Accepted

## Logs and after-submission

### REQ-39 Gap log
- **Requirement:** Keep one gap log per application, started at the fit check and carried through every later stage.
- **Spec:** Each entry: requirement ID (REQ-05), must-have or nice-to-have, what's missing, offsetting evidence (if any), how it's handled (cover-letter line, form answer, interview answer, skill to build), status. Entries come from the fit mapping (REQ-09), keywords that couldn't be proven (RES-01) and knockout criteria not met (REQ-29).
- **Acceptance:** 100% of unproven must-haves and unmet knockouts are in the log, and each has a handling decision before the application package is written.
- **Best today:** None (a gap is stated once and then dropped) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GAP-11 The submitted file is the tested file
- **Requirement:** Only the file frozen by the latest ATS Gate PASS for this job (GATE-14) may be uploaded or attached.
- **Spec:** The submission step receives the file and its fingerprint from the gate report, never a user-supplied or default file. Before uploading: recompute the fingerprint, compare it with the report, and confirm the job ID matches. If no PASS exists or the fingerprints differ, stop and say why. The same rule applies to email attachments and portal re-uploads. After uploading, record the fingerprint in the application log (GAP-13).
- **Acceptance:** 100% of submissions have a recorded fingerprint that equals a PASS report for the same job (OUT-4). 0 uploads of an untested file.
- **Origin:** Neither covers ("upload the tailored, gated CV") · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GAP-13 Link outcomes to the CV that was sent
- **Requirement:** Record every application outcome against the exact CV version and gate results, so later changes are based on what worked.
- **Spec:** Application log fields: job ID, company, role, level, positioning source (RES-10), CV fingerprint, gate verdict, must-have coverage %, weighted coverage %, fit verdict, waivers, date sent, outcome (no response, screen reject, interview, offer, withdrawn) and outcome date. GATE-17 reviews read from this log.
  - **Follow-up window (Answered: Q-10):** set per application from the company research. Fast-moving employers (startups, agencies): 7 days. Most companies: 14 days. Large corporate, public sector or government: 21 days. 21 days is the maximum; the usual range is 7–14. The person can shorten it for any application.
- **Acceptance:** 100% of submitted applications have every field filled. Outcome updated within the follow-up window.
- **Origin:** Neither covers ("learning which CV choices work") · **Priority:** Should · **Scope:** Adjacent · **Status:** Proposed

### GAP-14 Interview prep from the gap log
- **Requirement:** Turn every logged gap and every featured claim into prepared interview material once an interview is booked.
- **When (Answered: Q-11):** by default, prep is made when an interview is booked. A short prep sheet at submission is made only if the person asks for it and approves.
- **Spec:** For each gap: a short, honest answer (what's missing, the offsetting evidence, the plan to close it). For each lead achievement on the CV: a 60–90 second story (situation, action, result, metric) that matches the CV wording. For each knockout fact: a consistent one-line answer. Stored with the application's evidence pack (GATE-16).
- **Acceptance:** Every entry in the gap log (REQ-39) and every lead achievement (REQ-09) has prepared material before the interview takes place.
- **Origin:** Neither covers ("interview prep from the gap log") · **Priority:** Could · **Scope:** Adjacent · **Status:** Proposed

### REQ-33 Final pre-submit check
- **Requirement:** See **GAP-06** for the CV. A separate application checklist covers the form and cover letter.
- **Spec (application checklist):** Every required field filled or flagged · no leftover placeholders · salary entered as a single number in the right currency unless a range is required · portfolio field is a valid URL · cover letter within RES-08 limits · any fit gap acknowledged (REQ-10).
- **Acceptance:** Both checklists fully pass.
- **Best today:** Full (application only, no CV checks) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GAP-10 Consistency across public profiles
- **Requirement:** Job titles, companies and dates on the CV match the candidate's public profiles (e.g. LinkedIn).
- **Spec:** Compare each role field by field. Allowed differences: CV-only tailored headline and wording. Not allowed: title, company or date mismatches.
- **Acceptance:** 0 unexplained title, company or date mismatches.
- **Origin:** G10 · **Basis:** Default · **Priority:** Could · **Scope:** Core · **Status:** Proposed
