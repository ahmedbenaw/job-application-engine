# CV & ATS Requirements Spec

| Field | Value |
|---|---|
| Version | 0.11.0 (draft) |
| Created | 2026-10-05 |
| Last updated | 2026-10-05 (v0.11.0: capability wording INT-11; self-test reads frontmatter values; v0.10.1: release audit; v0.10.0: fallback ladder, harness, hooks) |
| Owner | Ben |
| Target | The **next version of the generic job-application-engine** (current: v2.1.1, generic-universal edition). This spec is not for any personal edition. Editions built on the generic engine inherit it |
| Implemented in | job-application-engine v2.2.0 (generic), built and tested 2026-10-05: 6 test cases at 100% (40/40), self-test 90/90 |
| Scope | Creating and refining a CV so it passes applicant tracking system (ATS) screening, plus the application steps around the CV |
| Derived from | "CV Skills ATS Map" (4 tools compared, 37 abilities, 8 contradictions, 10 gaps) and "Workflow vs Engine Map" (39 capabilities, 15 stages, 7 merge conflicts), and the "CV Information Collection Questionnaire, Universal Edition v3" |
| Tool-agnostic | Yes for Parts 0–6 (including 5A) and 8–10: no requirement names or depends on a specific skill, plugin or product. Part 7 applies the spec to the generic job-application-engine, as requested |

---

## How to use and update this file

1. **Single source of truth.** Each rule is written once and other items link to it by ID. Never copy a spec into two places.
2. **IDs are permanent.** Never reuse or renumber an ID. Retire an item by setting its status to `Deprecated` and noting why.
3. **Status values:** `Proposed` → `Accepted` → `Implemented` → `Verified` (passed its acceptance test) · `Deprecated`.
4. **Priority (MoSCoW):** `Must` = without it a screen can fail · `Should` = clear quality gain · `Could` = nice to have.
5. **Scope:** `Core` = affects the CV or its ATS result · `Adjacent` = around the CV (cover letter, forms, tracking).
6. **Basis** says how firm a number is: `Evidence` = observed ATS behaviour or common recruiter practice · `Convention` = widely used standard · `Default` = proposed starting value, tune it over time.
7. **Every change** gets a line in the Change log (bottom), and the version number goes up: patch for wording; minor for new items or changes to Proposed items (including tuning any value marked Default); major only when an Accepted item's acceptance criteria change.
8. **New items** use the templates in Part 10.
9. **Part 6 is the extraction register.** Every capability or stage found missing, split or conflicting in a compared workflow is listed there with the spec items that cover it. Record new comparisons there first, then add or extend items.
10. **Part 7 must stay in sync.** When an item is added, map it to at least one stage in Part 7.1.
11. **Version snapshots.** Every new version is also saved as a full copy in the `spec-versions/` folder, named `cv-ats-requirements-spec_vX.Y.Z.md`. The main file is always the latest. Snapshots exist from v0.2.0; v0.1.0, v0.4.0 and v0.4.1 are described in the Change log only.
12. **Generic engine only.** Every change must keep the next generic engine version fully compatible with v2.1.1 (Part 7.9). Nothing personal goes in this spec.

### ID scheme

| Prefix | Meaning | Part |
|---|---|---|
| `OUT-` | Measurable outcome (what "100%" means) | 0 |
| `RES-` | Rule that resolves a contradiction | 1 |
| `GAP-` | Requirement that closes a gap no tool covers | 2 |
| `REQ-` | Requirement for one ability in the coverage map | 3 |
| `GATE-` | ATS Gate: checks run on the final file before submission | 4 |
| `INT-` | Workflow integration: stage order, handoffs and the final verdict | 5 |
| `INQ-` | Intake questionnaire rules | 5A |
| `Q0.1`–`Q13.1` | Intake questionnaire field (labels, not requirements) | 5A |
| `S0`–`S15` | Stage in the proposed engine workflow (labels, not requirements) | 7 |

---

## Glossary (plain language)

| Term | Meaning |
|---|---|
| ATS | Applicant tracking system: software employers use to receive, read, rank and filter applications |
| Parse / read | The ATS pulling text out of your file and sorting it into fields (name, job titles, dates, skills) |
| Knockout question | A yes/no or fixed-answer form question that rejects you automatically (e.g. "Do you have a work permit for Germany?") |
| Keyword | A skill, tool, title, method or certification term in the job post that the ATS or a recruiter searches for |
| Must-have term | A keyword tied to a mandatory requirement in the job post |
| Keyword coverage | Share of must-have terms that appear in the CV in the job post's exact wording |
| Master record | The full, honest list of everything you've done, wider than any single CV |
| Evidence | A specific item in the master record (company + role + outcome or metric) that proves a claim |
| Locked keyword | A job-post term that later editing steps are not allowed to reword |
| Track | One of your positioning angles (e.g. product delivery, venture building) with its own master CV |
| Seniority level | How senior a role is, judged by scope and reporting line rather than the title alone (scale L0 = entry to L7 = C-suite) |
| Handoff | A defined set of data one stage passes to the next, so later stages don't have to re-guess it |
| Gap log | The running list of requirements you can't fully prove, carried from the fit check to the cover letter and interview prep |
| Precondition | Something that must already be true before a stage is allowed to start |
| Fingerprint | A unique code calculated from a file's bytes. If even one byte changes, the code changes |
| Verdict | The single pass/fail result of a gate |
| Checkpoint | A point where you are asked to review and approve before the workflow continues |
| Mandatory gate | A scored stop that needs 5/5 from you before the workflow continues |
| Complementary score | A score given to a step that doesn't stop you. It is shown right away with its reason, shown again at the next mandatory gate, and blocks only when escalated |
| Escalation | A complementary stage turning into a blocking gate because its score shows a problem |
| Intake questionnaire | The one-time form a person fills to build their master record and base CVs (Part 5A) |
| Track | One type of role a person targets. Each filled Section 1 of the form is one track, with its own base CV |
| Privacy class | Whether a form answer may appear on a CV: CV, Private (never printed) or Ask (only if the market expects it and the person agrees) |
| Readiness grade | The 1–5 grade showing how complete the intake form is |

---

## Part 0 — What "100%" means

No CV can be guaranteed to pass every ATS. Systems parse files differently, many rejections come from knockout questions rather than CV text, and a human still filters the ranked list. "100%" is therefore defined as four measurable outcomes. All four must pass before anything is submitted.

| ID | Outcome | Pass condition | Basis |
|---|---|---|---|
| OUT-1 | **Readable** | 100% of critical fields come out of the final file exactly right: name, email, phone, LinkedIn URL, every job title, every company, every date range, every section heading (GAP-01) | Evidence |
| OUT-2 | **Matched** | 100% of must-have terms are accounted for: each one is either in the CV in exact wording **with evidence**, or logged as a gap with a plan. Target: at least 90% present (REQ-27) | Default |
| OUT-3 | **Not knocked out** | 100% of knockout criteria in the post (location, work permit, relocation, notice, years, language, certifications) are checked against your facts and answered truthfully on the form and, where useful, on the CV (REQ-29, GAP-04) | Evidence |
| OUT-4 | **Delivered as tested** | 100% of submissions send the exact file that passed the ATS Gate (matching fingerprint) together with application answers that passed the combined final verdict (GAP-11, INT-04) | Default |

**Hard rule across all outcomes:** zero invented claims (RES-01, REQ-11).

---

## Part 1 — Rules that resolve contradictions

These rules settle points where existing approaches give opposite instructions.

### RES-01 Add a keyword only with evidence
- **Rule:** A missing job-post term may be added to the CV only if the master record contains evidence for it. Otherwise it goes on the gap log with a plan (cover letter, interview answer or skill to build).
- **Why:** An unproven keyword may get past the ATS but fails the interview, and it breaks the no-invention rule.
- **Acceptance:** Every keyword added during tailoring links to at least one evidence item. Count of unlinked added keywords = 0.
- **Origin:** C1 · **Priority:** Must · **Status:** Proposed

### RES-02 Locked keywords are exempt from style editing
- **Rule:** Before any rewriting for tone, readability or "less AI-sounding" text, the job-post keywords are locked. Later steps may reword the text around them but never the keywords themselves (spelling, hyphenation, word order, singular/plural).
- **Why:** ATS matching is literal. Varying "cross-functional" into "cross functional" can cost a match.
- **Acceptance:** Diff of locked terms before vs after editing = no changes.
- **Origin:** C2 · **Priority:** Must · **Status:** Proposed

### RES-03 One rubric, one definition per term
- **Rule:** Keep a single canonical review rubric. The scorecard rows must be exactly the rules the rubric explains, and each term (e.g. the parts of the bullet formula) has one definition used everywhere.
- **Why:** Two lists with the same name produce scores that can't be compared or acted on.
- **Acceptance:** Every scorecard row maps 1:1 to a rubric rule with evaluation criteria. A glossary check finds no term defined twice.
- **Origin:** C3 · **Priority:** Should · **Status:** Proposed

### RES-04 Bullet formula: outcome, metric, method (+ optional keyword detail)
- **Rule:** Default bullet = **Outcome** (what changed) + **Metric** (how much, worked into the sentence naturally) + **Method** (how you did it). Add a fourth **Specific** clause only when it carries a locked keyword (a tool, method or context named in the post).
- **Why:** The extra clause has ATS value only when it carries a keyword. Otherwise it just lengthens the bullet.
- **Acceptance:** 100% of bullets start with a past-tense action verb and state an outcome. A metric appears wherever the master record has one. No literal "as measured by". Every Specific clause contains a locked keyword.
- **Origin:** C4 · **Priority:** Must · **Status:** Proposed

### RES-05 Skills: block near the top, proof in the bullets
- **Rule:** Include a short skills block directly under the summary, written in the job post's exact wording. Every skill listed must also be proven in at least one experience bullet.
- **Why:** Skills sections are often read as their own ATS field, while recruiters trust skills shown in action.
- **Acceptance:** 8–12 skills (Default). Each listed skill appears in, or links to, at least one bullet.
- **Origin:** C5 · **Priority:** Must · **Status:** Proposed

### RES-06 Summary: 3 sentences, at most 60 words
- **Rule:** Sentence 1: years of experience + domain + target title. Sentence 2: 1–2 proof points with metrics. Sentence 3: value for this employer, including the post's top keyword.
- **Why:** Short enough for a 6–10 second skim and long enough to carry the top keywords early, where both ATS and recruiters look first.
- **Acceptance:** ≤3 sentences, ≤60 words (Default), at least 2 locked keywords, no generic self-descriptions (see REQ-14 banned list).
- **Origin:** C6 · **Priority:** Should · **Status:** Proposed

### RES-07 Cover letter closes with a committed follow-up
- **Rule:** The last paragraph commits to an action with a date ("I'll follow up on [date]"). Passive closes are banned: "I look forward to hearing from you", "I look forward to your reply", "please call me at your earliest convenience", "To Whom It May Concern" (as a greeting).
- **Acceptance:** 0 banned phrases. The close contains a dated action.
- **Origin:** C7 · **Priority:** Should · **Status:** Proposed

### RES-08 Cover letter length set by channel
- **Rule:** Email or online message: 200–250 words. Form text box: ≤450 words, or the form's limit if lower. Attached document: ≤500 words, one page.
- **Acceptance:** Word count within the limit for the declared channel.
- **Origin:** C8 · **Basis:** Default · **Priority:** Should · **Status:** Proposed

### RES-09 Approval budget
- **Rule:** In a multi-stage workflow, ask for a scored approval at 3 checkpoints only: (1) after the fit check and fact intake, (2) after the CV text has been critiqued, (3) before submission, on a full preview. Automatic gates (ATS Gate, final checklists) decide pass/fail on their own. Irreversible actions (submit, send, fill a live form) and changes to the master record always keep their explicit approval (REQ-34).
- **Why:** A score at every stage adds friction without adding safety. The automatic gates carry the safety.
- **Acceptance:** At most 3 scored approvals per application, plus an explicit approval for each irreversible action and record change. 0 irreversible actions without approval.
- **Origin:** Merge conflict "too many approval gates" · **Basis:** Default · **Priority:** Should · **Status:** Deprecated (v0.4.0). Replaced by RES-11: you chose the hybrid model.

### RES-10 Positioning source fallback
- **Rule:** Choose the CV starting point in this order: (1) the positioning track that matches the job's main requirement (GAP-08); (2) if no tracks are defined, the version that matches the role's seniority level (REQ-07); (3) otherwise the general master CV. Record which one was used and why.
- **Why:** A workflow that assumes tracks breaks on profiles that only have level-based versions, and the reverse.
- **Acceptance:** Every tailored CV records its source and the rule step that selected it. The workflow runs correctly with 0 tracks defined.
- **Origin:** Merge conflict "summary versions assume one profile type" · **Priority:** Should · **Status:** Proposed

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

---

## Part 2 — Requirements that close gaps no tool covers

### GAP-01 Read test on the final file
- **Requirement:** Before submission, extract the text from the exact file being sent, the way an ATS would, and check it field by field.
- **Spec:**
  - Run 2 independent text readers as the standard (one plain-text, one layout-aware). If only 1 is available, run 1 and flag it in the report. (Answered: Q-05)
  - Then review the file visually, as both an ATS and a recruiter would (GATE-18).
  - Compare extracted values with the master record for the critical fields in OUT-1.
  - Check that reading order survives (no merged columns, no sentences interleaved across sections).
  - Check that nothing comes out garbled (broken characters, ligatures split, bullets turned into symbols).
  - Check that contact details appear in the first lines of the extracted text, not only in a page header or footer.
- **Acceptance:** 100% of critical fields match exactly in both extractors. 0 reading-order breaks. 0 garbled characters.
- **Origin:** G1 · **Basis:** Evidence · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GAP-02 Submit-ready file with a parse-safe layout
- **Requirement:** Every tailored CV is delivered as a real file ready for upload, built to a layout that ATS parsers read reliably.
- **Spec:**
  - **Formats:** DOCX and a text-based PDF (selectable text, fonts embedded, not a scanned image). Use whichever the portal asks for. If it doesn't say, send **DOCX as the main file**. If the portal accepts more than one file, upload the PDF as well. Both files come from the same gate PASS and both are fingerprinted (GATE-14, GAP-11). (Answered: Q-01)
  - **Layout:** single column. No tables, text boxes, multi-column sections, images, icons, logos, charts or skill-rating bars.
  - **Contact details** in the body text, not inside the page header or footer.
  - **Fonts:** one standard font (e.g. Calibri, Arial, Helvetica, Georgia), 10–12 pt body, 14–18 pt name.
  - **Bullets:** standard round bullets or hyphens only.
  - **Links:** URLs written out in full.
  - **File name:** `Firstname-Lastname-CV-[Role].[ext]`. No spaces or special characters.
- **Acceptance:** Passes GAP-01. A layout lint reports 0 tables, 0 text boxes, 0 images, 0 header/footer text and exactly 1 column.
- **Origin:** G2 · **Basis:** Evidence/Convention · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GAP-03 Counted keyword coverage, before vs after
- **Requirement:** Measure keyword coverage by counting, not judgement, and report it for the original CV and the tailored CV.
- **Spec:**
  - Input is the locked keyword list (REQ-06), with each term tagged must-have or nice-to-have and weighted by how often the post repeats it.
  - Matching counts the exact form plus its declared variants (GAP-05).
  - Output is a table: term | weight | in original? | in tailored? | where (section) | evidence ID | gap note.
