"""
TRAINING-ERA MARKS (PROPOSED, co-authored) -- bounds on a writer's knowledge
cutoff from what the code uses, independent of commit date.

Delivered specification:

    TRAINING-ERA MARKS (PROPOSED)
      library versions, API calls, deprecated functions,
      syntax features a model used -> bounds its knowledge
      cutoff, independent of commit date
      e.g. code calling a function removed in 2024 -> written
      by a model trained before that change
      calibrate on labeled commits first (same gate)

Two kinds of mark, and they are not symmetric:

  INTRODUCED(date)  a feature that did not exist before `date`. Using it puts
                    the writer's cutoff ON OR AFTER `date` (lower bound). It can
                    still be copied from context the writer was given.
  REMOVED(date) /   an API gone (or deprecated) at `date`. The specification's
  DEPRECATED        example reads use of it as cutoff BEFORE `date` (upper
                    bound). That inference fails if models trained after the
                    change still emit the old API, so it is TESTED here before
                    it is used: a labeled model whose own INTRODUCED marks put
                    its cutoff after `date`, and which still uses the removed
                    API, is a counterexample, and REMOVED marks are then
                    reported as NOT_A_BOUND.

Gates, computed on LABELED commits before any unlabeled unit is read:
  lower bounds   TABLE_CONSISTENT if no labeled unit uses an INTRODUCED mark
                 dated after its own commit (that would be a wrong date in the
                 table or a pattern firing on something else)
  upper bounds   NO_COUNTEREXAMPLE / COUNTEREXAMPLE as above
  label marks    model_attribution.calibrate on the era marks (leave-one-repo-
                 out vs label shuffle): reported; this module emits no label
                 probabilities, so it gates nothing here

Every date in era_marks.json is CARRIED from Claude's memory, unverified.
Status of every output: DERIVED. Python units only (other kinds carry no
marks in the table). Patterns run on code with comments and string literals
stripped, so a file that NAMES a pattern (this one, the table) does not fire.

INTEREST: written by a Claude model; the labeled models are mostly Claude.
"""

import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import model_attribution as MA  # noqa: E402

STATUS = "DERIVED"
TABLE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "era_marks.json")

CHOICES = {
    1: "Python units only; units, labels and reading are model_attribution's",
    2: "comments, single-line strings and complete triple-quoted blocks inside "
       "the added text are stripped before matching",
    3: "a mark is present or absent per unit (no counts)",
    4: "lower bound = latest INTRODUCED date present; upper candidate = earliest "
       "REMOVED / DEPRECATED date present",
    5: "a label's cutoff lower bound = latest INTRODUCED date over all its "
       "units (contradicting units excluded)",
    6: "lower bounds only if the table is consistent on labeled commits; an "
       "upper candidate only from a removed/deprecated mark that some label "
       "REACHED (its own lower bound is on or after the change) with no "
       "counterexample; unreached marks are NOT_TESTED and withheld",
}

TRIPLE = re.compile(r'("""|\'\'\')(?:.|\n)*?\1')
SINGLE = re.compile(r'(?:[rbuRBUfF]{0,2})("([^"\\\n]|\\.)*"|\'([^\'\\\n]|\\.)*\')')
COMMENT = re.compile(r"#[^\n]*")


def load(path=TABLE):
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    for m in d["marks"]:
        m["rx"] = re.compile(m["pattern"], re.M)
        m.setdefault("source", d.get("source_default"))
    return d


def strip_code(text):
    text = TRIPLE.sub('""', text)
    text = SINGLE.sub('""', text)
    return COMMENT.sub("", text)


def present(text, table):
    code = strip_code(text)
    return sorted(m["id"] for m in table["marks"] if m["rx"].search(code))


def featurizer(table):
    def f(text, kind):
        if kind != "py":
            return {}
        ids = present(text, table)
        return {i: 1.0 for i in ids}
    return f


def bounds(ids, table):
    by = {m["id"]: m for m in table["marks"]}
    intro = [by[i] for i in ids if by[i]["kind"] == "INTRODUCED"]
    rem = [by[i] for i in ids if by[i]["kind"] in ("REMOVED", "DEPRECATED")]
    lo = max(intro, key=lambda m: m["date"]) if intro else None
    hi = min(rem, key=lambda m: m["date"]) if rem else None
    return lo, hi


def table_consistency(ref, table):
    by = {m["id"]: m for m in table["marks"]}
    bad = []
    for u in ref:
        for i in u["f"]:
            m = by[i]
            if m["kind"] == "INTRODUCED" and m["date"] > u["date"]:
                bad.append({"repo": u["repo"], "sha": u["sha"][:12], "path": u["path"],
                            "date": u["date"], "mark": i, "mark_date": m["date"]})
    return ("TABLE_CONSISTENT" if not bad else "TABLE_CONTRADICTED"), bad


