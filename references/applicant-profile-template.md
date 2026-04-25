# Applicant Profile Template
# Version: 1.0.0 | Generic Universal Edition
# Central source of truth for all job application sessions.
#
# HOW THIS PROFILE GETS POPULATED:
# The skill populates this file through the First-Use Setup Protocol (SKILL.md).
# Step 0 of that protocol detects and extracts from any uploaded documents or
# provided links BEFORE asking any questions manually. Provide as many of the
# following as you have — the skill will extract what it can and only ask for
# fields it could not find:
#
#   Recommended inputs (provide any combination):
#   - CV or resume as PDF or DOCX (most complete single source)
#   - LinkedIn profile public URL (linkedin.com/in/[your-handle])
#   - GitHub profile URL (github.com/[your-handle])
#   - Personal website or portfolio URL
#   - Behance, Dribbble, or other creative portfolio URL
#   - Paste your professional bio or summary directly into the chat
#
#   If you provide a CV and LinkedIn URL, most static and dynamic fields
#   can be populated automatically with zero manual typing required.
#
# HOW THIS PROFILE GETS UPDATED:
# After Phase 3 (Clarifying Intake) and after Phase 7 (Post-Submission Loop),
# the skill checks for new information that differs from the current profile
# and offers to update specific fields via APPROVE UPDATE. Updates are never
# written silently — every change requires explicit user approval.
#
# Time-sensitive fields (availability, salary anchors) are checked for
# staleness at every session start. Fields older than their review cycle
# are flagged and re-confirmed before the session proceeds.
#
# The SESSION LOG (separate from this file) holds application-specific
# outputs: gap statements, cover letter drafts, and application outcomes.
# Do not write session outputs into this profile — it holds truths only.

---
## FIELD DEPENDENCY MAP

When any dynamic field is updated, apply this cascade before the next session:

  [TARGET_SENIORITY_LEVEL] updated →
    recalculate [SALARY_TARGET] entries for each active market
    re-evaluate [POSITIONING_HEADLINE] version selection
    re-evaluate [PROFESSIONAL_SUMMARY] version selection

  [TARGET_SECTORS] updated →
    re-evaluate [KEY_EVIDENCE] project tag selection
    re-evaluate [PROFESSIONAL_SUMMARY] emphasis version

  [TOOLS_STACK] updated →
    re-evaluate [PORTFOLIO_ASSETS] relevance tags

  [AVAILABILITY] updated →
    update start date answer in all Phase 3 intakes immediately

  [LANGUAGE_PROFICIENCY] level advances →
    update any in-progress cover letters referencing that language

  Offer received or declined →
    update [SALARY_TARGET] for that market with ground-truth data
    append to excluded-companies-log.md with outcome

---
## CONFLICT RESOLUTION RULES

When two dynamic fields produce contradictory signals:

  [TARGET_SENIORITY_LEVEL] vs [SALARY_TARGET]: if the active level has no
  anchor for the target market, run salary research before Phase 4. Do not
  interpolate from a different level's anchor without noting the approximation.

  [COMPENSATION_PREFERENCES] vs company stage: if the candidate's equity
  floor exceeds what the company stage typically offers, flag this in Phase 2.
  Do not suppress the conflict.

  [AVAILABILITY] vs role start requirement: if the notice period creates a
  conflict with the role's stated start date, flag in Phase 3 before
  confirming availability. Do not commit to an impossible start date.

  [LANGUAGE_PROFICIENCY] vs role requirement: if the role requires a level
  the candidate has not reached, this is a mandatory gap in Phase 2 Column B.
  It cannot be omitted because the candidate is studying.

---
## SECTION 1 — STATIC FIELDS

Collected once at initialisation. Do not change between applications.

[CANDIDATE_NAME]: _______________
[PRIMARY_EMAIL]: _______________
[PRIMARY_PHONE]: _______________  (include country code)
[LINKEDIN_URL]: _______________
[PORTFOLIO_URL]: _______________  (GitHub, Behance, personal site, etc.)
[NATIONALITY]: _______________
[PASSPORT_COUNTRY]: _______________
[CURRENT_CITY]: _______________
[CURRENT_COUNTRY]: _______________