- **Acceptance:** Report shows must-have coverage % and weighted coverage % for both versions. Must-have coverage ≥ 90% (confirmed, Q-02). 100% of must-haves are present-with-evidence or logged as a gap (OUT-2).
- **Origin:** G3 · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GAP-04 Screening facts reflected on the CV
- **Requirement:** When a role has location or eligibility knockouts, state the relevant facts in the CV header so recruiter searches and manual screens can see them.
- **Spec:** One optional header line, e.g. "Open to relocation · [Work-permit status for target country] · Available [notice period]". Shown only when truthful and relevant to this role. Facts must match the form answers exactly.
- **Acceptance:** For each knockout criterion in the post, either the CV line or the form answer covers it, and the two never contradict each other.
- **Origin:** G4 · **Basis:** Evidence · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### GAP-05 Acronym + full-term pairs and variants
- **Requirement:** Write each key acronym once in full with the acronym in brackets, and keep a variant list for matching.
- **Spec:** First use: "Product-Led Growth (PLG)". Later uses may use either form. Maintain a variants map (e.g. PM ↔ Product Manager, B2B SaaS ↔ business-to-business software). Where the post uses only one form, that form must appear at least once exactly as written.
- **Acceptance:** 100% of acronyms used appear at least once in long form. Every term on the locked list appears at least once in the post's exact form.
- **Origin:** G5 · **Basis:** Convention · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### GAP-06 CV-specific final checklist
- **Requirement:** A gate that must fully pass before the CV is submitted, separate from any application-form checklist.
- **Spec:** Run inside the ATS Gate (Part 4). Its report (GATE-13) is this checklist's record. Checklist items: OUT-1, OUT-2 and OUT-3 pass · RES-01 (no unproven keywords) · RES-02 (locked terms unchanged) · REQ-11 (0 invented claims) · REQ-17 (length) · REQ-19 (hygiene) · REQ-24 (headings) · REQ-25 (dates) · GAP-02 (layout lint) · file name correct · no leftover placeholders such as `[Company]`.
- **Acceptance:** All items pass. Any failure blocks submission and shows the failing item.
- **Origin:** G6 · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GAP-07 Regional CV conventions
- **Requirement:** Apply a convention profile for the target country or region.
- **Spec:** Each profile defines expected length, page size (Letter or A4), whether to include a photo or personal details (date of birth, nationality, marital status), date and phone formats, spelling variant (US vs UK English), section names and any local norms. Ships with **6 country profiles**, each checked before release: US, UK, Germany, Netherlands, UAE/GCC, Saudi Arabia. Plus **one General International profile** used for any other country, with safe defaults: no photo, no personal details, up to 2 pages, DOCX, Month YYYY dates, standard headings. More countries are added on demand. Each profile also sets the section order for the first-job path (Q-16). (Answered: Q-03)
- **Acceptance:** A profile is chosen for every application. The CV meets every rule in that profile. Personal details appear only where the profile expects them.
- **Origin:** G7 · **Basis:** Convention (verify each profile before use) · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### GAP-08 Master CV per positioning track
- **Requirement:** Keep one master CV per positioning track and tailor from the closest one rather than from a single generic CV.
- **Spec:** Each track has a summary, bullet order, skills block and evidence emphasis, all drawn from the master record. A selection rule maps the job post's main requirement to a track.
- **Acceptance:** Every tailored CV records which track it came from. Track masters are reviewed whenever the master record changes (REQ-02).
- **Source:** Each filled Section 1 of the intake questionnaire creates one track (INQ-04).
- **How many:** 2 tracks per person is the recommended number. A 3rd is allowed when the person's targets truly differ (a different function or industry). If a 4th is requested, the engine suggests merging the closest two. (Answered: Q-04)
- **Origin:** G8 · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### GAP-09 Seniority-calibrated wording
- **Requirement:** CV wording matches the detected seniority level of the role (REQ-07).
- **Spec:** L0–L2: learning speed, hands-on delivery, early wins. L3–L4: ownership, delivery, cross-team influence. L5–L7: strategy, organisation building, outcomes at scale (revenue, markets, headcount, budgets).
- **Acceptance:** The summary and the top 3 bullets of the most recent role use the language tier for the detected level.
- **Origin:** G9 · **Basis:** Default · **Priority:** Could · **Scope:** Core · **Status:** Proposed

### GAP-10 Consistency across public profiles
- **Requirement:** Job titles, companies and dates on the CV match the candidate's public profiles (e.g. LinkedIn).
- **Spec:** Compare each role field by field. Allowed differences: CV-only tailored headline and wording. Not allowed: title, company or date mismatches.
- **Acceptance:** 0 unexplained title, company or date mismatches.
- **Origin:** G10 · **Basis:** Default · **Priority:** Could · **Scope:** Core · **Status:** Proposed

### GAP-11 The submitted file is the tested file
- **Requirement:** Only the file frozen by the latest ATS Gate PASS for this job (GATE-14) may be uploaded or attached.
- **Spec:** The submission step receives the file and its fingerprint from the gate report, never a user-supplied or default file. Before uploading: recompute the fingerprint, compare it with the report, and confirm the job ID matches. If no PASS exists or the fingerprints differ, stop and say why. The same rule applies to email attachments and portal re-uploads. After uploading, record the fingerprint in the application log (GAP-13).
- **Acceptance:** 100% of submissions have a recorded fingerprint that equals a PASS report for the same job (OUT-4). 0 uploads of an untested file.
- **Origin:** Neither covers ("upload the tailored, gated CV") · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GAP-12 One summary source
- **Requirement:** The professional summary is written once per application, in the CV, and every other summary is derived from it.
- **Spec:** Form "experience summary" fields, the cover-letter opening and short profile blurbs are made by shortening or adapting the CV summary, never written separately. Derived versions keep the same claims, metrics and locked keywords (INT-03). If a field's limit forces cuts, drop sentences rather than change facts.
- **Acceptance:** Every claim and metric in a derived summary also appears in the CV summary. 0 contradictions between them.
- **Origin:** Neither covers ("single summary source") · **Priority:** Should · **Scope:** Core · **Status:** Proposed

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

---

## Part 3 — Full coverage map as generic requirements (43 abilities)

Each requirement is written to cover its ability fully. **Best today** shows the strongest current coverage found among the compared tools, and what it still lacks. REQ-38 to REQ-43 were added in v0.3.0 from the Workflow vs Engine comparison and sit in the stage they belong to.

### Stage 1 — Source and intake

#### REQ-01 Master career record
- **Requirement:** Keep one structured master record of all experience, wider than any single CV, as the only source for every claim.
- **Spec:** Per role: title, company, one-line company description, dates (month + year), location, every achievement with outcome, metric, method and evidence ID. Also: skills, tools, certifications, education, languages with levels, portfolio links, positioning tracks (GAP-08), screening facts (work permit, relocation, notice), and things not to emphasise.
- **Intake source:** The intake questionnaire (Part 5A) is the standard way to fill this record. Fields added in v0.6.0: type of work per role, title changes inside one organisation, certificate expiry and verification, language levels converted to one scale, references policy, military service where relevant.
- **Acceptance:** Every field has a value or an explicit "none". Every achievement has an evidence ID.
- **Best today:** Full (no evidence IDs, no track links) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-02 Keep the record current
- **Requirement:** Detect stale facts and offer updates. Never change the record silently.
- **Spec:** Time-sensitive fields (availability, salary expectations, work-permit status, current role, certificate expiry) carry a last-confirmed date and an expiry period. Expiry periods are listed per field in the intake questionnaire (5A.3). Expired fields are flagged at the start of each session. New facts found during an application are proposed as updates for approval.
- **Acceptance:** 0 expired fields are used without re-confirmation. Every change is approved and logged.
- **Best today:** Full · **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### REQ-03 Read an existing CV file
- **Requirement:** Accept an existing CV (PDF, DOCX, text, or a profile export) and extract it into the master record format.
- **Spec:** Show only the fields that differ from the master record, for approval. Flag anything that couldn't be read.
- **Acceptance:** 100% of roles, dates and achievements extracted or flagged. Differences listed before any merge.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-04 Job post intake
- **Requirement:** Accept a job post as pasted text, a URL or a file, and capture the application form's questions too.
- **Spec:** Fetch the URL. If the page is behind a login or doesn't fully load, ask for the text. Capture form fields and custom questions. Store the post text with its source and date.
- **Acceptance:** Full post text captured. Form questions captured or explicitly marked unavailable.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### Stage 2 — Reading the job post

#### REQ-05 Must-have vs nice-to-have
- **Requirement:** Split every stated requirement into mandatory and preferred, numbered, and rank responsibilities by emphasis.
- **Spec:** Emphasis = position in the post + repetition + explicit wording ("must", "required"). Also capture domain, seniority signals and culture signals.
- **Acceptance:** 100% of requirement sentences classified. Each has an ID used in REQ-09.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-06 Keyword weighting and exact wording
- **Requirement:** Build a locked keyword list from the post: skills, tools, certifications, methods and titles in their exact form, weighted by repetition.
- **Spec:** Terms appearing more than once = high priority. Tag each term must-have or nice-to-have. Store its exact spelling, hyphenation and variants (GAP-05). The list is locked for all later steps (RES-02).
- **Acceptance:** Every noun phrase for a skill, tool, method, certification or title in the post is on the list, or deliberately excluded with a reason.
- **Best today:** Full (no lock, no variants, no counting) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-07 Seniority detection
- **Requirement:** Assign a seniority level (L0–L7) from scope, reporting line and responsibilities, not the title alone.
- **Spec:** Compare with the candidate's target range. Warn when the gap is more than 1 level. The level drives GAP-09 wording and REQ-35 tone.
- **Acceptance:** Level and reasoning recorded for every application.
- **Best today:** Full (not applied to CV wording) · **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### REQ-08 Company research
- **Requirement:** Produce a short, factual company brief before writing anything.
- **Spec:** What it does (no promotional language), stage and funding, size, tech stack, culture signals, market position, hiring manager name if public, one visible product gap or opportunity. Each fact has a source link and date.
- **Acceptance:** All fields filled or marked "not found". Every fact sourced.
- **Best today:** Full · **Priority:** Should · **Scope:** Adjacent · **Status:** Proposed

### Stage 3 — Fit and honesty

#### REQ-09 Evidence-to-requirement mapping
- **Requirement:** Map every numbered requirement to evidence in the master record, or to an honest gap.
- **Spec:** Two columns: covered (with evidence ID) and gaps. Each gap gets any partially offsetting evidence, stated next to it and not as a replacement for it. Pick 2–3 lead achievements to feature.
- **Acceptance:** 100% of mandatory requirements mapped to evidence or listed as gaps. Generic claims ("experienced in X") never count as evidence.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-10 Stop on a bad fit
- **Requirement:** Give a fit verdict and stop before writing when the fit is poor.
- **Spec:** Clean fit = all mandatory requirements covered. Stretch = 1–2 mandatory gaps with offsetting evidence (proceed, and the gap must be acknowledged). Mismatch = 2+ mandatory gaps without offset (stop and explain). The candidate may override a stop, and the override is logged.
- **Acceptance:** A verdict is recorded before any CV text is produced.
- **Best today:** Full · **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### REQ-11 No-invention guard
- **Requirement:** Every claim in every output traces to the master record or a confirmed answer from the candidate.
- **Spec:** Each bullet, metric, tool, title and date carries an evidence ID internally. An automated trace check runs before final output.
- **Acceptance:** 0 claims without evidence. 0 metrics that differ from the record. Includes keywords added under RES-01.
- **Best today:** Full (no automated trace check) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-39 Gap log
- **Requirement:** Keep one gap log per application, started at the fit check and carried through every later stage.
- **Spec:** Each entry: requirement ID (REQ-05), must-have or nice-to-have, what's missing, offsetting evidence (if any), how it's handled (cover-letter line, form answer, interview answer, skill to build), status. Entries come from the fit mapping (REQ-09), keywords that couldn't be proven (RES-01) and knockout criteria not met (REQ-29).
- **Acceptance:** 100% of unproven must-haves and unmet knockouts are in the log, and each has a handling decision before the application package is written.
- **Best today:** None (a gap is stated once and then dropped) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### Stage 4 — Writing the CV

#### REQ-12 Produce a full tailored CV
- **Requirement:** Output a complete tailored CV, not only feedback or fragments.
- **Spec:** Starts from the matching track master (GAP-08). Section order per REQ-24. Delivered as a file per GAP-02, plus an editable text version. Ships with a change log listing what changed and why.
- **Acceptance:** A complete CV that passes the GAP-06 checklist.
- **Best today:** Full (text only, not a tested file) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-13 Headline matches the job title
- **Requirement:** A headline under the name that mirrors the post's job title, or the closest truthful variant.
- **Spec:** Use the exact title when it fits your real level and function. Otherwise use the closest honest form (e.g. "Head of Product | Product Leader" for a "Director of Product" post) without claiming a title you didn't hold.
- **Acceptance:** Headline contains the post's title or a declared variant, and job titles in the experience section remain the real ones.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-14 Professional summary
- **Requirement:** A summary tuned to the role, following RES-06.
- **Spec:** Banned generic phrases (Default list, extend as needed): "passionate about", "results-driven", "strategic thinker", "team player", "proven track record", "dynamic". No pronouns (REQ-19).
- **Acceptance:** Meets RES-06. 0 banned phrases.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-15 Bullet formula
- **Requirement:** Every experience bullet follows RES-04.
- **Spec:** One sentence each. Starts with a strong past-tense verb (present tense for the current role is allowed only if used consistently). No "responsible for".
- **Acceptance:** 100% of bullets meet RES-04.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-16 Bullets ordered by relevance
- **Requirement:** Within each role, order bullets from strongest to weakest match with the post's top priorities.
- **Spec:** Rank by mapped requirement weight (REQ-05) × keyword weight (REQ-06). Lead achievements from REQ-09 go first in their role.
- **Acceptance:** The first bullet of each recent role maps to one of the post's top-3 requirements where evidence exists.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-17 Length control
- **Requirement:** Keep length right for the candidate's career stage and the regional profile.
- **Spec:** Default: 1 page under 5 years of experience; up to 2 pages for 5+ years; regional profile (GAP-07) overrides. 3–5 bullets for recent roles, 1–2 for roles older than 10 years. Flag any role with 6 or more.
- **Acceptance:** Page count and bullet counts within limits.
- **Best today:** Full · **Basis:** Convention · **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### REQ-18 Skills list in the post's words
- **Requirement:** A targeted skills block following RES-05.
- **Spec:** Skills chosen from the master record that the post asks for, using the locked keyword form, ordered by relevance, optionally grouped (Tools / Expertise).
- **Acceptance:** Meets RES-05. 100% of skills listed are on the locked list or are evidenced high-value extras (at most 2).
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-19 Hygiene: pronouns, email, titles
- **Requirement:** No personal pronouns, a professional email address, standard job titles.
- **Spec:** Scan for I, me, my, we, our, he, she, his, her. Email ideally firstname.lastname@ or a personal domain; flag nicknames and numbers. Unusual titles get a standard equivalent in brackets (e.g. "Product Ninja (Product Manager)"). Where a formal title understates the real job, use the honest standard title only when the duties match it, and be ready to explain it in an interview.
- **Acceptance:** 0 pronouns. Email flagged or passed. Every title is standard or has a standard equivalent.
- **Best today:** Full · **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### REQ-20 Career-changer and early-career mode
- **Requirement:** When direct experience in the target field is thin, bring transferable evidence forward.
- **Spec:** Triggered when years in the target function are under 1, or the target function differs from the last role. Brings forward coursework, certifications, projects, volunteer work, and past roles reframed in the target field's terms (honestly).
- **Acceptance:** When triggered, at least 3 transferable evidence items are featured and labelled truthfully.
- **Best today:** Full · **Priority:** Could · **Scope:** Core · **Status:** Proposed

