#!/usr/bin/env python3
"""Grade eval runs for job-application-engine with fixed, repeatable checks.

Usage:
  python3 evals/grade.py <iteration_dir>            # grades every <eval-dir>/<config>/run-*/outputs/response.md
  python3 evals/grade.py --response FILE --eval N   # grade one reply against eval N

Writes grading.json next to each run's outputs/ folder, in the format the
skill-creator benchmark and viewer read (expectations: text, passed, evidence).
Eval directories are matched to evals.json by name (e.g. "eval-1-mode-b" ↔ id 1).
"""
import argparse, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EVALS = json.load(open(os.path.join(HERE, "evals.json"), encoding="utf8"))["evals"]

def strip_code(text):
    return re.sub(r"```.*?```", "", text, flags=re.S)

def count_questions(text):
    """Questions the person must answer.

    The skill puts every question batch under a heading "Questions for you (N)".
    Count the numbered items after each such heading (until the next heading).
    If no such heading exists, count list items that contain '?' and take the
    larger of that and the highest list number in any block that asks for answers.
    """
    body = strip_code(text)
    lines = body.splitlines()
    total, found = 0, False
    for i, l in enumerate(lines):
        if re.search(r"(?i)questions for you", l):
            found = True
            for m in lines[i + 1:]:
                if re.match(r"\s*#{1,6}\s|\s*\*\*[^*]+\*\*\s*$", m) and not re.match(r"\s*\d+[.)]", m):
                    if total:
                        break
                    continue
                if re.match(r"\s*\d+[.)]\s", m):
                    total += 1
    if found:
        return total
    q = sum(1 for l in lines if re.match(r"\s*(\d+[.)]|[-*•])\s+.*\?", l))
    nums = [int(m.group(1)) for l in lines for m in [re.match(r"\s*(\d+)[.)]\s", l)] if m]
    return max(q, max(nums) if nums else 0)

def run_check(check, text, outputs_dir):
    t = check["type"]
    if t == "regex":
        m = re.search(check["pattern"], text)
        return bool(m), (f"found: {m.group(0)[:80]!r}" if m else f"pattern not found: {check['pattern']}")
    if t == "all_regex":
        missing = [p for p in check["patterns"] if not re.search(p, text)]
        return not missing, ("all patterns found" if not missing else f"missing: {missing}")
    if t == "not_regex":
        m = re.search(check["pattern"], text)
        return not m, ("not present (good)" if not m else f"found unwanted text: {m.group(0)[:80]!r}")
    if t == "max_questions":
        n = count_questions(text)
        return n <= check["max"], f"{n} questions (limit {check['max']})"
    if t == "regex_or_file":
        files = glob.glob(os.path.join(outputs_dir, "**", check["file_glob"]), recursive=True)
        m = re.search(check["pattern"], text)
        return bool(m or files), (f"file: {os.path.basename(files[0])}" if files else (f"found: {m.group(0)!r}" if m else "no evidence"))
    if t == "file_contains":
        # Evidence the bundled script ran: one of its output files carries its signature text.
        for f in glob.glob(os.path.join(outputs_dir, "**", "*"), recursive=True):
            if os.path.isfile(f) and os.path.getsize(f) < 5_000_000:
                with open(f, encoding="utf8", errors="ignore") as fh:
                    if re.search(check["pattern"], fh.read()):
                        return True, f"file: {os.path.relpath(f, outputs_dir)}"
        m = re.search(check.get("response_pattern", r"(?!x)x"), text)
        return bool(m), (f"found in reply: {m.group(0)!r}" if m else "no output file with the script's signature")
    return False, f"unknown check type {t}"

def grade_text(text, ev, outputs_dir="."):
    exp = []
    for a in ev["assertions"]:
        ok, why = run_check(a["check"], text, outputs_dir)
        exp.append({"text": a["text"], "passed": ok, "evidence": why})
    p = sum(e["passed"] for e in exp)
    return {"expectations": exp, "summary": {"passed": p, "failed": len(exp) - p, "total": len(exp), "pass_rate": round(p / len(exp), 3)}}

def eval_for_dir(name):
    m = re.match(r"eval-(\d+)", name)
    if m:
        for ev in EVALS:
            if ev["id"] == int(m.group(1)):
                return ev
    for ev in EVALS:
        if ev["name"] in name:
            return ev
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("iteration_dir", nargs="?")
    ap.add_argument("--response"); ap.add_argument("--eval", type=int)
    a = ap.parse_args()
    if a.response:
        ev = next(e for e in EVALS if e["id"] == a.eval)
        res = grade_text(open(a.response, encoding="utf8").read(), ev, os.path.dirname(a.response))
        print(json.dumps(res, indent=2, ensure_ascii=False)); sys.exit(0 if res["summary"]["failed"] == 0 else 1)
    totals = {}
    for resp in sorted(glob.glob(os.path.join(a.iteration_dir, "eval-*", "*", "run-*", "outputs", "response.md"))):
        outputs = os.path.dirname(resp); run = os.path.dirname(outputs)
        eval_dir = os.path.basename(os.path.dirname(os.path.dirname(run)))
        ev = eval_for_dir(eval_dir)
        if not ev:
            print(f"skip {resp}: no matching eval"); continue
        res = grade_text(open(resp, encoding="utf8").read(), ev, outputs)
        json.dump(res, open(os.path.join(run, "grading.json"), "w"), indent=2, ensure_ascii=False)
        cfg = os.path.basename(os.path.dirname(run))
        print(f"{eval_dir:34} {cfg:11} {res['summary']['passed']}/{res['summary']['total']}" + "".join(f"\n    FAIL {e['text']}: {e['evidence']}" for e in res["expectations"] if not e["passed"]))
        t = totals.setdefault(cfg, [0, 0]); t[0] += res["summary"]["total"]; t[1] += res["summary"]["failed"]
    print()
    for cfg, (total, failed) in sorted(totals.items(), key=lambda kv: kv[0] != "with_skill"):
        note = "  ← release bar: must be 100%" if cfg == "with_skill" else "  (comparison only)"
        print(f"{cfg:11} {total - failed}/{total} checks passed ({round(100 * (total - failed) / max(total, 1))}%){note}")
    # Only the skill under test sets the exit code; old_skill runs are a baseline.
    total, failed = totals.get("with_skill", [0, 0])
    sys.exit(0 if total and failed == 0 else 1)

if __name__ == "__main__":
    main()
