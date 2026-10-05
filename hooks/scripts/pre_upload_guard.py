#!/usr/bin/env python3
"""PreToolUse hook — job-application-engine v2.2.0 (GAP-11, invariant 15).

Blocks any upload of a CV file that is not the exact file frozen by the latest
ATS Gate PASS. Other uploads pass through untouched.

Covers upload tools (any tool name containing "upload") and shell tools (Bash,
device_bash) whose command sends a file with curl -F / -T / --upload-file /
--data-binary @, scp or rsync.

A CV file is any .docx, .pdf, .doc, .rtf or .odt whose name contains CV, resume,
résumé, Lebenslauf or "curriculum vitae" (A17 names every CV
Firstname-Lastname-CV-[Role]). A CV path that can't be checked on this machine
(missing, remote, unreadable) is blocked: unverifiable means untested.

Input: Claude Code hook JSON on stdin. Output: exit 0 to allow; exit 2 with a
plain reason on stderr to block (Claude reads the reason and re-runs the gate).
"""
import json, os, re, shlex, subprocess, sys
from urllib.parse import unquote, urlparse

GATE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "scripts", "ats_gate.py")
DOC_EXT = (".docx", ".pdf", ".doc", ".rtf", ".odt")
CV_NAME = re.compile(r"CV|(?i:(?<![a-z])(cv|resume|r[eé]sum[eé]|lebenslauf|curriculum[-_ .]?vitae)s?\d*(?![a-z]))")
SHELL_SEND = re.compile(r"\b(curl|scp|rsync|sftp)\b")

def paths_in(obj):
    """Collect file paths from any tool input shape (path, paths, files, filePath...)."""
    found = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str) and re.search(r"path|file", k, re.I):
                found.append(v)
            else:
                found += paths_in(v)
    elif isinstance(obj, list):
        for v in obj:
            found += paths_in(v) if not isinstance(v, str) else ([v] if os.path.splitext(v)[1] else [])
    return found

def paths_in_command(cmd):
    """File arguments of a shell command that sends files somewhere."""
    if not SHELL_SEND.search(cmd or ""):
        return []
    try:
        words = shlex.split(cmd)
    except ValueError:
        words = cmd.split()
    out = []
    for w in words:
        w = w.split("=", 1)[-1] if w.startswith(("file=", "-Ffile=")) else w
        w = w.lstrip("@").split(";")[0]
        if "=@" in w:
            w = w.split("=@", 1)[1]
        if w.lower().endswith(DOC_EXT):
            out.append(w)
    return out

def local_path(p, cwd):
    if p.startswith("file://"):
        p = unquote(urlparse(p).path)
    p = os.path.expanduser(p)
    if not os.path.isabs(p):
        p = os.path.join(cwd or os.getcwd(), p)
    return p

def block(reason):
    print(f"Blocked by job-application-engine: {reason} Run the ATS Gate (Phase 3C) and record the PASS before uploading.", file=sys.stderr)
    sys.exit(2)

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # not our business if the input isn't hook JSON
    tool, tin = data.get("tool_name", ""), data.get("tool_input", {}) or {}
    cand = paths_in_command(tin.get("command", "")) if re.search(r"bash", tool, re.I) else paths_in(tin)
    files = [p for p in cand if p.lower().endswith(DOC_EXT) and CV_NAME.search(os.path.basename(p))]
    for raw in files:
        f = local_path(raw, data.get("cwd"))
        if not os.path.isfile(f):
            block(f"{os.path.basename(raw)} looks like a CV but can't be checked from here (not found at {f}); an unverifiable CV counts as untested.")
        r = subprocess.run([sys.executable, GATE, "verify-upload", f], capture_output=True, text=True)
        if r.returncode != 0:
            try:
                reason = json.loads(r.stdout[r.stdout.index("{"):])["reason"]
            except Exception:
                reason = f"{os.path.basename(f)} has no matching ATS Gate PASS."
            block(reason)
    sys.exit(0)

if __name__ == "__main__":
    main()
