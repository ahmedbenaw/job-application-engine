# Hooks — job-application-engine v2.2.0

Two small hooks that enforce rules the skill already states, so a mistake can't slip through:

| Hook | When | What it does |
|---|---|---|
| `pre_upload_guard.py` | Before any tool whose name contains "upload", and before shell commands (Bash, device_bash) that send a file with curl, scp, rsync or sftp | If the file is a CV (.docx, .pdf, .doc, .rtf or .odt whose name contains CV, resume, résumé, Lebenslauf or curriculum vitae), it must match a recorded ATS Gate PASS. A CV path that can't be checked on this machine (missing, remote, `file://` that doesn't resolve) is blocked too. The check is against the job of the most recent PASS (the application in progress), so a CV passed for another job is refused, and a PASS whose job keyword list changed no longer counts. Otherwise the upload is **blocked** with a plain reason (GAP-11, invariant 15). Other uploads pass untouched. |
| `post_change_stale.py` | After Write, Edit, MultiEdit, Bash or NotebookEdit | Re-checks the fingerprints of CV files that passed. If one changed, its PASS is **cancelled** and Claude is told to re-run the gate (GATE-14). Never blocks. |

Both call `scripts/ats_gate.py` and use the state file `jae-state/gate_pass.json` (or `$JAE_STATE_DIR`). The PASS is recorded by `ats_gate.py record-pass --job [JOB_ID] --config [gate config]` at the end of Phase 3C; it re-runs the gate itself and records only a real PASS for that job.

## Where they run

- **Claude Code (plugin):** install the plugin build `job-application-engine-plugin.zip`. Its `hooks/hooks.json` loads these automatically. Restart Claude Code after installing.
- **Claude Code (settings):** copy `settings-snippet.json` into `.claude/settings.json` and replace `/ABSOLUTE/PATH/TO/` with where the skill lives.
- **Claude.ai, CoWork, Manus:** hooks don't run there. The same rules are enforced by the skill's own steps (Phase 3C freeze, Phase 6 verify-upload, invariant 15).

## Limits

- A CV is recognised by its file name. A17 always names CVs `Firstname-Lastname-CV-[Role]`, so engine-made CVs are covered; a file you rename without "CV" or "resume" in the name is not.
- Uploads made by running page scripts (JavaScript or browser "run code" tools) or by dragging with computer use are not intercepted. The skill's own rule (Phase 6 `verify-upload`, invariant 15) still applies there.

## Safety

- No network access, no credentials, no writes outside `jae-state/`.
- The upload guard only blocks CV files; every other upload is allowed.
- Remove a hook by deleting its entry from `hooks.json` (plugin) or your settings.

## Test

`python3 scripts/selftest.py` runs both hooks against sample hook input.
