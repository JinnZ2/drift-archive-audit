#!/usr/bin/env python3
"""
Channel-function scorer: F1-F4 per sensory channel, per document.

Scores HOW a channel is used, not how often it is mentioned.
Python stdlib only. No dependencies.

    F1 MENTION     sensory term as description
    F2 EVIDENCE    channel read for state
    F3 METHOD      channel used to teach / transmit / diagnose with
    F4 INSTRUMENT  something built IN or FOR the channel

Discriminator is FUNCTION BREADTH (how many of F1-F4 are reached),
not volume. Channels are kept separate and never summed.

LIMIT 5 applies to this file: a scorer written by a model inherits the
corpus priors under test. This is a first draft for a human-annotated
gold set to be built against, NOT a validated instrument. Report
inter-rater agreement before using any number it produces.

usage:  python3 instrument/channel_function.py <path> [<path> ...]
        python3 instrument/channel_function.py --self-test
"""
import os, re, sys, json, collections

CHANNELS = {
    "olfactory":       r"scent|smell|odou?r|olfact|aroma|incense|smoke|fragran",
    "auditory":        r"\bsound|acoustic|audit(ory|ion)|tone|pitch|timbre|resonan|hum\b|melody|harmon|\bloud|\bquiet|nois(e|y)|silen(t|ce)|muffl|ringing|\bhear(d|ing)?\b|\blisten",
    "vibration_haptic": r"vibrat|haptic|tactile|texture|\btouch|tremor|oscillat|\bshak(e|ing)|rattl|\bbuzz|judder",
    "proprio_kines":   r"propriocept|kinesthet|posture|gait|balance|movement|gesture|muscle memory",
    "thermal":         r"thermal|temperature|\bheat\b|\bcold\b|warmth|degrees? ?[CF]\b|\bhot\b|\bcool\b|freez|burn(t|ing)?\b",
    "baroceptive":     r"barometric|\bpressure\b|altitude|\bpsi\b|\bbar\b|pascal",
    "interoceptive":   r"intero(cept)?|gut feel|visceral|\bheart ?rate|breath(ing)?\b|fatigue",
}
# function markers, searched in a window around a channel hit
F2 = r"indicat|signal(s|led|ing)?\b|detect|reveal|diagnos|means that|tells? (you|us)|symptom|read(ing|s)? (as|for)|evidence of|precursor|warn"
F3 = r"teach|train|transmit|encod|learn|practice|method|technique|ritual|protocol for|how to|pass(ed|ing)? (down|on)|apprentic|calibrat"
F4 = r"\bprotocol\b|\bschema\b|\bsensor\b|\bspec(ification)?\b|\blog\b|\bharness\b|\binstrument\b|\btest (suite|rig|bench)|\bprocedure\b|\.json|\.py\b|\bAPI\b|\bmodule\b|\bpipeline\b"
WINDOW = 240   # characters either side of a channel hit

# technical register, built from CONTENT properties per LIMIT 6 — not style
TECH = {
    "quantified_unit": r"\b\d+(\.\d+)?\s?(mm|cm|\bm\b|km|kg|\bg\b|ms|\bs\b|hz|khz|mhz|ghz|kw|mw|\bw\b|v\b|amp|psi|bar|pa|°|deg|%|yr|years?)\b",
    "equation":        r"[a-zA-Z]\s?=\s?[^\s=]|\\\(|\$\$|∑|∫|√|≈|≥|≤",
    "falsifiable":     r"falsif|refut|predict(s|ion)|threshold|hypothes|if .{0,40} then .{0,40}(fail|hold|break)|null result|control (group|case)",
    "tolerance":       r"toleran|±|\bmargin\b|error bar|confidence interval|uncertaint",
}

