"""
REPO ARCHAEOLOGY -- model attribution from tool marks (PROPOSED, co-authored)

Delivered specification:

    1 DATE PRIOR  commit date -> which models existed and which interfaces
                  were in use then -> candidate set
    2 TOOL MARKS  per file: comment style, docstring format, naming habits,
                  stock phrases, library choices, error-handling patterns
    3 CALIBRATE   known recent commits (labeled) = reference set; test whether
                  marks separate them before trusting anything older
    4 OUTPUT      probability per model, never one label; status DERIVED;
                  "unattributable" allowed
    5 CONTROL     shuffled dates -> attribution should degrade

Reads git history READ-ONLY. Writes nothing into any repository it reads.

Why this exists here: CORRECTION-001 established that the git author field
names the pusher, not the content author. This instrument asks whether the
content itself carries marks of the model that wrote it.

INTEREST, declared: this instrument was written by a Claude model, and Claude
models are in the candidate set it scores. A reading that favours or disfavours
Claude is a reading by an interested party. The calibration and the controls
are the part a reader can recheck without trusting the author.

Units.  A unit is (commit, file): the lines that commit ADDED to that file.
Units are compared only within one file kind (py / md / json / other).
Merge commits are skipped (their added lines belong to the merged commits).

Labels (the reference set) come only from the commit itself:
  - a `Co-Authored-By: Claude <model>` trailer  -> "Claude <model>"
  - a `Co-authored-by: Manus` / `Perplexity` trailer -> that name
  - commits merged from a branch whose name contains "manus/" and carrying
    no other model trailer -> "Manus"
  - a bare "Claude" trailer, or two model trailers on one commit -> AMBIGUOUS,
    kept out of the reference set
Everything else is unlabeled and is the target set. A trailer is TRANSPORT
evidence (which tool committed), and a label read from it is the tool's own
self-report; that is the reference set's weakest joint and is printed.

[CHOICE n] markers name decisions the specification leaves open. All are
printed by --choices and in every report header.
"""

import json
import math
import os
import random
import re
import subprocess
import sys

STATUS = "DERIVED"

CHOICES = {
    1: "unit = (commit, file) added lines; merges skipped",
    2: "units compared only within one file kind: py / md / json / other",
    3: "MIN_LINES = 8 added non-blank lines for a unit to be scored",
    4: "classifier = nearest centroid on z-scored features, L1 mean distance",
    5: "MIN_UNITS = 10 units per (label, kind) for a label to enter the reference",
    6: "probabilities = softmax(-distance / T), T = 0.5",
    7: "UNATTRIBUTABLE if the nearest centroid distance exceeds the 95th "
       "percentile of reference units' distances to their own centroid",
    8: "calibration = leave-one-COMMIT-out and leave-one-REPO-out; statistic = "
       "mean probability given to the true label; null = labels shuffled across "
       "commits, R = 40, seeded; SEPARATES if observed > null 95th percentile",
    9: "gate = leave-one-REPO-out must SEPARATE for a kind before any unlabeled "
       "unit of that kind is attributed (repo and topic are confounded with label)",
    10: "date prior = labels whose FIRST SEEN date in this corpus is on or before "
        "the unit's date; first-seen is an observed UPPER bound on availability, "
        "not a release date, so the prior excludes on absence of evidence",
    11: "interface prior = interfaces.json; UNDECLARED unless the operator fills it",
    12: "control = commit dates shuffled across reference commits, R = 40; the "
        "date-prior calibration statistic should fall. In calibration, first-seen "
        "dates are recomputed WITHOUT the held commit, so a commit cannot vouch "
        "for its own label's availability",
}

MIN_LINES = 8
MIN_UNITS = 10
TEMP = 0.5
NULL_R = 40
SEED = 0

# Stock phrases: a declared word list, so a paraphrase steps around it.
STOCK = (
    "load-bearing", "honest", "comprehensive", "robust", "leverage", "seamless",
    "delve", "crucial", "note:", "todo", "readings only", "not interpreted",
    "proposed", "co-authored", "stated", "carried", "verify", "falsif",
    "in summary", "key insight", "let's", "this ensures", "for example",
)

