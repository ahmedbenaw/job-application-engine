#!/usr/bin/env python3
"""Self-test harness for job-application-engine v2.2.0.

Run before every release:  python3 scripts/selftest.py
Exit 0 = every check passed. Each line prints PASS or FAIL with a reason.

Checks:
  1. Structure   SKILL.md frontmatter, every file SKILL.md points to exists, JSON files load,
                 automations A01–A18 in order, 19 invariants, version numbers agree.
  2. ATS Gate    the clean fixture CV passes; the flawed fixture fails for the planted reasons.
  3. PASS state  record-pass → verify-upload → edit → check-stale → verify-upload blocks.
  4. Hooks       upload guard allows the tested file, blocks an untested CV, ignores non-CV files;
                 the change hook cancels a PASS after an edit.
  5. Evals       evals.json loads, every fixture exists, the grader runs.
"""
import glob, json, os, re, shutil, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GATE = os.path.join(ROOT, "scripts", "ats_gate.py")
FIX = os.path.join(ROOT, "evals", "fixtures")
results = []

def check(name, ok, why=""):
    results.append(ok)
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f" — {why}" if why and not ok else ""))

def run(args, env=None, stdin=None, cwd=None):
    return subprocess.run([sys.executable, *args], capture_output=True, text=True, env=env, input=stdin, cwd=cwd)

def json_tail(out):
    try:
        return json.loads(out[out.index("{"):])
    except Exception:
        return {}

# 1. Structure ---------------------------------------------------------------
def unquote(v):
    """A YAML scalar's value: 'x', "x" and x are the same (installers may add quotes)."""
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        v = v[1:-1]
    return v

def frontmatter(text):
    """(raw block, top-level values, metadata values) read as values, not as raw text."""
    m = re.match(r"\ufeff?---\r?\n(.*?)\r?\n---\s*(\r?\n|$)", text, re.S)
    raw = m.group(1) if m else ""
    top, meta, in_meta = {}, {}, False
    for line in raw.splitlines():
        t = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if t:
            top[t.group(1)] = unquote(t.group(2)) if t.group(2).strip() else ""
            in_meta = t.group(1) == "metadata"
            continue
        n = re.match(r"^\s+([A-Za-z_][\w-]*):\s*(.*)$", line)
        if in_meta and n:
            meta[n.group(1)] = unquote(n.group(2))
    return raw, top, meta

skill = open(os.path.join(ROOT, "SKILL.md"), encoding="utf8").read()
fm, fm_top, fm_meta = frontmatter(skill)
for sample in ('---\nname: "job-application-engine"\nmetadata:\n  version: \'2.2.0\'\n---\n',
               "---\nname: 'job-application-engine'\nmetadata:\n  version: \"2.2.0\"\n---\n",
               "---\nname: job-application-engine\nmetadata:\n  version: 2.2.0\n---\n"):
    _, t_, m_ = frontmatter(sample)
    if not (t_.get("name") == "job-application-engine" and m_.get("version") == "2.2.0"):
        break
check("quoted and unquoted name/version read the same (installers add quotes)", t_.get("name") == "job-application-engine" and m_.get("version") == "2.2.0")
check("frontmatter has name and description", fm_top.get("name") == "job-application-engine" and bool(fm_top.get("description")),
      f"name={fm_top.get('name')!r}")
