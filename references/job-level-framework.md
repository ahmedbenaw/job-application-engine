# Job Level Classification Framework — Generic Universal Edition
# Version: 1.0.0 | 7-Level Framework
# Used in: Phase 0 (discovery filtering), Phase 2 (role level detection),
# Phase 3 (salary percentile selection), Phase 4 (tone and positioning).

---
## The 7 Levels

LEVEL 0 — NOVICE
  Titles:       Intern
  Scope:        Learning under supervision. No independent ownership.
  Indicators:   Fixed tasks, structured mentorship, no decision authority
  Salary band:  Stipend or entry minimum; varies widely by market and sector
  Cover tone:   Learning velocity, enthusiasm, early wins, adaptability

LEVEL 1 — ENTRY
  Titles:       Junior [Role], Associate [Role], Graduate [Role]
  Scope:        Defined tasks with guidance. Limited independent decisions.
  Indicators:   0–3 years experience, works within established processes
  Salary band:  Entry band, floor to midpoint of market range
  Cover tone:   Specific early impact, growth trajectory, initiative taken

LEVEL 2 — MID
  Titles:       [Role] (no qualifier), Associate with full responsibility
  Scope:        Independent execution on a defined scope. Some cross-
                functional collaboration.
  Indicators:   3–6 years experience, owns delivery of specific features
                or workstreams
  Salary band:  Mid-market, floor to midpoint
  Cover tone:   Delivery ownership, collaboration, measurable outcomes

LEVEL 3 — SENIOR
  Titles:       Senior [Role], Team Lead, Staff [Role]
  Scope:        Independent ownership of a product area or function. Mentors
                junior members. Influences roadmap or strategy direction.
  Indicators:   6–10 years experience, owns a domain end to end
  Salary band:  Upper-market, midpoint to 75th percentile
  Cover tone:   Track record, owned metrics, strategic influence within scope

LEVEL 4 — MANAGER
  Titles:       Manager, Principal, Group [Role]
  Scope:        Manages a team or significant product area. Owns budget or
                headcount. Accountable for team output and delivery quality.
  Indicators:   8–12 years experience, direct reports, hiring authority
  Salary band:  Management band, midpoint to 75th percentile
  Cover tone:   Team outcomes, process design, stakeholder management,
                business impact of the team's work

LEVEL 5 — DIRECTOR
  Titles:       Director, Senior Director
  Scope:        Owns a department or major product line. Sets strategy within
                a business unit. Reports to VP or C-Suite.
  Indicators:   12–18 years experience, multi-team leadership, P&L proximity
  Salary band:  Director band, 75th percentile to stretch
  Cover tone:   Business unit performance, strategic direction, org design,
                cross-functional influence

LEVEL 6 — HEAD / VP
  Titles:       Head of [Function], VP of [Function], Vice President
  Scope:        Owns an entire function across the organisation. Sets strategy.
                Hires and structures the team. Board-level visibility.
  Indicators:   15+ years experience, full function ownership
  Salary band:  VP band, 75th percentile to stretch; equity is significant
  Cover tone:   Function-level impact, market positioning, talent strategy,
                organisational outcomes, relationship with leadership

LEVEL 7 — EXECUTIVE
  Titles:       C-Suite (CPO, CTO, CEO, CFO, COO), MD, President
  Scope:        Full organisational or company-wide accountability. Owns P&L
                or equivalent. Reports to board or investors.
  Indicators:   Investor relationships, board reporting, equity ownership
  Salary band:  Executive band; equity is a primary component; custom negotiation
  Cover tone:   Vision, governance, systemic impact, market-level outcomes,
                organisation-building at scale

---
## Detection Rules

Do not rely on the title alone. Read the JD scope, reporting line, team
size, and responsibilities to assign a level.

Startup calibration: at companies under 50 people, subtract one level from
the title to estimate true scope. A "Head of Product" at a 15-person startup
is typically Level 4–5 scope. At a 500-person company, the same title is
Level 6 scope.

Enterprise calibration: at companies over 1,000 people, add one level to
the title to reflect the organisational complexity. A "Senior Product Manager"
at a 2,000-person company may carry Level 4 scope and compensation.

---
## Level-to-Strategy Mapping

Level 0–2 applications:
  Lead with: potential, learning velocity, and early wins
  Evidence: growth trajectory, initiative, specific early impact
  Salary: floor to midpoint of the market band
  Tone: enthusiastic and specific; avoid overconfidence

Level 3–4 applications:
  Lead with: delivery track record and owned outcomes
  Evidence: metrics, cross-functional collaboration, scope owned
  Salary: midpoint to 75th percentile of the market band
  Tone: direct, evidence-led, delivery-focused

Level 5–7 applications:
  Lead with: strategic impact and organisational influence
  Evidence: business unit outcomes, team-building at scale, direction-setting
  Salary: 75th percentile to stretch; equity discussion always relevant
  Tone: strategic, systems-oriented, outcome-at-scale language

---
## Self-Identification Prompt

If the user has not stated a target level before Phase 0, present this:

"Before we begin the job search, please identify your target level from the
framework below. Select your primary target and the acceptable range:

  Level 0 — Intern
  Level 1 — Junior / Entry
  Level 2 — Mid-Level
  Level 3 — Senior / Team Lead
  Level 4 — Manager / Principal
  Level 5 — Director
  Level 6 — Head / VP
  Level 7 — Executive / C-Suite

Your primary target: ___
Your acceptable range: ___ to ___

If you are unsure, describe the scope and team size of roles you are
targeting and I will assign a level."