KIND_OF = {".py": "py", ".md": "md", ".json": "json", ".jsonl": "json"}

TRAILER = re.compile(r"(?im)^co-authored-by:\s*([^<\n]+?)\s*(?:<[^>\n]*>)?\s*$")
IDENT = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]{2,}\b")
DEF = re.compile(r"^\s*(?:def|class)\s+([A-Za-z_][A-Za-z0-9_]*)")
ASSIGN = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=[^=]")


# ------------------------------------------------------------------ labels

def labels_from_trailers(body):
    """Model labels on one commit message. Returns (labels, ambiguous)."""
    out, amb = set(), False
    for name in TRAILER.findall(body or ""):
        n = name.strip()
        low = n.lower()
        if low.startswith("claude"):
            if low == "claude":
                amb = True
            else:
                out.add(n)
        elif low.startswith("manus"):
            out.add("Manus")
        elif low.startswith("perplexity"):
            out.add("Perplexity")
        # a person's co-author trailer is not a model label
    if len(out) > 1:
        amb = True
    return out, amb


def commit_label(body, on_manus_branch=False):
    labs, amb = labels_from_trailers(body)
    if amb:
        return None, "AMBIGUOUS"
    if labs:
        return next(iter(labs)), "TRAILER"
    if on_manus_branch:
        return "Manus", "MANUS_BRANCH"
    return None, "UNLABELED"


# ---------------------------------------------------------------- features

def file_kind(path):
    return KIND_OF.get(os.path.splitext(path)[1].lower(), "other")


def _r(a, b):
    return a / b if b else 0.0


