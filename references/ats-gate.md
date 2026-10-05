# ATS Gate — Phase 3C
# job-application-engine v2.2.0 (generic)
# Read when: Phase 3C, before exporting the CV file; when a gate check fails; when writing the gate report

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

## The gate

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
- **Acceptance:** A missing input stops the gate with a message naming the input and which step provides it.
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
- **Spec:** Detect and count: tables · text boxes or frames · multiple columns · images, icons, shapes, charts · text in the page header or footer · non-standard bullet characters · fonts outside the allowed list · font sizes outside 10–12 pt for body text · links shown as words instead of full URLs · document properties (title and author must be the person, not a tool name) · page size against the country profile.
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
- **Spec:** Headings on the allowed list and in order (REQ-24) · 0 Private intake fields printed (INQ-03) · every date range matches the pattern (REQ-25) · page and bullet limits (REQ-17) · 0 pronouns and title check (REQ-19) · 0 leftover placeholders (anything in `[ ]` or `{ }`, "TBD", "XX") · 0 banned phrases (REQ-14, REQ-32) · spelling variant consistent with the regional profile (US or UK).
- **Acceptance:** Every sub-check passes.
- **Basis:** Convention · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-10 ATS platform profile
- **Requirement:** Apply the target platform's known rules (REQ-30).
- **Spec:** Check the file type the platform prefers, its file size limit (stay under 2 MB, confirmed in Q-07), any page limit, and whether it expects work history retyped into form fields. If the platform is unknown, apply the strictest common profile: DOCX, under 2 MB, plain layout.
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
- **Spec:** Report holds: run date and time · file names and fingerprints (GATE-14) · result of each check with its findings · coverage before → after · waivers with reasons · verdict. Verdicts: **PASS** (all checks pass) · **PASS WITH WAIVERS** (only Should-level checks waived) · **FAIL** (any Must check failed, with the step that owns the fix). The report is written in plain language and shows the most important failure first.
- **Acceptance:** A report exists for every run. The verdict follows these rules exactly.
- **Basis:** Default · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### GATE-14 Freeze and fingerprint
- **Requirement:** The file submitted is exactly the file that passed.
- **Spec:** After a PASS, compute a fingerprint (a hash, i.e. a unique code calculated from the file's bytes) for each file and record it in the report. Before submission, recompute it and compare. **Any edit after a PASS cancels the PASS** and the full gate runs again.
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

## Specs the gate runs

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

### REQ-24 Standard section headings and order
- **Requirement:** Use headings ATS parsers recognise, in the expected order.
- **Spec:** Order: Contact → Headline → Summary → Skills → Experience (most recent first) → Education → Certifications → optional (Languages, Projects, Publications). Heading names: "Summary", "Skills", "Experience" or "Professional Experience", "Education", "Certifications", "Languages". No creative names like "My Journey".
- **First-job path (Answered: Q-16):** for people with no work history, the country profile (GAP-07) decides whether Education comes before Experience.
- **Acceptance:** Every heading is on the allowed list and in order. Regional profile may adjust (GAP-07).
- **Best today:** Partial · **Basis:** Convention · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### REQ-25 Consistent date format
- **Requirement:** One date format for every role and qualification.
- **Spec:** Default "MMM YYYY – MMM YYYY" (e.g. "Aug 2025 – Feb 2026"), "Present" for the current role. Month always included for roles. Same dash style everywhere. Regional profile may change the format.
- **Acceptance:** 100% of date ranges match the chosen pattern, checked by a pattern match.
- **Best today:** Partial · **Basis:** Convention · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### REQ-30 ATS platform awareness
- **Requirement:** Detect which ATS the employer uses and apply its known behaviour.
- **Spec:** Detect from the application URL or page (e.g. Greenhouse, Lever, Workday, Ashby, SmartRecruiters, Taleo, iCIMS, Breezy). Each platform has a profile: preferred file type, known parsing quirks, field limits, and whether to retype work history into the form. Profiles are extendable.
- **Acceptance:** Platform recorded for every application. Its profile rules applied to the file (GAP-02) and the form (REQ-36).
- **Best today:** Partial (forms only) · **Basis:** Default (verify each profile) · **Priority:** Should · **Scope:** Core · **Status:** Proposed
