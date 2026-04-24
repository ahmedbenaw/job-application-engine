# Checklist Templates — Skill Instruction File
# Version: 1.0.0 | Documents the dynamic checklist system in SKILL.md
# Read when adapting the checklist format for a new platform or use case.

---
## Purpose

The dynamic session checklist is the live progress board that the system
prints at the start of every phase and updates after each scoring gate.
It serves three functions: it keeps the user informed of session state,
it prevents the system from skipping phases silently, and it provides
placeholder structure that constrains the LLM from hallucinating values
into unfilled fields.

## Checklist Design Principles

The checklist must always reflect the actual state of the session, not
an aspirational or projected state. It is updated after each scoring gate,
not before. A phase is never marked Complete until the user has confirmed
a score of 5 for that phase.

Placeholder tokens in the checklist header ([CANDIDATE_NAME], [ROLE_TITLE],
[COMPANY_NAME]) are populated at session start from the applicant profile.
If a value is unknown at session start, the token remains visible — this is
intentional. It signals to both the user and the system that a required value
has not yet been confirmed.

## Full Checklist Template

```
╔════════════════════════════════════════════════════════════════════╗
║          JOB APPLICATION ENGINE — SESSION STATUS BOARD            ║
╠════════════════════════════════════════════════════════════════════╣
║  Phase 0 │ Job Discovery          │ [STATUS] │ Score: [ /5]       ║
║  Phase 1 │ Company Intelligence   │ [STATUS] │ Score: [ /5]       ║
║  Phase 2 │ Fit Analysis           │ [STATUS] │ Score: [ /5]       ║
║  Phase 3 │ Clarifying Intake      │ [STATUS] │ Score: [ /5]       ║
║  Phase 4 │ Application Package    │ [STATUS] │ Score: [ /5]       ║
║  Phase 5 │ Writing Quality Pass   │ [STATUS] │ Score: [ /5]       ║
║  Phase 6 │ Governance Gate        │ [STATUS] │ Score: [ /5]       ║
║  Phase 7 │ Post-Submission Loop   │ [STATUS] │ Score: [ /5]       ║
╠════════════════════════════════════════════════════════════════════╣
║  Active Phase : [PHASE_NAME]                                      ║
║  Current Gate : [GATE_DESCRIPTION]                                ║
║  Awaiting     : [WHAT_IS_NEEDED_FROM_USER]                        ║
║  Candidate    : [CANDIDATE_NAME]                                  ║
║  Session Role : [ROLE_TITLE]     Company: [COMPANY_NAME]          ║
╚════════════════════════════════════════════════════════════════════╝

Status codes:
  ⏳ Pending   — phase has not started
  🔄 Active    — phase is currently running
  🔁 Revision  — phase output scored below 5, revision in progress
  ✅ Complete  — phase scored 5, gate passed, advancing
  🚫 Blocked   — phase cannot start until a preceding gate clears
```

## Example — Mid-Session State (Alex M., fictional)

```
╔════════════════════════════════════════════════════════════════════╗
║          JOB APPLICATION ENGINE — SESSION STATUS BOARD            ║
╠════════════════════════════════════════════════════════════════════╣
║  Phase 0 │ Job Discovery          │ ✅ Complete │ Score: 5/5      ║
║  Phase 1 │ Company Intelligence   │ ✅ Complete │ Score: 5/5      ║
║  Phase 2 │ Fit Analysis           │ ✅ Complete │ Score: 5/5      ║
║  Phase 3 │ Clarifying Intake      │ 🔄 Active   │ Score: [ /5]   ║
║  Phase 4 │ Application Package    │ ⏳ Pending  │ Score: [ /5]   ║
║  Phase 5 │ Writing Quality Pass   │ ⏳ Pending  │ Score: [ /5]   ║
║  Phase 6 │ Governance Gate        │ ⏳ Pending  │ Score: [ /5]   ║
║  Phase 7 │ Post-Submission Loop   │ ⏳ Pending  │ Score: [ /5]   ║
╠════════════════════════════════════════════════════════════════════╣
║  Active Phase : Clarifying Intake                                 ║
║  Current Gate : Product trial observation (awaiting user input)   ║
║  Awaiting     : User to complete 10-min product trial and return  ║
║  Candidate    : Alex M.                                           ║
║  Session Role : Senior Product Manager   Company: CloudBase Inc   ║
╚════════════════════════════════════════════════════════════════════╝
```

## Scoring Gate Template

Print this exact format after every phase output. Do not paraphrase it.

```
── PHASE [N] REVIEW GATE ──────────────────────────────────────────
Please respond with:
  1. What was correct
  2. Your score from 1 to 5  (5 required to proceed)
  3. What you expected for a perfect result at this phase
If score < 5, state what to revise. This phase reruns before advancing.
───────────────────────────────────────────────────────────────────
```

## Revision Loop Behaviour

When a score below 5 is received:
  1. Update the phase status to 🔁 Revision in the checklist.
  2. Read the user's stated expectation for a perfect result.
  3. Revise only the elements identified — do not rerun the entire phase.
  4. Present the revised output.
  5. Present the scoring gate again.
  6. If the revised score is 5, update status to ✅ Complete and advance.
  7. If the revised score is below 5 for a second time, ask the user
     whether to continue revising or to proceed despite the lower score.
     Do not force advancement. Do not stall indefinitely.

## Platform Notes

Claude.ai: print the checklist as formatted text. It renders in monospace
where code blocks are used, which preserves the box drawing characters.

Claude CoWork: generate the checklist as a static artifact that is updated
at each gate. The artifact persists across the subagent coordination flow.

Manus: maintain the checklist as a text block in the session instruction
context. Update it in place at each gate by replacing the previous version.