def features(text, kind):
    """Tool marks of one unit's added text. Ratios and rates only, no raw text."""
    lines = [l for l in text.split("\n") if l.strip()]
    n = len(lines) or 1
    joined = "\n".join(lines)
    low = joined.lower()
    nchar = len(joined) or 1
    f = {
        "mean_line_len": sum(len(l) for l in lines) / n / 100.0,
        "long_lines": _r(sum(len(l) > 88 for l in lines), n),
        "non_ascii": _r(sum(ord(c) > 127 for c in joined), nchar) * 100,
        "em_dash": _r(joined.count("—"), n),
        "double_hyphen": _r(joined.count(" -- "), n),
        "emoji": _r(sum(ord(c) > 0x2600 for c in joined), n),
        "stock_phrases": _r(sum(low.count(s) for s in STOCK), n),
        "caps_tokens": _r(len(re.findall(r"\b[A-Z][A-Z_]{3,}\b", joined)), n),
        "backticks": _r(joined.count("`"), n),
        "trailing_colon": _r(sum(l.rstrip().endswith(":") for l in lines), n),
    }
    if kind == "py":
        comments = [l for l in lines if l.lstrip().startswith("#")]
        idents = [m.group(1) for l in lines for m in (DEF.match(l), ASSIGN.match(l)) if m]
        f.update({
            "comment_lines": _r(len(comments), n),
            "comment_no_space": _r(sum(not l.lstrip()[1:2].isspace() and len(l.lstrip()) > 1
                                       for l in comments), len(comments)),
            "inline_comment": _r(sum("  #" in l and not l.lstrip().startswith("#") for l in lines), n),
            "docstring_dq": _r(joined.count('"""'), n),
            "docstring_sq": _r(joined.count("'''"), n),
            "google_args": _r(low.count("args:") + low.count("returns:"), n),
            "numpy_params": _r(joined.count("----------"), n),
            "rest_param": _r(low.count(":param"), n),
            "snake_ident": _r(sum("_" in i and i.lower() == i for i in idents), len(idents)),
            "camel_ident": _r(sum(any(c.isupper() for c in i[1:]) and "_" not in i for i in idents),
                              len(idents)),
            "ident_len": _r(sum(len(i) for i in IDENT.findall(joined)),
                            len(IDENT.findall(joined))) / 10.0,
            "type_hints": _r(joined.count("->") + len(re.findall(r"\w: (?:int|str|float|bool|list|dict)", joined)), n),
            "fstring": _r(len(re.findall(r"\bf[\"']", joined)), n),
            "format_call": _r(joined.count(".format("), n),
            "percent_fmt": _r(len(re.findall(r"[\"'] % ", joined)), n),
            "imp_numpy": float("import numpy" in joined),
            "imp_pathlib": float("pathlib" in joined),
            "imp_ospath": float("os.path" in joined),
            "imp_argparse": float("argparse" in joined),
            "imp_dataclass": float("dataclass" in joined),
            "imp_typing": float("from typing" in joined),
            "imp_unittest": float("unittest" in joined),
            "imp_pytest": float("pytest" in joined),
            "try_rate": _r(len(re.findall(r"^\s*try:", joined, re.M)), n),
            "bare_except": _r(len(re.findall(r"except\s*:", joined)), n),
            "raise_rate": _r(len(re.findall(r"\braise\b", joined)), n),
            "assert_rate": _r(len(re.findall(r"^\s*assert\b", joined, re.M)), n),
            "print_rate": _r(joined.count("print("), n),
        })
    elif kind == "md":
        f.update({
            "headings": _r(sum(l.startswith("#") for l in lines), n),
            "bullet_dash": _r(sum(l.lstrip().startswith("- ") for l in lines), n),
            "bullet_star": _r(sum(l.lstrip().startswith("* ") for l in lines), n),
            "numbered": _r(sum(bool(re.match(r"\s*\d+\.\s", l)) for l in lines), n),
            "bold": _r(joined.count("**"), n),
            "table_rows": _r(sum(l.lstrip().startswith("|") for l in lines), n),
            "fences": _r(joined.count("```"), n),
            "check_marks": _r(sum(joined.count(c) for c in "✅❌⚠"), n),
        })
    elif kind == "json":
        f.update({
            "keys_snake": _r(len(re.findall(r'"[a-z]+_[a-z_]+"\s*:', joined)), n),
            "keys_camel": _r(len(re.findall(r'"[a-z]+[A-Z][A-Za-z]*"\s*:', joined)), n),
            "indent2": _r(sum(l.startswith("  ") and not l.startswith("   ") for l in lines), n),
            "indent1": _r(sum(l.startswith(" ") and not l.startswith("  ") for l in lines), n),
        })
    return f


# ------------------------------------------------------------- git reading

def _git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True,
                          errors="replace", check=True).stdout


def manus_branch_commits(repo):
    """Commits brought in by merges from a branch whose name contains 'manus/'."""
    out = set()
    log = _git(repo, "log", "--all", "--merges", "--format=%H%x09%P%x09%s")
    for line in log.splitlines():
        parts = line.split("\t", 2)
        if len(parts) < 3 or "manus/" not in parts[2].lower():
            continue
        parents = parts[1].split()
        if len(parents) < 2:
            continue
        shas = _git(repo, "rev-list", parents[1], "^" + parents[0]).split()
        out.update(shas)
    return out


def read_units(repo, min_lines=MIN_LINES, featurizer=None):
    """Yield one record per (commit, file) with >= min_lines added non-blank lines.

    featurizer(text, kind) -> dict; defaults to `features` (tool marks)."""
    featurizer = featurizer or features
    name = os.path.basename(os.path.abspath(repo).rstrip("/"))
    shallow = _git(repo, "rev-parse", "--is-shallow-repository").strip() == "true"
    manus = manus_branch_commits(repo)
    sep = "\x1eCOMMIT\x1f"
    raw = _git(repo, "log", "--all", "--no-merges", "-p", "--unified=0", "--no-color",
               f"--format={sep}%H%x1f%ad%x1f%B%x1f", "--date=short")
    seen = set()
    units = []
    for chunk in raw.split(sep)[1:]:
        try:
            sha, date, body, diff = chunk.split("\x1f", 3)
        except ValueError:
            continue
        if sha in seen:
            continue
        seen.add(sha)
        label, how = commit_label(body, sha in manus)
        files, cur = {}, None
        for line in diff.split("\n"):
            if line.startswith("+++ "):
                p = line[4:]
                cur = p[2:] if p.startswith("b/") else None
                if cur is not None:
                    files.setdefault(cur, [])
            elif cur is not None and line.startswith("+") and not line.startswith("+++"):
                files[cur].append(line[1:])
        for path, added in files.items():
            text = "\n".join(added)
            if sum(1 for l in added if l.strip()) < min_lines:
                continue
            kind = file_kind(path)
            units.append({"repo": name, "sha": sha, "date": date, "path": path,
                          "kind": kind, "label": label, "label_source": how,
                          "f": featurizer(text, kind)})
    return units, shallow