keys = set(re.findall(r"^([a-z_-]+):", fm, re.M))
allowed = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
check("frontmatter uses only allowed top-level keys", keys <= allowed, f"extra: {sorted(keys - allowed)}")
refs = set(re.findall(r"`((?:references|scripts|docs|evals|hooks)/[^`*\s]+)`", skill))
missing = [r for r in refs if not os.path.exists(os.path.join(ROOT, r))]
check(f"all {len(refs)} files named in SKILL.md exist", not missing, f"missing: {missing}")
try:
    rules = json.load(open(os.path.join(ROOT, "rules.json"), encoding="utf8"))
    reg = json.load(open(os.path.join(ROOT, "automation-registry.json"), encoding="utf8"))
    check("rules.json and automation-registry.json load", True)
    ids = [a["id"] for a in reg["automations"]]
    check("automations A01–A18 present in order", ids == [f"A{i:02d}" for i in range(1, 19)], f"got {ids}")
    check("19 invariants in rules.json", len(rules["invariants"]) == 19, f"got {len(rules['invariants'])}")
    v = fm_meta.get("version") or fm_top.get("version")
    al = rules.get("automation_layer", {}).get("version")
    check("versions agree (SKILL.md, rules.json skill + automation_layer, registry)",
          v == rules["skill"]["version"] == al == reg["registry_version"],
          f"{v} / {rules['skill']['version']} / {al} / {reg['registry_version']}")
except Exception as e:
    check("rules.json and automation-registry.json load", False, str(e))
# docs/MANDATORY_EXCLUSIONS.md section D: no vendor browser brand as a JAE execution path
brand_hits = []
for base in ("SKILL.md", "rules.json", "automation-registry.json"):
    brand_hits += [base] if re.search(r"(?i)chrome", open(os.path.join(ROOT, base), encoding="utf8").read()) else []
for f in glob.glob(os.path.join(ROOT, "references", "**", "*.md"), recursive=True):
    if re.search(r"(?i)chrome", open(f, encoding="utf8").read()):
        brand_hits.append(os.path.relpath(f, ROOT))
check("no vendor browser brand names in skill files (MANDATORY_EXCLUSIONS D)", not brand_hits, f"found in {brand_hits}")
n_inv = len(re.findall(r"^\d+\. (Never|Always)", skill, re.M))
check("SKILL.md lists 19 invariants", n_inv == 19, f"got {n_inv}")

# 2. ATS Gate ------------------------------------------------------------------
r = run([GATE, "all", "gate_config_good.json"], cwd=FIX)
check("clean fixture CV passes the gate", r.returncode == 0 and "5/5" in r.stdout.splitlines()[0], r.stdout.splitlines()[0] if r.stdout else r.stderr[-200:])
r = run([GATE, "all", "gate_config_bad.json"], cwd=FIX)
rep = json_tail(r.stdout).get("files", {}).get("Alex-M-CV-Senior-PM.docx", {})
planted = {
    "table": rep.get("lint", {}).get("tables", 0) > 0,
    "header text": rep.get("lint", {}).get("header_footer_text") is True,
    "tool name as author": rep.get("lint", {}).get("properties_need_fixing") is True,
    "pronoun": bool(rep.get("hygiene", {}).get("pronouns")),
    "placeholders": bool(rep.get("hygiene", {}).get("placeholders")),
    "missing must-have": "Kubernetes" in rep.get("coverage", {}).get("missing_must", []),
}
check("flawed fixture fails the gate", r.returncode == 1)
for k, ok in planted.items():
    check(f"gate finds planted problem: {k}", ok)

# 2b. Regression checks for bugs found in eval runs -------------------------
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import ats_gate  # noqa: E402
import zipfile  # noqa: E402

def variant(dst, edit):
    """Copy the clean fixture DOCX and change its document.xml with edit(xml) -> xml."""
    with zipfile.ZipFile(os.path.join(FIX, "good_cv.docx")) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = edit(data.decode("utf8")).encode("utf8")
            zout.writestr(item, data)
    return dst