def label_cutoff_lower(ref, table, exclude):
    """Latest INTRODUCED date per label: a lower bound on that label's cutoff."""
    by = {m["id"]: m for m in table["marks"]}
    skip = {(b["sha"], b["path"]) for b in exclude}
    out = {}
    for u in ref:
        if (u["sha"][:12], u["path"]) in skip:
            continue
        for i in u["f"]:
            m = by[i]
            if m["kind"] == "INTRODUCED" and m["date"] > out.get(u["label"], ("", ""))[0]:
                out[u["label"]] = (m["date"], i)
    return out


def counterexamples(ref, table, lows):
    """Per REMOVED/DEPRECATED mark: can the labeled set test it, and does it fail?

    A labeled unit using mark R (gone at date D) is a COUNTEREXAMPLE when its
    label's own cutoff lower bound is on or after D: a model trained after the
    change still emits the old API. A mark is REACHED when some label's lower
    bound is on or after D (that label could have shown a counterexample). A
    mark no label reaches is NOT_TESTED: the test cannot fail on it, so its
    silence is not support."""
    by = {m["id"]: m for m in table["marks"]}
    rem = [m for m in table["marks"] if m["kind"] in ("REMOVED", "DEPRECATED")]
    per = {}
    for m in rem:
        reach = sorted(l for l, lo in lows.items() if lo[0] >= m["date"])
        per[m["id"]] = {"date": m["date"], "reached_by": reach, "counterexamples": [],
                        "uses_in_reference": 0}
    for u in ref:
        for i in u["f"]:
            m = by[i]
            if m["kind"] not in ("REMOVED", "DEPRECATED"):
                continue
            per[i]["uses_in_reference"] += 1
            lo = lows.get(u["label"])
            if lo and lo[0] >= m["date"]:   # cutoff on or after the change
                per[i]["counterexamples"].append(
                    {"label": u["label"], "repo": u["repo"], "sha": u["sha"][:12],
                     "path": u["path"], "label_cutoff_at_least": lo[0], "via": lo[1]})
    for v in per.values():
        v["state"] = ("COUNTEREXAMPLE" if v["counterexamples"] else
                      "NO_COUNTEREXAMPLE" if v["reached_by"] else "NOT_TESTED")
    return per


def read_target(target, table, lower_ok, upper_state):
    """upper_state: {mark id: COUNTEREXAMPLE | NO_COUNTEREXAMPLE | NOT_TESTED}.
    Only NO_COUNTEREXAMPLE marks give an upper candidate."""
    out = []
    for u in target:
        ids = sorted(u["f"])
        lo, _ = bounds(ids, table)
        ok = [i for i in ids if upper_state.get(i) == "NO_COUNTEREXAMPLE"]
        _, hi = bounds(ok, table)
        withheld = {i: upper_state[i] for i in ids if i in upper_state and i not in ok}
        rec = {"repo": u["repo"], "sha": u["sha"][:12], "date": u["date"],
               "path": u["path"], "marks": ids, "status": STATUS}
        if not ids:
            rec["state"] = "NO_ERA_MARK"
        else:
            rec["state"] = "MARKED"
        rec["cutoff_at_least"] = (None if lo is None else
                                  {"date": lo["date"], "mark": lo["id"], "version": lo["version"]}
                                  if lower_ok else "NOT_REPORTED: table contradicted on labeled commits")
        rec["cutoff_before_candidate"] = (None if hi is None else
                                          {"date": hi["date"], "mark": hi["id"],
                                           "version": hi["version"]})
        rec["upper_marks_withheld"] = withheld
        rec["after_commit_date"] = bool(lo and lo["date"] > u["date"])
        out.append(rec)
    return out