# --------------------------------------------------------------- classifier

def _keys(units):
    ks = sorted({k for u in units for k in u["f"]})
    return ks


def zscorer(ref):
    ks = _keys(ref)
    mu, sd = {}, {}
    for k in ks:
        v = [u["f"].get(k, 0.0) for u in ref]
        m = sum(v) / len(v)
        s = math.sqrt(sum((x - m) ** 2 for x in v) / len(v))
        mu[k], sd[k] = m, (s if s > 1e-12 else None)
    ks = [k for k in ks if sd[k] is not None]     # a constant feature cannot separate
    return ks, lambda f: [(f.get(k, 0.0) - mu[k]) / sd[k] for k in ks]


def _dist(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) / (len(a) or 1)


def _centroid(vs):
    n = len(vs)
    return [sum(c) / n for c in zip(*vs)]


def softmax(dists, temp=TEMP):
    m = min(dists.values())
    w = {k: math.exp(-(d - m) / temp) for k, d in dists.items()}
    s = sum(w.values())
    return {k: v / s for k, v in w.items()}


def reference_labels(ref, min_units=MIN_UNITS):
    c = {}
    for u in ref:
        c[u["label"]] = c.get(u["label"], 0) + 1
    return sorted(l for l, n in c.items() if n >= min_units)


class Model:
    """Nearest-centroid over one file kind's reference units."""

    def __init__(self, ref, min_units=MIN_UNITS):
        self.labels = reference_labels(ref, min_units)
        ref = [u for u in ref if u["label"] in self.labels]
        self.ok = len(self.labels) >= 2
        if not self.ok:
            return
        self.keys, self.z = zscorer(ref)
        vecs = {}
        for u in ref:
            vecs.setdefault(u["label"], []).append(self.z(u["f"]))
        self.cent = {l: _centroid(v) for l, v in vecs.items()}
        own = sorted(_dist(v, self.cent[l]) for l, vs in vecs.items() for v in vs)
        self.envelope = own[min(len(own) - 1, int(0.95 * len(own)))]

    def score(self, f):
        v = self.z(f)
        d = {l: _dist(v, c) for l, c in self.cent.items()}
        return d, softmax(d)


# -------------------------------------------------------------- date prior

def first_seen(ref):
    fs = {}
    for u in ref:
        fs[u["label"]] = min(fs.get(u["label"], u["date"]), u["date"])
    return fs


def candidates(date, fs):
    return sorted(l for l, d in fs.items() if d <= date)


def apply_prior(probs, cands):
    keep = {l: p for l, p in probs.items() if l in cands}
    s = sum(keep.values())
    if not keep or s <= 0:
        return None
    return {l: p / s for l, p in keep.items()}


def read_interfaces(path):
    try:
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
    except FileNotFoundError:
        return "UNDECLARED", "no interfaces.json"
    periods = d.get("periods") or []
    if not periods:
        return "UNDECLARED", d.get("_note", "no periods declared")
    return "DECLARED", periods


# ------------------------------------------------------------- calibration

