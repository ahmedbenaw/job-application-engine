# Job Application Engine
**Version 2.0.0 — Generic Universal Edition**
**Author: Ahmed Ossama | Product Leader, Builder & Venture Management Architect**

An end-to-end AI-powered job application system for Claude, Claude CoWork, and Manus.
Runs an 8-phase workflow — from multi-platform job discovery through company
intelligence, adversarial fit analysis, application package production, writing
quality audit, governance gate, and post-submission tracking — with a native
automation layer that executes 11 declared actions on the user's behalf with
explicit consent at every step.

> **No external agents or frameworks required.** All logic is embedded in the skill
> files. Drop the ZIP into any supported platform and run.

---

## Quick Start

1. [Download the latest ZIP from Releases](https://github.com/ahmedbenaw/job-application-engine/releases)
2. Fill in your details in `references/applicant-profile-template.md`
3. In Claude: go to **Customize → Skills → Create Skill → Upload ZIP** — the skill is then available across all your conversations
4. Say: *"Find me jobs similar to [ROLE] in [CITY]"* — the engine guides you from there

---

## What This Skill Does

The engine runs an 8-phase workflow governed by scoring gates. Every phase produces
output, presents it for review, and requires a score of 5 out of 5 before advancing.
A score below 5 triggers a revision loop within the same phase.

**Phase 0 — Job Discovery:** searches 10 platforms in two passes, filters excluded
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

**Automation Layer (v2.0):** 11 declared automations (A01–A11) execute on the
user's behalf under a three-tier consent system. Scoring gates evaluate quality.
Approval gates authorise real-world actions. These are entirely separate systems.

---

## Workflow Diagram

```mermaid
flowchart LR

  %% ── SESSION START ─────────────────────────────────────────────
  START([SESSION\nSTART]):::entry

  %% ── A0 — CAPABILITY DETECTION ────────────────────────────────
  subgraph CAP[" A0 — Capability Detection "]
    direction TB
    A0["Probe tools & MCP connections\nBuild & present Capability Map\nPlaywright disclosure if BrowserBase inactive"]:::automation
    CONFIRM_A0{Map\nconfirmed?}:::gate
  end
  START --> CAP
  CONFIRM_A0 -- No --> A0

  %% ── PHASE 0 — JOB DISCOVERY ──────────────────────────────────
  subgraph PH0[" Phase 0 — Job Discovery "]
    direction TB
    P0["10 platforms · 2-pass search\nFilter exclusions · Rank table\nFlag top 5"]:::phase
    A01["⚡ A01 T1\nJob Board Fetch\nauto-executes inline"]:::tier1
    A02["⚡ A02 T1\nFull JD Fetch\ntop 5 after scoring"]:::tier1
    G0{Score\n= 5?}:::gate
    P0 --> A01 --> A02 --> G0
    G0 -- "< 5 · Revise" --> P0
  end
  CONFIRM_A0 -- Yes --> PH0

  %% ── PHASE 1 — COMPANY INTELLIGENCE ──────────────────────────
  subgraph PH1[" Phase 1 — Company Intelligence "]
    direction TB
    P1["4 parallel ops\nJD fetch · Form fetch\nHiring manager ID\nCompany & product research"]:::phase
    A03["⚡ A03 T1\nForm Fetch & Parse\nplatform-aware strategy"]:::tier1
    G1{Score\n= 5?}:::gate
    P1 --> A03 --> G1
    G1 -- "< 5 · Revise" --> P1
  end
  G0 -- "= 5" --> PH1

  %% ── PHASE 2 — FIT ANALYSIS ───────────────────────────────────
  subgraph PH2[" Phase 2 — Fit Analysis "]
    direction TB
    P2["Role level detection\nRequirements extraction\n2-col evidence mapping\nCompensating evidence"]:::phase
    VERDICT{Verdict?}:::decision
    MISMATCH["🚫 MISMATCH\nHalt · Inform user\nNo materials produced"]:::halt
    G2{Score\n= 5?}:::gate
    P2 --> VERDICT
    VERDICT -- Mismatch --> MISMATCH
    VERDICT -- "Clean Fit or\nHonest Stretch" --> G2
    G2 -- "< 5 · Revise" --> P2
  end
  G1 -- "= 5" --> PH2

  %% ── PHASE 3 — CLARIFYING INTAKE ─────────────────────────────
  subgraph PH3[" Phase 3 — Clarifying Intake "]
    direction TB
    P3["5 critical gates · 3 important\nSalary research · Product trial\nCustom questions · Language level"]:::phase
    A08P3["📧 A08 T3\nEmail Hiring Manager\nif follow-up needed\nAPPROVE SEND"]:::tier3
    G3{Score\n= 5?}:::gate
    P3 --> A08P3 --> G3
    G3 -- "< 5 · Revise" --> P3
  end
  G2 -- "= 5" --> PH3

  %% ── PHASE 4 — APPLICATION PACKAGE ───────────────────────────
  subgraph PH4[" Phase 4 — Application Package "]
    direction TB
    P4["Standard fields · Summary\n5-para cover letter\nCustom question answers\nRoutes through Phase 5"]:::phase
    A06["📄 A06 T2\nCover Letter DOCX\nAPPROVE CREATE"]:::tier2
    DL1["⬇ Local Download\npresent_files · always first"]:::storage
    CQ1{Save to\ncloud?}:::decision
    A09a["☁ A09 T2\nCloud Save\nUser selects provider\nAPPROVE SAVE"]:::tier2
    G4{Score\n= 5?}:::gate
    P4 --> A06 --> DL1 --> CQ1
    CQ1 -- Yes --> A09a --> G4
    CQ1 -- No --> G4
    G4 -- "< 5 · Revise" --> P4
  end
  G3 -- "= 5" --> PH4

  %% ── PHASE 5 — WRITING QUALITY PASS ──────────────────────────
  subgraph PH5[" Phase 5 — Writing Quality Pass "]
    direction TB
    P5["25 patterns · 5 families\nPass 1: Remove patterns\nPass 2: Internal audit loop\nFinal version only — never draft"]:::phase
    G5{Score\n= 5?}:::gate
    P5 --> G5
    G5 -- "< 5 · Revise" --> P5
  end
  G4 -- "= 5" --> PH5

  %% ── PHASE 6 — GOVERNANCE GATE ────────────────────────────────
  subgraph PH6[" Phase 6 — Governance Gate "]
    direction TB
    P6["8 sequential checks\nFix all failures first\nNo open check presented"]:::phase
    A07["📦 A07 T2\nFull Package Doc\nAPPROVE CREATE"]:::tier2
    DL2["⬇ Local Download\npresent_files · always first"]:::storage
    CQ2{Save to\ncloud?}:::decision
    A09b["☁ A09 T2\nCloud Save\nUser selects provider\nAPPROVE SAVE"]:::tier2
    A04["🖥 A04 T3\nBrowser Form Fill\nBrowserBase primary\nPlaywright secondary\nAPPROVE FILL\ndoes NOT submit"]:::tier3
    A05["🚀 A05 T3\nApplication Submit\nafter A04 reviewed\nAPPROVE SUBMIT\nirreversible"]:::tier3
    G6{Score\n= 5?}:::gate
    P6 --> A07 --> DL2 --> CQ2
    CQ2 -- Yes --> A09b --> A04
    CQ2 -- No --> A04
    A04 --> A05 --> G6
    G6 -- "< 5 · Revise" --> P6
  end
  G5 -- "= 5" --> PH6

  %% ── PHASE 7 — POST-SUBMISSION LOOP ──────────────────────────
  subgraph PH7[" Phase 7 — Post-Submission Loop "]
    direction TB
    P7["3 branches by outcome"]:::phase
    BRANCH{Outcome?}:::decision
    BR_A["✅ Branch A — Submitted\nAnchor next search\nReturn to Phase 0"]:::branch
    BR_B["↩ Branch B — Withdrawn\nLog reason\nRefine next discovery"]:::branch
    BR_C["❌ Branch C — Rejected\nLog gap\nRecalibrate search"]:::branch
    A10["📅 A10 T2\nCalendar Reminder\nAPPROVE CALENDAR"]:::tier2
    A11["📧 A11 T2\nEmail to Self\nPackage record\nAPPROVE SEND"]:::tier2
    G7{Score\n= 5?}:::gate
    P7 --> BRANCH
    BRANCH -- Submitted --> BR_A
    BRANCH -- Withdrawn --> BR_B
    BRANCH -- Rejected --> BR_C
    BR_A --> A10 --> A11 --> G7
    BR_B --> G7
    BR_C --> G7
    G7 -- "< 5 · Revise" --> P7
  end
  G6 -- "= 5" --> PH7

  %% ── SESSION END ───────────────────────────────────────────────
  NEXT([NEXT\nDISCOVERY]):::entry
  DONE([SESSION\nCLOSE]):::entry
  G7 -- "= 5 · Branch A" --> NEXT
  NEXT -. "back to Phase 0" .-> PH0
  G7 -- "= 5 · B or C" --> DONE

  %% ── CONSENT TIER LEGEND ──────────────────────────────────────
  subgraph LEGEND[" Consent Tiers — always separate from scoring "]
    direction LR
    L1["⚡ Tier 1\nRead-only\nAuto-executes\nNo gate required"]:::tier1
    L2["📄 Tier 2\nReversible write\nAPPROVE ACTION\ntyped explicitly"]:::tier2
    L3["🚀 Tier 3\nIrreversible\nAPPROVE PHRASE\nFull data preview first\nScore ≠ Approval"]:::tier3
  end

  %% ── STYLES ────────────────────────────────────────────────────
  classDef entry      fill:#ede9fe,stroke:#7c3aed,stroke-width:2px,color:#3b0764,font-weight:bold
  classDef phase      fill:#dbeafe,stroke:#2563eb,stroke-width:1.5px,color:#1e3a5f
  classDef gate       fill:#dcfce7,stroke:#16a34a,stroke-width:1.5px,color:#14532d,font-weight:bold
  classDef decision   fill:#fef9c3,stroke:#ca8a04,stroke-width:1.5px,color:#713f12
  classDef automation fill:#f8fafc,stroke:#94a3b8,stroke-width:1px,color:#334155
  classDef tier1      fill:#d1fae5,stroke:#059669,stroke-width:1px,color:#064e3b
  classDef tier2      fill:#fef3c7,stroke:#d97706,stroke-width:1px,color:#78350f
  classDef tier3      fill:#fee2e2,stroke:#dc2626,stroke-width:1.5px,color:#7f1d1d,font-weight:bold
  classDef halt       fill:#fecaca,stroke:#b91c1c,stroke-width:2.5px,color:#450a0a,font-weight:bold
  classDef branch     fill:#dbeafe,stroke:#3b82f6,stroke-width:1px,color:#1e3a5f
  classDef storage    fill:#f3e8ff,stroke:#9333ea,stroke-width:1px,color:#3b0764
```

> **Reading the diagram:** Blue subgraphs = workflow phases · Green diamonds = scoring gates (5/5 required to advance, loops back on fail) · Yellow diamonds = decision points · Red box = Mismatch halt (workflow stops entirely) · Green nodes = Tier 1 automations (auto-execute, no gate) · Yellow/amber nodes = Tier 2 automations (APPROVE required) · Red nodes = Tier 3 automations (irreversible — full data preview + APPROVE PHRASE) · Purple nodes = local file download steps (always before cloud save) · Dashed arrow = loop back to Phase 0 after successful submission.

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

1. [Download the ZIP from Releases](https://github.com/ahmedbenaw/job-application-engine/releases)
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

1. [Download the ZIP from Releases](https://github.com/ahmedbenaw/job-application-engine/releases)
2. In CoWork, go to **Customize → Skills → Create Skill**
3. Upload the ZIP directly
4. The skill is now available to all agents in your CoWork environment
5. Open a new CoWork project and begin — CoWork routes parallel phases automatically

**Alternative — Workspace file upload** *(if Skills not available on your CoWork tier)*

1. [Download the ZIP from Releases](https://github.com/ahmedbenaw/job-application-engine/releases)
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

1. [Download the ZIP from Releases](https://github.com/ahmedbenaw/job-application-engine/releases)
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

Before your first job search session, complete your Applicant Profile:

1. Open `references/applicant-profile-template.md`
2. Fill in the **Static Fields** — name, contact details, education, exclusion list
3. Leave Dynamic Fields with their `[PLACEHOLDER]` tokens for now
4. Save the file and include it in your platform upload

The First-Use Setup Protocol inside the skill walks you through populating all
Dynamic Fields in your first session via a structured 25-question intake. After
that, the profile is your persistent source of truth across all sessions and roles.

---

## Automation Layer (v2.0)

Version 2.0 adds a native execution layer beneath the 8-phase workflow. All phases,
gates, and invariants from v1.0 are unchanged. The automation layer is purely additive.

### 11 Registered Automations

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

### Consent Tiers

**Tier 1 — Read-only:** auto-executes as part of the phase. No separate gate.

**Tier 2 — Reversible write:** requires `APPROVE [ACTION_NAME]` typed explicitly.
A score of 5 or "yes" is not accepted.

**Tier 3 — Irreversible:** requires the full consent gate — complete preview of all
data being transmitted, destination, and timestamp — followed by exact typed phrase.
Cannot be triggered by a score, "yes", or any paraphrase.

> **Approval and scoring are entirely separate systems and must never be conflated.**

### Capability Map

At session start, before Phase 0, the skill probes the current environment and
presents a Capability Map showing every automation as ACTIVE, LIMITED, or INACTIVE,
with the connection required to enable each inactive one. User acknowledges before proceeding.

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