Education (most recent first):
  [INSTITUTION_1] | [DEGREE_1] | [GRADUATION_YEAR_1]
  [INSTITUTION_2] | [DEGREE_2] | [GRADUATION_YEAR_2]

Certifications:
  [CERTIFICATION_1]
  [CERTIFICATION_2]

Hard Geography Exclusions (never apply, never appear in results):
  [EXCLUDED_GEOGRAPHY_1]
  [EXCLUDED_GEOGRAPHY_2]

Example (Alex M., fictional):
  [CANDIDATE_NAME]: Alex M.
  [PRIMARY_EMAIL]: alex.m@example.com
  [PRIMARY_PHONE]: +49 170 000 0000
  [LINKEDIN_URL]: https://linkedin.com/in/alex-m-example
  [PORTFOLIO_URL]: https://github.com/alex-m-example
  [NATIONALITY]: German
  [CURRENT_CITY]: Berlin
  Education: TU Berlin | MSc Computer Science | 2019
  Hard Exclusions: [none specified by Alex]

---
## SECTION 2 — DYNAMIC FIELDS

Each field carries its current value(s), activation logic, and update triggers.

---
### [DYNAMIC] [POSITIONING_HEADLINE]

Multiple versions, each valid under specific conditions.

Version A — [HEADLINE_VERSION_A_LABEL] (for [APPLICABLE_LEVEL_RANGE_A]):
  [HEADLINE_TEXT_A]

Version B — [HEADLINE_VERSION_B_LABEL] (for [APPLICABLE_LEVEL_RANGE_B]):
  [HEADLINE_TEXT_B]

Version C — [HEADLINE_VERSION_C_LABEL] (for fractional/consulting roles):
  [HEADLINE_TEXT_C]

Activation: [TARGET_SENIORITY_LEVEL] from Phase 2 determines which version
is active. Fractional or consulting role type overrides to Version C.

Review cycle: quarterly, or when a major achievement changes the positioning
claim at a given level.

Update trigger: new role category requires a version that does not exist, or
a significant achievement changes the claim in an existing version.

Example (Alex M., fictional):
  Version A — Mid-level product roles (Levels 3–4):
    "Product Manager and builder with 7 years delivering SaaS products from
    discovery through launch across B2B and enterprise markets in Europe."
  Version B — Senior leadership roles (Levels 5–6):
    "Senior product leader with 7 years building and scaling product teams
    across SaaS and cloud infrastructure in European and US markets."

---
### [DYNAMIC] [PROFESSIONAL_SUMMARY]

Multiple versions, each tagged by primary emphasis.

Version — [EMPHASIS_1] (activate when JD primary requirement is [CONDITION_1]):
  [SUMMARY_TEXT_1]

Version — [EMPHASIS_2] (activate when JD primary requirement is [CONDITION_2]):
  [SUMMARY_TEXT_2]

Version — [EMPHASIS_3] (activate when JD primary requirement is [CONDITION_3]):
  [SUMMARY_TEXT_3]

Activation: the version whose emphasis best matches the JD's primary
requirement is selected, then tailored to the specific role before output.

Review cycle: quarterly, or when a project concludes with a new metric
that upgrades the strongest version.

Update trigger: a new emphasis category is needed that has no existing version.

Example (Alex M., fictional):
  Product Delivery emphasis (use for SaaS product roles):
    "Product Manager with 7 years delivering B2B SaaS products from zero.
    Runs the full lifecycle — discovery, prototyping, engineering alignment,
    and launch — with a track record of shipping products that retain users
    and drive measurable revenue growth."
  Technical Leadership emphasis (use for engineering-adjacent roles):
    "Product leader with 7 years collaborating directly with engineering teams
    on SaaS and cloud infrastructure products. Comfortable in technical
    environments, writes requirements that engineers can act on without
    clarification, and has shipped frontend features using AI-assisted tools."

---
### [DYNAMIC] [TOOLS_STACK]

Full inventory with role-type emphasis guidance.