def loo(ref, group_key, prior_dates=None, fs=None, min_units=MIN_UNITS, marks=True):
    """Leave one group out; mean probability given to the true label.

    Features are z-scored once over the whole reference set (a small leak of the
    held-out group into the scaling, stated); centroids are recomputed without
    the held group by subtracting its sums. prior_dates: optional {sha: date}
    for the date prior (the control passes shuffled dates here).
    Returns (statistic, n_scored, chance)."""
    labels = reference_labels(ref, min_units)
    ref = [u for u in ref if u["label"] in labels]
    if len(labels) < 2:
        return None, 0, None
    keys, z = zscorer(ref)
    vec = [z(u["f"]) for u in ref]
    dim = len(keys)
    tot = {l: [0.0] * dim for l in labels}
    cnt = {l: 0 for l in labels}
    groups = {}
    for i, u in enumerate(ref):
        t = tot[u["label"]]
        for j, x in enumerate(vec[i]):
            t[j] += x
        cnt[u["label"]] += 1
        groups.setdefault(u[group_key], []).append(i)
    # first-seen dates WITHOUT the held group, so the held commit cannot vouch
    # for its own label's availability (that would make the prior circular)
    by_label = {}
    for u in ref:
        by_label.setdefault(u["label"], []).append((u["date"], u[group_key]))
    for v in by_label.values():
        v.sort()

    def fs_without(g):
        out = {}
        for l, v in by_label.items():
            for d, gg in v:
                if gg != g:
                    out[l] = d
                    break
        return out

    got = []
    for g, idx in groups.items():
        fs_g = fs_without(g) if prior_dates is not None else None
        gs = {l: [0.0] * dim for l in labels}
        gc = {l: 0 for l in labels}
        for i in idx:
            l = ref[i]["label"]
            gc[l] += 1
            for j, x in enumerate(vec[i]):
                gs[l][j] += x
        cent = {l: [(tot[l][j] - gs[l][j]) / (cnt[l] - gc[l]) for j in range(dim)]
                for l in labels if cnt[l] - gc[l] >= min_units}
        if len(cent) < 2:
            continue
        for i in idx:
            u = ref[i]
            if u["label"] not in cent:
                continue
            if marks:
                p = softmax({l: _dist(vec[i], c) for l, c in cent.items()})
            else:   # date-only baseline: marks ignored, every label equally likely
                p = {l: 1.0 / len(cent) for l in cent}
            if prior_dates is not None:
                p = apply_prior(p, candidates(prior_dates[u["sha"]], fs_g))
                if p is None:
                    got.append(0.0)
                    continue
            got.append(p.get(u["label"], 0.0))
    if not got:
        return None, 0, None
    return sum(got) / len(got), len(got), 1.0 / len(labels)


def shuffle_labels(ref, rng):
    """Shuffle labels across COMMITS, so units of one commit keep one label."""
    shas = sorted({u["sha"] for u in ref})
    lab = {}
    for u in ref:
        lab[u["sha"]] = u["label"]
    vals = [lab[s] for s in shas]
    rng.shuffle(vals)
    new = dict(zip(shas, vals))
    return [dict(u, label=new[u["sha"]]) for u in ref]