reg = tempfile.mkdtemp(prefix="jae-reg-")
amp = variant(os.path.join(reg, "amp.docx"), lambda x: x.replace("<w:t>Summary</w:t>", "<w:t>Summary P&amp;L</w:t>", 1))
check("reader decodes XML entities (P&L, not P&amp;L)", "P&L" in ats_gate.docx_plain(amp) and "&amp;" not in ats_gate.docx_plain(amp))
check("coverage counts a term with &", ats_gate.check_coverage(ats_gate.docx_plain(amp), [{"term": "P&L", "must": True}])["pass"])
white = variant(os.path.join(reg, "white.docx"), lambda x: x.replace("<w:r><w:t>Summary</w:t>", '<w:r><w:rPr><w:rFonts w:ascii="Comic Sans MS" w:hAnsi="Comic Sans MS"/><w:color w:val="FFFFFF"/></w:rPr><w:t>Summary</w:t>', 1))
lw = ats_gate.check_lint(white, ["Calibri", "Arial"], 2)
check("lint fails white text", lw["white_or_tiny_text"] and not lw["pass"])
check("lint fails a font outside the allowed list", "Comic Sans MS" in lw["fonts_outside_allowed"])
check("lint reads fonts set through styles, not only runs", "Calibri" in ats_gate.check_lint(os.path.join(FIX, "good_cv.docx"), [], 2)["fonts"])
cfg_nokw = os.path.join(reg, "nokw.json")
with open(cfg_nokw, "w") as f:
    json.dump({"files": [os.path.join(FIX, "good_cv.docx")], "expected": {"name": "Alex M.", "email": "alex@example.com"}}, f)
check("missing keyword list stops the gate (GATE-01)", run([GATE, "all", cfg_nokw]).returncode == 2)
check("verdict always agrees with the grade",
      [ats_gate.verdict_for(0, 5), ats_gate.verdict_for(0, 4), ats_gate.verdict_for(0, 3), ats_gate.verdict_for(1, 2)]
      == ["PASS", "PASS WITH WAIVERS", "PASS WITH WAIVERS", "FAIL"])
check("empty keyword list never counts as full coverage", not ats_gate.check_coverage("text", [])["pass"])
hy = run([GATE, "hygiene", os.path.join(FIX, "Alex-M-CV-Senior-PM.docx"), "--headings", "Summary,Skills,Experience,Education"])
check("hygiene command checks headings when given", "Skills" in json_tail(hy.stdout).get("duplicate_headings", []))
check("duplicate heading is flagged", "Skills" in (rep.get("hygiene", {}).get("duplicate_headings") or []))
hyg = ats_gate.check_hygiene("Built I/O pipeline for Phase I rollout. I led the team.")
check("pronoun check ignores I/O and Phase I but finds 'I led'", hyg["pronouns"] == ["I"] and
      not ats_gate.check_hygiene("Built I/O pipeline for Phase I rollout.")["pronouns"])
cfg_big = os.path.join(reg, "big.json")
good_cfg = json.load(open(os.path.join(FIX, "gate_config_good.json")))
good_cfg.update({"files": [os.path.join(FIX, "good_cv.docx")], "max_mb": 0.001, "original_text": os.path.join(FIX, "original_cv.txt"),
                 "approved_text": os.path.join(FIX, "approved_cv.txt")})
with open(cfg_big, "w") as f:
    json.dump(good_cfg, f)
big = run([GATE, "all", cfg_big])
check("file over the size limit is Should-level: 4/5, PASS WITH WAIVERS, exit 0",
      big.returncode == 0 and "4/5" in big.stdout.splitlines()[0] and json_tail(big.stdout).get("verdict") == "PASS WITH WAIVERS")
# Hardening checks from the adversarial review (each was a confirmed bypass before the fix)
def variant2(dst, edit=None, add=None):
    """Copy the clean fixture and edit any parts: edit={name: fn(str)->str}, add={name: str}."""
    edit, add = edit or {}, add or {}
    with zipfile.ZipFile(os.path.join(FIX, "good_cv.docx")) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename in edit:
                data = edit[item.filename](data.decode("utf8")).encode("utf8")
            zout.writestr(item, data)
        for name, text in add.items():
            zout.writestr(name, text)
    return dst
