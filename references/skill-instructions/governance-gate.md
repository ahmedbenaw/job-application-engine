# Governance Gate — Skill Instruction File
# Version: 1.0.0 | Nativized from Phase 6 of job-application-engine
# Documents the inline Governance Gate module embedded in SKILL.md.

---
## Purpose

The Governance Gate is the final quality checkpoint before the application
package is presented to the user. It runs eight checks in sequence. Any
check that fails must be fixed before presentation. The gate does not
present packages with known open issues.

## What It Replaces

This module nativizes the QA and Governance agent logic. It operates without
that external agent. All eight checks are embedded inline and run
deterministically against the produced output.

## The Eight Checks

Check 1 — Third-party completable:
Can a third party complete this application without asking any questions?
Every required field has a confirmed value or an explicit user-facing flag
that tells them what to supply. Pass: yes. Fail: any field is ambiguous.

Check 2 — Claim traceability:
Does every factual claim in the application trace back to the applicant
profile or a Phase 3 confirmed answer? No metrics, company names, tool
names, or project outcomes appear that were not explicitly confirmed.
Pass: all claims traceable. Fail: any unconfirmed claim exists.

Check 3 — Salary format:
Is the salary field a single gross figure in the correct local currency for
the target market? Not a range expressed in prose unless the form explicitly
requires a range.
Pass: numeric value, correct currency. Fail: prose range, net figure, or
wrong currency.

Check 4 — Gap acknowledgment:
Is any gap identified as an Honest Stretch in Phase 2 acknowledged honestly
in both the cover letter and the "why suitable" answer? Not hidden in one
and acknowledged in the other. Not softened in either.
Pass: gap named in both. Fail: absent or softened in either.

Check 5 — Placeholder resolution:
Are all placeholder tokens ([CANDIDATE_NAME], [COMPANY_A], [METRIC_A], etc.)
replaced with real confirmed values, or explicitly flagged to the user for
completion before submission?
Pass: all resolved or flagged. Fail: any token remains in final output.

Check 6 — Word count:
Is the cover letter within the word limit for its submission format?
Text box: under 450 words. Online or email: under 250 words.
Document upload: under 500 words.
Pass: within limit. Fail: over limit.

Check 7 — Portfolio URL validity:
Does the portfolio field contain a properly formatted URL starting with
https:// or http://, not placeholder text, a file path, or a description
of a URL?
Pass: valid URL format. Fail: any other content.

Check 8 — Salary field type:
Does the salary field contain a numeric value in currency format (e.g.
95000 or €95,000), not a range written as prose (e.g. "between 90 and
100 thousand euros")?
Pass: numeric. Fail: prose.

## Failure Protocol

When any check fails: fix the issue immediately. Do not present the package
to the user with an open check. After fixing, re-run the failed check to
confirm it passes before presenting.

## Example Pass Report (Alex M., fictional)

Check 1: ✅ All fields have confirmed values or flags
Check 2: ✅ All claims trace to profile or Phase 3 answers
Check 3: ✅ Salary: €92,000 gross, EUR
Check 4: ✅ React gap acknowledged in para 4 and "why suitable" Q2
Check 5: ✅ All tokens resolved
Check 6: ✅ Cover letter: 387 words (text box limit: 450)
Check 7: ✅ Portfolio: https://github.com/alex-m-example
Check 8: ✅ Salary field: 92000

All 8 checks passed. Package ready to present.