All tools:
  [TOOL_1] — [USAGE_CONTEXT_1]
  [TOOL_2] — [USAGE_CONTEXT_2]
  [TOOL_3] — [USAGE_CONTEXT_3]

Emphasis by role type:
  [ROLE_TYPE_A]: lead with [TOOLS_SUBSET_A]
  [ROLE_TYPE_B]: lead with [TOOLS_SUBSET_B]
  [ROLE_TYPE_C]: lead with [TOOLS_SUBSET_C]

Review cycle: update when a new tool enters active use, when a tool is
retired, or when a significant build is completed with an unlisted tool.

Example (Alex M., fictional):
  All tools: Figma (daily), Jira, Confluence, PostHog, Amplitude, Cursor
    (prototyping), React (basic, AI-assisted), SQL (query-level)
  Product management roles: lead with Jira, Confluence, PostHog, Amplitude
  AI-first or builder roles: lead with Cursor, React, Figma prototyping
  Data-heavy roles: lead with Amplitude, PostHog, SQL

---
### [DYNAMIC] [KEY_EVIDENCE]

Full catalogue of career achievements available for selection. The system
selects the two or three projects that produce the strongest fit signal
for the specific JD.

Project entries follow this format:
  Company: [COMPANY_NAME]
  Period: [START_DATE] – [END_DATE]
  Role: [ROLE_TITLE]
  Context: [ONE_OR_TWO_SENTENCE_CONTEXT]
  Metrics: [METRIC_1]; [METRIC_2]
  Tags: [REQUIREMENT_TYPES_THIS_PROJECT_SUPPORTS]

[PROJECT_1]:
  Company: [COMPANY_A]
  Period: [DATE_RANGE_A]
  Role: [ROLE_AT_A]
  Context: [CONTEXT_A]
  Metrics: [METRICS_A]
  Tags: [TAGS_A]

[PROJECT_2]:
  Company: [COMPANY_B]
  Period: [DATE_RANGE_B]
  Role: [ROLE_AT_B]
  Context: [CONTEXT_B]
  Metrics: [METRICS_B]
  Tags: [TAGS_B]

Activation: select projects whose tags most closely match the JD's mandatory
requirements from Phase 2. Maximum three per application. Prioritise
projects with specific metrics over those without.

Review cycle: update when a project concludes with confirmed metrics, or
when a better metric becomes available for an existing project.

Example (Alex M., fictional):
  Company: DataFlow GmbH
  Period: Jan 2023 – Aug 2024
  Role: Senior Product Manager
  Context: Led product strategy for a B2B SaaS analytics platform serving
    mid-market finance teams. Owned the full roadmap from discovery to
    launch across three concurrent initiatives.
  Metrics: 18% churn reduction in 6 months; 3 features shipped ahead of
    schedule; NPS improved from 32 to 47 over 12 months
  Tags: [saas] [b2b] [product_delivery] [roadmap_ownership] [user_research]
    [churn_reduction] [cross_functional]

---
### [DYNAMIC] [LANGUAGE_PROFICIENCY]

[LANGUAGE_1]: [LEVEL_1]  (e.g. Native, C2, B2, A2)
[LANGUAGE_2]: [LEVEL_2]
[LANGUAGE_3]: [LEVEL_3]  (note if actively studying)

Activation: foreground the language most relevant to the target company's
location and the JD's language requirements.

Review cycle: update immediately when a proficiency level advances or a
certification is completed.

Example (Alex M., fictional):
  German: Native
  English: C1 professional proficiency
  French: B1, conversational

---
### [DYNAMIC] [AVAILABILITY]

Current status: [AVAILABLE_DATE] from offer. [NOTICE_PERIOD_OR_NONE].

This field decays quickly. Confirm at the start of every new session.
Do not use a value more than 2 weeks old without re-confirming with the user.

Activation: used directly in Phase 3 start date answer.

Update trigger: immediately when an engagement begins or ends, or when a
contractual notice period changes.

Example (Alex M., fictional):
  Available: within 4 weeks of offer. Currently employed, 4-week notice
  period per contract. Earliest start: 30 days from offer date.