TBL = '<w:tbl><w:tr><w:tc><w:p><w:r><w:t>T</w:t></w:r></w:p></w:tc></w:tr></w:tbl>'
def body_add(xml, snippet):
    return xml.replace("<w:sectPr", snippet + "<w:sectPr", 1) if "<w:sectPr" in xml else xml.replace("</w:body>", snippet + "</w:body>", 1)
def to_x(xml):
    xml = xml.replace("xmlns:w=", "xmlns:x=")
    xml = re.sub(r"(</?)w:", r"\1x:", xml)
    return re.sub(r"(\s)w:(?=[\w-]+=)", r"\1x:", xml)
L = lambda f: ats_gate.check_lint(f, ["Calibri", "Arial"], 2)
px = variant2(os.path.join(reg, "prefix.docx"), {"word/document.xml": lambda x: to_x(body_add(x, TBL))})
check("renamed XML prefix can't hide a table", L(px)["tables"] == 1 and not L(px)["pass"])
decoy_doc = lambda x: x.replace("<w:t>Summary</w:t>", "<w:t>I led the team at [Company Name] TBD</w:t>", 1)
with zipfile.ZipFile(os.path.join(FIX, "good_cv.docx")) as z:
    real = decoy_doc(z.read("word/document.xml").decode("utf8"))
    wrels = z.read("word/_rels/document.xml.rels").decode("utf8") if "word/_rels/document.xml.rels" in z.namelist() else None
dc = variant2(os.path.join(reg, "decoy.docx"),
              {"_rels/.rels": lambda x: x.replace("word/document.xml", "word/real.xml"),
               "[Content_Types].xml": lambda x: x.replace('PartName="/word/document.xml"', 'PartName="/word/real.xml"')},
              dict({"word/real.xml": real}, **({"word/_rels/real.xml.rels": wrels} if wrels else {})))
check("a decoy document part can't hide the real one", "TBD" in ats_gate.check_hygiene(ats_gate.docx_plain(dc))["placeholders"])
ac = variant2(os.path.join(reg, "altchunk.docx"), {"word/document.xml": lambda x: body_add(x, '<w:altChunk r:id="rIdX"/>')})
check("embedded documents (altChunk) fail lint", L(ac)["embedded_documents"] == 1 and not L(ac)["pass"])
hr = variant2(os.path.join(reg, "hdr.docx"), add={"word/pagetop.xml": '<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:r><w:t>alex@example.com</w:t></w:r></w:p></w:hdr>'})
check("header text is found whatever the part is called", L(hr)["header_footer_text"])
hi = variant2(os.path.join(reg, "hdrimg.docx"), add={"word/header9.xml": '<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:p><w:r><w:drawing/></w:r></w:p></w:hdr>'})
check("images in a header are counted", L(hi)["images"] >= 1)
cm = variant2(os.path.join(reg, "remarks.docx"), add={"word/remarks.xml": '<w:comments xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:comment w:id="0"><w:p><w:r><w:t>note</w:t></w:r></w:p></w:comment></w:comments>'})
check("comments are found whatever the part is called", L(cm)["comments"])
inh = variant2(os.path.join(reg, "basedon.docx"),
               {"word/styles.xml": lambda x: x.replace("</w:styles>", '<w:style w:type="paragraph" w:styleId="Par"><w:rPr><w:rFonts w:ascii="DejaVu Serif" w:hAnsi="DejaVu Serif"/><w:sz w:val="6"/></w:rPr></w:style><w:style w:type="paragraph" w:styleId="Kid"><w:basedOn w:val="Par"/></w:style></w:styles>'),
                "word/document.xml": lambda x: x.replace("<w:p><w:r><w:t>Summary</w:t>", '<w:p><w:pPr><w:pStyle w:val="Kid"/></w:pPr><w:r><w:t>Summary</w:t>', 1)})
