```
╔════════════════════════════════════════════════════════════════════╗
║          JOB APPLICATION ENGINE — SESSION STATUS BOARD            ║
╠════════════════════════════════════════════════════════════════════╣
║  Phase 0  │ Job Discovery           │ ✅ Skipped │ —               ║
║  Phase 1  │ Company Intelligence    │ ✅ │ M1 Score 5/5            ║
║  Phase 2  │ Fit Analysis            │ ✅ │ M2 Score 5/5            ║
║  Phase 3  │ Clarifying Intake       │ ✅ │ M3 Score 5/5            ║
║  Phase 3B │ CV Build                │ ✅ │ M4 Score 5/5            ║
║  Phase 3C │ ATS Gate                │ ✅ │ PASS, frozen            ║
║  Phase 4–5│ Package + Writing Pass  │ ✅ │ M5 Score 5/5            ║
║  Phase 6  │ Combined Final Verdict  │ 🔄 │ PASS (checks 1–9)       ║
║  Phase 7  │ Post-Submission Loop    │ ⏳ │ —                       ║
╠════════════════════════════════════════════════════════════════════╣
║  Execution mode : agent_supported   Session mode: B                ║
║  Awaiting       : APPROVE FILL (exact phrase) + 2 answers below    ║
║  Candidate      : Alex M.                                          ║
║  Role / Company : Senior Product Manager / Acme Data GmbH          ║
╚════════════════════════════════════════════════════════════════════╝
```

Browser control is active, so I can fill the form if you approve each step. "Fill it in now" isn't the approval though. Filling a live employer form is a step that can't be fully undone, so it needs the exact phrase below after you've checked the data.

Here's what I'll type, word for word.

```
── TIER 3 CONSENT GATE — BROWSER FORM FILLING ──────────────────────
  ACTION     : Fill the Acme Data GmbH application form (fill only, NO submit)
  PLATFORM   : Employer careers site
               https://jobs.example.com/acme/apply/acme-spm-2026-10
  TOOL       : browser control
  DATA       :
    [1] First name            : Alex
    [2] Last name             : M.
    [3] Email                 : alex@example.com
    [4] Phone                 : +49 151 0000000
    [5] Salary expectation    : 95000  (gross, EUR per year)
    [6] Notice period         : 3 months
    [7] "Why Acme?" (max 100 words, this answer is 40):
        Acme's open data catalogue is the product I have wanted to
        build on for two years. At DataFlow I cut onboarding time by
        40% for a similar tool, and I want to bring that
        discovery-led approach to Acme's self-serve analytics.
    [8] CV upload             : Alex-M-CV-Senior-PM.docx (main file)
                                + Alex-M-CV-Senior-PM.pdf only if the
                                form takes a second file
  TIMESTAMP  : 2026-10-05, at the moment you approve
  NOTE       : This fills the form but does NOT submit it.
               Submitting is a separate step with its own phrase.
  ⚠ Some sites don't let you fully clear a field once it's filled.

  To confirm, type exactly:  APPROVE FILL
  Type CANCEL to get the answers as paste-ready text instead.
────────────────────────────────────────────────────────────────────
```

**Before you approve: 1 blocker, 2 questions**

1. **CV file check (blocker for item 8 only).** Before any upload I check that the file is the exact one that passed the ATS Gate for this job. I ran that check, and this workspace has no saved PASS record for job `acme-spm-2026-10`. The PASS from the earlier session didn't come over with the file. Until that's fixed I won't attach any CV. The text fields [1]–[7] aren't affected. Pick one:
   - **A:** point me to the saved records folder from the earlier session (`jae-state`), and I'll check the file against it
   - **B:** I re-run the ATS Gate on the same two files and record the PASS again. The CV text doesn't change. If any check fails, I stop and tell you.
2. **Privacy or data-consent box.** You haven't told me whether you agree to the employer's privacy terms, so by default I'll leave that box for you to tick yourself. Reply **tick it** if you want me to do it.
3. **Anything not on the list.** If the form asks for something that's not in items [1]–[8] (for example a LinkedIn link, a cover letter box or a start date), I'll stop at that field and ask you. I won't make up an answer.

**What happens after APPROVE FILL**

1. I open the form. If it asks you to log in, you log in yourself. I never type or keep passwords.
2. I fill items [1]–[8] in order and stop before the Submit button.
3. I screenshot every filled page, compare it with the list above, and show you the result.
4. Once the CV is uploaded, I check the site's own preview of it (name, job titles, dates).
5. Only then do I ask for **APPROVE SUBMIT**, as a separate step.
6. If the site blocks me partway, I stop straight away and give you the remaining answers to paste.

**What you need to do now:** reply with **APPROVE FILL**, plus **A** or **B** for the CV check, plus **tick it** if you want the consent box ticked.

Nothing was filled, uploaded or submitted.
