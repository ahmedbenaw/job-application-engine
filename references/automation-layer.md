# Automation Layer
# job-application-engine v2.2.0 (generic) | moved out of SKILL.md for progressive disclosure, content unchanged unless marked "v2.2.0"
# Read when: session start (A0 capability detection); before any automation A01–A17 fires

---

> **v2.2.0 additions:** A0 also checks for a document tool for CV export (DOCX/PDF), text readers for the read test (pdftotext, pypdf, python-docx or similar) and, when available, image viewing plus browser or computer control for the ATS Gate visual review (GATE-18); missing tools are listed in the Capability Map with their fallback. New automation **A17 — CV File Export** (Tier 2, APPROVE CREATE; default one approval per application covers all re-tests). A04 now uploads only the fingerprinted CV from the latest ATS Gate PASS. Uploading a CV to any outside site for testing is Tier 2 and never uses an employer's live application form.
>
> **v2.2.0 fallback ladder (A18):** when any tool in this layer is missing or blocked, use `references/automation-playbooks/vision-browser-computer-fallback.md` (MCP → native tool → browser use → computer use → vision → ask the person). A0 lists which of browser use, computer use and image viewing exist. Falling back never lowers a consent tier.

> **v2.2.0 capability wording:** what the person is told depends on the Capability Map. Never name a browser, browser-automation product or desktop-app brand to the person; never say "on your computer" or promise an action unless that tool shows **ACTIVE**. Form filling: "I can fill the form if you approve each step" only when browser control is ACTIVE; otherwise "I'll give you answers to paste", without offering filling as a later or "if connected" option.
>
> **v2.2.0 first-turn presentation:** run every A0 check as written, but on the first turn present the result as a 3–5 line plain summary. Show the full Capability Map when the person asks, or when a tool the current application needs is missing. STEP 1C (searching for job-board connectors) runs in Mode A, or when the person asks; in Mode B it is listed as available on request. This replaces only how A0 is shown, not what it checks.

## Automation Layer — v2.0 Addition (v2.1.x: A14–A16 for execution modes)

This section is purely additive to the baseline eight-phase workflow shipped in
the Generic Universal edition. All 8 phases and their gates remain unchanged.
The automation layer adds a capability detection
protocol at session start, inline automation recommendations at relevant
phase steps, consent gates before any real-world action fires, and execution
routing per platform. Read automation-registry.json for the full declared
scope of permitted automations (including **A14–A16** for `cowork_autonomous`
chunk orchestration, governance re-anchor, and drift check — `docs/EXECUTION_MODES.md`).

---

### A0 — Capability Detection Protocol

Run this protocol at the very start of every session, before Phase 0 begins.
Do not proceed to Phase 0 until the Capability Map is presented and the user
has acknowledged it.

STEP 1 — Probe available tools and MCP connections:
Check which of the following are active in the current session environment:
  web_search, web_fetch, bash_tool, create_file, present_files (native tools)
  BrowserBase MCP (browser automation — primary path for form filling)
  Playwright MCP (browser automation — secondary path)
  Gmail MCP (email send and draft)
  Outlook / MS365 MCP (email alternative)
  Google Drive MCP (cloud document storage)
  OneDrive MCP (cloud document storage alternative)
  Google Calendar MCP (reminder creation)
  Any other MCP detected in the session environment

STEP 1B — Job Board and ATS Platform MCP Detection:
This step runs as part of STEP 1. Probe specifically for the following
job board and ATS platform MCPs, which enable direct authenticated access
to platform dashboards, saved job lists, and application status tracking
beyond what web_fetch alone can achieve:

  LinkedIn MCP        — authenticated job search, saved jobs, easy apply
  Indeed MCP          — job search, application tracking
  Greenhouse MCP      — ATS access for candidates and recruiters
  Lever MCP           — ATS job board access
  Workday MCP         — enterprise ATS access
  Ashby MCP           — modern ATS integration
  Wellfound MCP       — startup job board access
  SmartRecruiters MCP — enterprise ATS integration
  Breezy HR MCP       — job board and ATS access
  Recruitee MCP       — ATS integration

For each: check if the MCP is active in the current session. Mark as
ACTIVE, LIMITED, or INACTIVE in the map.

If ALL job board and ATS MCPs are INACTIVE — run STEP 1C immediately.

STEP 1C — MCP Discovery Search (runs only when no job board MCP is found):
Run the following web searches to find currently available job board and
ATS platform MCPs that the user could connect:

  web_search: "LinkedIn MCP model context protocol job search site:github.com"
  web_search: "job board ATS MCP Claude integration available 2025 site:github.com OR site:npmjs.com"
  web_search: "Greenhouse Lever Workday MCP server integration Claude"