li = L(inh)
check("fonts and sizes inherited through basedOn are checked", "DejaVu Serif" in li["fonts_outside_allowed"] and li["white_or_tiny_text"])
fr = variant2(os.path.join(reg, "frame.docx"), {"word/document.xml": lambda x: x.replace("<w:p><w:r><w:t>Summary</w:t>", '<w:p><w:pPr><w:framePr w:w="2000" w:hAnchor="page"/></w:pPr><w:r><w:t>Summary</w:t>', 1)})
check("floating frames count as text boxes", L(fr)["text_boxes"] >= 1)
mv = variant2(os.path.join(reg, "move.docx"), {"word/document.xml": lambda x: x.replace("<w:r><w:t>Summary</w:t></w:r>", '<w:moveFrom w:id="1" w:author="a"><w:r><w:t>Summary</w:t></w:r></w:moveFrom>', 1)})
check("tracked moves count as tracked changes", L(mv)["tracked_changes"])
vh = variant2(os.path.join(reg, "vanish.docx"), {"word/document.xml": lambda x: x.replace("<w:r><w:t>Summary</w:t>", '<w:r><w:rPr><w:vanish w:val="true"/><w:color w:themeColor="background1" w:val="FEFEFE"/></w:rPr><w:t>Summary</w:t>', 1)})
check("hidden and near-white text are caught in any attribute form", L(vh)["hidden_text"] and L(vh)["white_or_tiny_text"])
hy = ats_gate.check_hygiene("MY TEAM helped us grow; did it myself for him. TODO, TBC, Lorem ipsum, start ____ , <Company>. Remote, US.")
check("hygiene catches all-caps and extra pronouns, TODO/TBC/lorem/blanks, and allows 'US'",
      {"MY", "us", "myself", "him"} <= set(hy["pronouns"]) and "US" not in hy["pronouns"] and len(hy["placeholders"]) >= 5)
extra = " ".join(f"Stuffedword{i}" for i in range(40))
pair_doc = variant2(os.path.join(reg, "Pair-CV.docx"), {"word/document.xml": lambda x: x.replace("<w:t>Summary</w:t>", f"<w:t>Summary {extra}</w:t>", 1)})
pair_pdf = os.path.join(reg, "Pair-CV.pdf"); shutil.copy(os.path.join(FIX, "good_cv.pdf"), pair_pdf)
pc = dict(good_cfg, files=[pair_doc, pair_pdf], max_mb=2)
check("a PDF whose words don't match its DOCX fails", "text differs from" in ats_gate.run_all(pc)["grade_line"])
nop = os.path.join(reg, "nopath"); os.makedirs(nop); os.symlink(sys.executable, os.path.join(nop, "python3"))
np_out = json_tail(run([GATE, "lint", os.path.join(FIX, "good_cv.pdf")], dict(os.environ, PATH=nop)).stdout)
check("PDF checks report missing tools instead of passing silently", any("pdffonts" in x for x in np_out.get("checks_not_run", [])))
try:
    from reportlab.pdfgen import canvas  # optional: only to build the invisible-text test file
    inv = os.path.join(reg, "invisible.pdf"); c = canvas.Canvas(inv); c.drawString(50, 750, "Alex M.")
    t = c.beginText(50, 700); t.setTextRenderMode(3); t.textLine("SQL Kubernetes"); c.drawText(t); c.showPage(); c.save()
    check("invisible PDF text (render mode 3) fails lint", ats_gate.check_lint(inv, [], 2).get("invisible_text") is True)
except ImportError:
    print("SKIP  invisible PDF text check (reportlab not installed)")
cfg_pdf = os.path.join(reg, "pdfonly.json")
good_cfg.update({"files": [os.path.join(FIX, "good_cv.pdf")], "max_mb": 2})
with open(cfg_pdf, "w") as f:
    json.dump(good_cfg, f)
