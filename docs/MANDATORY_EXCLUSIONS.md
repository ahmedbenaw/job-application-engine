# Mandatory scope — what JAE does and does not claim

This file is **normative**. The skill must be honest about which actions are **JAE-declared** (`automation-registry.json`), which are **host-governed** (Claude, CoWork, Manus, OS), and which are **never** allowed. Silence is forbidden for commonly confused capabilities.

**Related:** [platform-capabilities.md](platform-capabilities.md), [EXECUTION_MODES.md](EXECUTION_MODES.md), [SKILL.md](../SKILL.md), [rules.json](../rules.json).  
CoWork product context (host-dependent): [Claude CoWork (Anthropic)](https://www.anthropic.com/product/claude-cowork), [Cowork (claude.com)](https://claude.com/product/cowork).

---

## A. Hard prohibited (never, regardless of user consent in chat)

- **Inventing automations:** Claiming to run an action as a JAE automation when no `Axx` entry exists in `automation-registry.json` with a matching scope.
- **Bypassing invariants** in [rules.json](../rules.json) `invariants` and `SKILL.md` non-negotiables (e.g. application text before Phase 3, hidden mismatch).
- **Hidden subagents:** Spawning or routing to agents or parallel threads not described in `SKILL.md` and `platform_routing` in [rules.json](../rules.json). CoWork Tier-1 parallelism is **read-only and skill-authored** only; **Tier 2/3 never on subagents.**
- **Irreversible actions without consent:** Submit/send/fill and other Tier 2/3 actions without the **exact** approval path defined in the skill and registry.
- **Scoring = approval:** Using a phase score, “yes,” or paraphrase as a substitute for Tier 2/3 approval phrases.
- **Credential persistence:** Storing or replaying the user’s job-platform or email credentials outside the session rules in `automation_layer`.

JAE is a **custom skill**, not a host product. It does not imply Anthropic (or any vendor) endorses this repository.

---

## B. Host-capability-gated (allowed only with host + JAE law)

These are **not** “excluded from CoWork.” They are **excluded as unsupervised or ungoverned JAE claims.** When the user opts into `cowork_autonomous` in [EXECUTION_MODES.md](EXECUTION_MODES.md) and the **host** exposes the capability, JAE may **orchestrate** work using the host’s product features **only** while:

- **Phases 0–7, scoring gates, and consent tiers remain the law of the session.**
- After each autonomous **chunk**, the skill **re-anchors** to the agent-supported workflow (current phase, checklist, invariants) per `SKILL.md` and A14–A16 in `automation-registry.json`.
- The user respects the product’s own approval UI, folder access, and plan limits (see product pages; availability is **host/plan-dependent**).

**Examples of host-governed surface (wording, not a promise of availability):** desktop/connector/automation features that the **Claude** app or CoWork exposes; computer-use-style interaction where the product provides it, subject to that product’s consent and safety model.

**JAE must not** claim to configure OS-level crons, external schedulers, or headless **unattended** jobs **as a named JAE automation** unless a future registry entry explicitly defines them.

---

## C. Registry-native (JAE must declare)

Any action presented as a **JAE-executed** automation (A01–A16, etc.) must appear in [automation-registry.json](../automation-registry.json) with **phase, tier, approval phrase, and scope boundary.** Browser automation in JAE remains **BrowserBase (primary) / Playwright (secondary)** per registry — not a separate “Chrome” vendor primitive; map host-bundled browser experiences to the Capability Map, not a forked JAE code path (see D).

If a new host feature is needed in scope, add it to the registry and `CHANGELOG.md` in a versioned release.

---

## D. Named browser products (not separate JAE primitives)

JAE does **not** branch on vendor-specific browser brand names (e.g. a particular browser) as a **distinct** execution path. The Capability Map uses **MCP and host-reported** tool status. Host marketing names for connectors are mapped to the same JAE rules.

---

## E. Unattended scheduling (strict meaning)

**JAE does not** define or trigger **timer-based, fully unattended** workflows that have **no** live user session. In-session **calendar (A10)** and host **scheduled tasks** the user sets **outside** JAE are outside this skill’s registry unless explicitly added later.

---

## Cross-references

- [EXECUTION_MODES.md](EXECUTION_MODES.md) — `agent_supported` vs `cowork_autonomous`
- [platform-capabilities.md](platform-capabilities.md)
- [SKILL.md](../SKILL.md) — Platform Execution Notes, A0, execution mode gate
- [rules.json](../rules.json) — `execution_modes`, `platform_routing`, `automation_layer`