#### REQ-21 Role-family vocabulary
- **Requirement:** Use the hiring vocabulary of the target role family (e.g. product management, engineering, finance), not generic business language.
- **Spec:** Each role family has a term pack: core activities, typical metrics, frameworks and seniority signals. The pack must be extendable, starting with product management.
- **Acceptance:** The summary and top bullets use at least 3 terms from the matching pack that are also backed by evidence.
- **Best today:** Full (one role family only) · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### Stage 5 — ATS readability

#### REQ-22 Submit-ready CV file
- **Requirement:** See **GAP-02**.
- **Acceptance:** GAP-02 passes.
- **Best today:** Partial (file output exists only for non-CV documents) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-23 Parse-safe layout rules
- **Requirement:** See **GAP-02** (layout, fonts, header/footer, bullets, links).
- **Acceptance:** GAP-02 layout lint passes.
- **Best today:** None · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-24 Standard section headings and order
- **Requirement:** Use headings ATS parsers recognise, in the expected order.
- **Spec:** Order: Contact → Headline → Summary → Skills → Experience (most recent first) → Education → Certifications → optional (Languages, Projects, Publications). Heading names: "Summary", "Skills", "Experience" or "Professional Experience", "Education", "Certifications", "Languages". No creative names like "My Journey".
- **First-job path (Answered: Q-16):** for people with no work history, the country profile (GAP-07) decides whether Education comes before Experience.
- **Acceptance:** Every heading is on the allowed list and in order. Regional profile may adjust (GAP-07).
- **Best today:** Partial · **Basis:** Convention · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-25 Consistent date format
- **Requirement:** One date format for every role and qualification.
- **Spec:** Default "MMM YYYY – MMM YYYY" (e.g. "Aug 2025 – Feb 2026"), "Present" for the current role. Month always included for roles. Same dash style everywhere. Regional profile may change the format.
- **Acceptance:** 100% of date ranges match the chosen pattern, checked by a pattern match.
- **Best today:** Partial · **Basis:** Convention · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-26 Acronym and full-term pairs
- **Requirement:** See **GAP-05**.
- **Acceptance:** GAP-05 passes.
- **Best today:** None · **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### REQ-27 Measured keyword coverage
- **Requirement:** See **GAP-03**.
- **Acceptance:** GAP-03 passes and OUT-2 holds.
- **Best today:** Partial (judgement score, no counting) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-28 Read test on the real file
- **Requirement:** See **GAP-01**.
- **Acceptance:** GAP-01 passes and OUT-1 holds.
- **Best today:** None · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-29 Screening (knockout) answers
- **Requirement:** Find every knockout criterion in the post and the form, and answer each truthfully from the master record.
- **Spec:** Criteria: location, work permit or visa, relocation, travel, in-office days, notice period, minimum years, languages and levels, degrees, certifications, salary range. Answers come from confirmed facts only. Where a criterion isn't met, flag it before submitting. Feeds GAP-04.
- **Acceptance:** 100% of criteria identified and answered, or flagged. Form and CV agree (OUT-3).
- **Best today:** Full (form only, not reflected on the CV) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-30 ATS platform awareness
- **Requirement:** Detect which ATS the employer uses and apply its known behaviour.
- **Spec:** Detect from the application URL or page (e.g. Greenhouse, Lever, Workday, Ashby, SmartRecruiters, Taleo, iCIMS, Breezy). Each platform has a profile: preferred file type, known parsing quirks, field limits, and whether to retype work history into the form. Profiles are extendable.
- **Acceptance:** Platform recorded for every application. Its profile rules applied to the file (GAP-02) and the form (REQ-36).
- **Best today:** Partial (forms only) · **Basis:** Default (verify each profile) · **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### REQ-31 Regional CV conventions
- **Requirement:** See **GAP-07**.
- **Acceptance:** GAP-07 passes.
- **Best today:** None · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### Stage 6 — Quality and final check

#### REQ-32 Remove AI-sounding writing
- **Requirement:** Remove patterns readers associate with machine-written text from the CV and all application text, without breaking locked keywords (RES-02).
- **Spec:** Pattern list (extendable): inflated significance ("testament to", "pivotal"), promotional words ("groundbreaking", "vibrant"), formula structures (forced lists of three, "not just X but Y"), vague attributions, filler openers ("In order to", "It is important to note"), chatbot phrases, stacked hedging, identical sentence rhythm, overuse of bold. Run a second pass that asks what still reads as machine-written, and fix it.
- **Acceptance:** 0 listed patterns. Locked-keyword diff unchanged.
- **Best today:** Full (not applied to CVs, conflicts with exact keywords) · **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### REQ-33 Final pre-submit check
- **Requirement:** See **GAP-06** for the CV. A separate application checklist covers the form and cover letter.
- **Spec (application checklist):** Every required field filled or flagged · no leftover placeholders · salary entered as a single number in the right currency unless a range is required · portfolio field is a valid URL · cover letter within RES-08 limits · any fit gap acknowledged (REQ-10).
- **Acceptance:** Both checklists fully pass.
- **Best today:** Full (application only, no CV checks) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-34 Approval gates
- **Requirement:** The candidate approves at the decisions that matter, without a gate at every step.
- **Spec:** Required approvals: fit verdict when it is a stretch or mismatch (REQ-10), any change to the master record (REQ-02), the final CV before export, and anything irreversible (submit, send, fill a live form) after a full preview of the data. Everything else runs without stopping.
- **Acceptance:** 0 irreversible actions without explicit approval. Routine steps don't block.
- **Best today:** Full (gates on every phase, which is heavy) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-38 CV critique and scorecard
- **Requirement:** After writing and before the ATS Gate, check the CV text against one canonical rubric (RES-03) and fix every failed rule.
- **Spec:** The rubric covers at least: summary (RES-06, REQ-14), bullet formula (RES-04), relevance order (REQ-16), skills (RES-05), length (REQ-17), hygiene (REQ-19), role-family language (REQ-21), seniority wording (GAP-09) and evidence-only keywords (RES-01). Each row records the rule, pass or fail, a quote from the CV and a suggested fix. The score is a count of passed rules, not an opinion out of 10.
- **Acceptance:** Every rubric row is evaluated with a quote. 0 failed Must rows when the CV goes to the gate.
- **Best today:** Full as a review, but with two inconsistent rubrics and opinion-based scores · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### Stage 7 — Around the CV

#### REQ-35 Cover letter
- **Requirement:** A tailored cover letter grounded in the master record and the company brief.
- **Spec:** Addressed to a named person where one can be found, otherwise their title. Structure: why this role and company · 1–2 evidence stories with metrics · one specific observation about the company's product, from the candidate's own use · gap acknowledgement when the fit is a stretch · committed close (RES-07). Length per RES-08. Tone matches the seniority level (REQ-07). Passes REQ-32.
- **Acceptance:** All parts present. 0 banned phrases. Within the length limit. Every claim traced (REQ-11).
- **Best today:** Full · **Priority:** Should · **Scope:** Adjacent · **Status:** Proposed

#### REQ-36 Job search, forms, salary and tracking
- **Requirement:** Support the steps after the CV: finding roles, filling forms, researching salary, and tracking outcomes.
- **Spec:** Search across job boards with exclusion and priority filters. Answer form questions with the exact question text shown above each answer. Salary from current market data (floor, target, stretch) set by level, in local currency. Log each application's status and outcome, and feed rejections back into targeting.
- **Acceptance:** Every application logged with status. Salary figure has a dated source. Form answers trace to the record.
- **Best today:** Full · **Priority:** Could · **Scope:** Adjacent · **Status:** Proposed

#### REQ-37 Saved output with a naming rule
- **Requirement:** Save every output with a predictable name and keep versions.
- **Spec:** Working files: `[type]-[Company]-[Role]-[YYYY-MM-DD].[ext]`. Submitted CV: GAP-02 file name. Each saved set includes the keyword coverage report (GAP-03), read-test result (GAP-01) and change log.
- **Acceptance:** 100% of outputs follow the rule. Each application folder holds the full evidence set.
- **Best today:** Full (text only) · **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### REQ-40 Submit the tested file
- **Requirement:** See **GAP-11**.
- **Acceptance:** GAP-11 passes and OUT-4 holds.
- **Best today:** None (the original file is uploaded) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### REQ-41 Single summary source
- **Requirement:** See **GAP-12**.
- **Acceptance:** GAP-12 passes.
- **Best today:** None · **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### REQ-42 Learn which CV choices work
- **Requirement:** See **GAP-13** (the data) and **GATE-17** (the review).
- **Acceptance:** GAP-13 and GATE-17 pass.
- **Best today:** None (outcomes are logged by company only) · **Priority:** Should · **Scope:** Adjacent · **Status:** Proposed

#### REQ-43 Interview prep from known gaps
- **Requirement:** See **GAP-14**.
- **Acceptance:** GAP-14 passes.
- **Best today:** None · **Priority:** Could · **Scope:** Adjacent · **Status:** Proposed

---

## Part 4 — ATS Gate

The ATS Gate is the step that runs after the CV text is final and before anything is submitted. It turns the CV text into the actual file, tests that file, and blocks submission until every Must check passes. It **runs** the checks defined elsewhere in this spec (GAP-01, GAP-02, GAP-03, GAP-04, GAP-06 and others). It **adds** what only a gate can do: a fixed order of checks, stop rules, a single report, re-running after any edit, waivers, and proof that the file that passed is the exact file sent.

**Best today:** None. No compared tool tests the final CV file before submission. Every GATE item below starts from zero.

### Gate flow

| Order | Check | ID | Blocks submission if failed |
|---|---|---|---|
| 0 | Entry criteria met | GATE-01 | Yes |
| 1 | Export the file(s) | GATE-02 | Yes |
| 2 | Layout lint | GATE-03 | Yes |
| 3 | Read test | GATE-04 | Yes |
| 3b | Visual review as ATS and recruiter | GATE-18 | Yes for unreadable, cut-off or overlapping text; otherwise reported |
| 4 | Locked-keyword integrity in the file | GATE-05 | Yes |
| 5 | Keyword coverage, before vs after + stuffing cap | GATE-06 | Yes |
| 6 | Evidence trace on the file | GATE-07 | Yes |
| 7 | Knockout alignment (CV ↔ form) | GATE-08 | Yes |
| 8 | Content hygiene | GATE-09 | Yes |
| 9 | ATS platform profile | GATE-10 | Should-level failures can be waived |
| 10 | Regional profile | GATE-11 | Should-level failures can be waived |
| 11 | Recruiter skim test | GATE-12 | No (advisory) |
| 12 | Gate report + verdict | GATE-13 | — |
| 13 | Freeze and fingerprint the passed file | GATE-14 | Yes |

### GATE-00 Gate definition
- **Requirement:** Every CV passes through the ATS Gate before it is submitted. No path to submission skips it.
- **Spec:** Position: after the CV text is approved (REQ-12, REQ-34) and before the application is submitted (REQ-36). Runs every check in the order above. Checks 1–8 (including 3b) and 13 stop the gate at the first failure. Checks 9–11 always run and report.
- **Acceptance:** 100% of submitted CVs have a gate report with verdict PASS or PASS WITH WAIVERS (GATE-13).
- **Basis:** Default · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-01 Entry criteria
- **Requirement:** The gate starts only when all its inputs exist.
- **Spec:** Required inputs: final approved CV text · master record (REQ-01) · locked keyword list with must-have tags and weights (REQ-06) · the original CV, for the before/after comparison · knockout criteria list (REQ-29) · regional profile (GAP-07) · ATS platform, or "unknown" (REQ-30) · target channel (upload, email, form).
- **Acceptance:** A missing input stops the gate with a message naming the input and which step provides it. The counted-check script refuses to start without the files, the locked keyword list, and the expected name and email for the read test.
- **Handoff:** Inputs arrive through the structured handoff record (INT-02), including the gap log (REQ-39).
- **Basis:** Default · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-02 Export
- **Requirement:** Produce the submission file(s) from the approved text, following GAP-02.
- **Spec:**
  - Export DOCX and text-based PDF from the same source, so their content is identical.
  - Set document properties: title = "Firstname Lastname – CV", author = candidate name. Remove company, template and old-author metadata.
  - Remove hidden content: comments, tracked changes, hidden text, unused styles carrying old text.
  - **Banned:** white or tiny text, text placed off the page, and keyword lists hidden anywhere in the file. Parsers read this text, recruiters see it in the parsed view, and it is treated as manipulation.
  - Embed fonts in the PDF. No password or editing restrictions.
- **Consent:** In the engine, creating a file is a Tier 2 action. The export runs as new automation A17 and needs APPROVE CREATE. By default, one APPROVE CREATE per application, given at M4, covers every export and re-test for that job. The person can switch to approving every single export, for one application or for all. (Answered: Q-18)
- **Acceptance:** Both files exist. Their extracted text matches each other apart from layout whitespace. 0 hidden or invisible text, 0 comments, 0 tracked changes. Properties set correctly.
- **Basis:** Evidence/Convention · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-03 Layout lint
- **Requirement:** Automatically check the exported file against the GAP-02 layout rules.
- **Spec:** Detect and count: tables · text boxes or frames · multiple columns · images, icons, shapes, charts · text in the page header or footer · non-standard bullet characters · fonts outside the allowed list · font sizes outside 10–12 pt for body text · links shown as words instead of full URLs · document properties (title and author must be the person, not a tool name) · page size against the country profile · white or tiny text (GATE-02 ban). Fonts and sizes are read where they actually apply: run settings, the styles the document uses, document defaults and theme fonts. A PDF's text can't show tables or header text, so the source DOCX is always gated with its PDF; a PDF tested alone is flagged, and a PDF whose words match its DOCX less than 90% fails. Content is read through the package relationships and whatever namespace prefix the file uses; embedded documents, floating frames, every tracked-change kind, and header, footer and comment parts under any name are counted. Known limits: PDF white or tiny text is caught by the word match and the visual review (GATE-18), not per character.
- **Acceptance:** Every count = 0 except allowed items. Exactly 1 column. Report lists each finding with its location.
- **Basis:** Evidence · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-04 Read test
- **Requirement:** Run GAP-01 on each exported file.
- **Spec:** Adds to GAP-01: a field-by-field table (field | expected from master record | extractor A result | extractor B result | match?). Critical fields: name, email, phone, LinkedIn/portfolio URL, each job title, company, start and end date, each section heading, each degree and certification. Contact details must appear within the first 10 lines of extracted text (Default).
- **Acceptance:** 100% of critical fields match in both extractors for both files. 0 reading-order breaks. 0 garbled characters. (OUT-1)
- **Basis:** Evidence · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-05 Locked-keyword integrity in the file
- **Requirement:** The locked keywords survive export unchanged (RES-02).
- **Spec:** Search the **extracted text** (not the source text) for each locked term in its exact form. Catches changes that export introduces: hyphens turned into special dashes, ligatures (fi, fl) splitting words, smart quotes, words broken across lines, auto-capitalisation.
- **Acceptance:** 100% of locked terms that are in the approved text are found in the extracted text in exact form.
- **Basis:** Evidence · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-06 Keyword coverage, before vs after, with a stuffing cap
- **Requirement:** Run GAP-03 on the extracted text of the original CV and of the gated file, and cap repetition.
- **Spec:**
  - Coverage table and percentages per GAP-03, measured on extracted text so they reflect what the ATS actually sees.
  - **Stuffing cap:** no single keyword appears more than 4 times, and about 3 is the normal target (summary, skills block, one bullet) (Answered: Q-06), and no keyword appears outside a real sentence, bullet or skills entry.
  - Report the change: must-have coverage % before → after, weighted coverage % before → after.