check("a PDF tested without its DOCX is flagged", "without its source DOCX" in run([GATE, "all", cfg_pdf]).stdout.splitlines()[0])
br = variant(os.path.join(reg, "br.docx"), lambda x: x.replace("<w:t>Summary</w:t>", "<w:t>Skills: SQL</w:t><w:br/><w:t>Kubernetes rollout</w:t>", 1))
br_text = ats_gate.docx_plain(br)
check("reader keeps line breaks inside a paragraph (no 'SQLKubernetes')", "SQLKubernetes" not in br_text and ats_gate.count_term(br_text, "Kubernetes") == 1)
check("read test with nothing to compare does not pass", not ats_gate.check_read(os.path.join(FIX, "good_cv.docx"), {})["pass"])
check("fingerprint command exits 0 on success", run([GATE, "fingerprint", os.path.join(FIX, "good_cv.docx")]).returncode == 0)
loose = dict(good_cfg, files=[os.path.join(FIX, "good_cv.docx")], max_mb=2)
loose.pop("approved_text")
check("missing approved CV text is reported, not silently loose", "no approved CV text" in ats_gate.run_all(loose)["grade_line"])
shutil.rmtree(reg, ignore_errors=True)

# 3 + 4. PASS state and hooks ------------------------------------------------
tmp = tempfile.mkdtemp(prefix="jae-selftest-")
env = dict(os.environ, JAE_STATE_DIR=os.path.join(tmp, "state"))
cv = os.path.join(tmp, "Test-Person-CV-Analyst.docx"); shutil.copy(os.path.join(FIX, "good_cv.docx"), cv)
bad = os.path.join(tmp, "Other-CV-Analyst.docx"); shutil.copy(os.path.join(FIX, "Alex-M-CV-Senior-PM.docx"), bad)
note = os.path.join(tmp, "notes.pdf"); shutil.copy(os.path.join(FIX, "good_cv.pdf"), note)
def gate_cfg(path, job, files, **extra):
    c = json.load(open(os.path.join(FIX, "gate_config_good.json")))
    c.update({"job": job, "files": files, "original_text": os.path.join(FIX, "original_cv.txt"),
              "approved_text": os.path.join(FIX, "approved_cv.txt")}, **extra)
    with open(path, "w") as f:
        json.dump(c, f)
    return path
good_files = [os.path.join(FIX, n) for n in ("good_cv.docx", "good_cv.pdf")]
check("record-pass re-runs the gate and freezes a PASS", run([GATE, "record-pass", "--job", "T0", "--config", gate_cfg(os.path.join(tmp, "c0.json"), "T0", good_files)], env).returncode == 0)
check("record-pass refuses without a gate config", run([GATE, "record-pass", "--job", "TX"], env).returncode != 0)
check("record-pass refuses a config for another job", run([GATE, "record-pass", "--job", "TX", "--config", os.path.join(tmp, "c0.json")], env).returncode == 1)
check("record-pass refuses a failing CV (no hand-written report can stand in)", run([GATE, "record-pass", "--job", "TB", "--config", gate_cfg(os.path.join(tmp, "cb.json"), "TB", [bad])], env).returncode == 1)
wv = gate_cfg(os.path.join(tmp, "cw.json"), "TW", [cv], max_mb=0.001)
check("record-pass refuses PASS WITH WAIVERS without --waived", run([GATE, "record-pass", "--job", "TW", "--config", wv], env).returncode == 1)
check("record-pass accepts PASS WITH WAIVERS with --waived", run([GATE, "record-pass", "--job", "TW", "--config", wv, "--waived"], env).returncode == 0)
check("record-pass saves the PASS", run([GATE, "record-pass", "--job", "T1", "--config", gate_cfg(os.path.join(tmp, "c1.json"), "T1", [cv])], env).returncode == 0)
check("verify-upload accepts the tested file", run([GATE, "verify-upload", "--job", "T1", cv], env).returncode == 0)
check("verify-upload refuses a different file", run([GATE, "verify-upload", "--job", "T1", bad], env).returncode == 1)
guard = os.path.join(ROOT, "hooks", "scripts", "pre_upload_guard.py")
stale = os.path.join(ROOT, "hooks", "scripts", "post_change_stale.py")
payload = lambda p: json.dumps({"tool_name": "mcp__browser__file_upload", "tool_input": {"paths": [p]}})
check("upload hook allows the tested CV", run([guard], env, payload(cv)).returncode == 0)
check("upload hook blocks an untested CV", run([guard], env, payload(bad)).returncode == 2)
check("upload hook ignores non-CV files", run([guard], env, payload(note)).returncode == 0)
for nm in ("AlexCV.pdf", "Alex-CVs.pdf", "Curriculum-Vitae-Alex.pdf", "Alex-CV.rtf"):
    pth = os.path.join(tmp, nm); shutil.copy(bad, pth)  # untested bytes under a CV-like name
    check(f"upload hook checks a CV named {nm}", run([guard], env, payload(pth)).returncode == 2)
