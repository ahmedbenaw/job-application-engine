# Intake Questionnaire v4
# job-application-engine v2.2.0 (generic)
# Read when: First-Use Setup Step 2 (questions for missing fields); when a person adds a new target; when an expiring field needs re-confirming

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

## Intake questionnaire v4

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
- **Spec:** First batch: only what the current application needs to start (target, contact, eligibility, start date), minus anything already extracted. Later batches are asked where the answer is used: pay and CV format preferences in Phase 3; missing role details, results and proof in Phase 3B; optional extras only when they would strengthen the CV for the target role. Every batch is one numbered list under the heading **Questions for you (N)** and gives an approximate count of questions left (for example "about 13 more, asked later").
- **Acceptance:** 0 messages with more than 10 questions. The first batch contains no question the current application doesn't need yet.
- **Origin:** Engine v2.2.0 test runs (first turn asked 27–28 questions) · **Priority:** Must · **Scope:** Core · **Status:** Proposed

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

---

## Arabic labels (maintained by hand)

English is the master text. These Arabic labels use the same field IDs. Any other language is auto-translated from the English master at run time (INQ-01), and the person confirms the English copy of key fields at sign-off.

| ID | التسمية بالعربية |
|---|---|
| Q0.1 | وضعك الحالي: أول وظيفة · تغيير المسار المهني · العودة إلى العمل · صاحب خبرة · قيادي تنفيذي |
| Q0.2 | سنوات الخبرة ذات الصلة |
| Q0.3 | اللغة التي تريد تعبئة الاستبيان بها |
| Q1.1 | المسمى الوظيفي الدقيق المستهدف |
| Q1.2 | القطاع أو المجال |
| Q1.3 | بلد أو منطقة التقديم |
| Q1.4 | المستوى الوظيفي الذي تستهدفه، بكلمات بسيطة |
| Q1.5 | من 1 إلى 3 إعلانات وظائف حقيقية (النص الكامل أو الروابط) |
| Q1.6 | أهم الكلمات المفتاحية المتكررة في تلك الإعلانات (اختياري: يستخرجها النظام أيضاً) |
| Q1.7 | المدن المفضلة |
| Q1.8 | أماكن لن تتقدم إليها أبداً |
| Q1.9 | هل أنت مستعد للانتقال؟ إلى أي مدن؟ |
| Q2.1 | الاسم الكامل (كما في الوثائق الرسمية أو لينكد إن) |
| Q2.2 | رقم الهاتف مع رمز الدولة |
| Q2.3 | البريد الإلكتروني |
| Q2.4 | المدينة والبلد |
| Q2.5 | رابط لينكد إن أو الملف المهني |
| Q2.6 | معرض الأعمال أو الموقع الشخصي أو نماذج الأعمال |
| Q3.1 | تصريح العمل أو حالة التأشيرة لكل بلد مستهدف |
| Q3.2 | هل تحتاج إلى كفالة تأشيرة؟ |
| Q3.3 | فترة الإشعار أو أقرب تاريخ لبدء العمل |
| Q3.4 | أي التزام حالي يؤثر على موعد بدئك |
| Q3.5 | الجنسية (فقط إذا تطلبها البلد المستهدف أو فحص الأهلية) |
| Q4.1 | الراتب السنوي الإجمالي المستهدف لكل بلد، أو "أفضّل عدم الإفصاح" |
| Q4.2 | العملة |
| Q4.3 | هل تقبل حصصاً في الملكية أو مكافآت؟ وما الذي لا تقبله؟ |
| Q5.1 | الهوية المهنية (الحالية أو المأمولة) |
| Q5.2 | من 3 إلى 5 نقاط قوة يمكنك دعمها بمثال |
| Q5.3 | أقوى نتيجة قابلة للقياس أو مؤهل |
| Q5.4 | ما الذي تبحث عنه (الدور ونوع المؤسسة) |
| Q5.5 | لمسار أول وظيفة: الهدف المهني (الدور، نقاط القوة، القيمة التي ستضيفها) |
| Q6.1 | المسمى الوظيفي القياسي (وليس الداخلي أو الابتكاري) |
| Q6.2 | اسم المؤسسة |
| Q6.3 | السياق في سطر واحد (الحجم، النوع، البيئة) |
| Q6.4 | الموقع |
| Q6.5 | طبيعة العمل: دوام كامل، دوام جزئي، عقد، عمل حر، تدريب، تطوع، مشروع |
| Q6.6 | تاريخ البدء (MM/YYYY) |
| Q6.7 | تاريخ الانتهاء (MM/YYYY أو "حتى الآن") |
| Q6.8 | تغييرات المسمى الوظيفي داخل نفس المؤسسة، مع التواريخ |
| Q6.9 | ما كنت مسؤولاً عنه (من 3 إلى 6 نقاط) |
| Q6.10 | النتائج والأثر (من 2 إلى 5 نقاط، بالأرقام أو النطاق) |
| Q6.11 | إثبات اختياري لكل نتيجة: رابط أو مستند أو شخص يمكنه التأكيد |
| Q6.12 | الأدوات والمعدات والأنظمة والأساليب المستخدمة |
| Q6.13 | للمسار التنفيذي: الميزانية، حجم الفريق، الإيرادات أو الأرباح والخسائر، الأسواق، التعامل مع مجلس الإدارة أو المستثمرين |
| Q7.1 | المؤهل أو البرنامج |
| Q7.2 | المؤسسة أو الجهة المقدمة |
| Q7.3 | الموقع |
| Q7.4 | البداية والنهاية (مع الشهر إن كنت تعرفه) |
| Q7.5 | التقدير أو مرتبة الشرف (فقط إذا كان قوياً وذا صلة) |
| Q7.6 | المقررات الدراسية، الأوسمة، رسالة التخرج، التخصص |
| Q8.1 | المهارات التقنية أو المتخصصة، مع المستوى |
| Q8.2 | الأدوات والآلات والبرمجيات والأنظمة |
| Q8.3 | الأساليب والعمليات واللوائح والمعايير التي تتقنها |
| Q8.4 | نقاط القوة القابلة للنقل، مع مثال لكل منها |
| Q8.5 | أي شيء تريد استبعاده (قديم أو غير ذي صلة) |
| Q9.1 | الاسم الرسمي للشهادة أو الرخصة |
| Q9.2 | الجهة المانحة |
| Q9.3 | تاريخ الحصول عليها |
| Q9.4 | تاريخ الانتهاء، أو "لا تنتهي" |
| Q9.5 | رابط التحقق أو رقم الشهادة (وليس رقم هوية حكومية أبداً) |
| Q10.1 | اللغة والمستوى بأي معيار (يُحوَّل إلى A1–C2 أو اللغة الأم) |
| Q11.1 | المشاريع البارزة: الاسم، دورك، النتيجة، الأدوات |
| Q11.2 | المنشورات، براءات الاختراع، المحاضرات |
| Q11.3 | الجوائز أو التكريمات |
| Q11.4 | التطوع أو الأدوار المجتمعية |
| Q11.5 | الخدمة العسكرية (حيث تكون ذات صلة في ذلك السوق) |
| Q12.1 | الصورة الشخصية في السيرة الذاتية: تضمين أو استبعاد |
| Q12.2 | البيانات الشخصية في السيرة الذاتية (تاريخ الميلاد، الحالة الاجتماعية، الجنسية) |
| Q12.3 | الطول المفضل |
| Q12.4 | نوع الملف المفضل (DOCX ما لم يحدد الإعلان PDF) |
| Q12.5 | تعليمات التنسيق من صاحب العمل أو جهة التوظيف |
| Q12.6 | المراجع: مدرجة أو "متاحة عند الطلب" |
| Q13.1 | "كل ما ورد هنا صحيح، وكتبت "غير متوفر" حيث لم أكن أعرف." |