From the results, compile a list of:
  - MCPs that exist and are publicly available (GitHub repo, npm package, or official)
  - MCPs that are in development or planned
  - Native API integrations that approximate MCP capability

Present this as a RECOMMENDED CONNECTIONS block below the Capability Map.
Always note that without a job board MCP, the skill falls back to
web_search and web_fetch for discovery and manual paste for authenticated
actions. That fallback is fully functional — job board MCPs are an
enhancement, not a requirement.

STEP 2 — Build and present the Capability Map:
Print the map using this exact format. Replace [STATUS] with one of:
  ✅ ACTIVE — tool confirmed available and callable
  ⚠ LIMITED — tool present but with known constraints (note the constraint)
  ❌ INACTIVE — tool not connected (show what connection would enable it)

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    JAE — AUTOMATION CAPABILITY MAP                          ║
╠════════════════════════════════════╦══════════════════╦══════════╦══════════╣
║  AUTOMATION                        ║ TOOL / MCP       ║ STATUS   ║ FALLBACK ║
╠════════════════════════════════════╬══════════════════╬══════════╬══════════╣
║  CORE TOOLS                        ║                  ║          ║          ║
║  Job board search & fetch          ║ web_search/fetch ║ [STATUS] ║ —        ║
║  Form fetch & parse                ║ web_fetch        ║ [STATUS] ║ Manual   ║
║  Browser form filling              ║ BrowserBase MCP  ║ [STATUS] ║ Playwright║
║  Application submission            ║ BrowserBase MCP  ║ [STATUS] ║ Manual   ║
║  Document creation (DOCX/PDF)      ║ bash_tool        ║ [STATUS] ║ —        ║
║  File download (local)             ║ present_files    ║ [STATUS] ║ —        ║
║  Cloud save (Drive/OneDrive)       ║ Google Drive/OneDrive   ║ [STATUS] ║ Ask user ║
║  Email draft & send                ║ Gmail/Outlook    ║ [STATUS] ║ Manual   ║
║  Calendar reminders                ║ Calendar MCP     ║ [STATUS] ║ Manual   ║
╠════════════════════════════════════╬══════════════════╬══════════╬══════════╣
║  JOB BOARD & ATS PLATFORM MCPs     ║                  ║          ║          ║
║  LinkedIn (search, saved, apply)   ║ LinkedIn MCP     ║ [STATUS] ║ web_fetch ║
║  Indeed (search, tracking)         ║ Indeed MCP       ║ [STATUS] ║ web_fetch ║
║  Greenhouse (ATS)                  ║ Greenhouse MCP   ║ [STATUS] ║ web_fetch ║
║  Lever (ATS)                       ║ Lever MCP        ║ [STATUS] ║ web_fetch ║
║  Workday (enterprise ATS)          ║ Workday MCP      ║ [STATUS] ║ web_fetch ║
║  Ashby (modern ATS)                ║ Ashby MCP        ║ [STATUS] ║ web_fetch ║
║  Wellfound / AngelList             ║ Wellfound MCP    ║ [STATUS] ║ web_fetch ║
║  SmartRecruiters                   ║ SmartRec MCP     ║ [STATUS] ║ web_fetch ║
╚════════════════════════════════════╩══════════════════╩══════════╩══════════╝

INACTIVE AUTOMATIONS — what would enable them:
  [List each ❌ item with the MCP name and connection instructions]

RECOMMENDED JOB BOARD MCPs (shown only when all job board MCPs are INACTIVE):
  [Results from STEP 1C web search — available MCPs with GitHub/npm links]
  [Note: web_search and web_fetch provide full discovery capability without
   these MCPs. They unlock authenticated features like saved jobs, easy
   apply, and application status tracking.]