def run(repos, table_path=TABLE, r=MA.NULL_R, seed=MA.SEED):
    table = load(table_path)
    feat = featurizer(table)
    units = []
    for repo in repos:
        u, _ = MA.read_units(repo, featurizer=feat)
        units += [x for x in u if x["kind"] == "py"]
    ref = [u for u in units if u["label"] is not None]
    target = [u for u in units if u["label"] is None and u["label_source"] == "UNLABELED"]
    tstate, bad = table_consistency(ref, table)
    lows = label_cutoff_lower(ref, table, bad)
    per = counterexamples(ref, table, lows)
    upper_state = {k: v["state"] for k, v in per.items()}
    marked_ref = [u for u in ref if u["f"]]
    rep = {"status": STATUS + "; PROPOSED; every table date CARRIED, unverified",
           "choices": CHOICES, "py_units": len(units), "reference_units": len(ref),
           "reference_units_with_a_mark": len(marked_ref), "target_count": len(target),
           "mark_counts_reference": _counts(ref), "mark_counts_target": _counts(target),
           "table_check": {"state": tstate, "contradictions": bad},
           "label_cutoff_at_least": {k: {"date": v[0], "via": v[1]} for k, v in sorted(lows.items())},
           "removed_check": per,
           "label_separation_repo_out": MA.calibrate(marked_ref, "repo", r, seed),
           "label_separation_commit_out": MA.calibrate(marked_ref, "sha", r, seed)}
    res = read_target(target, table, tstate == "TABLE_CONSISTENT", upper_state)
    rep["target_states"] = MA._count(res, "state")
    rep["target_after_commit_date"] = sum(r_["after_commit_date"] for r_ in res)
    yr = {}
    for r_ in res:
        if r_["state"] == "MARKED" and isinstance(r_["cutoff_at_least"], dict):
            k = r_["date"][:4]
            yr.setdefault(k, []).append(r_["cutoff_at_least"]["date"])
    rep["target_lower_bounds_by_commit_year"] = {
        k: {"marked_units": len(v), "latest_lower_bound": max(v), "earliest": min(v)}
        for k, v in sorted(yr.items())}
    rep["target_units"] = res
    return rep


def _counts(units):
    c = {}
    for u in units:
        for i in u["f"]:
            c[i] = c.get(i, 0) + 1
    return dict(sorted(c.items()))


def render(rep):
    out = [f"TRAINING-ERA MARKS ({rep['status']})",
           "INTEREST: written by a Claude model; labeled models are mostly Claude.",
           f"py units {rep['py_units']}  reference {rep['reference_units']} "
           f"(with a mark: {rep['reference_units_with_a_mark']})  target {rep['target_count']}",
           "choices: " + "; ".join(f"[{k}] {v}" for k, v in rep["choices"].items()), "",
           "mark counts, reference: " + json.dumps(rep["mark_counts_reference"]),
           "mark counts, target:    " + json.dumps(rep["mark_counts_target"]), "",
           f"GATE lower bounds: {rep['table_check']['state']}  "
           f"contradictions {len(rep['table_check']['contradictions'])}"]
    for b in rep["table_check"]["contradictions"][:10]:
        out.append(f"  {b['repo']} {b['sha']} {b['path']} {b['date']}: {b['mark']} dated {b['mark_date']}")
    out.append("GATE upper bounds, per removed/deprecated mark:")
    for k, v in rep["removed_check"].items():
        out.append(f"  {k} (gone {v['date']}): {v['state']}  uses in reference "
                   f"{v['uses_in_reference']}  reached by {v['reached_by']}")
        for c in v["counterexamples"][:5]:
            out.append(f"    {c['label']} {c['repo']} {c['sha']} {c['path']}: cutoff >= "
                       f"{c['label_cutoff_at_least']} via {c['via']}")
    out.append("label cutoff lower bounds (from own INTRODUCED marks): "
               + json.dumps(rep["label_cutoff_at_least"]))
    out.append("label separation on era marks, repo-out: "
               + json.dumps(rep["label_separation_repo_out"], sort_keys=True))
    out.append("label separation on era marks, commit-out: "
               + json.dumps(rep["label_separation_commit_out"], sort_keys=True))
    out.append("")
    w = {}
    for r_ in rep["target_units"]:
        for k, v in r_.get("upper_marks_withheld", {}).items():
            w[f"{k}:{v}"] = w.get(f"{k}:{v}", 0) + 1
    out.append("target upper marks withheld: " + json.dumps(w))
    out.append("target states: " + json.dumps(rep["target_states"])
               + f"  lower bound after own commit date: {rep['target_after_commit_date']}")
    out.append("target lower bounds by commit year: "
               + json.dumps(rep["target_lower_bounds_by_commit_year"]))
    return "\n".join(out)