- **Acceptance:** Must-have coverage ≥ 90% (confirmed, Q-02). 100% of must-haves are present with evidence or on the gap log (OUT-2). 0 terms over the cap.
- **Basis:** Default · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-07 Evidence trace on the file
- **Requirement:** Run the no-invention check (REQ-11, RES-01) on the extracted text of the final file.
- **Spec:** Every metric, tool, title, company, date and added keyword in the extracted text is matched to an evidence ID in the master record. Numbers must match exactly (e.g. "35%" in the file = "35%" in the record).
- **Acceptance:** 0 claims without evidence. 0 numeric mismatches.
- **Basis:** Default · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-08 Knockout alignment
- **Requirement:** The CV and the application answers agree on every knockout fact (REQ-29, GAP-04).
- **Spec:** For each knockout criterion: compare the planned form answer, the CV header line (if used) and the master record. Check that the CV doesn't contradict the facts, e.g. a location line that suggests no relocation, or an expired availability date.
- **Acceptance:** 100% of criteria answered or flagged. 0 contradictions between CV, form and record (OUT-3).
- **Basis:** Evidence · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-09 Content hygiene
- **Requirement:** Re-check the content rules on the extracted text.
- **Spec:** Headings on the allowed list and in order (REQ-24) · 0 Private intake fields printed (INQ-03) · every date range matches the pattern (REQ-25) · page and bullet limits (REQ-17) · 0 pronouns and title check (REQ-19; "I" in "I/O" or "Phase I" is not a pronoun) · each heading appears once · 0 leftover placeholders (anything in `[ ]` or `{ }`, "TBD", "XX") · 0 banned phrases (REQ-14, REQ-32) · spelling variant consistent with the regional profile (US or UK).
- **Acceptance:** Every sub-check passes.
- **Basis:** Convention · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-10 ATS platform profile
- **Requirement:** Apply the target platform's known rules (REQ-30).
- **Spec:** Check the file type the platform prefers, its file size limit (stay under 2 MB, confirmed in Q-07), any page limit, and whether it expects work history retyped into form fields. If the platform is unknown, apply the strictest common profile: DOCX, under 2 MB, plain layout. A file over the size limit is a Should-level finding (grade 4/5, waivable), not a Must failure.
- **Acceptance:** Every rule in the selected profile passes, or a failure is waived with a reason (GATE-15).
- **Basis:** Default (verify each profile) · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### GATE-11 Regional profile
- **Requirement:** Check the file against the selected regional profile (GAP-07).
- **Spec:** Length, photo and personal details present or absent as the profile expects, date and phone formats, section names.
- **Acceptance:** Every rule passes, or a failure is waived with a reason (GATE-15).
- **Basis:** Convention (verify each profile) · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### GATE-12 Recruiter skim test
- **Requirement:** The top third of page 1 gives a recruiter the match within a 6–10 second skim.
- **Spec:** Name, headline with the target title (REQ-13), summary with at least 2 locked keywords (RES-06) and the first role's title and dates are all visible in the top third of page 1. Check on a rendered image of the page.
- **Acceptance:** All 4 elements visible in the top third. Advisory: reported, does not block.
- **Basis:** Default · **Priority:** Could · **Scope:** Core · **Status:** Proposed

### GATE-18 Visual review as ATS and as recruiter
- **Requirement:** Look at the exported file the way a person and a hiring system would see it, not only as extracted text.
- **Spec:**
  - **As the ATS:** turn each page into an image and check by eye (computer vision) that the reading order matches the extracted text, and that nothing overlaps, is cut off or is hidden.
  - **As the recruiter:** do the 6–10 second skim (GATE-12) on the rendered page: name, target title, summary and latest role visible in the top third; layout clean and consistent.
  - **Extra check when tools allow:** use browser or computer control to open the file in a CV-parsing preview or ATS simulator and compare its parsed fields with the master record. This is read-only checking. Uploading the file to any outside site is a Tier 2 action and needs the person's approval. It is never done through an employer's live application form.
  - Every finding is shown as a one-line grade with its reason (INT-05).
