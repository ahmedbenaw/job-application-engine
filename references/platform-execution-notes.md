# Platform Execution Notes
# job-application-engine v2.2.0 (generic) | moved out of SKILL.md for progressive disclosure, content unchanged unless marked "v2.2.0"
# Read when: platform-specific behaviour (Claude.ai, CoWork, Manus)

---

## Platform Execution Notes

Canonical reference: `docs/platform-capabilities.md`. **Execution modes:** `docs/EXECUTION_MODES.md`. **Scope law (what JAE may claim vs host features):** `docs/MANDATORY_EXCLUSIONS.md`. JAE does **not** fabricate undeclared automations or bypass invariants; host capabilities (e.g. CoWork, connectors) are used only under product limits, user consent, and — in Mode 2 — mandatory re-anchor to this skill’s phase governance.

Claude.ai (web chat): Run all phases **sequentially** in one conversation.
Wait for the scoring gate before advancing. Confirm explicitly before Phase 4.
Present the status board each phase. **Agentic** here means in-conversation
tools and MCPs per host policy — not CoWork-class workspace VM automation.

Claude CoWork: Phases 0, 1, and Phase 3 salary research run as **parallel
Tier-1 subagents** where `rules.json` permits. Phase 2 must return a verdict
before Phase 4. Phases 5 and 6 run **sequentially**. Tier 2 and Tier 3
automations run only on the **main coordination thread**. Package output as a
downloadable file when the host supports it. Status board as a **static file
artifact** updated per gate (see `references/skill-instructions/checklist-templates.md`).
Parallelism is **authored in this skill**; CoWork **allows** it — the product
does not auto-route phases without these rules.

**hybrid_chat_review (DEFAULT):** Run Phases 0 and 1 in CoWork. Copy the Company
Intelligence Brief into Claude.ai. Run Phases 2–7 in Claude.ai for sequential
gates and in-chat review of drafting.

**cowork_end_to_end (SECONDARY):** Run Phases 0–7 entirely in CoWork when
workspace files, downloadable packages, or staying in one agent workspace
dominate the session goals.

Manus — **primary:** Skills tab → **+ Add** → **Upload a skill** (`.zip` /
`.skill`) or **Import from GitHub** with the public repository URL.
**Fallback:** upload extracted workspace files; or paste `rules.json` as
session-scope instructions. Maintain the status board as a **text block** in
session context. All phase outputs require user confirmation before advancing.
If `present_files` is INACTIVE, use **A0 STEP 2A — Mandatory artifact fallback**
immediately for any local download step.

---