def selftest():
    checks, fails = 0, 0

    def ck(name, cond):
        nonlocal checks, fails
        checks += 1
        if not cond:
            fails += 1
            print(f"FAIL {name}")

    t = load()
    ck("table loads, every row dated and sourced",
       all(m["date"] and m["source"] and m["kind"] in ("INTRODUCED", "REMOVED", "DEPRECATED")
           for m in t["marks"]))
    ck("walrus", present("if (n := len(x)) > 3:\n    pass", t) == ["walrus"])
    ck("match_case", "match_case" in present("match cmd:\n    case 1:\n        pass", t))
    ck("union pipe", "union_pipe" in present("def f(x: int | None) -> int:\n    return 1", t))
    ck("builtin generics", "builtin_generics" in present("def f(x: list[int]) -> dict[str, int]:", t))
    ck("pep695", {"pep695_generics", "type_statement"} <= set(present(
        "def f[T](x: T) -> T:\n    return x\ntype Pair = tuple[int, int]", t)))
    ck("distutils removed", present("from distutils.core import setup", t) == ["distutils"])
    ck("np alias", present("x = np.float(3)", t) == ["numpy_scalar_alias"])
    ck("np.float64 not an alias", present("x = np.float64(3)", t) == [])
    ck("openai old sdk", present("r = openai.ChatCompletion.create(model='m')", t) == ["openai_chatcompletion"])
    ck("comment does not fire", present("# from distutils import x\nx = 1", t) == [])
    ck("string does not fire", present("p = 'import distutils'\nq = \"x := 1\"", t) == [])
    ck("docstring does not fire", present('"""\nmatch x:\nimport imp\n"""\ny = 2', t) == [])
    ck("plain code no marks", present("def f(x):\n    return x + 1", t) == [])

    lo, hi = bounds(["walrus", "type_statement", "distutils"], t)
    ck("lower = latest intro", lo["id"] == "type_statement")
    ck("upper = earliest removed", hi["id"] == "distutils")

    def U(label, sha, date, ids, repo="r"):
        return {"repo": repo, "sha": sha, "date": date, "path": "a.py", "kind": "py",
                "label": label, "label_source": "TRAILER", "f": {i: 1.0 for i in ids}}

    ref = [U("A", "a1", "2026-08-01", ["type_statement"]),
           U("A", "a2", "2026-08-02", ["distutils"]),
           U("B", "b1", "2026-08-03", ["walrus"])]
    st, bad = table_consistency(ref, t)
    ck("consistent table", st == "TABLE_CONSISTENT" and not bad)
    st2, bad2 = table_consistency([U("A", "x", "2020-01-01", ["type_statement"])], t)
    ck("intro after commit date contradicts", st2 == "TABLE_CONTRADICTED" and len(bad2) == 1)
    lows = label_cutoff_lower(ref, t, [])
    ck("label lower bound", lows["A"] == ("2023-10-02", "type_statement"))
    per = counterexamples(ref, t, lows)
    ck("counterexample found: A knows 3.12 syntax, still imports distutils",
       per["distutils"]["state"] == "COUNTEREXAMPLE" and per["distutils"]["uses_in_reference"] == 1)
    ck("reached, unused -> NO_COUNTEREXAMPLE", per["imp_module"]["state"] == "NO_COUNTEREXAMPLE")
    ck("unreached -> NOT_TESTED", per["cgi"]["state"] == "NOT_TESTED")
    per2 = counterexamples(ref[1:], t, label_cutoff_lower(ref[1:], t, []))
    ck("no reach without a later lower bound", per2["distutils"]["state"] == "NOT_TESTED")

    tgt = [U(None, "t1", "2025-07-01", ["walrus", "distutils"]), U(None, "t2", "2025-07-01", [])]
    res = read_target(tgt, t, True, {"distutils": "COUNTEREXAMPLE"})
    ck("target lower bound reported", res[0]["cutoff_at_least"]["date"] == "2019-10-14")
    ck("upper withheld after counterexample", res[0]["cutoff_before_candidate"] is None
       and res[0]["upper_marks_withheld"] == {"distutils": "COUNTEREXAMPLE"})
    r3 = read_target(tgt, t, True, {"distutils": "NO_COUNTEREXAMPLE"})
    ck("upper given when tested and held", r3[0]["cutoff_before_candidate"]["mark"] == "distutils")
    ck("no mark state", res[1]["state"] == "NO_ERA_MARK" and res[1]["cutoff_at_least"] is None)
    ck("never a label", all(not ({"label", "model", "top"} & set(r_)) for r_ in res))
    ck("status DERIVED", all(r_["status"] == "DERIVED" for r_ in res))
    res2 = read_target(tgt, t, False, {})
    ck("lower withheld when table contradicted", str(res2[0]["cutoff_at_least"]).startswith("NOT_REPORTED"))
    ck("non-py carries no marks", featurizer(t)("x := 1", "md") == {})
    print(f"checks: {checks}   failed: {fails}")
    return 0 if fails == 0 else 1


def main(argv):
    if "--self-test" in argv:
        return selftest()
    if "--choices" in argv:
        for k, v in CHOICES.items():
            print(f"[CHOICE {k}] {v}")
        return 0
    out = None
    args = [a for a in argv if not a.startswith("--")]
    if "--json" in argv:
        out = argv[argv.index("--json") + 1]
        args = [a for a in args if a != out]
    if not args:
        print(__doc__)
        return 2
    rep = run(args)
    print(render(rep))
    if out:
        if os.path.exists(out):
            print(f"REFUSED: {out} exists; not overwritten", file=sys.stderr)
            return 2
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(rep, fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
