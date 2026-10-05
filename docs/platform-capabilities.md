# Platform capabilities — canonical reference for JAE

README and `SKILL.md` **summarize** this document; they **must not** contradict it.

**Execution modes (v2.1.x and later):** [EXECUTION_MODES.md](EXECUTION_MODES.md) — `agent_supported` (default) vs `cowork_autonomous` (CoWork, opt-in).  
**Scope law:** [MANDATORY_EXCLUSIONS.md](MANDATORY_EXCLUSIONS.md).  
**Current version:** 2.2.0. Phases 0–7 keep their numbers; v2.2.0 adds sub-phases **2A** (job analysis), **3B** (CV Build) and **3C** (ATS Gate), five mandatory 5/5 gates (**M1–M5**) with a visible grade for every other phase, **A17** (CV file export) and **A18** (fallback ladder and visual audits). Design record: [CV_ATS_REQUIREMENTS_SPEC_v0.11.0.md](CV_ATS_REQUIREMENTS_SPEC_v0.11.0.md).

---

## Claude.ai (web chat; Skills or Project Knowledge)

**In scope for JAE**

- Full **eight-phase** workflow (with sub-phases 2A, 3B, 3C) **sequentially** in one conversation.
- Mandatory 5/5 gates M1–M5 plus a visible grade after every other phase; no CV or application text before the Phase 3 facts are confirmed (the CV is written in Phase 3B).
- **Tools/MCP** available in that chat session (per host policy): `web_search`, `web_fetch`, and others probed in A0.
- **Phase 3C ATS Gate** needs file creation and code execution for `scripts/ats_gate.py`. When the session lacks them, the counted checks are marked **not run**, the gate cannot PASS, and nothing is uploaded; run Phases 3B–3C in CoWork instead (see hybrid patterns).
- **Agent Skills** (where the product offers them): upload skill ZIP per product UI — see Anthropic documentation for current paths and plan requirements.
- **Execution mode:** `agent_supported` only (no `cowork_autonomous` in this product surface).

**Mandatory limitations**

- Phases do **not** run as parallel subagents; high-volume parallel discovery is slower than CoWork for the same authored parallelism.
- “Agentic” here means **in-conversation** tool and MCP use within product limits — **not** the same as CoWork workspace-style execution.

**Install (primary vs fallback)**

1. **Primary:** Skills upload (product-dependent naming — e.g. Customize → Skills → Create Skill).
2. **Fallback:** Project Knowledge — upload `SKILL.md`, `rules.json`, `automation-registry.json`, all files under `references/`, and `scripts/ats_gate.py` (see repo layout). `evals/` and `hooks/` are for maintainers and are not needed to run the skill.

---

## Claude CoWork

**In scope for JAE (explicitly harnessed)**

- **Parallel Tier-1** read-only work: Phases **0**, **1**, and **salary research inside Phase 3**, as parallel subagents, per `SKILL.md` and `rules.json`.
- **Sequential** Phases **2A**, **3B**, **3C**, **5** and **6**; Phase **2** verdict before Phase **3B** (first CV text) and Phase **4** begin. A17 CV export (Tier 2) runs on the main thread.
- **Tier 2 and Tier 3** automations: **always** on the **main coordination thread** after consent — **never** on a subagent.
- **Artifacts:** checklist as **static file** updated per gate (`references/skill-instructions/checklist-templates.md`). Package output described as **downloadable** when the host supports file presentation.
- **MCP:** BrowserBase, Playwright, email, cloud storage, calendar — only when connected and listed in A0 Capability Map.
- **Execution modes:** Default **`agent_supported`**. User may opt into **`cowork_autonomous`** for larger host-driven chunks **only** with explicit opt-in and **mandatory re-anchor** to the same phase law after each chunk — see [EXECUTION_MODES.md](EXECUTION_MODES.md) and A14–A16 in `automation-registry.json`.

**Mandatory wording**