check("upload hook blocks a CV it can't check (missing or remote path)", run([guard], env, payload("/Users/someone/Documents/Alex-M-CV.pdf")).returncode == 2)
check("upload hook resolves file:// paths", run([guard], env, payload("file://" + bad)).returncode == 2)
check("upload hook checks files sent with curl in Bash", run([guard], env, json.dumps({"tool_name": "Bash", "tool_input": {"command": f"curl -F 'cv=@{bad}' https://example.com/apply"}})).returncode == 2)
check("upload hook ignores ordinary Bash commands", run([guard], env, json.dumps({"tool_name": "Bash", "tool_input": {"command": "ls -la"}})).returncode == 0)
with open(cv, "ab") as f:
    f.write(b"\0")  # simulate an edit after the PASS
out = run([stale], env, json.dumps({"tool_name": "Bash", "tool_input": {"command": "edit"}}))
check("change hook cancels the PASS after an edit", "cancelled" in out.stdout and out.returncode == 0, out.stdout[-200:])
check("upload hook blocks the edited CV", run([guard], env, payload(cv)).returncode == 2)
hooks = json.load(open(os.path.join(ROOT, "hooks", "hooks.json"), encoding="utf8"))
kw_cfg = json.load(open(os.path.join(FIX, "gate_config_good.json"))); kw_cfg["keywords"] = os.path.join(tmp, "kw.json")
with open(kw_cfg["keywords"], "w") as f:
    json.dump(json.load(open(os.path.join(FIX, "gate_config_good.json")))["keywords"], f)
kw_cfg["files"] = [os.path.join(FIX, "good_cv.docx")]
for k in ("approved_text", "original_text"):
    kw_cfg[k] = os.path.join(FIX, kw_cfg[k])
with open(os.path.join(tmp, "kwpath.json"), "w") as f:
    json.dump(kw_cfg, f)