---
### [DYNAMIC] [RELOCATION_STATUS]

Open to relocation: [YES/NO/CONDITIONAL]

Preferred cities (rank highest in discovery):
  [CITY_1], [CITY_2], [CITY_3]

Acceptable cities or regions:
  [ACCEPTABLE_REGION_1]

Hard exclusions (never apply):
  [EXCLUDED_CITY_OR_COUNTRY_1]

In-office tolerance: up to [MAX_DAYS_PER_WEEK] days per week acceptable.

Visa and work authorisation:
  [CURRENT_AUTHORISATION_STATUS]
  [ACTIVE_APPLICATIONS_IF_ANY]

Review cycle: update when visa status changes, when a city is added or
removed from preferences, or when personal circumstances change.

Example (Alex M., fictional):
  Open to relocation: Yes
  Preferred: Amsterdam, Berlin, Zurich
  Acceptable: any major Western European tech hub
  Hard exclusions: none
  In-office tolerance: up to 3 days per week
  Visa status: German citizen, no restrictions in EU/EEA

---
### [DYNAMIC] [COMPENSATION_PREFERENCES]

Full-time employment — by company stage:
  Seed / Pre-seed: base floor [SEED_BASE_FLOOR]; equity [SEED_EQUITY_RANGE]
  Series A–C:      base target [SERIES_A_C_BASE]; equity [SERIES_A_C_EQUITY]
  Scale-up / Enterprise: full market-rate base; bonus [BONUS_RANGE]

Fractional or consulting:
  Day rate target: [DAY_RATE_TARGET] (derived from FTE annual ÷ 220 × 1.4)
  Currency: [DAY_RATE_CURRENCY]

Equity preferences:
  Preferred instrument: [EQUITY_INSTRUMENT]  (options / RSUs / warrants)
  Minimum vesting schedule: [VESTING_YEARS] years
  Minimum cliff: [CLIFF_MONTHS] months
  Equity floor (meaningful threshold): [EQUITY_FLOOR_PERCENT]%
  Strike price: must be disclosed before offer acceptance

Non-cash compensation priority order:
  1. Equity (as above)
  2. [BENEFIT_2]
  3. [BENEFIT_3]
  4. [BENEFIT_4]
  5. [BENEFIT_5]

Conflict rule: if compensation model conflicts with role structure (e.g.
no equity at seed stage), flag in Phase 2 before producing application.

Review cycle: quarterly, or when personal financial priorities change,
or when offer data calibrates the model.

Example (Alex M., fictional):
  Seed: base floor €70K; equity 0.5%–1.5%, 4yr vest, 1yr cliff
  Series A–C: base target €90K; equity 0.1%–0.3%, standard vest
  Enterprise: full market-rate; equity welcome not required
  Day rate: €550/day for fractional engagements
  Equity floor: 0.1% at Series A or later is the minimum meaningful grant
  Priority benefits: equity, remote flexibility, development budget

---
## SECTION 3 — SALARY ARCHITECTURE

### Market Entry Format
Market | Currency | Level | Floor | Target | Stretch | Net@Target | Rate | Source | Date | Refresh

### Confirmed Entries
[MARKET_1] | [CURRENCY_1] | [LEVEL_RANGE_1] | [FLOOR_1] | [TARGET_1] | [STRETCH_1] | [NET_1] | [TAKE_HOME_RATE_1] | [SOURCE_1] | [SOURCE_DATE_1] | [REFRESH_DUE_1]

Example (Alex M., fictional):
  Amsterdam | EUR | L3–4 | €80,000 | €92,000 | €108,000 | ~€64K/yr | ~70% | Glassdoor NL 2025 | Mar 2025 | Sep 2025

### Markets Requiring Research
[MARKET_2] | [CURRENCY_2] | anchor needed — run Phase 3 salary protocol
[MARKET_3] | [CURRENCY_3] | anchor needed — run Phase 3 salary protocol

