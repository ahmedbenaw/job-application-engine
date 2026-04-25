# Job Application Engine
**Version 2.0.0 — Generic Universal Edition**

**Author: _Ahmed AW (Ben Zayed) | Product Leader, Builder & Venture Architect_**

An end-to-end AI-powered job application system for Claude, Claude CoWork, and Manus.
Supports two session entry modes: Mode A discovers matching roles across 10 platforms;
Mode B takes a CV and job URL directly and applies without discovery. Runs an 8-phase
workflow with a native automation layer executing 13 declared actions on the user's
behalf under a three-tier consent system. Job board and ATS platform MCPs are detected
automatically at session start — if none are connected, the skill searches online and
recommends available options.

> **No external agents or frameworks required.** All logic is embedded in the skill
> files. Drop the ZIP into any supported platform and run.

---

## Quick Start

1. [Download `JAE-v2.0-Generic-Universal-2026-04-25.zip` from the v2.0.0 release Assets](https://github.com/ahmedbenaw/job-application-engine/releases/tag/v2.0.0)
2. In Claude: go to **Customize → Skills → Create Skill → Upload ZIP**
3. Choose your entry mode:

**Mode A — Discover roles matching your profile:**
> *"Find me Senior Product Manager roles in Berlin with relocation support"*
> The skill searches 10 platforms, ranks results, and guides the full workflow.

**Mode B — Apply to a specific role you already have:**
> Upload your CV (PDF or DOCX) + paste the job URL in the same message.
> The skill skips discovery entirely and runs the full application workflow
> for that specific role — from company intelligence through to submission.

---

## What This Skill Does

The engine runs an 8-phase workflow governed by scoring gates. Every phase produces
output, presents it for review, and requires a score of 5 out of 5 before advancing.
A score below 5 triggers a revision loop within the same phase.

**A0 — Capability Detection:** probes all tools and MCP connections at session start,
including a dedicated scan of 10 job board and ATS platform MCPs (LinkedIn, Indeed,
Greenhouse, Lever, Workday, Ashby, Wellfound, SmartRecruiters, Breezy HR, Recruitee).
If none are connected, it searches online and presents recommended MCPs. Presents the
full Capability Map before any phase begins.

**Session Entry Gate:** detects the session mode automatically from uploaded files,
URLs, and message content. Routes to Mode A or Mode B without the user needing to
specify. Presents both options explicitly if the mode is ambiguous.

**Mode A — Job Discovery:** user wants to find matching roles. Proceeds to Phase 0.

**Mode B — Direct Application:** user has a specific role. Upload a CV and paste a
job URL — Phase 0 is skipped entirely, and the skill runs Phases 1–7 for that role.

**Phase 0 — Job Discovery (Mode A only):** searches 10 platforms in two passes,
uses active job board MCPs for authenticated access where available, filters excluded
geographies, ranks results by relocation support and level match, flags the top 5.

**Phase 1 — Company Intelligence:** runs four parallel operations — job posting fetch,
application form fetch with platform-aware strategy, hiring manager identification,
and company and product research — producing a Company Intelligence Brief.

**Phase 2 — Fit Analysis:** adversarial two-column gap mapping against the candidate
profile. Returns one of three verdicts: Clean Fit, Honest Stretch, or Mismatch.
A Mismatch verdict halts the workflow — no application materials are produced.

**Phase 3 — Clarifying Intake:** collects all remaining inputs in a single block —
portfolio URL, salary confirmation, availability, relocation, custom form questions,
product trial observation, and language level where required.

**Phase 4 — Application Package:** produces all deliverables — standard form fields,
experience summary, five-paragraph cover letter following both canonical templates,
and copy-paste answers to every custom question. Routes through Phase 5 before presenting.

**Phase 5 — Writing Quality Pass:** 25-pattern audit across 5 families removes
AI-generated patterns. Two internal passes run; only the final version is presented.

**Phase 6 — Governance Gate:** eight sequential checks verify completeness, claim
traceability, salary format, gap acknowledgment, token resolution, word count, URL
validity, and salary field type. No package is presented with a known open check.

**Phase 7 — Post-Submission Loop:** three branches — submitted (anchors next
discovery), withdrawn (logs reason, refines next pass), rejected (identifies gap,
recalibrates search).

**Automation Layer (v2.0):** 13 declared automations (A01–A13) execute on the
user's behalf under a three-tier consent system. Scoring gates evaluate quality.
Approval gates authorise real-world actions. These are entirely separate systems.

---

## Workflow Diagram

```mermaid
flowchart TB

  %% ── SESSION START ─────────────────────────────────────
  START([" 🟢 Session Start "]):::entry

  %% ── A0 — CAPABILITY DETECTION ────────────────────────
  subgraph CAP["  A0 · Capability Detection"]
    direction LR
    A0_PW["Playwright\nDisclosure"]:::step
    A0_CONF{Capability Map\nConfirmed?}:::gate
    A0_PT["Probe Tools &\nConnections"]:::step
    A0_CM["Build\nCapability Map"]:::step
    A0_JB["Job Board &\nATS MCP Probe"]:::step
    A0_REC["Recommend\nMCPs if none found"]:::autonode
    A0_PW --> A0_CONF
    A0_CONF -- No --> A0_PW
    A0_CONF -- Yes --> A0_PT --> A0_CM --> A0_JB --> A0_REC
  end
  START --> CAP

  %% ── SESSION ENTRY GATE ────────────────────────────────
  subgraph SEG["  Session Entry Gate"]
    direction LR
    SEG_D{Mode\nDetected?}:::gate
    SEG_A["Mode A\nJob Discovery"]:::step
    SEG_B["Mode B\nDirect Apply"]:::step
    SEG_D -- "Mode A" --> SEG_A
    SEG_D -- "Mode B\nCV + Job URL" --> SEG_B
  end
  CAP --> SEG

  %% ── PHASE 0 — JOB DISCOVERY (Mode A only) ────────────
  subgraph PH0["  P0 · Job Discovery  ·  Mode A only"]
    direction LR
    P0_PS["Platform Search\n& Filter"]:::step
    P0_JB["Job Board\nFetch"]:::step
    P0_MCP["Job Board MCP\nif active"]:::autonode
    P0_G{Top 5\nScored?}:::gate
    P0_FJ["Full JD\nFetch"]:::step
    P0_PS --> P0_JB --> P0_MCP --> P0_G
    P0_G -- No --> P0_PS
    P0_G -- Yes --> P0_FJ
  end
  SEG_A --> PH0

  %% ── PHASE 1 — COMPANY INTELLIGENCE ──────────────────
  subgraph PH1["  P1 · Company Intelligence"]
    direction LR
    P1_PR["Parallel\nResearch"]:::step
    P1_FF["Form Fetch\n& Parse"]:::step
    P1_G{Company\nScore 5?}:::gate
    P1_PR --> P1_FF --> P1_G
    P1_G -- No --> P1_PR
  end
  P0_FJ --> PH1
  SEG_B --> PH1

  %% ── PHASE 2 — FIT ANALYSIS ───────────────────────────
  subgraph PH2["  P2 · Fit Analysis"]
    direction LR
    P2_FV{Fit\nVerdict?}:::gate
    P2_MH(["🚫 Mismatch\nHalt"]):::halt
    P2_RE["Role & Requirements\nExtraction"]:::step
    P2_EM["Evidence\nMapping"]:::step
    P2_FS{Fit\nScore 5?}:::gate
    P2_FV -- Mismatch --> P2_MH
    P2_FV -- "Clean Fit or\nHonest Stretch" --> P2_FS
    P2_FS -- No --> P2_RE --> P2_EM --> P2_FS
  end
  P1_G -- Yes --> PH2

  %% ── PHASE 3 — CLARIFYING INTAKE ─────────────────────
  subgraph PH3["  P3 · Clarifying Intake"]
    direction LR
    P3_CG["Critical Gates\n& Research"]:::step
    P3_EH["Email Hiring\nManager"]:::autonode
    P3_G{Intake\nScore 5?}:::gate
    P3_CG --> P3_EH --> P3_G
    P3_G -- No --> P3_CG
  end
  P2_FS -- Yes --> PH3

  %% ── PHASE 4 — APPLICATION PACKAGE ───────────────────
  subgraph PH4["  P4 · Application Package"]
    direction LR
    P4_SQ{Save to\nCloud?}:::gate
    P4_CS["Cloud\nSave"]:::storage
    P4_PM["Prepare Application\nMaterials"]:::step
    P4_CL["Create Cover\nLetter"]:::step
    P4_LD["Local\nDownload"]:::storage
    P4_G{Package\nScore 5?}:::gate
    P4_SQ -- Yes --> P4_CS --> P4_PM
    P4_SQ -- No --> P4_PM
    P4_PM --> P4_CL --> P4_LD --> P4_G
    P4_G -- No --> P4_SQ
  end
  P3_G -- Yes --> PH4

  %% ── PHASE 5 — WRITING QUALITY PASS ──────────────────
  subgraph PH5["  P5 · Writing Quality Pass"]
    direction LR
    P5_PA["Pattern Removal\n& Audit"]:::step
    P5_G{Writing\nScore 5?}:::gate
    P5_PA --> P5_G
    P5_G -- No --> P5_PA
  end
  P4_G -- Yes --> PH5

  %% ── PHASE 6 — GOVERNANCE GATE ────────────────────────
  subgraph PH6["  P6 · Governance Gate"]
    direction LR
    P6_SC{Save to\nCloud 2?}:::gate
    P6_CS2["Cloud\nSave 2"]:::storage
    P6_BF["Browser\nForm Fill"]:::danger
    P6_AS["Application\nSubmit"]:::danger
    P6_G{Governance\nScore 5?}:::gate
    P6_SQ["Sequential\nChecks"]:::step
    P6_FP["Create Full\nPackage Doc"]:::step
    P6_LD["Local\nDownload 2"]:::storage
    P6_SC -- Yes --> P6_CS2 --> P6_BF
    P6_SC -- No --> P6_BF
    P6_BF --> P6_AS --> P6_G
    P6_G -- No --> P6_SQ --> P6_FP --> P6_LD --> P6_SC
  end
  P5_G -- Yes --> PH6

  %% ── PHASE 7 — POST SUBMISSION LOOP ──────────────────
  subgraph PH7["  P7 · Post Submission Loop"]
    direction LR
    P7_OB{Outcome\nBranching}:::gate
    P7_A["Branch A\nSubmitted"]:::branchA
    P7_B["Branch B\nWithdrawn"]:::branchB
    P7_C["Branch C\nRejected"]:::branchC
    P7_CR["Calendar\nReminder"]:::step
    P7_ES["Email\nto Self"]:::step
    P7_G{Post-Submission\nScore 5?}:::gate
    P7_OB -- Submitted --> P7_A
    P7_OB -- Withdrawn --> P7_B
    P7_OB -- Rejected --> P7_C
    P7_A --> P7_CR --> P7_ES --> P7_G
    P7_B --> P7_G
    P7_C --> P7_G
    P7_G -- No --> P7_OB
  end
  P6_G -- Yes --> PH7

  %% ── SESSION END ──────────────────────────────────────
  NEXT([" 🔄 Next Discovery "]):::entry
  DONE([" ⏹ Session Close "]):::entry
  P7_G -- "Yes · Branch A" --> NEXT
  NEXT -. "back to P0" .-> PH0
  P7_G -- "Yes · B or C" --> DONE

  %% ── LEGEND ───────────────────────────────────────────
  subgraph LEGEND["  Legend — Consent Tiers · separate from scoring"]
    direction LR
    LL1["⚡ Tier 1 — Auto\nRead-only · no gate"]:::step
    LL2["📄 Tier 2 — APPROVE\nReversible write"]:::step
    LL3["🚀 Tier 3 — APPROVE PHRASE\nIrreversible · full preview\nScore ≠ Approval"]:::danger
    LLG{Score Gate\n1–5 · need 5}:::gate
    LLS([Session\nStart/End]):::entry
  end

  %% ── STYLES — light mode ──────────────────────────────
  classDef entry    fill:#ccfbf1,stroke:#0d9488,stroke-width:2px,color:#134e4a,font-weight:bold
  classDef step     fill:#e0f2fe,stroke:#0284c7,stroke-width:1.5px,color:#0c4a6e
  classDef autonode fill:#fff7ed,stroke:#ea580c,stroke-width:1.5px,color:#7c2d12
  classDef gate     fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d,font-weight:bold
  classDef halt     fill:#fee2e2,stroke:#dc2626,stroke-width:2.5px,color:#7f1d1d,font-weight:bold
  classDef danger   fill:#fecaca,stroke:#ef4444,stroke-width:2px,color:#7f1d1d
  classDef storage  fill:#ede9fe,stroke:#7c3aed,stroke-width:1.5px,color:#4c1d95
  classDef branchA  fill:#d1fae5,stroke:#059669,stroke-width:1.5px,color:#064e3b
  classDef branchB  fill:#ffedd5,stroke:#f97316,stroke-width:1.5px,color:#7c2d12
  classDef branchC  fill:#fee2e2,stroke:#ef4444,stroke-width:1.5px,color:#7f1d1d
```

| Symbol | Meaning |
|--------|---------|
| 🟢 Teal pill | Session start **and** end — both `Session Start` and `Session Close` |
| 🟩 Green diamond | Scoring gate — 5/5 required · loops back on fail |
| 🟦 Blue rectangle | Process step — auto-executes · also Tier 2 reversible actions |
| 🟧 Orange rectangle | Automation node — active MCP or Tier 3 `APPROVE PHRASE` (e.g. `APPROVE SEND`) |
| 🟥 Red rounded pill | **Mismatch halt** — workflow stops entirely |
| 🟣 Purple rectangle | File storage — local download always before cloud save |
| 🔴 Light-red rectangle | Irreversible action — `APPROVE SUBMIT` and `APPROVE FILL` |
| `- -` Dashed arrow | Loop back to Phase 0 after successful submission |
| `- -` Dashed arrow | Loop back to Phase 0 after successful submission |

---

## Who It Is For

This generic edition works for any job seeker running a structured, disciplined
application process. It is particularly suited to candidates applying across multiple
markets, targeting different seniority levels simultaneously, or managing several
active applications in parallel. The Applicant Profile template holds multiple versions
of key fields — positioning headlines, professional summaries, evidence selection —
so the system adapts to each role without starting from scratch.

---

## Repository Structure

```
job-application-engine/
├── README.md                                ← This file + workflow diagram
├── LICENSE                                  ← MIT licence
├── CHANGELOG.md                             ← Version history (v1.0 + v2.0)
├── .gitignore
├── SKILL.md                                 ← Main skill file
│                                               8-phase engine + automation layer
├── rules.json                               ← Machine-readable workflow rules
│                                               + automation layer bindings
├── automation-registry.json                 ← All 11 permitted automations
│                                               (A01–A11) · scope-locked
└── references/
    ├── applicant-profile-template.md        ← Central source of truth · fill first
    ├── cover-letter-templates.md            ← Both canonical templates
    ├── salary-anchors-template.md           ← Market salary data
    ├── job-level-framework.md               ← 7-level classification framework
    ├── excluded-companies-log.md            ← Discovery filter + outcomes log
    ├── automation-playbooks/                ← Automation execution specs
    │   ├── job-board-access.md             ← A01, A02 — search & fetch
    │   ├── application-filling.md          ← A03, A04, A05 — form fill & submit
    │   ├── email-actions.md                ← A08, A11 — email draft & send
    │   └── document-creation.md            ← A06, A07, A09 — docs & cloud save
    └── skill-instructions/                  ← Inline module documentation
        ├── fit-analysis.md                  ← Phase 2 module
        ├── writing-quality.md               ← Phase 5 module (25 patterns)
        ├── governance-gate.md               ← Phase 6 module (8 checks)
        └── checklist-templates.md           ← Dynamic status board system
```

---

## Platform Setup

> **Supported platforms with native Agent Skills:** Claude.ai (Pro and above) and
> Claude CoWork support native skill installation — this is the correct primary method
> and gives the skill full agentic capabilities. All other methods listed below are
> alternatives for free tiers or platforms that do not support the Skills feature.

---

### Claude.ai — Web or Mobile

**Primary — Agent Skills install (Pro and above)**

This is the correct installation method. It makes the skill available across every
conversation and gives it full agentic execution capability.

1. [Download the ZIP from Releases](https://github.com/ahmedbenaw/job-application-engine/releases/tag/v2.0.0)
2. In Claude, click your profile icon → **Customize**
3. Go to **Skills** → **Create Skill**
4. Upload the ZIP file directly
5. The skill is now active across all your Claude conversations — no project setup required
6. Begin any conversation with: *"Find me jobs similar to [ROLE] in [CITY]"*

**Alternative — Project Knowledge upload** *(free tier or if Skills not available)*

If you are on a free plan or your account does not have the Skills feature:

1. Go to [claude.ai](https://claude.ai) → **Projects** → **New Project**
2. Open **Project Settings** → **Project Knowledge**
3. Upload these files individually: `SKILL.md`, `rules.json`, `automation-registry.json`,
   and every file inside `references/` including both subdirectories
4. Use the skill within conversations inside that project only

**Alternative — Git clone then upload to Project Knowledge**

```bash
git clone https://github.com/ahmedbenaw/job-application-engine.git
```

Upload the individual files from the cloned folder into Project Knowledge as above.

**How it runs on Claude.ai:** all phases run sequentially in one conversation.
The system presents each phase output and waits for your scoring gate response.
Confirm explicitly before Phase 4 — this is where application text is first written.

**Best for:** single-candidate sessions where you want full sequential control and
direct review at every step.

**Limitation:** phases cannot run in parallel. For high-volume discovery across all
10 platforms simultaneously, CoWork is significantly faster.

---

### Claude CoWork

**Primary — Agent Skills install**

CoWork supports native skill installation. Install once; the skill is available
across all CoWork projects and agents.

1. [Download the ZIP from Releases](https://github.com/ahmedbenaw/job-application-engine/releases/tag/v2.0.0)
2. In CoWork, go to **Customize → Skills → Create Skill**
3. Upload the ZIP directly
4. The skill is now available to all agents in your CoWork environment
5. Open a new CoWork project and begin — CoWork routes parallel phases automatically

**Alternative — Workspace file upload** *(if Skills not available on your CoWork tier)*

1. [Download the ZIP from Releases](https://github.com/ahmedbenaw/job-application-engine/releases/tag/v2.0.0)
2. Open Claude CoWork → **New Project** → **Upload**
3. Upload all 20 files individually, preserving the `references/` folder hierarchy
4. CoWork reads `rules.json` as the workflow instruction source

**Alternative — Git clone**

```bash
git clone https://github.com/ahmedbenaw/job-application-engine.git
```

Upload the cloned files into the CoWork workspace as above.

**How it runs on CoWork:** Phases 0, 1, and salary research in Phase 3 run as
parallel subagents. Phase 2 must return a verdict before Phase 4 begins. Phases 5
and 6 always run sequentially. Tier 2 and Tier 3 consent gates always run in the
main coordination thread — never dispatched to a subagent.

**Best for:** high-volume discovery, multiple simultaneous applications, or when
you need the final package as a downloadable file.

**Limitation:** subagent output transfer requires user coordination. For a simpler
linear experience, use Claude.ai.

---

### Claude.ai + CoWork Combined

This is the recommended approach for any serious application. Install the skill
via **Customize → Skills → Create Skill → Upload ZIP** on both platforms.

**How to run:**
- **Phases 0 and 1** → run in CoWork for parallel discovery speed
- Copy the **Company Intelligence Brief** from CoWork into a Claude.ai conversation
- **Phases 2 through 7** → run in Claude.ai for sequential gate control and writing

**Best for:** applications where Phase 0 searches more than 5 platforms and you want
both parallel research speed and granular control over the application writing phases.

---

### Manus

Manus does not currently support the Agent Skills install format. Use the file
upload method below as the primary approach.

**Primary — Upload files + rules.json as session instruction source**

1. [Download the ZIP from Releases](https://github.com/ahmedbenaw/job-application-engine/releases/tag/v2.0.0)
2. Extract the ZIP locally
3. Upload all extracted files into your Manus project workspace
4. Manus reads `rules.json` as the session instruction source governing the full
   8-phase sequence and automation routing
5. Begin — Manus follows the phase sequence as defined in `rules.json`

**Alternative — Paste rules.json as session instruction** *(if file upload not available)*

Copy the full contents of `rules.json` and paste it into the Manus project as a
`.json` or `.md` file at session start.

**Alternative — Git clone**

```bash
git clone https://github.com/ahmedbenaw/job-application-engine.git
```

**How it runs on Manus:** all phase outputs confirmed by user before advancing.
Tier 1 automations execute inline. Tier 2 and Tier 3 consent gates surface as text
prompts. Status board maintained as a text block updated at each gate. Browser
automation uses Manus's native browser tools when BrowserBase and Playwright MCPs
are unavailable.

**Best for:** agent-based workflows across longer time horizons or managing multiple
applications as background tasks.

**Limitation:** Manus does not support `present_files`. Final output must be copied
from the conversation rather than downloaded as a file.

---

## First-Use Setup Protocol

The skill builds your Applicant Profile automatically — it extracts data from
any documents or links you provide before asking a single question manually.

**What to provide (any combination works):**

| Source | What gets extracted |
|---|---|
| CV / Resume (PDF or DOCX) | Name, contact, education, work history, tools, skills, certifications |
| LinkedIn profile URL | Headline, experience, education, skills, certifications, contact |
| GitHub profile URL | Repos, languages, tools, project descriptions |
| Personal website / portfolio URL | Bio, projects, contact information |
| Behance / Dribbble URL | Project names, descriptions, tools used |
| Text description in chat | Any background you describe in your opening message |

**How it works:**

1. At session start, the skill runs **Step 0 — Document Detection** first.
   It reads every uploaded file and fetches every URL you provided.
2. It extracts every recognisable profile field from those sources and
   presents a confirmation summary showing what was found.
3. You confirm, correct, or add to the extracted values.
4. Only for fields that could not be extracted does it ask follow-up questions.
5. The complete profile is presented for final review and a scoring gate
   (score of 5 required before the workflow begins).

**If you provide a CV and a LinkedIn URL, most fields populate with zero
manual typing.** If you provide nothing, the skill asks all 25 fields
sequentially.

**Profile updates during and after applications:**

The profile is not a one-time setup. The skill updates it at two points
during every application cycle:

After **Phase 3 (Clarifying Intake):** if new information collected during
the intake differs from the profile (new salary confirmation, updated
availability, new tool added to your stack, language level change), the
skill flags the difference and asks for approval to update the profile field.

After **Phase 7 (Post-Submission Loop):** every application outcome —
submitted, withdrawn, or rejected — is logged and checked for profile
implications. An offer received updates salary anchors. A recurring rejection
pattern triggers a seniority or sector targeting review. All updates require
explicit `APPROVE UPDATE` before being written.

**Staleness checks at every session start:**

Time-sensitive fields (availability, active notice period, salary anchors)
are checked at the start of every session. Fields that are stale beyond their
review cycle are flagged and re-confirmed before Phase 0 begins.

---

## Automation Layer (v2.0)

Version 2.0 adds a native execution layer beneath the 8-phase workflow. All phases,
gates, and invariants from v1.0 are unchanged. The automation layer is purely additive.

### 13 Registered Automations

| ID | Automation | Phase | Tier | Approval Phrase |
|---|---|---|---|---|
| A01 | Job board search and fetch | 0 | 1 — auto | — |
| A02 | Full JD fetch for top 5 | 0 post-table | 1 — auto | — |
| A03 | Application form fetch and parse | 1 | 1 — auto | — |
| A04 | Browser form field filling | 6 | 3 | `APPROVE FILL` |
| A05 | Application submission | 6 post-fill | 3 | `APPROVE SUBMIT` |
| A06 | Cover letter DOCX creation | 4 | 2 | `APPROVE CREATE` |
| A07 | Full application package document | 6 | 2 | `APPROVE CREATE` |
| A08 | Email to hiring manager / recruiter | 3 or 7 | 3 | `APPROVE SEND` |
| A09 | Cloud document save | After A06 / A07 | 2 | `APPROVE SAVE` |
| A10 | Calendar follow-up reminder | 7 | 2 | `APPROVE CALENDAR` |
| A11 | Confirmation email to self | 7 | 2 | `APPROVE SEND` |
| A12 | Job board MCP authenticated search | 0 (when MCP active) | 1 — auto | — |
| A13 | Job board MCP discovery search | A0 Step 1C | 1 — auto | — |

### Consent Tiers

**Tier 1 — Read-only:** auto-executes as part of the phase. No separate gate.

**Tier 2 — Reversible write:** requires `APPROVE [ACTION_NAME]` typed explicitly.
A score of 5 or "yes" is not accepted.

**Tier 3 — Irreversible:** requires the full consent gate — complete preview of all
data being transmitted, destination, and timestamp — followed by exact typed phrase.
Cannot be triggered by a score, "yes", or any paraphrase.

> **Approval and scoring are entirely separate systems and must never be conflated.**

### Capability Map

At session start, before any phase begins, the skill probes the current environment
and presents a Capability Map with two sections: core tools and automations, and a
dedicated Job Board & ATS Platform MCPs section. Every automation shows as ACTIVE,
LIMITED, or INACTIVE with the connection required to enable each inactive one.

If all job board and ATS MCPs are inactive, the skill automatically runs A13 —
a web search that finds currently available job board MCPs on GitHub and npm —
and presents recommendations below the Capability Map. web_search and web_fetch
provide full discovery capability without MCPs; job board MCPs are an enhancement
that unlocks authenticated features (saved jobs, Easy Apply, application status tracking).

### Browser Automation

**BrowserBase MCP** is the primary path. **Playwright MCP** is the secondary path —
a plain-language disclosure of its behaviour and limitations is presented before use.
When neither is available, the skill generates pre-staged numbered answers for manual entry.

### Email and Cloud Storage

Email provider is always selected by the user per session — never assumed or hardcoded.
Documents are always presented for local download first; cloud save is offered separately
after, with provider selection and folder path confirmation before any upload.

---

## Customisation

**Add a geography exclusion:** append to `[HARD_EXCLUSION_GEOGRAPHIES]` in the
Applicant Profile and to `references/excluded-companies-log.md`.

**Add a salary market:** append to Confirmed Anchors in `references/salary-anchors-template.md`.

**Add an automation:** declare in `automation-registry.json` with ID, phase binding,
consent tier, approval phrase, tool/MCP requirement, and scope boundary.

**Adapt for a specific candidate:** populate the Applicant Profile with their data.
Dynamic fields, salary architecture, and evidence catalogue all support multiple
simultaneous variants activated by role context.

---

## Key Design Decisions

**Why two session entry modes?** Most documentation assumes the user starts with no
role in mind. In practice, the most common session start is a user arriving with a
CV already written and a specific job URL to apply to. Forcing them through a
10-platform discovery phase they do not need wastes time and creates friction at
exactly the wrong moment. Mode B exists to meet users where they actually are.

**Why extract profile data from documents instead of asking questions?** A candidate
who uploads a CV and LinkedIn URL should not be asked to re-type information that
already exists in structured form. Document extraction first, gap-fill questions
second, means most profiles populate with minimal manual input. Questions are a
fallback, not the default.

**Why detect job board MCPs automatically and search for more if none are found?**
Users do not know which MCPs exist or which would help them. Requiring them to
research and connect MCPs before the skill is useful creates unnecessary friction.
The skill surfaces what is available and what is possible — the user decides what
to connect.

**Why a scoring gate at every phase?** Gates give the system a learning signal between
phases. Without them, errors compound and the final package is harder to fix.

**Why is Mismatch a hard halt?** Two or more mandatory gaps with no compensating
evidence means the application is not viable — producing materials anyway wastes the
candidate's time and reputation.

**Why is the product trial observation required?** A candidate who used the product
and noticed something actionable is categorically different from one who read the
website. This paragraph cannot be generated without the trial.

**Why 25 patterns across 5 families?** Statistical regularities in AI-generated
text are detectable. Removing patterns is necessary but not sufficient — the output
must also vary rhythm, add specificity, and match the candidate's seniority voice.

**Why is approval separate from scoring?** Scoring gates evaluate output quality.
Consent gates authorise irreversible real-world actions. Conflating them would allow
a phase score to accidentally trigger a form submission or email send.

---

## Licence

MIT. See `LICENSE` for full terms.

---

## Changelog

See `CHANGELOG.md` for the full version history. Current version: **2.0.0**.
