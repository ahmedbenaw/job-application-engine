# Job Board Access Playbook
# Automation ID: A01, A02
# Version: 2.0.0 | Part of job-application-engine automation layer
# Consent tier: 1 (read-only — no separate gate required)

---
## Purpose

Covers all strategies for accessing job listings, fetching full job
descriptions, and navigating job board search results as part of Phase 0
(Job Discovery) and Phase 1 (Company Intelligence). All actions in this
playbook are Tier 1 — they execute inline as part of the phase workflow
without a separate consent gate.

---
## Platform Access Strategies

### High-Reliability Platforms (direct fetch works)

GREENHOUSE (boards.greenhouse.io)
  Search: web_search `site:boards.greenhouse.io [ROLE_TITLE] [SECTOR]`
  Fetch: web_fetch the full URL — renders completely without JavaScript
  Form: append nothing — fetch the posting URL directly for full JD content
  Reliability: high

LEVER (jobs.lever.co)
  Search: web_search `site:jobs.lever.co [ROLE_TITLE] [CITY]`
  Fetch: web_fetch the full URL — renders completely
  Reliability: high

BREEZY HR (breezy.hr)
  Search: web_search `site:breezy.hr [ROLE_TITLE]`
  Fetch: web_fetch the posting URL — full JD accessible
  Custom questions: render client-side — flagging to user required
  Reliability: high for JD content, limited for form questions

WELLFOUND / ANGELLIST (wellfound.com)
  Search: web_search `site:wellfound.com jobs [ROLE_TITLE] [CITY]`
  Fetch: web_fetch for public listings — renders JD
  Reliability: medium — some pages require JavaScript rendering

RELOCATE.ME (relocate.me)
  Search: web_search `site:relocate.me [ROLE_TITLE]`
  Fetch: web_fetch — renders listing content
  Note: prioritise this platform for relocation roles
  Reliability: high

EUROTECHJOBS (eurotechjobs.com)
  Search: web_search `site:eurotechjobs.com [ROLE_TITLE]`
  Fetch: web_fetch — renders listing
  Reliability: high

REMOTEOK (remoteok.com)
  Search: web_search `site:remoteok.com [ROLE_TITLE]`
  Fetch: web_fetch — renders listing
  Reliability: medium

WELCOME TO THE JUNGLE / OTTA (welcometothejungle.com)
  Search: web_search `site:welcometothejungle.com [ROLE_TITLE]`
  Fetch: web_fetch — renders partial content
  Reliability: medium

---
### High Bot-Detection Platforms (search results only — no direct fetch)

LINKEDIN (linkedin.com/jobs)
  Strategy: web_search `site:linkedin.com/jobs [ROLE_TITLE] [CITY]`
  Fetch: do NOT attempt direct job listing fetch — LinkedIn blocks non-auth
  Result: use search snippets only for discovery; direct the user to open
    the full listing in their browser if needed
  Reliability: low for direct fetch; high for search discovery

INDEED (indeed.com)
  Strategy: web_search `site:indeed.com [ROLE_TITLE] [CITY]`
  Fetch: do NOT attempt direct fetch for job listings — often blocked
  Result: use search snippets for discovery; direct user to open in browser
  Reliability: low for direct fetch; high for search discovery

---
## Search Query Construction

Pass 1 queries anchor on the most recent or stated target role:
  Format: "[ROLE_TITLE]" [CITY_OR_REGION] relocation visa sponsorship [SECTOR]
  Example: "Product Manager" Berlin relocation visa sponsorship SaaS

Pass 2 queries broaden to CV-fit:
  Format: [PRIMARY_SKILL] [SECONDARY_SKILL] [SECTOR] [REGION] relocation
  Example: product management 0-to-1 SaaS Europe relocation visa

Always append current year to search queries for freshness:
  Example: "Senior Product Manager" Berlin relocation 2026

---
## Full Posting Fetch for Top 5 (A02)

After the ranked discovery table is scored at 5, offer to fetch full JD
content for the top 5 flagged results automatically.

Execution:
  For each of the top 5 URLs, run web_fetch in sequence.
  If a platform blocks the fetch, note it and skip to the next.
  Present fetched content as expandable summaries — not full dumps.
  Highlight: role title, mandatory requirements, preferred requirements,
    application deadline if visible, hiring manager name if visible.

Output format per posting:
  [RANK]. [COMPANY] — [ROLE_TITLE] — [LOCATION]
  Mandatory requirements: [extracted list]
  Preferred requirements: [extracted list]
  Application deadline: [if found]
  Hiring contact: [if found]
  Full JD: [available on request]

---
## Exclusion Filter Application

Before presenting any result, check company HQ against the hard exclusion
list in the applicant profile [HARD_EXCLUSION_GEOGRAPHIES].
Remove all excluded companies from the results table before presenting.
Log each excluded company to references/excluded-companies-log.md.
Never present an excluded company even if the role is highly relevant.