- Parallelism is **authored** in this skill and **allowed** by CoWork; the product does not “auto-route phases” without the skill’s rules.
- **Availability and plans** of CoWork, connectors, and controls are **product-owned**; see [Claude CoWork (Anthropic)](https://www.anthropic.com/product/claude-cowork) and [Cowork (claude.com)](https://claude.com/product/cowork). JAE does not hardcode a plan matrix here.

**Scope (not “exclusion of CoWork”)**

- See [MANDATORY_EXCLUSIONS.md](MANDATORY_EXCLUSIONS.md): **hard-prohibited** JAE mis-claims, **host-governed** features under Mode 2 + re-anchor, **registry-native** automations for anything presented as a named Axx.

---

## Manus

**In scope for JAE (primary install — current product)**

1. **Skills:** Skills tab → **+ Add** → **Upload a skill** (`.zip` / `.skill`) **or** **Import from GitHub** with this repository’s public URL.
2. **Fallback:** Extract ZIP and upload workspace files; or paste `rules.json` as session instruction source.

**Mandatory limitation**

- Phase 3C needs code execution for `scripts/ats_gate.py`. Without it, the counted checks are marked **not run** and the gate cannot PASS.
- `present_files` may be **INACTIVE** on some Manus sessions. When INACTIVE, follow **`SKILL.md` A0 — Mandatory artifact fallback** (inline deliverable text + user save instructions). Never assume a file download primitive exists.
- **Execution mode:** `agent_supported` only unless Manus later exposes an equivalent; default remains guided governance.

---

## Hybrid patterns (both mandatory; one default)

### Default: `hybrid_chat_review`

- Run **Phases 0 and 1** in **CoWork** for parallel discovery and company intelligence speed.
- Copy the **Company Intelligence Brief** into **Claude.ai**.
- Run **Phases 2–7** in **Claude.ai** for sequential scoring gates and in-chat review of drafting.
- **v2.2.0:** if the Claude.ai session can't create files or run code, run **Phases 3B–3C** (CV export and ATS Gate) in CoWork, then continue in Claude.ai with the gate report.

**When to recommend:** User wants parallel discovery plus **single-thread chat** review for writing phases.

### Secondary: `cowork_end_to_end`

- Run **Phases 0–7** entirely in **CoWork** when **local artifacts**, **downloadable packages**, or **heavy file/browser** work should stay in one workspace.

**When to recommend:** User prioritizes workspace files and CoWork-local delivery over chat-only review.

**Optional:** In CoWork, combine `cowork_end_to_end` with `cowork_autonomous` for execution chunks **only** under [EXECUTION_MODES.md](EXECUTION_MODES.md).

**Machine-readable keys:** `rules.json` → `platform_notes.hybrid_chat_review`, `platform_notes.cowork_end_to_end`.

---

## Fallbacks and visual audits (A18, v2.2.0) — all hosts

- When a tool a step needs is missing or blocked, the skill moves down one ladder: connector (MCP) → native tool → browser use → computer use → vision → ask the person. It names the rung it used in the grade line.
- Browser use follows the registry order (BrowserBase, then Playwright, then a host-reported browser tool shown in the Capability Map). Computer use and image viewing are used **only** where the host offers them, under the host's own consent UI.
- The same abilities audit work on purpose: CV pages as images (GATE-18), filled forms before submit, the portal's preview of the parsed CV, the confirmation page.
- Reading and looking are Tier 1. Falling back **never lowers** a consent tier. The person logs in themselves; credentials are never typed or stored. Never unattended (see [MANDATORY_EXCLUSIONS.md](MANDATORY_EXCLUSIONS.md) section E).
- **Capability wording:** replies never name a browser, browser-automation product or desktop-app brand, never say "on your computer", and never promise an action unless the A0 Capability Map shows that tool ACTIVE. Form filling: "I can fill the form if you approve each step" only when browser control is ACTIVE; otherwise "I'll give you answers to paste".
- Reference: `references/automation-playbooks/vision-browser-computer-fallback.md`.

---

## Claude Code (optional, v2.2.0) — enforcement hooks and maintainer tooling

Not a primary end-user platform for JAE. Two uses:

1. **Plugin with hooks:** the release asset `job-application-engine-plugin.zip` installs the same skill plus two opt-in hooks: block uploading a CV that is not the file from the latest ATS Gate PASS (GAP-11), and cancel a PASS after any edit (GATE-14). Alternative: copy `hooks/settings-snippet.json` into `.claude/settings.json`. Hooks do **not** run on Claude.ai, CoWork or Manus; there the same rules hold as skill instructions (invariant 15 and GATE-14).
2. **Release checks:** `python3 scripts/selftest.py` and `evals/` (see `evals/README.md`). Release bar: 100% of both.

Use either the plugin or a Skills upload in the same account, not both.

---

## Links

- [MANDATORY_EXCLUSIONS.md](MANDATORY_EXCLUSIONS.md)
- [EXECUTION_MODES.md](EXECUTION_MODES.md)
- [SKILL.md](../SKILL.md)
- [rules.json](../rules.json)
