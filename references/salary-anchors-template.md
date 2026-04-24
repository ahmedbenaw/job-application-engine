# Salary Anchors Template — Generic Universal Edition
# Version: 1.0.0
# Stores working salary research outputs and offer history.
# The full compensation preference model lives in applicant-profile-template.md.
# This file stores the research outputs and ground-truth offer data.

---
## Confirmed Anchors

Format: MARKET | CURRENCY | LEVEL | FLOOR | TARGET | STRETCH | NET@TARGET | TAKE-HOME | SOURCE | DATE | REFRESH

[MARKET_1] | [CURRENCY_1] | [LEVEL_RANGE] | [FLOOR] | [TARGET] | [STRETCH] | [NET] | [TAKE_HOME_%] | [SOURCE] | [DATE] | [REFRESH_DUE]

Example (Alex M., fictional):
Amsterdam, Netherlands | EUR | L3–4 | €80,000 | €92,000 | €108,000 | ~€64,400/yr | ~70% | Glassdoor NL 2025 | Mar 2025 | Sep 2025

---
## Markets Requiring Research

[MARKET_2] | [CURRENCY_2] | no anchor — run Phase 3 salary research protocol

---
## Regional Take-Home Reference Rates

Germany:      ~60–65% (Steuerklasse 1, single, no dependants)
Netherlands:  ~70% standard; ~80% if 30% ruling applies
UK:           ~65–70% (income tax + National Insurance)
UAE:          100% (no personal income tax)
Saudi Arabia: 100% for most categories
France:       ~55–62%
USA:          ~65–72% (varies significantly by state)
Switzerland:  ~75–80%

---
## Offer History Log

Format: Date | Market | Role | Company | Offered Gross | Status | Notes
Status options: Accepted | Declined | Pending | Withdrawn

(Append after each offer received, accepted, or declined)

---
## Update Protocol

After offer received, accepted, or declined: append to Offer History Log.
After new market research run: append a new Confirmed Anchor entry.
Set Refresh Due to 6 months from the source date.
Flag any anchor whose source date has passed at next session start.
