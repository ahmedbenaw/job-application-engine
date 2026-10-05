#!/usr/bin/env python3
"""PostToolUse hook — job-application-engine v2.2.0 (GATE-14).

After any tool that can change files, re-check the fingerprints of every CV
file frozen by an ATS Gate PASS. A changed file cancels its PASS, and Claude is
told so it re-runs the gate. Never blocks; only informs.
"""
import json, os, subprocess, sys

GATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "scripts", "ats_gate.py")

def main():
    try:
        json.load(sys.stdin)
    except Exception:
        pass
    r = subprocess.run([sys.executable, GATE, "check-stale"], capture_output=True, text=True)
    try:
        newly = json.loads(r.stdout[r.stdout.index("{"):]).get("newly_stale", [])
    except Exception:
        newly = []
    if newly:
        names = ", ".join(f"{n['file']} (job {n['job']})" for n in newly)
        print(json.dumps({"systemMessage": f"job-application-engine: the ATS Gate PASS is cancelled for {names} because the file changed after it passed. Re-run the ATS Gate (Phase 3C) before any upload."}))
    sys.exit(0)

if __name__ == "__main__":
    main()