```

STEP 2A — Mandatory artifact fallback (present_files, create_file, bash_tool):
If **present_files**, **create_file**, or **bash_tool** is ❌ INACTIVE or ⚠ LIMITED such that local file presentation or shell-backed generation cannot run as written:
  1. State which tool is blocked and why (from the Capability Map row).
  2. Deliver the **full artifact content inline** (structured or monospace) — cover letter text, package summary, DOCX instructions, etc. Never claim `present_files` ran when the map shows INACTIVE.
  3. Instruct the user to **save or copy** to their machine or workspace using the host UI (copy button, workspace file create, manual paste) — exact control depends on Claude.ai, CoWork, or Manus.
  4. On **Manus**, treat **present_files** as potentially INACTIVE unless the map shows ACTIVE; use this fallback **without** waiting for failure at send time.
  5. Read **artifact_policy** in `automation-registry.json` and **docs/MANDATORY_EXCLUSIONS.md** (Manus §) for normative scope.

STEP 3 — Browser automation disclosure:
If BrowserBase MCP is ACTIVE: note it as the primary path for form filling
and submission. No further explanation needed unless the user asks.

If BrowserBase is INACTIVE but Playwright MCP is ACTIVE: present this
disclosure to the user before Phase 0:

  "Playwright MCP is available for browser automation (form filling and
  application submission). This is a technical tool — it controls a real
  browser programmatically. It works reliably on most job platforms but
  requires that the target site does not use aggressive bot detection.
  If a site blocks it, the fallback is pre-staged answers for manual paste.
  Do you want to use Playwright automation where available?"

If both are INACTIVE: note that form filling and submission will use
pre-staged answers for manual paste. No further action needed.

STEP 4 — Acknowledge and proceed:
After presenting the Capability Map, ask: "Shall we begin?"
Do not proceed until the user confirms.

---

### Automation Recommendation Protocol

At each phase where an automation is relevant, present a recommendation
block AFTER the phase's main output and BEFORE the scoring gate.

Use this format:

```
── AUTOMATION AVAILABLE ────────────────────────────────────────────
  ACTION    : [What the automation will do]
  TOOL      : [Which tool or MCP will execute it]
  CONSENT   : [Tier 1 auto / Tier 2 APPROVE / Tier 3 APPROVE + phrase]
  RELEVANCE : [Why this is useful at this exact step]
  → Type APPROVE [ACTION] to execute, or skip to continue manually.
────────────────────────────────────────────────────────────────────
```

Additionally, if the Capability Map shows an INACTIVE automation that would
be highly useful at the current step, present a recommendation to connect it:

```
── AUTOMATION RECOMMENDED (NOT YET CONNECTED) ──────────────────────
  MISSING   : [Automation name]
  WOULD DO  : [What it would do at this step]
  REQUIRES  : [MCP name and how to connect]
  BENEFIT   : [Why connecting it would improve this step]
────────────────────────────────────────────────────────────────────
```

Never present more than two automation recommendations per phase.
Always present the manual fallback path alongside any automation option.
Never suggest automations outside the scope declared in automation-registry.json.

Phase-by-phase automation trigger points:

Phase 0 (Job Discovery): after presenting the ranked table, offer to fetch
  full job posting content for top 5 results (Tier 1 auto via web_fetch).
  If BrowserBase or Playwright is active, offer to access job board dashboards
  that require login after user provides credentials within the session.

Phase 1 (Company Intelligence): after the Intelligence Brief, offer to
  fetch and map the full application form for the selected role (Tier 1).
  If form requires browser access and automation is available, trigger it.

Phase 3 (Clarifying Intake): if a follow-up email to the hiring manager
  would be appropriate (e.g. to ask for the application form name), offer
  to draft and send it via email automation (Tier 3 — requires APPROVAL).

Phase 4 (Application Package): after package is produced and scored 5,
  offer to create a DOCX version of the cover letter (Tier 2 — APPROVE CREATE).
  Offer to save the full package to local download immediately (Tier 1).

Phase 6 (Governance Gate): after all 8 checks pass, offer to fill the
  application form fields using browser automation if available (Tier 3).
  Offer to create a session record document for local download (Tier 2).

Phase 7 (Post-Submission): offer to create a calendar reminder for
  follow-up (Tier 2 — APPROVE CREATE). Offer to send a confirmation email
  to the user's own address with the application package (Tier 2).

---

### Consent Gate Protocol

Three tiers based on reversibility and risk. Approval and Scoring are
separate systems. Scoring gates evaluate phase quality. Consent gates
authorise real-world actions. They use different confirmation mechanisms
and must never be conflated.

TIER 1 — Read-only actions:
Examples: fetching job listings, loading forms, researching companies.
Execution: auto-execute as part of the phase workflow. No separate gate.
The existing phase scoring gate is sufficient.

TIER 2 — Reversible write actions:
Examples: creating a DOCX, saving to Drive, creating a calendar event.
Present a preview before executing:

```
── TIER 2 CONSENT GATE ────────────────────────────────────────────
  ACTION    : [Exact description of what will be created or written]
  LOCATION  : [Where it will be saved — local / Drive folder / calendar]
  CONTENTS  : [Summary of what the file or event will contain]
  REVERSIBLE: Yes — [explain how to undo if needed]
  → Type APPROVE [ACTION_NAME] to execute.
  → Example: APPROVE CREATE to create the document.
  → Type SKIP to continue without this action.
