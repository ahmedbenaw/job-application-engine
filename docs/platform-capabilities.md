# Platform capabilities — canonical reference for JAE

README and `SKILL.md` **summarize** this document; they **must not** contradict it.

---

## Claude.ai (web chat; Skills or Project Knowledge)

**In scope for JAE**

- Full **eight-phase** workflow **sequentially** in one conversation.
- Scoring gate after every phase; explicit confirmation before Phase 4 (first application text).
- **Tools/MCP** available in that chat session (per host policy): `web_search`, `web_fetch`, and others probed in A0.
- **Agent Skills** (where the product offers them): upload skill ZIP per product UI — see Anthropic documentation for current paths and plan requirements.

**Mandatory limitations**

- Phases do **not** run as parallel subagents; high-volume parallel discovery is slower than CoWork for the same authored parallelism.
- “Agentic” here means **in-conversation** tool and MCP use within product limits — **not** the same as CoWork workspace/VM-style automation.

**Install (primary vs fallback)**

1. **Primary:** Skills upload (product-dependent naming — e.g. Customize → Skills → Create Skill).
2. **Fallback:** Project Knowledge — upload `SKILL.md`, `rules.json`, `automation-registry.json`, and all files under `references/` (see repo layout).

---

## Claude CoWork

**In scope for JAE (explicitly harnessed)**

- **Parallel Tier-1** read-only work: Phases **0**, **1**, and **salary research inside Phase 3**, as parallel subagents, per `SKILL.md` and `rules.json`.
- **Sequential** Phases **5** and **6**; Phase **2** verdict before Phase **4** begins.
- **Tier 2 and Tier 3** automations: **always** on the **main coordination thread** after consent — **never** on a subagent.
- **Artifacts:** checklist as **static file** updated per gate (`references/skill-instructions/checklist-templates.md`). Package output described as **downloadable** when the host supports file presentation.
- **MCP:** BrowserBase, Playwright, email, cloud storage, calendar — only when connected and listed in A0 Capability Map.

**Mandatory wording**

- Parallelism is **authored** in this skill and **allowed** by CoWork; the product does not “auto-route phases” without the skill’s rules.

**Mandatory exclusions**

- See [MANDATORY_EXCLUSIONS.md](MANDATORY_EXCLUSIONS.md) for scheduling, generic OS computer use, and undeclared browser primitives.

---

## Manus

**In scope for JAE (primary install — current product)**

1. **Skills:** Skills tab → **+ Add** → **Upload a skill** (`.zip` / `.skill`) **or** **Import from GitHub** with this repository’s public URL.
2. **Fallback:** Extract ZIP and upload workspace files; or paste `rules.json` as session instruction source.

**Mandatory limitation**

- `present_files` may be **INACTIVE** on some Manus sessions. When INACTIVE, follow **`SKILL.md` A0 — Mandatory artifact fallback** (inline deliverable text + user save instructions). Never assume a file download primitive exists.

---

## Hybrid patterns (both mandatory; one default)

### Default: `hybrid_chat_review`

- Run **Phases 0 and 1** in **CoWork** for parallel discovery and company intelligence speed.
- Copy the **Company Intelligence Brief** into **Claude.ai**.
- Run **Phases 2–7** in **Claude.ai** for sequential scoring gates and in-chat review of drafting.

**When to recommend:** User wants parallel discovery plus **single-thread chat** review for writing phases.

### Secondary: `cowork_end_to_end`

- Run **Phases 0–7** entirely in **CoWork** when **local artifacts**, **downloadable packages**, or **heavy file/browser** work should stay in one workspace.

**When to recommend:** User prioritizes workspace files and CoWork-local delivery over chat-only review.

**Machine-readable keys:** `rules.json` → `platform_notes.hybrid_chat_review`, `platform_notes.cowork_end_to_end`.

---

## Links

- [MANDATORY_EXCLUSIONS.md](MANDATORY_EXCLUSIONS.md)
- [SKILL.md](../SKILL.md)
- [rules.json](../rules.json)
