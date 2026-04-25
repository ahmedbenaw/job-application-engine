# Execution modes — JAE v2.1.x

This document is **normative** for how the skill may combine **governance** (eight phases, scoring gates, consent tiers) with **host execution** (Claude / CoWork / Manus) without drifting.

**Machine-readable:** [rules.json](../rules.json) → `execution_modes`.  
**Skill behavior:** [SKILL.md](../SKILL.md) — *Execution mode gate* and *Mode 2 re-anchor*.

---

## 1) Definitions

| Key | Name | Default |
|-----|------|---------|
| `agent_supported` | **Agent-supported (Mode 1)** | **Yes** — used unless the user opts into Mode 2 on a supported host |
| `cowork_autonomous` | **CoWork autonomous (Mode 2)** | **Opt-in** — only on **Claude CoWork** when the user explicitly requests it |

**Session entry modes (unchanged):** **Mode A** (discovery) vs **Mode B** (direct apply) are **orthogonal** to execution mode. You still run Mode A/B detection as today; execution mode only affects **how aggressively** the host may drive multi-step work **inside** the same phase law.

---

## 2) Mode 1 — `agent_supported` (default)

- Full **A0 → Phase 0–7** path with **scoring gate** every phase and **Tier 2/3** consent exactly as in `automation-registry.json`.
- **CoWork:** parallel Tier-1 work only where `rules.json` and `SKILL.md` allow; irreversible work on the main thread.
- **Claude.ai / Manus:** sequential governance as already documented in [platform-capabilities.md](platform-capabilities.md).

---

## 3) Mode 2 — `cowork_autonomous` (opt-in, CoWork only)

**Intent:** Use CoWork’s ability to run **larger multi-step host execution** where the product allows, **without** giving up JAE’s workflow law.

**Non-negotiable (anti-drift):**

- **Governance is always the agent-supported phase model** — the eight phases, invariants, and registry scope remain the source of truth.
- The skill **does not** “skip to submission” or collapse phases. Any fast host execution must be **chunked** and followed by a **re-anchor** step (A15/A16) that verifies alignment with the current phase and checklist.
- **Irreversible actions** (submit, send, fill, etc.): **default** remains **unchanged** — same Tier 3/2 requirements unless a future, explicit, versioned policy says otherwise.
- If the user’s request, tool output, or host behavior conflicts with phase scope, **stop**, return to a normal agent-supported checkpoint, and reconcile.

**Opt-in phrases (one is enough, exact match):**

- `JAE MODE: COWORK_AUTONOMOUS`
- `I opt in to JAE CoWork autonomous mode with phase governance`

To **leave** Mode 2 and return to Mode 1 in-session:

- `JAE MODE: AGENT_SUPPORTED`

If the user never sends an opt-in phrase, remain in **Mode 1**.

---

## 4) Per-chunk loop (Mode 2)

For each **autonomous chunk** (see A14 in `automation-registry.json`):

1. **Pre-chunk:** State current phase, objective, and allowed tools/scope for *this* chunk.
2. **Run chunk** (host execution as permitted, with A14 consent if required by tier).
3. **Post-chunk re-anchor (A15):** Confirm phase status, checklist row, invariants, and that no phase boundary was crossed without a completed gate.
4. **Drift check (A16):** If ambiguity, tool conflict, or scope creep — pause and return to full agent-supported presentation for that step.

---

## 5) What Mode 2 does *not* mean

- Not permission to add undeclared automations or “ghost” Axx.
- Not permission to run Tier 2/3 on subagents.
- Not a guarantee that every host feature (e.g. computer use, scheduling UI) is available on the user’s plan or region — see [platform-capabilities.md](platform-capabilities.md) and the vendor’s pages.

---

## 6) References (external, read-only for wording discipline)

- [Claude CoWork (Anthropic)](https://www.anthropic.com/product/claude-cowork)
- [Cowork (claude.com)](https://claude.com/product/cowork) — plan and control language is **product-owned**
- [Computer use tool (API doc)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) — safety and consent themes for host-like automation
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — incremental progress and verification
- [Safe and trustworthy agents](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents) — human control and transparency

JAE does not claim these pages describe this repo; they inform **responsible** wording.