def calibrate(ref, group_key, r=NULL_R, seed=SEED, min_units=MIN_UNITS):
    obs, n, chance = loo(ref, group_key, min_units=min_units)
    if obs is None:
        return {"state": "NOT_EVALUABLE", "reason": "fewer than 2 labels with enough units"}
    rng = random.Random(seed)
    null = []
    for _ in range(r):
        v, _, _ = loo(shuffle_labels(ref, rng), group_key, min_units=min_units)
        if v is not None:
            null.append(v)
    null.sort()
    q95 = null[min(len(null) - 1, int(0.95 * len(null)))] if null else None
    sep = q95 is not None and obs > q95
    return {"state": "SEPARATES" if sep else "DOES_NOT_SEPARATE",
            "statistic": round(obs, 4), "units": n, "chance": round(chance, 4),
            "null_q95": None if q95 is None else round(q95, 4),
            "null_median": None if not null else round(null[len(null) // 2], 4),
            "null_draws": len(null)}


def date_control(ref, r=NULL_R, seed=SEED, min_units=MIN_UNITS):
    """Date prior with true dates vs shuffled dates (across commits)."""
    labels = reference_labels(ref, min_units)
    ref = [u for u in ref if u["label"] in labels]
    if len(labels) < 2:
        return {"state": "NOT_EVALUABLE"}
    fs = first_seen(ref)
    true = {u["sha"]: u["date"] for u in ref}
    base, _, _ = loo(ref, "sha", min_units=min_units)
    with_true, n, _ = loo(ref, "sha", true, fs, min_units)
    dates_only, _, _ = loo(ref, "sha", true, fs, min_units, marks=False)
    rng = random.Random(seed)
    shas = sorted(true)
    shuf = []
    for _ in range(r):
        d = [true[s] for s in shas]
        rng.shuffle(d)
        v, _, _ = loo(ref, "sha", dict(zip(shas, d)), fs, min_units)
        if v is not None:
            shuf.append(v)
    shuf.sort()
    med = shuf[len(shuf) // 2] if shuf else None
    degrades = med is not None and med < with_true
    return {"state": "DEGRADES" if degrades else "DOES_NOT_DEGRADE",
            "no_prior": round(base, 4), "prior_true_dates": round(with_true, 4),
            "dates_only_no_marks": round(dates_only, 4),
            "prior_shuffled_median": None if med is None else round(med, 4),
            "shuffles": len(shuf), "units": n}


# ------------------------------------------------------------------ attribute

def attribute(target, model, gate_open, fs, gate_reason):
    """Per unlabeled unit: state + probability per label. Never one label."""
    out = []
    for u in target:
        rec = {"repo": u["repo"], "sha": u["sha"][:12], "date": u["date"],
               "path": u["path"], "kind": u["kind"], "status": STATUS}
        if not gate_open:
            rec.update(state="NOT_ATTRIBUTED", reason=gate_reason, probabilities=None,
                       probabilities_with_date_prior=None)
            out.append(rec)
            continue
        d, p = model.score(u["f"])
        cands = candidates(u["date"], fs)
        pp = apply_prior(p, cands)
        if min(d.values()) > model.envelope:
            state, why = "UNATTRIBUTABLE", "outside every reference label's envelope"
        elif pp is None:
            state, why = "UNATTRIBUTABLE", "no reference label observed on or before this date"
        else:
            state, why = "ATTRIBUTED_AS_DISTRIBUTION", "within envelope"
        rec.update(state=state, reason=why, candidates=cands,
                   probabilities={k: round(v, 3) for k, v in sorted(p.items())},
                   probabilities_with_date_prior=None if pp is None else
                   {k: round(v, 3) for k, v in sorted(pp.items())})
        out.append(rec)
    return out


# ---------------------------------------------------------------------- run

def run(repos, interfaces_path, r=NULL_R, seed=SEED):
    units, shallow = [], {}
    for repo in repos:
        u, sh = read_units(repo)
        units += u
        shallow[os.path.basename(os.path.abspath(repo).rstrip("/"))] = sh
    ref_all = [u for u in units if u["label"] is not None]
    target = [u for u in units if u["label"] is None and u["label_source"] == "UNLABELED"]
    ambiguous = sum(u["label_source"] == "AMBIGUOUS" for u in units)
    iface = read_interfaces(interfaces_path)
    rep = {"status": STATUS + "; PROPOSED instrument; readings, no verdict",
           "choices": CHOICES, "repos": shallow, "units": len(units),
           "reference_units": len(ref_all), "target_units": len(target),
           "ambiguous_units": ambiguous, "interface_prior": iface, "kinds": {}}
    for kind in ("py", "md", "json", "other"):
        ref = [u for u in ref_all if u["kind"] == kind]
        tgt = [u for u in target if u["kind"] == kind]
        counts = {}
        for u in ref:
            counts[u["label"]] = counts.get(u["label"], 0) + 1
        k = {"reference_counts": dict(sorted(counts.items())),
             "label_sources": _count(ref, "label_source"),
             "reference_labels": reference_labels(ref)}
        k["calibration_commit_out"] = calibrate(ref, "sha", r, seed)
        k["calibration_repo_out"] = calibrate(ref, "repo", r, seed)
        k["date_control"] = date_control(ref, r, seed)
        fs = first_seen([u for u in ref if u["label"] in k["reference_labels"]])
        k["first_seen"] = dict(sorted(fs.items(), key=lambda x: x[1]))
        gate = k["calibration_repo_out"]["state"] == "SEPARATES"
        why = ("leave-one-repo-out calibration: " + k["calibration_repo_out"]["state"])
        m = Model(ref) if gate else None
        res = attribute(tgt, m, gate and m is not None and m.ok, fs, why)
        k["target_states"] = _count(res, "state")
        k["target_units"] = res
        rep["kinds"][kind] = k
    return rep


def _count(rows, key):
    c = {}
    for r_ in rows:
        c[r_[key]] = c.get(r_[key], 0) + 1
    return dict(sorted(c.items()))


def render(rep):
    out = [f"REPO ARCHAEOLOGY -- model attribution ({rep['status']})",
           "INTEREST: written by a Claude model; Claude models are candidates here.",
           f"units {rep['units']}  reference {rep['reference_units']}  target "
           f"{rep['target_units']}  ambiguous (kept out) {rep['ambiguous_units']}",
           "repos (shallow?): " + json.dumps(rep["repos"], sort_keys=True),
           f"interface prior: {rep['interface_prior'][0]} ({rep['interface_prior'][1]})",
           "reference labels are trailer self-reports (transport evidence), not content facts",
           "choices: " + "; ".join(f"[{k}] {v}" for k, v in rep["choices"].items()), ""]
    for kind, k in rep["kinds"].items():
        out.append(f"== kind {kind}")
        out.append("  reference counts: " + json.dumps(k["reference_counts"]))
        out.append("  label sources: " + json.dumps(k["label_sources"]))
        out.append("  labels with >= MIN_UNITS: " + json.dumps(k["reference_labels"]))
        out.append("  first seen (observed upper bound): " + json.dumps(k["first_seen"]))
        for name in ("calibration_commit_out", "calibration_repo_out", "date_control"):
            out.append(f"  {name}: " + json.dumps(k[name], sort_keys=True))
        out.append("  target states: " + json.dumps(k["target_states"]))
        out.append("")
    return "\n".join(out)


# ----------------------------------------------------------------- selftest

def _synth(label, sha, repo, date, style, rng):
    if style == "a":
        f = {"x": 1.0 + rng.gauss(0, 0.1), "y": rng.gauss(0, 0.1)}
    elif style == "b":
        f = {"x": rng.gauss(0, 0.1), "y": 1.0 + rng.gauss(0, 0.1)}
    else:
        f = {"x": rng.gauss(0, 0.5), "y": rng.gauss(0, 0.5)}
    return {"repo": repo, "sha": sha, "date": date, "path": "f.py", "kind": "py",
            "label": label, "label_source": "TRAILER", "f": f}


def selftest():
    checks, fails = 0, 0

    def ck(name, cond):
        nonlocal checks, fails
        checks += 1
        if not cond:
            fails += 1
            print(f"FAIL {name}")

    labs, amb = labels_from_trailers("x\n\nCo-Authored-By: Claude Opus 5.5 <noreply@x>\n")
    ck("trailer label", labs == {"Claude Opus 5.5"} and not amb)
    ck("bare Claude ambiguous", commit_label("Co-Authored-By: Claude <a@b>")[1] == "AMBIGUOUS")
    ck("two models ambiguous", commit_label(
        "Co-Authored-By: Claude Opus 5 <a>\nCo-authored-by: Manus <m>")[1] == "AMBIGUOUS")
    ck("person not a label", commit_label("Co-authored-by: JinnZ2 <x>")[1] == "UNLABELED")
    ck("manus branch", commit_label("", True) == ("Manus", "MANUS_BRANCH"))
    ck("perplexity", commit_label("Co-authored-by: Perplexity <p>")[0] == "Perplexity")

    f = features('def foo_bar(x: int) -> int:\n    """Args: x"""\n    # c\n    return x\n', "py")
    ck("py features", f["snake_ident"] == 1.0 and f["type_hints"] > 0 and f["google_args"] > 0)
    ck("no raw text in features", all(isinstance(v, float) for v in f.values()))

    rng = random.Random(1)
    sep = []
    for i in range(30):
        sep.append(_synth("A", f"a{i}", f"r{i % 3}", "2026-08-01", "a", rng))
        sep.append(_synth("B", f"b{i}", f"r{i % 3}", "2026-10-01", "b", rng))
    c = calibrate(sep, "sha", 20)
    ck("separable styles SEPARATE", c["state"] == "SEPARATES")
    ck("separable by repo too", calibrate(sep, "repo", 20)["state"] == "SEPARATES")
    same = [dict(u, f=_synth("Z", "z", "r", "2026-08-01", "n", rng)["f"]) for u in sep]
    ck("identical styles DO_NOT_SEPARATE", calibrate(same, "sha", 20)["state"] == "DOES_NOT_SEPARATE")

    m = Model(sep)
    d, p = m.score({"x": 1.0, "y": 0.0})
    ck("probabilities sum to 1", abs(sum(p.values()) - 1) < 1e-9)
    ck("distribution, A favoured", p["A"] > p["B"])

    fs = first_seen(sep)
    ck("candidate set before B", candidates("2026-09-01", fs) == ["A"])
    ck("empty candidate set", candidates("2025-01-01", fs) == [])
    ck("prior renormalizes", apply_prior({"A": 0.2, "B": 0.8}, ["A"]) == {"A": 1.0})
    ck("prior with no candidates is None", apply_prior({"A": 1.0}, []) is None)

    # date-coupled styles: prior helps with true dates, shuffling hurts
    dc = date_control(sep, 20)
    ck("shuffled dates degrade", dc["state"] == "DEGRADES")
    ck("true-date prior >= no prior", dc["prior_true_dates"] >= dc["no_prior"] - 1e-9)
    ck("dates-only baseline reported", 0 < dc["dates_only_no_marks"] <= 1)

    tgt = [dict(_synth(None, "t1", "r9", "2026-11-01", "a", rng), label_source="UNLABELED"),
           dict(_synth(None, "t2", "r9", "2025-01-01", "a", rng), label_source="UNLABELED"),
           {"repo": "r9", "sha": "t3", "date": "2026-11-01", "path": "f.py", "kind": "py",
            "label": None, "label_source": "UNLABELED", "f": {"x": 50.0, "y": 50.0}}]
    res = attribute(tgt, m, True, fs, "")
    ck("in envelope -> distribution", res[0]["state"] == "ATTRIBUTED_AS_DISTRIBUTION")
    ck("before any label -> unattributable", res[1]["state"] == "UNATTRIBUTABLE")
    ck("far outside -> unattributable", res[2]["state"] == "UNATTRIBUTABLE")
    single = {"label", "top", "best", "attributed_to", "model"}
    ck("never one label", all(not (single & set(r_)) for r_ in res))
    closed = attribute(tgt, m, False, fs, "gate closed")
    ck("gate closed -> no probabilities",
       all(r_["probabilities"] is None and r_["state"] == "NOT_ATTRIBUTED" for r_ in closed))
    ck("status DERIVED", all(r_["status"] == "DERIVED" for r_ in res + closed))

    st, why = read_interfaces("/nonexistent/interfaces.json")
    ck("interface prior undeclared", st == "UNDECLARED")
    print(f"checks: {checks}   failed: {fails}")
    return 0 if fails == 0 else 1


def main(argv):
    if "--self-test" in argv:
        return selftest()
    if "--choices" in argv:
        for k, v in CHOICES.items():
            print(f"[CHOICE {k}] {v}")
        return 0
    args = [a for a in argv if not a.startswith("--")]
    out = None
    if "--json" in argv:
        out = argv[argv.index("--json") + 1]
        args = [a for a in args if a != out]
    iface = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "interfaces.json")
    if not args:
        print(__doc__)
        return 2
    rep = run(args, iface)
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
