# CV Build — Phase 3B
# job-application-engine v2.2.0 (generic)
# Read when: Phase 3B (writing, critiquing and styling the CV); Phase 4 when deriving the form summary

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

## Writing rules

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

### RES-10 Positioning source fallback
- **Rule:** Choose the CV starting point in this order: (1) the positioning track that matches the job's main requirement (GAP-08); (2) if no tracks are defined, the version that matches the role's seniority level (REQ-07); (3) otherwise the general master CV. Record which one was used and why.
- **Why:** A workflow that assumes tracks breaks on profiles that only have level-based versions, and the reverse.
- **Acceptance:** Every tailored CV records its source and the rule step that selected it. The workflow runs correctly with 0 tracks defined.
- **Origin:** Merge conflict "summary versions assume one profile type" · **Priority:** Should · **Status:** Proposed

## Abilities

### REQ-12 Produce a full tailored CV
- **Requirement:** Output a complete tailored CV, not only feedback or fragments.
- **Spec:** Starts from the matching track master (GAP-08). Section order per REQ-24. Delivered as a file per GAP-02, plus an editable text version. Ships with a change log listing what changed and why.
- **Acceptance:** A complete CV that passes the GAP-06 checklist.
- **Best today:** Full (text only, not a tested file) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### REQ-13 Headline matches the job title
- **Requirement:** A headline under the name that mirrors the post's job title, or the closest truthful variant.
- **Spec:** Use the exact title when it fits your real level and function. Otherwise use the closest honest form (e.g. "Head of Product | Product Leader" for a "Director of Product" post) without claiming a title you didn't hold.
- **Acceptance:** Headline contains the post's title or a declared variant, and job titles in the experience section remain the real ones.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### REQ-14 Professional summary
- **Requirement:** A summary tuned to the role, following RES-06.
- **Spec:** Banned generic phrases (Default list, extend as needed): "passionate about", "results-driven", "strategic thinker", "team player", "proven track record", "dynamic". No pronouns (REQ-19).
- **Acceptance:** Meets RES-06. 0 banned phrases.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### REQ-15 Bullet formula
- **Requirement:** Every experience bullet follows RES-04.
- **Spec:** One sentence each. Starts with a strong past-tense verb (present tense for the current role is allowed only if used consistently). No "responsible for".
- **Acceptance:** 100% of bullets meet RES-04.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### REQ-16 Bullets ordered by relevance
- **Requirement:** Within each role, order bullets from strongest to weakest match with the post's top priorities.
- **Spec:** Rank by mapped requirement weight (REQ-05) × keyword weight (REQ-06). Lead achievements from REQ-09 go first in their role.
- **Acceptance:** The first bullet of each recent role maps to one of the post's top-3 requirements where evidence exists.
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### REQ-17 Length control
- **Requirement:** Keep length right for the candidate's career stage and the regional profile.
- **Spec:** Default: 1 page under 5 years of experience; up to 2 pages for 5+ years; regional profile (GAP-07) overrides. 3–5 bullets for recent roles, 1–2 for roles older than 10 years. Flag any role with 6 or more.
- **Acceptance:** Page count and bullet counts within limits.
- **Best today:** Full · **Basis:** Convention · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### REQ-18 Skills list in the post's words
- **Requirement:** A targeted skills block following RES-05.
- **Spec:** Skills chosen from the master record that the post asks for, using the locked keyword form, ordered by relevance, optionally grouped (Tools / Expertise).
- **Acceptance:** Meets RES-05. 100% of skills listed are on the locked list or are evidenced high-value extras (at most 2).
- **Best today:** Full · **Priority:** Must · **Scope:** Core · **Status:** Proposed

### REQ-19 Hygiene: pronouns, email, titles
- **Requirement:** No personal pronouns, a professional email address, standard job titles.
- **Spec:** Scan for I, me, my, we, our, he, she, his, her. Email ideally firstname.lastname@ or a personal domain; flag nicknames and numbers. Unusual titles get a standard equivalent in brackets (e.g. "Product Ninja (Product Manager)"). Where a formal title understates the real job, use the honest standard title only when the duties match it, and be ready to explain it in an interview.
- **Acceptance:** 0 pronouns. Email flagged or passed. Every title is standard or has a standard equivalent.
- **Best today:** Full · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### REQ-20 Career-changer and early-career mode
- **Requirement:** When direct experience in the target field is thin, bring transferable evidence forward.
- **Spec:** Triggered when years in the target function are under 1, or the target function differs from the last role. Brings forward coursework, certifications, projects, volunteer work, and past roles reframed in the target field's terms (honestly).
- **Acceptance:** When triggered, at least 3 transferable evidence items are featured and labelled truthfully.
- **Best today:** Full · **Priority:** Could · **Scope:** Core · **Status:** Proposed

### REQ-21 Role-family vocabulary
- **Requirement:** Use the hiring vocabulary of the target role family (e.g. product management, engineering, finance), not generic business language.
- **Spec:** Each role family has a term pack: core activities, typical metrics, frameworks and seniority signals. The pack must be extendable, starting with product management.
- **Acceptance:** The summary and top bullets use at least 3 terms from the matching pack that are also backed by evidence.
- **Best today:** Full (one role family only) · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### REQ-26 Acronym and full-term pairs
- **Requirement:** See **GAP-05**.
- **Acceptance:** GAP-05 passes.
- **Best today:** None · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### REQ-32 Remove AI-sounding writing
- **Requirement:** Remove patterns readers associate with machine-written text from the CV and all application text, without breaking locked keywords (RES-02).
- **Spec:** Pattern list (extendable): inflated significance ("testament to", "pivotal"), promotional words ("groundbreaking", "vibrant"), formula structures (forced lists of three, "not just X but Y"), vague attributions, filler openers ("In order to", "It is important to note"), chatbot phrases, stacked hedging, identical sentence rhythm, overuse of bold. Run a second pass that asks what still reads as machine-written, and fix it.
- **Acceptance:** 0 listed patterns. Locked-keyword diff unchanged.
- **Best today:** Full (not applied to CVs, conflicts with exact keywords) · **Priority:** Should · **Scope:** Core · **Status:** Proposed

### REQ-38 CV critique and scorecard
- **Requirement:** After writing and before the ATS Gate, check the CV text against one canonical rubric (RES-03) and fix every failed rule.
- **Spec:** The rubric covers at least: summary (RES-06, REQ-14), bullet formula (RES-04), relevance order (REQ-16), skills (RES-05), length (REQ-17), hygiene (REQ-19), role-family language (REQ-21), seniority wording (GAP-09) and evidence-only keywords (RES-01). Each row records the rule, pass or fail, a quote from the CV and a suggested fix. The score is a count of passed rules, not an opinion out of 10.
- **Acceptance:** Every rubric row is evaluated with a quote. 0 failed Must rows when the CV goes to the gate.
- **Best today:** Full as a review, but with two inconsistent rubrics and opinion-based scores · **Priority:** Must · **Scope:** Core · **Status:** Proposed

## Positioning and wording

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

### GAP-12 One summary source
- **Requirement:** The professional summary is written once per application, in the CV, and every other summary is derived from it.
- **Spec:** Form "experience summary" fields, the cover-letter opening and short profile blurbs are made by shortening or adapting the CV summary, never written separately. Derived versions keep the same claims, metrics and locked keywords (INT-03). If a field's limit forces cuts, drop sentences rather than change facts.
- **Acceptance:** Every claim and metric in a derived summary also appears in the CV summary. 0 contradictions between them.
- **Origin:** Neither covers ("single summary source") · **Priority:** Should · **Scope:** Core · **Status:** Proposed
