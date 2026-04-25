# Mandatory exclusions — what JAE does **not** trigger

This file is **normative**. If a capability is not listed here as **in scope** in [platform-capabilities.md](platform-capabilities.md) or in `automation-registry.json`, the skill **must not** imply the model runs it. Silence is forbidden: excluded product features are listed explicitly.

---

## 1. Unattended scheduling and background cron

**Excluded:** Timer-based, hourly/daily, or fully unattended workflows that run without a live user session.

**Why:** No automation ID in `automation-registry.json` defines unattended execution. Tier 2/3 actions require explicit in-session consent. Phase 7 calendar-related automations (e.g. A10) are **in-session, consent-gated** only.

**User outside JAE:** May use host product schedulers (Claude, CoWork, Manus, OS) manually; JAE does not configure them.

---

## 2. OS-level “computer use” (generic mouse/keyboard / arbitrary desktop apps)

**Excluded:** Undeclared OS automation, generic desktop control, or any action not expressed as a declared automation with tools/MCP named in the registry.

**Why:** Scope is locked to `automation-registry.json`. Browser paths are **BrowserBase MCP (primary)** and **Playwright MCP (secondary)** with disclosure — not open-ended “computer use.”

---

## 3. Named browser surfaces (e.g. “Claude in Chrome”) as a separate JAE primitive

**Resolution (mandatory):** JAE does **not** name or branch on vendor-specific browser products (e.g. Chrome) as a **distinct execution primitive**. Browser automation in this skill is **MCP-based** only, as declared in `SKILL.md` (A0) and `automation-registry.json` (`browser_automation`). If the host exposes browser capability through a bundled browser experience, the model maps it to **active BrowserBase/Playwright MCP** in the Capability Map — not to a separate JAE code path.

---

## 4. Hidden or undeclared subagents

**Excluded:** Spawning agents not described by platform routing. CoWork Tier 1 parallelism is **only** for read-only work as specified in `SKILL.md` and `rules.json` (`platform_routing.claude_cowork.tier_1`). Irreversible (Tier 2/3) actions **never** run on subagents.

---

## 5. Capabilities implied by marketing but not in registry

Any host feature (e.g. long-running VM jobs, generic file system sync, third-party OAuth flows not covered by listed MCPs) is **out of scope** unless added to `automation-registry.json` with tier, approval phrase, and CHANGELOG entry.

---

## Cross-references

- Canonical host behavior: [platform-capabilities.md](platform-capabilities.md)
- Skill law: [SKILL.md](../SKILL.md) — Platform Execution Notes, A0, Platform-Aware Automation Routing
- Machine-readable routing: [rules.json](../rules.json) — `platform_notes`, `platform_routing`, `automation_layer`