- **Acceptance:** Every exported file has a visual review result. 0 files pass with unreadable, cut-off or overlapping text. No outside upload happens without approval.
- **Basis:** Your decision on Q-05 · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### GATE-13 Gate report and verdict
- **Requirement:** Each gate run produces one report with a single verdict.
- **Spec:** Report holds: run date and time · file names and fingerprints (GATE-14) · result of each check with its findings · coverage before → after · waivers with reasons · verdict. Verdicts: **PASS** (all checks pass) · **PASS WITH WAIVERS** (only Should-level checks waived) · **FAIL** (any Must check failed, with the step that owns the fix). The report is written in plain language and shows the most important failure first. The verdict always agrees with the grade: PASS only at 5/5; PASS WITH WAIVERS when only Should-level findings or warnings remain; FAIL on any Must failure. The report is saved with the evidence pack.
- **Acceptance:** A report exists for every run. The verdict follows these rules exactly.
- **Basis:** Default · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-14 Freeze and fingerprint
- **Requirement:** The file submitted is exactly the file that passed.
- **Spec:** After a PASS, compute a fingerprint (a hash, i.e. a unique code calculated from the file's bytes) for each file and record it in the report. Before submission, recompute it and compare. **Any edit after a PASS cancels the PASS** and the full gate runs again. A PASS WITH WAIVERS is frozen only after the person accepts each waiver. Freezing re-runs every counted check from the gate configuration, which names the job; a PASS can't come from a typed or stale report, or from another job's run. A PASS belongs to one job and one keyword list: uploads are checked against the job in progress, and changing that job's keyword list cancels its PASS.
- **Acceptance:** The fingerprint at submission equals the fingerprint in the PASS report. 0 submissions with a mismatched or missing fingerprint.
- **Handoff:** The submission step must take the file and fingerprint from this report (GAP-11).
- **Basis:** Default · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-15 Fail handling and waivers
- **Requirement:** Failures send the work back to the step that owns the fix. Only Should-level checks can be waived.
- **Spec:**
  - Each failure names the owning step (e.g. layout → export settings, missing keyword → RES-01 decision, wrong date → master record).
  - After a fix, the full gate re-runs from check 0, not just the failed check.
  - **Retry limits (Answered: Q-08):** normal issues (only Should-level checks failing, gate grade 4) get **1** automatic retry, then the engine asks the person. Major issues (any Must check failing, gate grade 2 or lower, or the grade falling) get **up to 5** retries, until every major issue is fixed.
  - **Retry points (decides whether another automatic try is worth it):**

    | Factor | Points |
    |---|---|
    | The failing check is a Must check | +2 |
    | The failing check is a Should check | +1 |
    | The last try improved the grade | +1 |
    | The last try made no change | 0 |
    | The last try made it worse | −1 |
    | The fix needs no new facts from the person | +1 |
    | The fix needs new facts from the person | Stop and ask now |

    Retry only when the points are 2 or more and the retry limit isn't reached. Two tries in a row with no progress: stop and ask.
  - Every retry decision is shown as a one-line grade with its reason (INT-05), for example: "Retry 2 of 5 · read test still loses role dates · 3 points · fix: put dates on the title line".
  - Waivers are allowed only for GATE-10 and GATE-11, need explicit approval (REQ-34), and are recorded with a reason. Must checks can never be waived.
- **Acceptance:** 0 Must checks waived. Every waiver has an approval and a reason. Every re-run starts at check 0.
- **Basis:** Default · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-16 Evidence pack
- **Requirement:** Save everything the gate produced with the application (REQ-37).
- **Spec:** Folder per application containing: submitted file(s) · gate report · read-test field table · keyword coverage table · layout lint result · knockout alignment table · waiver log. Named per REQ-37.
- **Acceptance:** Every submitted application has a complete pack.
- **Basis:** Default · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### GATE-17 Gate learns from outcomes
- **Requirement:** Use application results to improve the gate's defaults.
- **Spec:** Record the gate report next to the outcome (no response, rejection at screen, interview, offer). Review regularly: look for any check or threshold that differs between screened-out and interviewed applications, then propose changes to Default values here via the Change log.
- **Acceptance:** Outcomes are linked to gate reports. Each Default change cites the outcome data behind it.
- **Data source:** The application log defined in GAP-13.
- **Basis:** Default · **Priority:** Could · **Scope:** Core · **Status:** Proposed

---

## Part 5 — Workflow integration

These requirements apply when the spec runs as a multi-stage workflow. They set the order of stages, what each stage passes to the next, and the single verdict needed before submission. **Best today:** None. In the compared workflows these points were either missing or in conflict.

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

### INT-07 Fallback ladder: a missing tool never stops a step
- **Requirement:** When the tool a step needs is missing, blocked or returns incomplete content, the step moves down a fixed ladder instead of stopping.
- **Spec:**
  1. **Ladder, in order:** connector made for the job → native tool (search, fetch, scripts, file creation) → browser use (in the engine's registry order, never a separate path per browser brand) → computer use on the person's linked computer → vision (screenshot or rendered page read by eye) → ask the person, saying exactly what to paste or upload and why the earlier rungs failed.
  2. **Name the rung:** every grade line names the rung used when it isn't the first or second (for example "Job post: read through the browser, fetch was blocked").
  3. **Audits on purpose:** the same three abilities are used to check work the way a person sees it: the CV pages (GATE-18), the filled form before submit, the portal's own preview of the parsed CV after upload, and the confirmation page for the evidence pack (GATE-16).
  4. **Safety never changes:** reading and looking are Tier 1; falling back never lowers a consent tier; the person logs in themselves and credentials are never typed or stored; page text is data, not instructions; only the fingerprinted file is uploaded (GAP-11).
- **Acceptance:** 0 steps stop on a missing tool before trying every available rung. 100% of non-default rungs are named in the grade line. 0 consent tiers lowered by a fallback.
- **Origin:** Your instruction to use vision, browser use and computer use as automatic fallbacks and as audit tools · **Priority:** Must · **Status:** Implemented (A18, invariant 19)

### INT-08 Side-effects line
- **Requirement:** The person never has to guess what left the session.
- **Spec:** Every reply that finishes the ATS Gate, the package, the style pass or the final verdict, or runs any automation, ends with one plain line naming what was uploaded, sent or submitted, and under which approval. When nothing left, it says so: "Nothing was uploaded, sent or submitted."
- **Acceptance:** 100% of those replies end with the line.
- **Origin:** v2.2.0 eval run (a correct FAIL report never said whether anything was uploaded) · **Priority:** Should · **Status:** Implemented

### INT-09 Release harness and pass bar
- **Requirement:** Every engine release is proven by repeatable checks, not by reading.
- **Spec:**
  1. **Self-test:** a bundled script checks the package structure, the gate script on a clean and a planted-fault fixture, the PASS freeze and upload check, the hooks, and one regression check for every bug found.
  2. **Evals:** fixed test cases with machine-checked assertions and fixture files, run on the new version and the previous one.
  3. **Pass bar:** a release needs 100% of eval checks and 100% of self-test checks. The previous version's score is shown for comparison only.
  4. **Bug rule:** a bug found during a test run is fixed, gets a regression check, and the affected test is run again.
  5. **Install-proof:** checks read skill metadata as values (quoted or not), so a copy installed by a platform passes the same checks.
- **Acceptance:** Self-test 100%. Evals 100% on the release build. Every fixed bug has a regression check.
- **Origin:** Your instruction to include harness, scripts and evals inside the skill · **Priority:** Should · **Status:** Implemented

### INT-10 Optional enforcement hooks
- **Requirement:** Where the platform supports hooks, the two rules that guard a submission are enforced by code, not only by instructions.
- **Spec:**
  - **Before any upload:** block a CV file that is not the fingerprinted file from the latest ATS Gate PASS for that job (GAP-11, GATE-14).
  - **After any file change:** cancel a recorded PASS whose file bytes changed, and say so (GATE-14).
  - Opt-in, read-only apart from the PASS state file, never collects data. Where hooks don't run (chat apps), the same rules hold as instructions.
- **Acceptance:** An untested or edited CV upload is blocked in 100% of hook-enabled sessions. 0 non-CV files blocked.
- **Origin:** Your instruction to add hooks · **Priority:** Could · **Status:** Implemented (Claude Code plugin)

### INT-11 Capability wording: promise only what the session can do
- **Requirement:** What the person is told matches what this session can actually do.
- **Spec:**
  1. **No brand names:** never name a browser, browser-automation product or desktop-app brand to the person. Say "browser control", "a document app", "a PDF viewer".
  2. **No promises beyond the map:** never say "on your computer", and never promise an action, unless the A0 Capability Map shows the tool for it as ACTIVE. Otherwise say what will happen instead.
  3. **Form filling:** "I can fill the form if you approve each step" only when browser control is ACTIVE. Otherwise "I'll give you answers to paste", with no offer to fill later or "if connected".
- **Acceptance:** 0 test replies with a browser or app brand or "on your computer". 0 offers to fill a form when browser control is inactive. Both form-filling tests (browser control inactive and active) pass.
- **Origin:** Owner request after release testing · **Priority:** Must · **Status:** Implemented (generic edition)

---

## Part 5A — Intake questionnaire

### 5A.1 What it is

A fill-in form a person completes **once**, before any job is picked. It collects everything needed to build the master record (REQ-01) and a base CV for each type of role the person is targeting. It is for **public use**: any person, from intern to C-suite, any industry, any country. It is offered in English and Arabic, with the same field IDs in both.

- **Based on:** "CV Information Collection Questionnaire, ATS-Optimized, Universal Edition v3". This part defines **v4**, which keeps every v3 field and adds what the workflow needs.
- **Runs inside:** stage S1 (Profile) as the engine's first-use setup. It is not a new stage, so no stage numbers change.
- **Never asks twice:** facts already found in an uploaded CV, LinkedIn export or earlier answers are pre-filled. The person only confirms them.

### 5A.2 Rules

#### INQ-01 One form for anyone
- **Requirement:** One form serves every person, level, industry and country by showing only the sections that apply.
- **Spec:**
  - The first answer (Q0.1, "your situation") picks the path: **First job** (student, graduate, intern) · **Career change** · **Returning to work** · **Experienced** · **Executive** (heads a function or company).
  - First job: asks for an objective instead of a summary, and asks for projects, coursework and volunteering in full. Experience entries are optional, never invented. The country profile decides whether Education comes first (Q-16).
  - Career change: adds "transferable evidence" prompts that feed REQ-20.
  - Executive: adds the scale block in Section 6 (budget, team size, revenue, markets, board exposure) that feeds GAP-09.
  - Every field accepts "N/A". Optional sections can be skipped completely.
  - **Languages (Answered: Q-17):** English is the master text and Arabic is maintained by hand. Any other language is auto-translated on the fly from the English master, keeping the same field IDs. Answers are stored in the language given plus an English copy. Names, organisation names and job titles keep their original spelling. At sign-off, the person confirms the English copy of key fields (titles, dates, results), so translation mistakes can't reach the CV.
- **Acceptance:** A person on each of the 5 paths can finish the form without meeting a question that doesn't apply to them. Both language versions have identical field IDs.
- **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### INQ-02 Fill once, then only confirm
- **Requirement:** The form follows the engine's existing first-use steps exactly, so nothing is asked twice.
- **Spec:**
  1. **Extract first** (engine Step 0): read any uploaded CV, LinkedIn export, portfolio link or pasted text, and pre-fill matching fields.
  2. **Show what was found** (engine Step 1): the person confirms or corrects pre-filled fields.
  3. **Ask only the gaps** (engine Step 2): the form is the full question list for this step. Only empty or unconfirmed fields are shown.
  4. **Sign off once** (engine Step 3): one 5/5 review of the whole record. This is a one-time setup check per person, not one of the 5 per-application gates in RES-11.
  5. **Keep fresh** (engine Step 4): fields with an expiry are re-confirmed when they expire (see the Expires column in 5A.3).
  6. **Update with approval** (engine Step 5): any change after sign-off is proposed and needs APPROVE UPDATE.
- **Acceptance:** 0 questions asked for fields already filled and confirmed. Every change after sign-off has an APPROVE UPDATE record.
- **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### INQ-03 Every field has an ID, a destination and a privacy class
- **Requirement:** Every question in the form has a permanent ID, a clear destination, and a rule for whether it may appear on a CV.
- **Spec:** Each field in 5A.3 lists:
  - **ID** (Q-section.number, never reused)
  - **Feeds** (the master-record field, engine field and spec items it supplies)
  - **Privacy class:** **CV** = may appear on the CV · **Private** = used only for matching, eligibility or forms, never printed on the CV · **Ask** = printed only if the regional profile (GAP-07) expects it **and** the person agrees
- **Acceptance:** 100% of fields have all three. 0 Private fields appear in any CV file (checked at GATE-09).
- **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### INQ-04 Each target becomes a positioning track
- **Requirement:** Section 1 (Target) can be filled once per type of role, and each completed Section 1 becomes one positioning track (GAP-08, RES-10).
- **Spec:**
  - Each track holds: target title(s), industry, country or region, seniority level, 1–3 sample job ads and their top keywords.
  - 2 tracks per person recommended, up to 3 when targets truly differ (GAP-08).
  - The keywords from the sample ads form the track's **base keyword list**, which shapes the track's base CV.
  - For each real job, S4 still builds that job's own locked keyword list (REQ-06). The base list never replaces it. S4's grade line (INT-05) shows the difference, for example "6 of this job's 12 must-have terms are not in your base CV".
- **Acceptance:** Every track has a base CV and a base keyword list. Every job's locked list is built from that job's ad, not copied from the track.
- **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### INQ-05 Results become evidence
- **Requirement:** Every result entered in the form becomes an evidence item the rest of the workflow can trace.
- **Spec:** Each result (Q6.10) automatically gets an evidence ID (E-[entry]-[number]). The person can optionally add proof: a link, a document, or who could confirm it. Results without numbers use scale ("largest account", "one of 3 sites"). "N/A" is always accepted. Nothing is ever filled in by guessing (REQ-11).
- **Acceptance:** 100% of results have an evidence ID. 0 results contain numbers the person didn't enter.
- **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### INQ-06 The form collects; the spec decides the output
- **Requirement:** Answers are raw input. The CV is always produced to this spec's rules, whatever the person typed.
- **Spec:** Three known differences between the v3 form and this spec are converted automatically, without asking the person again:

  | The form collects | The CV follows |
  |---|---|
  | A summary of 3–4 lines | RES-06: 3 sentences, at most 60 words |
  | "Work Experience" as a heading | REQ-24 allowed headings |
  | Education dates as years only | REQ-25 date pattern (the month is used when known) |

  The same applies to every other output rule in this spec (bullet formula, skills block, layout, file type).
- **Acceptance:** 0 CV outputs that break a spec rule because of how a form answer was written.
- **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### INQ-07 Privacy and sensitive details
- **Requirement:** The form collects sensitive details only when they are needed, and never prints them by default.
- **Spec:**
  - **Government ID numbers** (passport, national ID) are never collected.
  - **Nationality, date of birth, marital status and photo** are collected only when a target country's regional profile expects them or an eligibility check needs them. Their class is **Ask**.
  - **Salary** is optional and **Private**. "Prefer not to say" is accepted; the engine then runs its market salary research as usual (Phase 3).
  - **Work permit and visa status** are **Private**. They appear on the CV only as the optional screening line (GAP-04), in words the person approves.
- **Acceptance:** 0 government ID numbers stored. 0 Ask fields printed without the person's agreement.
- **Priority:** Must · **Scope:** Core · **Status:** Proposed

#### INQ-08 Readiness grade
- **Requirement:** The form shows how ready the record is, in the same visible style as every other grade (INT-05).
- **Spec:** One line after the form, for example: "Intake: 4/5 · missing: notice period, proof for 2 results. Not stopping." 5 = every required field answered or marked N/A. 4 = optional gaps only. 3 or lower = a required field for the chosen path is empty. A grade of 3 or lower is raised at the one-time sign-off (INQ-02 step 4). It never adds a per-application gate.
- **Acceptance:** Every completed form shows a readiness line with its reasons.
- **Priority:** Should · **Scope:** Core · **Status:** Proposed

#### INQ-09 Ask in small batches
- **Requirement:** Never ask more than 10 questions in one message.
- **Spec:** First batch: only what the current application needs to start (target, contact, eligibility, start date), minus anything already extracted. Later batches are asked where the answer is used: pay and CV format preferences at M3 (S6); missing role details, results and proof at S7; optional extras only when they would strengthen the CV for the target role. Every batch gives an approximate count of questions left.
- **Acceptance:** 0 messages with more than 10 questions. The first batch contains no question the current application doesn't need yet.
- **Origin:** Engine v2.2.0 test runs: the first message asked 27–28 questions; after this rule, 6 and 9 · **Priority:** Must · **Scope:** Core · **Status:** Accepted

### 5A.3 Questionnaire v4: field list

**Asked:** *All* = every path · *Path* = only for the named paths · *Optional* = skippable. **Expires** follows the engine's freshness rules. Fields marked **(new)** are not in v3.

| ID | Field | Asked | Privacy | Expires | Feeds |
|---|---|---|---|---|---|
| **Section 0 — Your situation (new)** | | | | | |
| Q0.1 | Your situation: first job · career change · returning · experienced · executive | All | Private | — | INQ-01 path, REQ-20, GAP-09 |
| Q0.2 | Years of relevant experience | All | CV | — | [YEARS_EXPERIENCE], REQ-07, RES-06 |
| Q0.3 | Language to fill the form in | All | Private | — | INQ-01 |
| **Section 1 — Target (one per type of role)** | | | | | |
| Q1.1 | Exact job title(s) you're aiming for | All | CV | — | [TARGET_ROLE_TYPES], REQ-13, INQ-04 |
| Q1.2 | Industry or field | All | Private | — | [TARGET_SECTORS], REQ-21 |
| Q1.3 | Country or region you're applying in | All | Private | — | GAP-07, [PREFERRED_CITIES] |
| Q1.4 | Seniority you're aiming for, in plain words (new) | All | Private | — | [TARGET_SENIORITY_LEVEL], REQ-07 |
| Q1.5 | 1–3 real job ads (text or links) | All | Private | — | INQ-04, REQ-04 |
| Q1.6 | Top keywords repeated across those ads (optional: the system also extracts them) | Optional | Private | — | INQ-04 base keyword list |
| Q1.7 | Preferred cities (new) | All | Private | — | [PREFERRED_CITIES] |
| Q1.8 | Places you will never apply to (new) | Optional | Private | — | [HARD_EXCLUSION_GEOGRAPHIES] |
| Q1.9 | Open to relocation? Which cities? (new) | All | Private | 6 months | [RELOCATION_STATUS], REQ-29, GAP-04 |
| **Section 2 — Contact** | | | | | |
| Q2.1 | Full name (as on your official documents or LinkedIn) | All | CV | — | [CANDIDATE_NAME], GAP-10 |
| Q2.2 | Phone with country code | All | CV | — | [PRIMARY_PHONE] |
| Q2.3 | Email | All | CV | — | [PRIMARY_EMAIL], REQ-19 |
| Q2.4 | City and country | All | CV | 6 months | [CURRENT_CITY], [CURRENT_COUNTRY] |
| Q2.5 | LinkedIn or professional profile | Optional | CV | — | [LINKEDIN_URL], GAP-10 |
| Q2.6 | Portfolio, website or work samples | Optional | CV | — | [PORTFOLIO_URL], [PORTFOLIO_ASSETS] |
| **Section 3 — Eligibility and availability (new)** | | | | | |
| Q3.1 | Work permit or visa status for each target country | All | Private | 6 months | REQ-29, GAP-04, GATE-08 |
| Q3.2 | Need visa sponsorship? | All | Private | 6 months | REQ-29, Phase 0 ranking |
| Q3.3 | Notice period, or earliest start date | All | Private | 2 weeks | [AVAILABILITY], REQ-29 |
| Q3.4 | Any current commitment that affects your start | Optional | Private | 2 weeks | engine Step 4 |
| Q3.5 | Nationality (only if a target country or eligibility check needs it) | Path | Ask | — | [NATIONALITY], INQ-07 |
| **Section 4 — Pay (new, optional)** | | | | | |
| Q4.1 | Target gross yearly pay per target country, or "prefer not to say" | Optional | Private | 6 months | [SALARY_TARGET_GROSS], REQ-36 |
| Q4.2 | Currency | Optional | Private | — | REQ-36 |
| Q4.3 | Open to equity or bonus? Anything you won't accept? | Optional | Private | 6 months | REQ-36 |
| **Section 5 — Summary inputs** | | | | | |
| Q5.1 | Headline identity (current or aspired) | All | CV | — | [POSITIONING_HEADLINE], REQ-13 |
| Q5.2 | 3–5 core strengths you can back with an example | All | CV | — | REQ-14, RES-06 |
| Q5.3 | Strongest measurable result or credential | All | CV | — | REQ-14, REQ-09 |
| Q5.4 | What you're seeking (role and type of organisation) | All | CV | — | [PROFESSIONAL_SUMMARY], RES-06 |
| Q5.5 | First-job path: objective (role, strengths, value you'll add) | Path | CV | — | REQ-20 |
| **Section 6 — Experience (one block per role, newest first)** | | | | | |
| Q6.1 | Standard job title (not internal or creative) | All* | CV | — | REQ-19, REQ-13 |
| Q6.2 | Organisation name | All* | CV | — | REQ-01, GAP-10 |
| Q6.3 | One-line context (size, type, setting) | All* | CV | — | REQ-01 |
| Q6.4 | Location | All* | CV | — | REQ-01 |
| Q6.5 | Type of work: full-time, part-time, contract, self-employed, internship, volunteer, project | All* | CV | — | REQ-01 |
| Q6.6 | Start date (MM/YYYY) | All* | CV | — | REQ-25 |
| Q6.7 | End date (MM/YYYY or Present) | All* | CV | — | REQ-25 |
| Q6.8 | Title changes in the same organisation, each with dates | Optional | CV | — | REQ-01, REQ-24, REQ-25 |
| Q6.9 | What you were responsible for (3–6 points) | All* | CV | — | REQ-15, REQ-09 |
| Q6.10 | Results and impact (2–5 points, numbers or scale) | All* | CV | — | INQ-05, RES-04, REQ-09, [KEY_EVIDENCE] |
| Q6.11 | Optional proof for each result: link, document, or who could confirm (new) | Optional | Private | — | INQ-05, GATE-07 |
| Q6.12 | Tools, equipment, systems, methods used | All* | CV | — | [TOOLS_STACK], RES-05, REQ-18 |
| Q6.13 | Executive path: budget, team size, revenue or P&L, markets, board or investor exposure (new) | Path | CV | — | GAP-09, REQ-21 |
| **Section 7 — Education and training (one block each)** | | | | | |
| Q7.1 | Qualification or programme | Optional | CV | — | REQ-01 |
| Q7.2 | Institution or provider | Optional | CV | — | REQ-01 |
| Q7.3 | Location | Optional | CV | — | REQ-01 |
| Q7.4 | Start and end (month if you know it) | Optional | CV | — | REQ-25 |
| Q7.5 | Grade or distinction (only if strong and relevant) | Optional | CV | — | GAP-07 |
| Q7.6 | Coursework, honours, thesis, specialisation | Optional | CV | — | REQ-20 |
| **Section 8 — Skills** | | | | | |
| Q8.1 | Technical or specialist skills, with level | All | CV | — | RES-05, REQ-18 |
| Q8.2 | Tools, machinery, software, systems | All | CV | — | [TOOLS_STACK], REQ-18 |
| Q8.3 | Methods, processes, rules and standards you know | Optional | CV | — | REQ-18, GAP-05 |
| Q8.4 | Transferable strengths, each with an example | Optional | CV | — | REQ-20, REQ-09 |
| Q8.5 | Anything to leave out (old or irrelevant) | Optional | Private | — | REQ-01 "not to emphasise" |
| **Section 9 — Certifications and licences (one block each)** | | | | | |
| Q9.1 | Official name | Optional | CV | — | REQ-01, REQ-18 |
| Q9.2 | Issuing body | Optional | CV | — | REQ-01 |
| Q9.3 | Date obtained | Optional | CV | — | REQ-25 |
| Q9.4 | Expiry date, or "no expiry" (new: drives re-checks) | Optional | Private | At expiry | REQ-02 |
| Q9.5 | Verification link or credential number (never a government ID number) | Optional | Private | — | INQ-05, INQ-07 |
| **Section 10 — Languages** | | | | | |
| Q10.1 | Language and level on any scale (converted to A1–C2 or Native) | Optional | CV | — | [LANGUAGE_PROFICIENCY], REQ-29 |
| **Section 11 — Optional extras** | | | | | |
| Q11.1 | Notable projects: name, your role, outcome, tools | Optional | CV | — | INQ-05, REQ-20 |
| Q11.2 | Publications, patents, talks | Optional | CV | — | REQ-01 |
| Q11.3 | Awards or recognition | Optional | CV | — | REQ-01 |
| Q11.4 | Volunteering or community roles | Optional | CV | — | REQ-20 |
| Q11.5 | Military service (where relevant in that market) | Optional | CV | — | GAP-07 |
| **Section 12 — Market and format preferences** | | | | | |
| Q12.1 | Photo on CV: include or leave out | Optional | Ask | — | GAP-07, INQ-07 |
| Q12.2 | Personal details on CV (date of birth, marital status, nationality) | Optional | Ask | — | GAP-07, INQ-07 |
| Q12.3 | Preferred length | Optional | Private | — | REQ-17 |
| Q12.4 | Preferred file type (DOCX unless the ad says PDF) | Optional | Private | — | GAP-02, REQ-30 |
| Q12.5 | Employer or recruiter formatting instructions | Optional | Private | — | REQ-30, GATE-10 |
| Q12.6 | References: listed or "available on request" | Optional | CV | — | REQ-24 |
| **Section 13 — Confirmation (new)** | | | | | |
| Q13.1 | "Everything here is true. I wrote N/A where I didn't know." | All | Private | — | REQ-11, INQ-05 |

*All\** = required on the Experienced, Returning, Career change and Executive paths; optional on the First job path.

### 5A.4 Where the form touches the workflow

| Stage (Part 7) | What it uses from the form | What changes for the person |
|---|---|---|
| S1 Profile | Every section | Fills the form once (minus pre-filled fields), signs off once |
| S2 Find jobs | Q1.1–Q1.9, Q3.2 | Searches use the target, cities, exclusions and sponsorship need |
| S4 Read the job ad | Q1.5–Q1.6 base keyword list | Sees how far this job's keywords are from the base CV |
| S5 Fit | Q6.10–Q6.11 evidence, Q8 skills | Fit check cites evidence IDs |
| S6 Confirm your facts (M3) | Q1.9, Q3.1–Q3.5, Q4.1–Q4.3, Q12.1–Q12.5 | Only confirms. Asked again only if a field has expired |
| S7 Write the CV | Track base CV, Sections 5–11 | Writing starts from the base CV, not from zero |
| S10 ATS test | Q12.4–Q12.5, privacy classes | Checks file type, employer instructions, and that no Private field is printed |
| S11 Cover letter and answers | Q5.2–Q5.4, Q6.10 | Letter uses your own strengths and results |
| S15 After sending | Any new fact | New facts are proposed as form updates (APPROVE UPDATE) |

### 5A.5 Zero-conflict check

| Existing rule | How the form behaves | Conflict? |
|---|---|---|
| Engine Step 0: extract before asking | Pre-fills from uploads and links first (INQ-02) | None |
| Engine Step 2: gap-fill master list | The form contains every Step 2 field and more. Only gaps are shown | None |
| Engine Step 3: one 5/5 profile sign-off | Kept as is, once per person. Not counted in RES-11's 5 per-application gates | None |
| Engine Step 4: availability every 2 weeks, salary every 6 months | Same values in the Expires column | None |
| Engine Step 5: APPROVE UPDATE | Every later change to a form answer uses it | None |
| Engine Phase 3 critical gates | Pre-filled from the form, still confirmed at M3 | None |
| Engine invariant: no invented facts | N/A rule and Q13.1 confirmation | None |
| Engine invariant: research salary before suggesting one | Salary is optional. If blank, research runs as usual | None |
| Engine consent tiers | Filling the form is read-and-write to your own record only; nothing is sent | None |
| Editions built on the generic engine with a pre-filled profile | The form opens with everything already filled and asks only for gaps or new targets | None |
| Spec RES-11 (5 gates per application) | Adds no per-application gate | None |
| Spec INT-01 (preconditions) | Supplies the knockout facts, regional profile and positioning source S7 needs | None. It satisfies them earlier |
| Spec INT-05 (visible grades) | Readiness grade uses the same one-line format | None |
| Spec output rules | INQ-06: the spec wins, converted automatically | None |

---

## Part 6 — Extraction register

A permanent record of what each comparison found and which spec items now cover it. "Engine" means the current generic job-application-engine (v2.1.1). "Combined workflow" means the 7-step workflow from the CV Skills ATS Map.

### 6.1 Capability grid: neither covers (5)

| Capability | What was missing | Covered by | New in |
|---|---|---|---|
| Evidence IDs per achievement | Claims can't be traced automatically | REQ-01, GATE-07 | Already in v0.1; the gap is in implementation, not the spec |
| Single summary source | CV and form summaries can disagree | GAP-12, REQ-41 | v0.3 |
| Upload the tailored, gated CV | The original CV is uploaded | GAP-11, REQ-40, OUT-4 | v0.3 |
| Learning which CV choices work | Outcomes logged by company only | GAP-13, REQ-42, GATE-17 | v0.3 (GATE-17 extended) |
| Interview prep from the gap log | Gaps are logged and then dropped | GAP-14, REQ-43, REQ-39 | v0.3 |

### 6.2 Capability grid: the engine lacks, the combined workflow has

| Capability | Engine today | Covered by |
|---|---|---|
| Locked, weighted keyword list | None | REQ-06, RES-02, INT-03, GATE-05 |
| Writes a tailored CV | None | REQ-12 |
| CV writing rules | Form summary only | RES-04, RES-05, RES-06, REQ-13, REQ-14, REQ-15, REQ-16, REQ-17, REQ-18 |
| CV critique | None | REQ-38 (new in v0.3), RES-03 |
| Evidence-only keyword additions | Principle only, no keyword step | RES-01 |
| CV file export, parse-safe | Cover letter and package only | GAP-02, GATE-02, GATE-03 |
| Read test | None | GAP-01, GATE-04 |
| Counted keyword coverage | None | GAP-03, GATE-06 |
| Freeze the passed file | None | GATE-14, GAP-11 |
| Knockout facts on the CV | Form only (partial) | GAP-04, GATE-08 |
| Seniority applied to CV wording | Level detected, not applied (partial) | GAP-09 |
| Gaps carried across outputs | Letter and one answer only (partial) | REQ-39 (new in v0.3) |

### 6.3 Stage alignment: the engine's missing, gapped, split or conflicting stages

| Stage | Relation | Issue | Covered by |
|---|---|---|---|
| Keywords | Missing | No keyword step | REQ-06, RES-02 |
| CV writing | Missing | Never writes a CV | REQ-12 to REQ-21, RES-04, RES-05, RES-06 |
| Critique | Missing | No CV review | REQ-38 |
| ATS Gate | Missing | No tests on the file | Part 4 (GATE-00 to GATE-17) |
| Intake | Conflict | Facts must come before any writing | INT-01 |
| Writing quality | Conflict | Style pass can reword keywords | INT-03, RES-02 |
| Final check | Split | Two gates, two reports | INT-04 |
| Submit | Gap | Original CV uploaded | GAP-11, OUT-4 |
| Profile | Reused, gap inside | No evidence IDs | REQ-01 |
| Fit | Reused, gap inside | Requirements not handed over | INT-02 |
| Package | Reused, gap inside | A second summary can drift | GAP-12 |
| After | Reused, gap inside | Outcomes not linked to the CV | GAP-13 |

### 6.4 Merge conflicts → resolutions

| Conflict | Severity | Resolved by |
|---|---|---|
| CV written before intake clears | High | INT-01 |
| Original CV gets uploaded | High | GAP-11 |
| Two final gates, no combined verdict | High | INT-04 |
| Anti-AI pass rewrites locked keywords | Medium | INT-03 |
| Too many approval gates | Medium | RES-11 (replaces RES-09) |
| Two summaries that can disagree | Medium | GAP-12 |
| Summary versions assume one profile type | Medium | RES-10 |

### 6.5 Intake questionnaire v3 → v4

| Item | Result |
|---|---|
| What v3 is | A universal fill-in form (English and Arabic) collecting everything needed for an ATS-safe CV, for any level, industry and country |
| Spec items v3 fully covered | 0 of 90 (it collects facts but doesn't write, test, check or send) |
| Spec items v3 partly covered | 22 of 90 |
| Facts the workflow needs from a person | v3 supplied about 15 of ~20. v4 supplies all of them (adds pay, notice period, eligibility, seniority, exclusions, proof) |
| v3 fields kept in v4 | All 55. Mapping: 1–5 → Q1.1–Q1.6 · 6–11 → Q2.1–Q2.6 · 12 → Q1.9 and Q3.1 · 13–17 → Q5.1–Q5.4 and Q0.2 · Objective → Q5.5 · 18–28 → Q6.1–Q6.12 · 29–34 → Q7.1–Q7.6 · 35–39 → Q8.1–Q8.5 · 40–43 → Q9.1–Q9.5 · 44 → Q10.1 · 45–49 → Q11.1–Q11.5 · 50–55 → Q12.1–Q12.6 |
| One v3 detail removed | Government ID numbers (part of v3 item 51) are no longer collected (INQ-07) |
| v3 differences with the spec | 3 (summary length, heading name, education dates). The spec wins, converted automatically (INQ-06) |
| New in v4 | Section 0 (situation path), Section 3 (eligibility and availability), Section 4 (pay), Q1.4, Q1.7–Q1.9, Q6.11 proof, Q6.13 executive scale, Q9.4 expiry, Section 13 confirmation |

### 6.6 Engine v2.2.0 build and test runs (7 iterations)

| Finding | Covered by |
|---|---|
| Steps could stop on a blocked page or missing tool | INT-07 |
| A correct FAIL report didn't say whether anything was uploaded | INT-08 |
| Gate script: a saved report couldn't be re-read to freeze a PASS | INT-09 (regression check), GATE-14 |
| Gate script: "P&amp;L" read instead of "P&L"; fonts set by styles and themes not seen; white text, wrong fonts and sizes didn't fail; duplicate headings not checked | GATE-03, GATE-09 |
| Gate script: verdict could disagree with the grade; missing inputs gave a soft pass; size limit treated as Must; "I/O" counted as a pronoun; a PDF alone hid tables | GATE-01, GATE-03, GATE-09, GATE-10, GATE-13 |
| With few must-have keywords, one honest gap makes 90% impossible | Q-19 (open) |
| Replies could name a browser product or promise actions the session can't take; the self-test failed on installer-added quotes in name/version | INT-11; INT-09 (frontmatter read as values) |
| Release audit: A18 named a vendor browser product; one version field still 2.1.1 | INT-07 (browser order from the registry), INT-09 (two new self-test checks) |
| Release-build eval: the PASS could be frozen without a gate report, from a hand-written report, for a file the report never tested, or for another job | GATE-14 (freezing re-runs the gate from a config that names the job) |
| Adversarial review of the gate script: 12 bypasses (renamed XML prefix, decoy part, embedded documents, unverifiable or oddly named CV paths, shell uploads, invisible PDF text, silent PDF checks, renamed header/comment parts, style inheritance, frames and tracked moves, hygiene word gaps) | GATE-02, GATE-03, GATE-09, INT-10; known limits listed in GATE-03 |

---

## Part 7 — Proposed next version of the generic job-application-engine

This part applies the whole spec (Parts 0–6, including 5A) to the **generic** job-application-engine, as its next version. The current version is v2.1.1 (generic-universal). The engine stays the backbone, and 7.9 shows that every current component is kept, extended or changed, never removed. Labels used below: **As is** · **Changed** · **Moved** · **New**.

### 7.1 Current vs proposed, stage by stage

| Stage | Current generic engine (v2.1.1) | Proposed next version | Change | Spec items applied |
|---|---|---|---|---|
| S0 Setup | Execution mode · A0 capability detection · entry gate (Mode A / B) | Same, plus ATS platform detection when a job URL is given, and A0 lists which fallback rungs exist (INT-07) | Changed (small) | REQ-30, REQ-34, INT-07 |
| S1 Profile | First-use Steps 0–5: build profile, staleness check, update proposals | Intake questionnaire v4 (Part 5A) run through the same Steps 0–5: extract first, ask only gaps, then keep fresh. Builds the master record with evidence IDs, one track and base CV per target, screening facts and expiry dates | Changed | REQ-01, REQ-02, REQ-03, GAP-08, GAP-10, INQ-01, INQ-02, INQ-03, INQ-04, INQ-05, INQ-06, INQ-07, INQ-08, INQ-09 |
| Setup sign-off | Step 3 profile score (5/5), first use only | Same, once per person; shows the readiness grade (INQ-08) | As is | INQ-02, RES-11 |
| S2 Discovery (Mode A) | Phase 0: 10 boards, ranked top 20 | Same; the selected role opens a handoff record | Changed (small) | REQ-36, INT-02, INT-05, INQ-04 |
| S3 Job & company | Phase 1: post and form fetch, company brief, hiring manager | Same; post text and form questions saved to the handoff record | Changed (small) | REQ-04, REQ-08, REQ-30, INT-02 |
| M1 Company brief gate | Phase 1 score (5/5) | Mandatory 5/5 | As is | RES-11 |
| S4 Job analysis | Inside Phase 2 (requirements only) | Separate stage: classify requirements, build the locked keyword list with weights and variants, detect level | New (split out of Phase 2) | REQ-05, REQ-06, REQ-07, GAP-05, RES-02, INT-01, INT-05, INQ-04, INT-06 |
| S5 Fit | Phase 2: evidence columns, verdict, halt on mismatch | Same verdict rules; evidence mapped by ID; gap log started | Changed | REQ-09, REQ-10, REQ-11, REQ-39, INT-06 |
| M2 Fit gate | Phase 2 score (5/5) | Mandatory 5/5, also covers S4 | As is (wider) | RES-11 |
| S6 Fact intake | Phase 3, run before the package only | Moved before any writing. Adds knockout facts, regional profile and positioning source | Moved + changed | INT-01, REQ-29, GAP-04, GAP-07, RES-10, REQ-36, INQ-02 |
| M3 Facts gate | Phase 3 score (5/5) | Mandatory 5/5 | As is | RES-11 |
| S7 CV build | None | Write the CV from the chosen positioning source | New | REQ-12, REQ-13, REQ-14, REQ-15, REQ-16, REQ-17, REQ-18, REQ-19, REQ-20, REQ-21, REQ-24, REQ-25, REQ-26, RES-01, RES-04, RES-05, RES-06, GAP-09, GAP-12, REQ-41, INQ-04, INQ-06 |
| S8 CV critique | None | Check against one rubric, fix failed rules | New | REQ-38, RES-03, INT-05 |
| S9 CV style pass | Phase 5 runs on application text only | Same pass applied to the CV, protected terms left untouched | Changed | REQ-32, INT-03 |
| M4 CV text gate | None | Mandatory 5/5 covering S7–S9; shows the S8 critique score | New | RES-11 |
| S10 ATS Gate | None | Export the file and run the gate checks; freeze on PASS | New | GATE-00, GATE-01, GATE-02, GATE-03, GATE-04, GATE-05, GATE-06, GATE-07, GATE-08, GATE-09, GATE-10, GATE-11, GATE-12, GATE-13, GATE-14, GATE-15, GATE-18, GAP-01, GAP-02, GAP-03, GAP-06, REQ-22, REQ-23, REQ-27, REQ-28, REQ-31, OUT-1, OUT-2, OUT-3, INT-05, INQ-03, INT-07, INT-08, INT-10 |
| S11 Application package | Phase 4: form fields, own summary, cover letter, answers | Same outputs; summary derived from the CV; gap log drives the gap lines | Changed | REQ-35, RES-07, RES-08, GAP-12, REQ-39, REQ-36, INT-03 |
| S12 Package style pass | Phase 5 | Same pass, protected terms left untouched | Changed | REQ-32, INT-03 |
| M5 Package gate | Phase 4 and Phase 5 scores | One mandatory 5/5 covering S11–S12 | Changed (2 scores → 1) | RES-11 |
| S13 Final verdict | Phase 6: 8 application checks | One combined verdict: ATS Gate + application checklist + public-profile consistency + gap log handled | Changed | INT-04, REQ-33, GAP-06, GAP-10, INT-05 |
| Submit approval | APPROVE FILL / APPROVE SUBMIT after a data preview | Same exact phrases, only after the combined verdict PASS; complementary scores since M5 shown | As is | REQ-34, RES-11 |
| S14 Fill & submit | A04 fill + A05 submit; uploads "the file provided by the user" | Uploads only the fingerprinted file from the latest PASS; exact-phrase approval kept | Changed | GAP-11, REQ-40, OUT-4, GATE-14, REQ-34 |
| S15 After | Phase 7 branches A/B/C + A08–A11 follow-ups | Same branches; outcome logged against CV fingerprint and gate results; interview prep; gate tuning; evidence pack | Changed | GAP-13, GAP-14, REQ-42, REQ-43, GATE-16, GATE-17, REQ-37, REQ-02, INT-05 |

### 7.1a Where each current score goes

| Current engine score | Proposed | Type |
|---|---|---|
| First-use Step 3 profile sign-off | Setup sign-off, once per person | One-time 5/5 (not per application) |
| Phase 0 Discovery | S2 | Complementary |
| Phase 1 Company intelligence | M1 | Mandatory |
| Phase 2 Fit analysis | M2 (also covers the new S4 job analysis) | Mandatory |
| Phase 3 Clarifying intake | M3 | Mandatory |
| Phase 4 Application package | M5 | Mandatory |
| Phase 5 Writing quality | M4 for the CV pass, M5 for the package pass | Mandatory (inside both) |
| Phase 6 Governance | S13 combined verdict | Complementary (its checks still block on failure) |
| Phase 7 Post-submission | S15 | Complementary |
| (none) CV critique, ATS Gate | S8, S10 | Complementary (their checks still block on failure) |

No current score is lost: 5 become mandatory gates, and the rest are kept as complementary scores that show at the next mandatory gate and can escalate.

### 7.2 Before vs after

| Property | Current | Proposed |
|---|---|---|
| Produces a tailored CV | No | Yes (S7) |
| CV tested as a file before sending | No | Yes: 14 checks on the exported file (S10) |
| Keyword coverage measured | No | Counted, before vs after, with a stuffing cap (GATE-06) |
| File sent = file tested | No: the original CV is uploaded | Yes: fingerprint checked at upload (S14) |
| Facts confirmed before writing | For the package only | For everything, including the CV (INT-01) |
| Style pass safe for keywords | No exemption | Protected terms (INT-03) |
| Final checks | 8 application checks | One combined verdict for CV + application (INT-04) |
| Scored approvals per application | 8 mandatory in Mode A, 7 in Mode B | 5 mandatory in both modes, plus 6 complementary scores in Mode A (5 in Mode B) that block only on escalation, plus explicit approval for each irreversible action (RES-11) |
| Gaps carried through | Stated in the cover letter and one answer | Gap log through package and interview prep (REQ-39, GAP-14) |
| Learning from outcomes | Re-weights the next search | Also links each outcome to the CV version and gate results (GAP-13) |
| Who it works for | Anyone, through first-use questions | Anyone, through one structured form with 5 paths (first job to executive), any country, English and Arabic (INQ-01) |
| Questions asked twice | Possible across Step 2 and Phase 3 | Never: answers are pre-filled and only confirmed (INQ-02) |
| "100%" outcomes measured | None | OUT-1 to OUT-4 on every application |

### 7.3 Flow

Read top to bottom. **STOP** = you score 5/5 before it continues. **Doesn't stop you** = grades itself, shows you the grade and reason right away (INT-05), and only stops you at a grade of 3 or lower (RES-11).

| # | Step | Type | Goes where on failure |
|---|---|---|---|
| 1 | S0 Setup, S1 Profile: fill the intake form once (only gaps), then sign off once | Setup sign-off, once per person | Fix the record |
| 2 | S2 Find jobs (Mode A only) | Doesn't stop you | — |
| 3 | S3 Research the company | **STOP M1** | Redo S3 |
| 4 | S4 Read the job ad, make the word list | Doesn't stop you (reviewed at M2) | — |
| 5 | S5 Fit check | **STOP M2** | Mismatch ends here |
| 6 | S6 Confirm your facts | **STOP M3** | Redo S6 |
| 7 | S7 Write CV, S8 Check CV, S9 Polish CV | **STOP M4** | Redo S7–S9 |
| 8 | S10 ATS test on the file | Doesn't stop you | Fail goes back to row 7 |
| 9 | S11 Cover letter and answers, S12 Polish | **STOP M5** | Redo S11–S12 |
| 10 | S13 Final check | Doesn't stop you | Fail goes back to row 9 |
| 11 | You type APPROVE SUBMIT | Your explicit OK | Waits |
| 12 | S14 Send the tested file | Runs on its own | Wrong file blocks the send |
| 13 | S15 After sending | Doesn't stop you | Next job goes back to row 2 |

### 7.4 Stop points

| Where | Stops when | Goes back to |
|---|---|---|
| S5 | Fit verdict is Mismatch (unless you override, which is logged) | S2 or end |
| Any stage | A precondition is unmet (INT-01) | The stage that supplies it |
| S10 | ATS Gate FAIL on a Must check | The stage that owns the fix (GATE-15) |
| S13 | Combined verdict FAIL | S11, or S7 if the CV is the cause |
| S14 | No PASS for this job, or fingerprint mismatch (GAP-11) | S10 |
| M1–M5 | Your score is below 5 | Revision loop for the stages that gate covers |
| Complementary stage | Escalated: automatic score 3 or lower, or your score below 5 | That stage, until it reaches 5/5 |
| Anywhere | An irreversible action without explicit approval | Waits for approval |

### 7.5 What stays as is

Mode A / B entry gate · discovery search logic and ranking · company research operations · fit verdict rules · cover-letter templates and banned closes · salary research protocol · consent tiers and exact approval phrases · automations A01–A16 · execution modes and re-anchor checks · the excluded-companies log.

### 7.6 Rollout order

| Wave | What | Why first |
|---|---|---|
| 1 · Stop the biggest losses | INQ-02, INQ-03, INQ-05, INQ-06, INQ-07 (intake form basics), GAP-11 (upload the tested file), INT-01 (facts before writing), INT-04 (one verdict), S7 CV build (REQ-12 to REQ-19), S10 core gate checks (GATE-00 to GATE-09, GATE-13 to GATE-15) | Without these, tailoring either doesn't happen or doesn't reach the employer |
| 2 · Make it reliable | INT-02, INT-03, REQ-38, REQ-39, RES-10, RES-11, INQ-01, INQ-04, INQ-08, GAP-12, GAP-13, GATE-10, GATE-11, GATE-16 | Removes drift between stages and cuts approval friction |
| 3 · Make it learn | GAP-14, GATE-12, GATE-17, GAP-09, GAP-10, REQ-20 | Improves results over time once the data exists |

### 7.7 Workflow acceptance

An application run on the proposed workflow passes when all of the following hold:

1. OUT-1, OUT-2, OUT-3 and OUT-4 all hold.
2. 0 invented claims (REQ-11, GATE-07).
3. The combined final verdict is PASS (INT-04).
4. All 5 mandatory gates (M1–M5) passed at 5/5. Every complementary stage has a logged score, and every escalation was resolved. Each irreversible action had an explicit approval (RES-11).
5. Every Must item that applies to the run is recorded as evaluated in a stage report.

### 7.8 Coverage check

Two checks run for every version: (1) every active spec item maps to a stage or rollout wave; (2) every component of the current generic engine appears in 7.9 as Kept, Extended, Changed or New, so the next version covers 100% of v2.1.1.

Every active (not deprecated) OUT, RES, GAP, REQ, GATE and INT item in this spec is mapped to at least one stage in 7.1 or one wave in 7.6. The check is re-run for every version.

### 7.9 Compatibility with the current generic engine (v2.1.1)

Every part of the current generic engine is listed here with what happens to it in the next version. **Kept** = unchanged · **Extended** = same behaviour plus additions · **Changed** = behaviour changes, described. No part is removed, so anything that works in v2.1.1 still works.

#### Phase names in the next version

The next version keeps every current phase number and name. New work is added as sub-phases, so existing references to "Phase 3" or "Phase 6" stay valid.

| Next-version phase | Spec stages | Status |
|---|---|---|
| First-Use Setup (Steps 0–5) | S1 + intake questionnaire (Part 5A) + setup sign-off | Extended |
| Phase 0 Job Discovery | S2 | Kept (reads the new intake fields) |
| Phase 1 Company Intelligence | S3 + M1 | Kept |
| Phase 2 Fit Analysis, with new Step 2A Job analysis | S4 + S5 + M2 | Extended |
| Phase 3 Clarifying Intake (moved before any writing) | S6 + M3 | Changed (order) |
| Phase 3B CV Build (new) | S7 + S8 + S9 + M4 | New sub-phase |
| Phase 3C ATS Gate (new) | S10 | New sub-phase |
| Phase 4 Application Package | S11 + M5 | Extended |
| Phase 5 Writing Quality Pass | S9 (CV) + S12 (package) | Extended (protected terms) |
| Phase 6 Governance Gate | S13 combined verdict | Extended |
| Phase 7 Post-Submission Loop | S15 | Extended |

#### Every current component

| Current component | Next version | What changes |
|---|---|---|
| Execution mode gate (agent_supported, cowork_autonomous) | Kept | Mode 2 re-anchoring also covers Phases 3B and 3C |
| A0 Capability detection | Extended | Also checks that a document tool for CV export (DOCX/PDF), text readers for the read test, and image viewing plus browser or computer control for the visual review (GATE-18) are available. First turn shows a 3–5 line summary (full map on request or when a needed tool is missing), together with the extracted details and the first question batch in one message; replying counts as "Begin" |
| First-Use Setup Steps 0–5 | Extended | Step 2's question list becomes the intake questionnaire v4. Steps 0, 1, 3, 4 and 5 behave as before |
| Session entry gate (Mode A / B) | Extended | No CV and no job link with "help me apply": Mode A after setup; pasting a link switches to Mode B |
| Dynamic session checklist (status board) | Extended | New rows for Phases 2A, 3B, 3C; each row shows its grade and reason (INT-05) |
| Level classification framework | Extended | Also sets CV wording by level (GAP-09) |
| Phase scoring gate format (5/5, 3 prompts) | Kept | Used unchanged at M1–M5 and setup sign-off. Other phases show complementary scores (RES-11) |
| Consent tiers 1–3 and exact approval phrases | Kept | New actions use the existing tiers (see A17 below) |
| A01–A03, A05, A08–A16 automations | Kept | — |
| A04 Browser form filling | Changed | Uploads only the fingerprinted file from the latest ATS Gate PASS (GAP-11) |
| New A18 Fallback and visual audit | New | Tier 1. Runs the INT-07 ladder when a tool is missing, and the visual audits (CV pages, filled form, portal preview, confirmation page). Never lowers a consent tier |
| New enforcement hooks (Claude Code plugin only) | New, opt-in | INT-10. Block an untested CV upload; cancel a PASS after an edit. Nothing changes where hooks don't run |
| New self-test, evals and grader inside the skill | New | INT-09. For maintainers; not used during an application |
| A06 Cover letter DOCX, A07 package document | Extended | The package document includes the gated CV file |
| New A17 CV file export | New | Creates the CV DOCX/PDF for the ATS Gate. Tier 2 (APPROVE CREATE), like A06. Default: one approval per application covers all re-tests; can be switched to every export |
| Browser, email, document storage protocols | Kept | — |
| Platform-aware routing and platform notes | Extended | Adds ATS platform profiles (REQ-30) |
| Applicant profile template | Extended | Adds intake fields (5A.3), evidence IDs, tracks, privacy classes, expiry dates |
| Salary anchors template | Kept | Fed by intake Section 4 when given |
| Excluded companies log | Extended | Each entry links to the application log (GAP-13) |
| Application log | New | GAP-13. Written under the same APPROVE UPDATE rule as the excluded companies log |
| Cover letter templates | Kept | Gap lines come from the gap log (REQ-39); summary derived from the CV (GAP-12) |
| Fit analysis, writing quality, governance gate references | Extended | As described in Phases 2, 5, 6 above |
| Invariants (all 12) | Kept, 7 added (13–19) | All 12 still hold. The new order makes "no application text before Phase 3" apply to the CV too. Invariant 19 is new in this version: never stop on a missing tool before the fallback ladder, and never lower a consent tier when falling back |
| rules.json, automation-registry.json | Extended | New phases, A17, new gates and complementary scores added; nothing removed |
| Mandatory exclusions document | Kept | — |

---

## Part 8 — Traceability

### Outcomes → requirements

| Outcome | Requirements that deliver it |
|---|---|
| OUT-1 Readable | GAP-01, GAP-02, REQ-22, REQ-23, REQ-24, REQ-25, REQ-28, REQ-30 · verified by GATE-02, GATE-03, GATE-04, GATE-18 |
| OUT-2 Matched | REQ-05, REQ-06, GAP-03, GAP-05, RES-01, RES-02, RES-05, REQ-13, REQ-14, REQ-18, REQ-27 · verified by GATE-05, GATE-06 |
| OUT-3 Not knocked out | REQ-29, GAP-04, REQ-01 (screening facts), REQ-02 · verified by GATE-08 |
| OUT-4 Delivered as tested | GAP-11, REQ-40, GATE-14, INT-04 · verified at stage S14 |
| Zero invention (all outcomes) | RES-01, REQ-09, REQ-11 · verified by GATE-07 |

### Gaps → coverage-map items

| Gap | Covers ability |
|---|---|
| GAP-01 | REQ-28 |
| GAP-02 | REQ-22, REQ-23 |
| GAP-03 | REQ-27 |
| GAP-04 | Extends REQ-29 |
| GAP-05 | REQ-26 |
| GAP-06 | REQ-33 (CV half) |
| GAP-07 | REQ-31 |
| GAP-08 | Extends REQ-01, REQ-12 |
| GAP-09 | Extends REQ-07 |
| GAP-10 | New ability (not in the original 37) |
| GAP-11 | REQ-40 |
| GAP-12 | REQ-41 |
| GAP-13 | REQ-42 (with GATE-17) |
| GAP-14 | REQ-43 |

### ATS Gate → what each check runs

| Gate check | Runs or verifies |
|---|---|
| GATE-02 Export | GAP-02, REQ-22 |
| GATE-03 Layout lint | GAP-02, REQ-23 |
| GATE-04 Read test | GAP-01, REQ-28, OUT-1 |
| GATE-18 Visual review | GATE-12, GATE-03, GATE-04, OUT-1 |
| GATE-05 Locked-keyword integrity | RES-02, REQ-06 |
| GATE-06 Keyword coverage | GAP-03, GAP-05, REQ-27, OUT-2 |
| GATE-07 Evidence trace | RES-01, REQ-11 |
| GATE-08 Knockout alignment | REQ-29, GAP-04, OUT-3 |
| GATE-09 Content hygiene | REQ-14, REQ-17, REQ-19, REQ-24, REQ-25, REQ-32 |
| GATE-10 Platform profile | REQ-30 |
| GATE-11 Regional profile | GAP-07, REQ-31 |
| GATE-12 Skim test | REQ-13, RES-06 |
| GATE-13 Report | GAP-06, REQ-33 (CV half) |
| GATE-14 Freeze | REQ-34 (approval before irreversible actions) |
| GATE-16 Evidence pack | REQ-37 |

### Workflow integration → where it applies

| Item | Applies to stages (Part 7) | Connects |
|---|---|---|
| INT-01 Stage preconditions | S4–S14 | REQ-04, REQ-05, REQ-10, REQ-29, REQ-39, GAP-07, RES-10, REQ-06, GATE-01 |
| INT-02 Structured handoffs | S2–S15 | Every stage input and output |
| INT-03 Protected terms | S9, S10 (GATE-05), S11, S12 | RES-02, REQ-32, GAP-12 |
| INT-04 One final verdict | S13 | GATE-13, REQ-33, GAP-06, GAP-10, REQ-39 |
| INT-05 Visible grades | S2, S4, S8, S10, S13, S15 and M1–M5 | RES-11, GAP-13 |
| INT-06 Shared requirement list | S4, S5, M2 | REQ-05, REQ-06, REQ-09, REQ-39 |
| INT-07 Fallback ladder | S0–S15 | GATE-18, GAP-11, REQ-34, GATE-16 |
| INT-08 Side-effects line | S10–S15 | REQ-34, INT-05 |
| INT-09 Release harness | Every release | GATE-03, GATE-09, GATE-13, GATE-14 |
| INT-10 Enforcement hooks | S10, S14 | GAP-11, GATE-14 |
| INT-11 Capability wording | S0, S3, S14 and every reply | INT-07, REQ-34 |

### Intake questionnaire → where it feeds

| Form sections | Feeds | Stages |
|---|---|---|
| 0 Situation | INQ-01 paths, REQ-07, REQ-20, GAP-09 | S1 |
| 1 Target | INQ-04, GAP-08, RES-10, REQ-06, GAP-07 | S1, S2, S4 |
| 2 Contact | REQ-01, REQ-19, GAP-10 | S1, S10 |
| 3 Eligibility, 4 Pay | REQ-29, GAP-04, REQ-36 | S6, S10, S11 |
| 5 Summary inputs | REQ-13, REQ-14, RES-06 | S7, S11 |
| 6 Experience | INQ-05, RES-04, REQ-09, REQ-15, GAP-09 | S5, S7 |
| 7–11 Education, skills, certificates, languages, extras | REQ-01, REQ-18, RES-05, REQ-20, REQ-02 | S5, S7 |
| 12 Market and format | GAP-07, GAP-02, REQ-17, REQ-30, INQ-07 | S6, S10 |
| 13 Confirmation | REQ-11 | S1 |

### Priority summary

| Priority | Count | IDs |
|---|---|---|
| Must | 63 | RES-01, 02, 04, 05, 11 · GAP-01, 02, 03, 06, 11 · REQ-01, 03, 04, 05, 06, 09, 11, 12, 13, 14, 15, 16, 18, 22, 23, 24, 25, 27, 28, 29, 33, 34, 38, 39, 40 · GATE-00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 13, 14, 15 · INT-01, 02, 03, 04, 05, 06, 07, 11 · INQ-01, 02, 03, 05, 06, 07, 09 |
| Should | 34 | RES-03, 06, 07, 08, 10 · GAP-04, 05, 07, 08, 12, 13 · REQ-02, 07, 08, 10, 17, 19, 21, 26, 30, 31, 32, 35, 37, 41, 42 · GATE-10, 11, 16, 18 · INQ-04, 08 · INT-08, 09 |
| Could | 9 | GAP-09, 10, 14 · REQ-20, 36, 43 · GATE-12, 17 · INT-10 |
| Deprecated | 1 | RES-09 (not counted above) |

---

## Part 9 — Open questions

| ID | Question | Affects |
|---|---|---|
| Q-01 | ~~DOCX or PDF as the default when the portal doesn't say? Currently DOCX~~ **Answered in v0.8.0:** DOCX as the main file; also upload PDF when the portal accepts more than one file | GAP-02 |
| Q-02 | ~~Must-have coverage target: keep 90% or raise it?~~ **Answered in v0.8.0:** 90% | OUT-2, GAP-03 |
| Q-03 | ~~Which regional profiles to verify first?~~ **Answered in v0.8.0:** 6 country profiles plus one General International profile for every other country; more on demand | GAP-07 |
| Q-04 | ~~Which positioning tracks become master CVs?~~ **Answered in v0.8.0:** 2 tracks per person recommended; up to 3 when targets truly differ | GAP-08 |
| Q-05 | ~~Which text extractors to use for the read test?~~ **Answered in v0.8.0:** 2 readers as standard, 1 minimum; plus a visual review as ATS and recruiter using vision and browser or computer control (GATE-18) | GAP-01, GATE-04 |
| Q-06 | ~~Keyword repetition cap: keep 4 or change?~~ **Answered in v0.8.0:** No more than 4 times; about 3 is the normal target | GATE-06 |
| Q-07 | ~~File size limit when the platform is unknown: keep 2 MB?~~ **Answered in v0.8.0:** 2 MB | GATE-10 |
| Q-08 | ~~Max failed gate runs before asking the candidate: keep 3?~~ **Answered in v0.8.0:** 1 retry for normal issues; up to 5 for major issues, decided by retry points (GATE-15) | GATE-15 |
| Q-09 | ~~Adopt the 3-checkpoint approval budget, or keep a scored gate at every stage?~~ **Answered in v0.4.0:** hybrid, 5 mandatory gates plus complementary scores (RES-11) | RES-09, RES-11 |
| Q-10 | ~~Follow-up window before marking an application "no response": keep 30 days?~~ **Answered in v0.8.0:** Set per application: 7 days (fast employers), 14 (most), 21 (large or government); 21 is the maximum | GAP-13 |
| Q-11 | ~~Generate interview prep at submission, or only once an interview is booked?~~ **Answered in v0.8.0:** When an interview is booked; a short prep sheet at submission only on request and approval | GAP-14 |
| Q-12 | ~~Should job analysis (S4) stay a separate stage, or run inside the fit check?~~ **Answered in v0.8.0:** Keep Step 2A, sharing one requirement list with the fit check (INT-06) | Part 7 |
| Q-13 | ~~Automatic score mapping for complementary stages: keep the default (5 / 4 / 3 / 1–2)?~~ **Answered in v0.4.1:** keep the default | RES-11 |
| Q-14 | ~~Escalation threshold: escalate at an automatic score of 3 or lower, or only at 2 or lower?~~ **Answered in v0.4.1:** 3 or lower | RES-11 |
| Q-15 | ~~Add a separate stop to review the job-ad word list right after S4?~~ **Answered in v0.4.1:** no, it's reviewed at M2 | RES-11 |
| Q-16 | ~~First-job path: keep Experience before Education (REQ-24), or allow Education first for people with no work history? Default: keep REQ-24~~ **Answered in v0.8.0:** The country profile decides | REQ-24, INQ-01 |
| Q-17 | ~~Add more form languages beyond English and Arabic? Default: not yet~~ **Answered in v0.8.0:** Auto-translate any language from the English master; English and Arabic maintained by hand | INQ-01 |
| Q-19 | **Open.** With few must-have keywords, one honest gap makes the 90% coverage rule impossible (4 must-haves, 1 unproven = 75%), which clashes with "gap logged instead of invented" (OUT-2). Options: (a) keep 90% as is: the role is a stop, and the person decides whether to apply anyway; (b) count logged gaps as covered for roles with fewer than 10 must-haves, but show them in the grade line; (c) require 90% only when there are 10 or more must-haves, otherwise allow at most 1 logged gap. Until answered: (a) | GATE-06, OUT-2 |
| Q-18 | ~~Approval for creating the CV file (A17): one APPROVE CREATE per application covering every re-test, or approve every export?~~ **Answered in v0.8.0:** One approval per application by default; can be switched to every export | GATE-02, Part 7.9 |

---

## Part 10 — Templates for new items

```markdown
#### REQ-XX <Ability name>
- **Requirement:** <one sentence, what must be true>
- **Spec:** <how, with concrete rules and numbers>
- **Acceptance:** <a test with a pass/fail result>
- **Best today:** <Full | Partial | None (+ what it lacks)> · **Basis:** <Evidence | Convention | Default> · **Priority:** <Must | Should | Could> · **Scope:** <Core | Adjacent> · **Status:** Proposed
```

```markdown
### RES-XX <Rule name>
- **Rule:** <the decision>
- **Why:** <the conflict it settles>
- **Acceptance:** <a test>
- **Origin:** <source> · **Priority:** <…> · **Status:** Proposed
```

```markdown
### GATE-XX <Check name>
- **Requirement:** <what the gate must verify>
- **Spec:** <how it is checked, on the extracted text or the file>
- **Acceptance:** <pass/fail rule; say whether it blocks submission>
- **Basis:** <…> · **Priority:** <Must = blocks, cannot be waived | Should = waivable | Could = advisory> · **Scope:** Core · **Status:** Proposed
```

A new GATE check also needs a row in the Gate flow table (Part 4) with its run order.

```markdown
### INT-XX <Integration rule name>
- **Requirement:** <what must hold between stages>
- **Spec:** <stages involved, data passed, order or blocking rule>
- **Acceptance:** <a pass/fail test across stages>
- **Origin:** <comparison or conflict> · **Priority:** <…> · **Status:** Proposed
```

A new intake question gets the next free Q number in its section, plus Asked, Privacy, Expires and Feeds values in 5A.3.

When adding an item: give it the next free ID, link it in Part 8, record where it came from in Part 6, map it to a stage in Part 7.1, update the priority summary, and add a Change log line.

---

## Change log

| Version | Date | Change |
|---|---|---|
| 0.11.0 | 2026-10-05 | New INT-11 capability wording (Must; generic edition): no browser or app brand names, never "on your computer" or a promised action unless the A0 Capability Map shows the tool ACTIVE, form-filling wording by browser-control state; 2 new form-filling tests and a wording check on every test reply (6 tests, 40/40). INT-09 adds install-proof metadata reading (quoted name/version). Part 6.6, Part 8 and priority summary (63/34/9) updated. |
| 0.10.1 | 2026-10-05 | Release audit against the engine repo's normative docs: INT-07 browser rung follows the registry order with no vendor brand path; INT-09 self-test now also checks all version fields and vendor brand names; GATE-14 freezing a PASS now requires the gate report and refuses any file the report did not test (found by the release-build eval run); GATE-04 read test can't pass with nothing to compare; GATE-05 warns when no approved CV text is given; GATE-02/03/09 and INT-10 hardened against 12 bypasses found by an adversarial review (see Part 6.6); GATE-14 freezing re-runs the gate from a config naming the job, uploads are checked against the job in progress, and a changed keyword list cancels the PASS; 85 checks; Part 6.6 row added; header updated. Wording only, no acceptance criteria changed. |
| 0.10.0 | 2026-10-05 | From the v2.2.0 eval review (4 test cases, 7 iterations, final run 25/25 = 100% vs 17/25 = 68% for v2.1.1; self-test 45/45): INT-07 fallback ladder (A18, invariant 19); INT-08 side-effects line; INT-09 release harness and 100% pass bar; INT-10 optional enforcement hooks; GATE-01 script refuses missing inputs; GATE-03 white or tiny text, fonts via styles and themes, PDF-alone flag; GATE-09 "I/O" not a pronoun, each heading once; GATE-10 size limit is Should-level; GATE-13 verdict always agrees with the grade, report saved; GATE-14 waivers accepted before freezing; Part 6.6, 7.1, 7.9, Part 8 and priority summary (62/34/9) updated; Q-19 opened. |
| 0.9.0 | 2026-10-05 | From building and testing job-application-engine v2.2.0 (3 test cases, pass rate 41% → 88% vs v2.1.1): INQ-09 ask in small batches (max 10 questions); A0 first-turn presentation and one first message (7.9); no-CV-no-link routes to Mode A (7.9); GATE-03 checks document properties and page size; GAP-07 adds page size; "Implemented in" header row. |
| 0.8.0 | 2026-10-05 | All 14 open questions answered (Q-01 to Q-08, Q-10 to Q-12, Q-16 to Q-18) and applied: DOCX main + PDF when allowed (GAP-02); 90% confirmed; 6 country profiles + General International (GAP-07); 2 tracks, up to 3 (GAP-08, INQ-04); 2 readers + new GATE-18 visual review as ATS and recruiter; repeat cap 4, target 3 (GATE-06); 2 MB confirmed; retry points with 1 / up to 5 retries (GATE-15); follow-up window 7/14/21 days (GAP-13); interview prep when booked (GAP-14); new INT-06 shared requirement list; first-job section order set by country profile (REQ-24); auto-translated form languages (INQ-01); A17 approval once per application, switchable (GATE-02, 7.9). Versioning rule 7 clarified. |
| 0.7.0 | 2026-10-05 | Framed as the next version of the generic job-application-engine (not any personal edition): Target row, rule 12, Part 7 retitled, new 7.9 compatibility table covering every v2.1.1 component and next-version phase names (Phases 2A, 3B, 3C added; nothing removed); new automation A17 (CV export, Tier 2) noted in GATE-02; Q-18 added; personal-edition wording removed from 5A.5. |
| 0.6.0 | 2026-10-05 | Added Part 5A, intake questionnaire v4 (from the Universal v3 form, for public use at any level, industry and country): rules INQ-01 to INQ-08, field list Q0.1–Q13.1 with privacy and expiry, workflow touchpoints, zero-conflict check against the engine's first-use Steps 0–5. Linked into REQ-01, REQ-02, GAP-08, GATE-09, RES-11 (setup sign-off is one-time), Part 6.5 register, Part 7 (7.1, 7.1a, 7.2, 7.3, 7.6), traceability, glossary, ID scheme, Q-16 and Q-17, templates. |
| 0.5.1 | 2026-10-05 | Added version snapshots: full copies of each version in `spec-versions/`, plus rule 11 in "How to use". |
| 0.5.0 | 2026-10-05 | Added INT-05: every grade from a step that doesn't stop you is shown live with its reason, and again at the next stop; the After-sending grade shows at the start of the next application. "Background" renamed to "Doesn't stop you". RES-11, Part 7.1, 7.3, glossary and traceability updated. |
| 0.4.1 | 2026-10-05 | Your two decisions confirmed: the job-ad word list is reviewed at M2 (no extra stop); background steps stop you at a score of 3 or lower. Q-13, Q-14 and Q-15 answered. Flow chart replaced by a table. |
| 0.4.0 | 2026-10-05 | Q-09 answered: hybrid approval model. Added RES-11 (5 mandatory 5/5 gates M1–M5 + complementary scores with roll-up, escalation and logging); RES-09 deprecated; INT-01, Part 6.4, Part 7 (7.1 gate rows, new 7.1a score map, 7.2, 7.3 flow (later replaced by a table), 7.4 stops, 7.6, 7.7) updated; glossary +3; Q-13 and Q-14 added. |
| 0.3.0 | 2026-10-05 | From the Workflow vs Engine comparison: OUT-4; RES-09 (approval budget), RES-10 (positioning fallback); GAP-11 to GAP-14; REQ-38 (CV critique), REQ-39 (gap log), REQ-40 to REQ-43; new Part 5 Workflow integration (INT-01 to INT-04); new Part 6 extraction register; new Part 7 proposed job-application-engine workflow (current vs proposed); handoff notes on GATE-01, GATE-14, GATE-17; glossary, ID scheme, traceability, open questions (Q-09 to Q-12) and templates updated; parts renumbered (IDs unchanged). |
| 0.2.0 | 2026-10-05 | Added Part 4, ATS Gate: gate flow and 18 checks (GATE-00 to GATE-17); GAP-06 now runs inside the gate; traceability, priority summary, open questions (Q-06 to Q-08) and templates updated; parts renumbered (IDs unchanged). |
| 0.1.0 | 2026-10-05 | First draft: 3 outcomes, 8 rules (from contradictions C1–C8), 10 gap requirements (from G1–G10), 37 ability requirements (from the coverage map, A01–A37), traceability, open questions, templates. |