### Regional Take-Home Reference Rates
Germany:      ~60–65%
Netherlands:  ~70% standard; ~80% with 30% ruling
UK:           ~65–70%
UAE:          100% (no income tax)
Saudi Arabia: 100% for most categories
France:       ~55–62%
USA:          ~65–72% (varies by state)
Switzerland:  ~75–80%

### Multi-Currency Handling
When compensation is split across currencies: store both figures separately.
Flag exchange rate risk as a user decision point. Do not convert on behalf
of the user. Note the exposure and ask whether to factor it into negotiation.

### Salary Architecture Update Triggers
Refresh any market entry when:
  Six months elapsed since source date (flag at next session start)
  Offer received in that market (record offered figure and outcome)
  Target seniority level changes (re-run research for new level range)
  Significant macroeconomic event affects target market
  Role is fractional (switch to day rate: annual ÷ 220 × 1.4)

### Offer History Log
Format: Date | Market | Role | Company | Offered Gross | Status | Notes
(append after each offer received, accepted, or declined)

---
## SECTION 4 — PORTFOLIO AND WORK SAMPLES

[ASSET_1]:
  URL: [URL_1]
  Contains: [DESCRIPTION_1]
  Best for: [ROLE_TYPES_1]

[ASSET_2]:
  URL: [URL_2]  (or "available on request")
  Contains: [DESCRIPTION_2]
  Best for: [ROLE_TYPES_2]

Review cycle: update when a new asset is created, when a link becomes stale,
or when an existing asset is updated with a better outcome.

Example (Alex M., fictional):
  GitHub: https://github.com/alex-m-example
    Contains: product analytics dashboards, AI-assisted feature prototypes,
    internal tooling scripts. Best for: AI-first roles, engineering-adjacent.
  Figma portfolio: available on request
    Contains: SaaS onboarding flows, mobile UX redesigns, design system docs.
    Best for: product management, UX-adjacent roles.

---
## SECTION 5 — SECTOR AND INDUSTRY POSITIONING

Active sectors (targeted, with supporting project evidence):
  [SECTOR_1]: [PROJECT_NAMES_SUPPORTING_SECTOR_1]
  [SECTOR_2]: [PROJECT_NAMES_SUPPORTING_SECTOR_2]

Secondary sectors (experience exists, not primary target):
  [SECONDARY_SECTOR_1]: [BRIEF_EVIDENCE]

Excluded sectors: [EXCLUDED_SECTOR_OR_NONE]

Review cycle: update when a new sector is first targeted or when a project
produces a significant new metric in an existing sector.

---
## SECTION 6 — TARGET SENIORITY LEVEL

Primary target: Level [PRIMARY_LEVEL] ([LEVEL_NAME]) at [COMPANY_TYPE]
Acceptable range: Level [MIN_LEVEL] to Level [MAX_LEVEL]

Startup calibration note: see SKILL.md Level Classification Framework.
A Level 4 title at a 500-person company and a Level 6 title at a 15-person
startup may describe the same scope of responsibility.

Conflict rule: if the system detects a persistent pattern of applying to
roles more than one level above or below the stated target, flag this to
the user before Phase 4 and ask whether to recalibrate.

Review cycle: quarterly, or following a significant achievement that
justifies targeting a higher level.

---
## SECTION 7 — SCHEDULED REVIEW CYCLES

Real-time (within 48 hours of any change):
  [AVAILABILITY]

Per-application (generate fresh, store to session log only):
  Active gap statement | Cover letter | Custom question answers

Monthly:
  [PORTFOLIO_URLS] — check for stale links

Quarterly:
  [POSITIONING_HEADLINE] | [PROFESSIONAL_SUMMARY] | [COMPENSATION_PREFERENCES]
  [TARGET_SENIORITY_LEVEL] assessment

Every 6 months:
  [SALARY_ARCHITECTURE] entries | [TOOLS_STACK] | [SECTOR_TARGETING]

Annually or on event:
  [LANGUAGE_PROFICIENCY] | Education | [RELOCATION_STATUS] | [KEY_EVIDENCE]

On offer received or declined:
  [SALARY_ARCHITECTURE] for that market (ground-truth calibration)
  excluded-companies-log.md (append outcome)
