# Fit Analysis — Skill Instruction File
# Version: 1.0.0 | Nativized from Phase 2 of job-application-engine
# This file documents the inline Fit Analysis module embedded in SKILL.md.
# Read when extending or adapting Phase 2 for a new use case.

---
## Purpose

The Fit Analysis module is an adversarial gap-mapping process that runs
between the Company Intelligence phase and the Clarifying Questions intake.
Its sole output is a verdict — Clean Fit, Honest Stretch, or Mismatch —
plus a session gap statement. No application text is produced until the
verdict is returned.

## What It Replaces

This module nativizes the logic previously attributed to the RD-001 Truth
Razor adversarial reasoning agent. It operates without that agent. The
adversarial stance is achieved through the instruction to run the analysis
pessimistically rather than optimistically — mapping evidence as it exists
in the profile, not as the candidate wishes it existed.

## Execution Steps

Step 1 — Role level detection: assign a level from the Level Classification
Framework based on JD scope, reporting line, and responsibilities. Not the
title alone.

Step 2 — Requirements extraction: separate mandatory from preferred. Number
each requirement for reference in the evidence mapping.

Step 3 — Two-column evidence mapping: Column A lists direct evidence from the
profile for each requirement. Column B lists gaps for requirements not covered.
Evidence must be traceable. General claims do not qualify.

Step 4 — Compensating evidence: for every gap, identify whether related
capability offsets it. State both gap and offset — never one without the other.

Step 5 — Verdict assignment: Clean Fit / Honest Stretch / Mismatch.

Step 6 — Session gap statement: one paragraph to the session log only.
Not the applicant profile.

## Verdict Definitions

Clean Fit: all mandatory requirements covered by direct evidence from the
profile. Preferred requirements may have minor gaps.

Honest Stretch: one or two mandatory requirements have gaps that are offset
by compensating evidence. The application is viable but the gap must be named
explicitly in the cover letter and "why suitable" answer.

Mismatch: two or more mandatory requirements have gaps with no meaningful
compensating evidence. The phase halts and informs the user. No application
materials are produced.

## What Is and Is Not Acceptable Evidence

Acceptable: company name + role title + specific outcome or metric.
Not acceptable: general statements like "experienced in X" or "strong
background in Y" without a specific traceable instance.

## Example (Alex M., fictional — Honest Stretch verdict)

JD requirement: hands-on React development experience (mandatory).
Column A: Alex has managed engineering teams building React-based products
for 3 years at DataFlow GmbH, with close collaboration on component design
and UX implementation.
Column B: Alex has not written production React code independently.
Compensating evidence: Alex has shipped UI prototypes using AI-assisted
coding tools and has a demonstrated ability to work fluently in engineering
environments, understanding the constraints and patterns the role requires.
Verdict: Honest Stretch — gap must be acknowledged in the application.
Session gap statement: "The JD requires hands-on React development; Alex's
background is in managing React-based product delivery rather than writing
production code. In practice, Alex has prototyped front-end features using
AI-assisted tools and has shipped working UIs into production in close
collaboration with engineering leads."