def score_text(text):
    t = text.lower()
    out = {}
    for ch, pat in CHANNELS.items():
        hits = list(re.finditer(pat, t))
        if not hits:
            continue
        f = {"F1": len(hits), "F2": 0, "F3": 0, "F4": 0}
        for m in hits:
            lo, hi = max(0, m.start()-WINDOW), min(len(t), m.end()+WINDOW)
            w = t[lo:hi]
            if re.search(F2, w): f["F2"] += 1
            if re.search(F3, w): f["F3"] += 1
            if re.search(F4, w): f["F4"] += 1
        f["breadth"] = sum(1 for k in ("F1","F2","F3","F4") if f[k] > 0)
        f["top"] = max(k for k in ("F1","F2","F3","F4") if f[k] > 0)
        out[ch] = f
    return out

def tech_score(text):
    t = text.lower()
    return {k: len(re.findall(p, t)) for k, p in TECH.items()}

def score_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="strict") as fh:
            text = fh.read()
    except (UnicodeDecodeError, OSError):
        return None
    if len(text) < 200:
        return None
    ch = score_text(text)
    if not ch:
        return None
    return {"path": path, "bytes": len(text), "channels": ch, "tech": tech_score(text)}

def walk(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        else:
            for base, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d != ".git"]
                for f in files:
                    if f.endswith((".md", ".json", ".txt", ".py", ".js", ".jsx", ".yaml", ".yml")):
                        yield os.path.join(base, f)

# Construction-bias note, recorded 2026-09-22, found BY this self-test:
# the first auditory pattern held only TECHNICAL acoustic vocabulary
# (acoustic, timbre, resonance) and missed plain descriptors (loud, quiet,
# noisy). That skew scores F1 DOWN for plain-register speakers and inflates
# the apparent function breadth of technical-register ones -- i.e. it builds
# the H1 tradeoff into the CHANNEL scorer, which LIMIT 6 only anticipated in
# the technical-register scorer. Plain descriptors were added to auditory,
# vibration_haptic and thermal. The other channels should be re-audited by a
# human for the same skew before any number here is used.

SELF_TEST = [
    ("it smelled bad in there",                                    "olfactory", "F1"),
    ("the smell indicates a bearing is about to fail",             "olfactory", "F2"),
    ("we teach the scent sequence so it can be passed down",       "olfactory", "F3"),
    ("scent_binding_protocol.json defines the anchor schema",      "olfactory", "F4"),
    ("that vibration signals a cracked mount",                     "vibration_haptic", "F2"),
    ("the room was loud",                                          "auditory",  "F1"),
    ("it got hot fast",                                            "thermal",   "F1"),
    ("the panel was shaking",                                      "vibration_haptic", "F1"),
]

def self_test():
    ok = 0
    for text, ch, want in SELF_TEST:
        got = score_text(text).get(ch, {}).get("top")
        mark = "PASS" if got == want else "FAIL"
        ok += got == want
        print(f"  {mark}  want={want} got={got}  {text[:52]!r}")
    print(f"\n  {ok}/{len(SELF_TEST)} pass")
    print("  NOTE: passing a self-test authored with the scorer proves")
    print("  internal consistency only. It is not validity. See LIMIT 5.")
    return ok == len(SELF_TEST)

def main(argv):
    if "--self-test" in argv:
        sys.exit(0 if self_test() else 1)
    rows = [r for p in walk(argv or ["."]) if (r := score_file(p))]
    agg = collections.defaultdict(lambda: {"files":0,"F1":0,"F2":0,"F3":0,"F4":0,"max_breadth":0})
    for r in rows:
        for ch, f in r["channels"].items():
            a = agg[ch]; a["files"] += 1
            for k in ("F1","F2","F3","F4"):
                if f[k]: a[k] += 1
            a["max_breadth"] = max(a["max_breadth"], f["breadth"])
    print(f"{'channel':<20}{'files':>7}{'F1':>6}{'F2':>6}{'F3':>6}{'F4':>6}{'max breadth':>13}")
    for ch in CHANNELS:
        if ch in agg:
            a = agg[ch]
            print(f"{ch:<20}{a['files']:>7}{a['F1']:>6}{a['F2']:>6}{a['F3']:>6}{a['F4']:>6}{a['max_breadth']:>13}")
    print(f"\ndocuments scored: {len(rows)}")
    return rows

if __name__ == "__main__":
    main(sys.argv[1:])