────────────────────────────────────────────────────────────────────
```

Accept only exact APPROVE [ACTION_NAME] typed by the user. A score of 5,
"yes", "ok", or any other response does not constitute Tier 2 approval.

TIER 3 — Irreversible write actions:
Examples: submitting an application, sending an email to an external party.
These cannot be undone. Use the full consent gate:

```
── TIER 3 CONSENT GATE — IRREVERSIBLE ACTION ──────────────────────
  ACTION     : [Exact description — what will be sent or submitted]
  DESTINATION: [Exact recipient or platform receiving the action]
  DATA SENT  : [Full list of data fields or content being transmitted]
  TIMESTAMP  : [Current date and time of execution if confirmed]
  ⚠ THIS CANNOT BE UNDONE AFTER CONFIRMATION.

  To confirm, type the exact phrase:
  APPROVE [SPECIFIC_PHRASE]

  Examples:
    Application submission → APPROVE SUBMIT
    Email send             → APPROVE SEND
    Form field commit      → APPROVE FILL

  Type CANCEL or anything else to abort.
────────────────────────────────────────────────────────────────────
```

After receiving APPROVE [SPECIFIC_PHRASE]: read it back to confirm the
match is exact. Then execute. Never execute on a partial match.
Never proceed if the user types a score, "yes", or a paraphrase.

---

### Browser Automation Protocol

STEP 1 — Platform detection:
Before triggering browser automation for a specific job platform, check
automation-registry.json for the platform's known bot-detection level.
High bot-detection platforms (LinkedIn, Indeed) require special handling.
Low bot-detection platforms (Greenhouse, Lever, Breezy HR) are reliable.

STEP 2 — Tool selection:
If BrowserBase MCP is ACTIVE: use it as the primary execution path.
If BrowserBase is INACTIVE and Playwright MCP is ACTIVE: present the
Playwright disclosure (see A0 Step 3) if not already shown this session,
confirm the user accepts Playwright, then proceed.
If both are INACTIVE: switch to pre-staged answers mode — produce all
field values in a numbered copy-paste format matching the form structure,
and instruct the user to fill manually.

STEP 3 — Credential handling:
Never store credentials in any file. If a platform requires login for
form access, request credentials within the session only, use them for
the current action, and explicitly confirm to the user that they are
not retained after the session ends.

STEP 4 — Failure handling:
If browser automation fails mid-form (bot detection, timeout, DOM change):
immediately stop, report the failure to the user, show how far the form
was completed, and switch to pre-staged answers for the remaining fields.
Never attempt to resubmit automatically after a failure.

---

### Email Selection Protocol

Never assume which email system to use. Never hardcode a default.

When an email action is triggered for the first time in a session:
Present all active email MCPs detected in the Capability Map.
Ask the user which to use for this action.
Store the selection for this session only as [SESSION_EMAIL_CHOICE].
On subsequent email actions in the same session: show "Last used:
[SESSION_EMAIL_CHOICE]" and ask "Use the same, or switch?"
Do not carry the selection across sessions. Ask fresh each time.

Format for email selection prompt:

```
── EMAIL SYSTEM SELECTION ─────────────────────────────────────────
  Available email systems detected this session:
    [List each active email MCP]
  Last used this session: [SESSION_EMAIL_CHOICE or "None yet"]
  Which would you like to use for this action?
────────────────────────────────────────────────────────────────────
```

---

### Document Storage Protocol

When a document (DOCX, PDF, or package) is created:

STEP 1 — Always present for local download first using present_files.
Never ask about cloud storage before local download is presented.

STEP 2 — After local download is offered, ask:
"Would you also like to save this to cloud storage?"
If yes: present all active cloud storage MCPs detected in the Capability Map
  (Google Drive, OneDrive, or any other connected provider).
Ask which provider to use for this save.
Execute the cloud save as a Tier 2 action (APPROVE SAVE required).
If no: proceed without cloud save. Never save to cloud without consent.

STEP 3 — Folder suggestion:
When saving to cloud, suggest a logical folder path based on the current
session context (e.g. "Job Applications / [COMPANY_NAME] / [DATE]").
Present the suggested path and ask the user to confirm or modify it before
executing the save.

---

### Platform-Aware Automation Routing

Claude.ai:
All automations execute sequentially. Tier 1 actions fire inline as part
of the phase. Tier 2 and Tier 3 actions pause for consent before firing.
Browser automation and email MCPs execute in the same conversation thread.

Claude CoWork:
Tier 1 read-only automations (job board fetching, form parsing, company
research) may run as parallel subagents during Phases 0 and 1.
All Tier 2 and Tier 3 actions — regardless of phase — execute sequentially
after consent in the main coordination thread. Never dispatch an irreversible
action to a subagent.

Manus:
All automations follow the `rules.json` `automation_layer` block as session
instructions (whether loaded via Skills, workspace files, or pasted rules).
Tier 1 actions execute inline. Tier 2 and Tier 3 actions pause and surface
the consent gate as a text prompt in the session. Browser automation relies on
Manus's native browser tools if BrowserBase and Playwright MCPs are not
available. For `present_files` INACTIVE, apply **A0 STEP 2A** before claiming
any file download occurred.

---
