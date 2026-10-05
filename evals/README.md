# Evals — job-application-engine v2.2.0

6 test cases with fixed, repeatable checks (`evals.json`), fixture files (`fixtures/`), a grader (`grade.py`) and the replies from the last release run (`results/latest/`).

| # | Test | What it proves |
|---|---|---|
| 1 | CV + job ad, new person | Mode B, extraction first, small first batch of questions, new phases on the board, nothing written early |
| 2 | Flawed CV file through the ATS test | The gate finds every planted problem and refuses to send |
| 3 | Student with no CV | First-job path, no invented experience, discovery, local context, small first batch |
| 4 | Job page that won't load | The fallback ladder (browser → computer use → vision → paste) keeps the work going |
| 5 | Form filling, browser control inactive | Gives answers to paste; promises nothing it can't do |
| 6 | Form filling, browser control active | Offers "I can fill the form if you approve each step", previews, asks for APPROVE FILL, checks the tested CV |

Every test also checks capability wording: no browser or app brand names and never "on your computer". Tests 5 and 6 carry a `session_capabilities` line: give it to the runner as the session's A0 Capability Map.

## Run

1. For each eval, run the skill on the prompt with its fixture files (one fresh session or subagent each). Save the reply to `<workspace>/iteration-N/eval-<id>-<name>/with_skill/run-1/outputs/response.md`.
2. Grade: `python3 evals/grade.py <workspace>/iteration-N`. It exits 0 only when every `with_skill` check passes. Runs of the previous version (any other folder name, e.g. `old_skill`) are shown for comparison and never change the exit code.
3. Optional viewer: skill-creator's `aggregate_benchmark` and `eval-viewer/generate_review.py` read the `grading.json` files this writes.

The pass bar for a release is 100% of checks.

## Before a release

1. `python3 scripts/selftest.py` → must print every check as PASS (90/90 at v2.2.0; the count grows as regression checks are added).
2. Run all 6 evals on the final build and grade → `with_skill` must be 100%. Copy each `with_skill` reply to `results/latest/eval-<id>-<name>.md`; the self-test scans them (or scan a fresh run with `python3 scripts/selftest.py --replies <iteration dir>`).
3. A bug found by a test run gets fixed, gets a regression check in `scripts/selftest.py`, and its eval is run again.

Last release run (v2.2.0): with_skill 40/40 (100%), v2.1.1 24/40 (60%).