out_json = os.path.join(tmp, "gate_report.json")
r_kw = run([GATE, "all", os.path.join(tmp, "kwpath.json"), "--out", out_json])
check("`all` accepts a keywords file path", r_kw.returncode == 0 and "5/5" in r_kw.stdout.splitlines()[0])
check("`all --out` writes a valid JSON report", json.load(open(out_json)).get("verdict") == "PASS")
# A PASS belongs to one job and one keyword list
cv_a = os.path.join(tmp, "Ann-Lee-CV-JobA.docx")
with zipfile.ZipFile(os.path.join(FIX, "good_cv.docx")) as zin, zipfile.ZipFile(cv_a, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        zout.writestr(item.filename, zin.read(item.filename))  # same content, different bytes
cv_b = os.path.join(tmp, "Ann-Lee-CV-JobB.docx"); shutil.copy(os.path.join(FIX, "good_cv.docx"), cv_b)
cfg_a = gate_cfg(os.path.join(tmp, "ja.json"), "JA", [cv_a]); cfg_b = gate_cfg(os.path.join(tmp, "jb.json"), "JB", [cv_b])
check("job A's CV records its own PASS", run([GATE, "record-pass", "--job", "JA", "--config", cfg_a], env).returncode == 0)
check("job B's CV records its own PASS", run([GATE, "record-pass", "--job", "JB", "--config", cfg_b], env).returncode == 0)
check("job A's CV still verifies for job A when asked by name", run([GATE, "verify-upload", "--job", "JA", cv_a], env).returncode == 0)
check("a CV that passed for job A is refused while job B is in progress", run([GATE, "verify-upload", cv_a], env).returncode == 1)
check("upload hook blocks job A's CV during job B", run([guard], env, payload(cv_a)).returncode == 2)
check("job B's own CV is allowed", run([GATE, "verify-upload", cv_b], env).returncode == 0)
kb = json.load(open(cfg_b)); kb["keywords"].append({"term": "Kubernetes", "must": True, "weight": 1})
with open(cfg_b, "w") as f:
    json.dump(kb, f)
check("changing the job's keyword list cancels its PASS", run([GATE, "verify-upload", "--job", "JB", cv_b], env).returncode == 1)
check("check-stale reports the cancelled PASS", "Ann-Lee-CV-JobB.docx" in run([GATE, "check-stale"], env).stdout)
check("hooks.json has PreToolUse and PostToolUse", {"PreToolUse", "PostToolUse"} <= set(hooks.get("hooks", {})))
shutil.rmtree(tmp, ignore_errors=True)

# 5. Evals -------------------------------------------------------------------
ev = json.load(open(os.path.join(ROOT, "evals", "evals.json"), encoding="utf8"))
files = [f for e in ev["evals"] for f in e.get("files", [])]
check(f"evals.json loads ({len(ev['evals'])} evals)", len(ev["evals"]) >= 4)
check("every eval fixture exists", all(os.path.exists(os.path.join(ROOT, "evals", f)) for f in files))
check("every eval has assertions with checks", all(a.get("check") for e in ev["evals"] for a in e["assertions"]))
g = run([os.path.join(ROOT, "evals", "grade.py"), "--help"])
check("grader runs", g.returncode == 0)

# Capability wording (generic edition): test replies never name a browser/app brand or say "on your computer"
cw = ev.get("capability_wording", {})
check("every eval checks capability wording", bool(cw.get("pattern")) and all(
    any(a["check"].get("pattern") == cw["pattern"] and a["check"].get("type") == "not_regex" for a in e["assertions"]) for e in ev["evals"]))
cw_re = re.compile(cw.get("pattern", r"(?!x)x"))
check("capability wording pattern catches brands and 'on your computer'",
      all(cw_re.search(t) for t in ("I'll open it in Chrome", "save it on your computer", "open the file in Word", "BrowserBase is active"))
      and not any(cw_re.search(t) for t in ("browser control is active", "I'll give you answers to paste", "a word count of 120")))
bundled = sorted(glob.glob(os.path.join(ROOT, "evals", "results", "latest", "eval-*.md")))
replies = list(bundled)
if "--replies" in sys.argv:  # also scan a fresh eval run: --replies <iteration dir>
    d = sys.argv[sys.argv.index("--replies") + 1]
    replies += glob.glob(os.path.join(d, "eval-*", "with_skill", "run-*", "outputs", "response.md"))
check("a stored test reply exists for every eval", {int(re.match(r"eval-(\d+)", os.path.basename(f)).group(1)) for f in bundled} >= {e["id"] for e in ev["evals"]},
      f"found {len(bundled)} for {len(ev['evals'])} evals")
hits = {os.path.relpath(f, ROOT): sorted({m.group(0) for m in cw_re.finditer(open(f, encoding="utf8").read())}) for f in replies}
hits = {k: v for k, v in hits.items() if v}
check(f"test replies name no browser/app brand and never say 'on your computer' ({len(replies)} scanned)", not hits, f"{hits}")

print(f"\n{sum(results)}/{len(results)} checks passed")
sys.exit(0 if all(results) else 1)
