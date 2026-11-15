# REPO ARCHAEOLOGY — model attribution from tool marks

Status: **PROPOSED** instrument, co-authored; every output is **DERIVED**.
Run once, 2026-11-15, on 13 local clones. What is established: on this corpus,
tool marks separate the labeled reference set only for markdown, and only
weakly; for Python, JSON and other files they do not, so those units are not
attributed. Most of what the date prior gains comes from the dates, not the
marks. Nothing here establishes which model wrote any unlabeled file.

**INTEREST.** Written by a Claude model. Claude models are in the candidate
set. The calibration, the null and the date control are the parts a reader
can recheck without trusting the author.

Code: `instrument/model_attribution.py` (stdlib). Selftest:
`python3 instrument/model_attribution.py --self-test`.
Run output: `model-attribution-2026-11-15.txt`.

## Delivered specification

```
REPO ARCHAEOLOGY — model attribution (PROPOSED)
1 DATE PRIOR  commit date → which models existed and which
              interfaces she used then → candidate set
2 TOOL MARKS  per file: comment style, docstring format,
              naming habits, stock phrases, library choices,
              error-handling patterns
3 CALIBRATE   known recent commits (Claude Code / Opus /
              Fable / Manus, labeled) = reference set;
              test whether marks separate them before
              trusting anything older
4 OUTPUT      probability per model, never one label;
              status DERIVED; "unattributable" allowed
5 CONTROL     shuffled dates → attribution should degrade
```

Why here: `CORRECTION-001` says the git author field names the pusher, not
the content author. This asks whether the content carries its writer's marks.

## What was built

| Step | Implementation |
|---|---|
| unit | (commit, file): the lines the commit added to that file, at least 8 non-blank. Merges skipped. Compared only within one file kind (py / md / json / other). |
| labels | Read from the commit only. `Co-Authored-By: Claude <model>` → that model; `Manus` / `Perplexity` trailers → that name; commits merged from a `manus/` branch with no other model trailer → Manus. A bare "Claude" trailer or two model trailers → AMBIGUOUS, kept out. A person's co-author trailer is not a label. Everything else is the target set. |
| 1 date prior | Candidate set = labels **first seen** in this corpus on or before the unit's date. First-seen is an observed upper bound on availability, not a release date, so the prior excludes on absence of evidence. Interface prior: `interfaces.json`, **UNDECLARED** (operator knowledge, not authored here). |
| 2 tool marks | Per unit, ratios only (no text kept): line length, non-ASCII, em dashes, `--`, emoji, a declared stock-phrase word list, caps tokens, backticks; for Python also comment style, docstring quotes and format (Google / NumPy / reST), snake vs camel names, identifier length, type hints, f-string vs `.format` vs `%`, imports (numpy, pathlib, os.path, argparse, dataclasses, typing, unittest, pytest), try / bare except / raise / assert / print rates; for markdown headings, bullet style, numbering, bold, tables, fences; for JSON key case and indent. |
| 3 calibrate | Nearest centroid on z-scored marks, probabilities by softmax. Statistic: mean probability given to the true label. Leave-one-COMMIT-out and leave-one-REPO-out, each against a null of labels shuffled across commits (R = 40, seeded). **Gate:** leave-one-REPO-out must SEPARATE for a kind before any unlabeled unit of that kind is scored. |
| 4 output | Per unit: state, probabilities over every reference label, the same with the date prior, candidate set, status DERIVED. No field names one model (asserted in the selftest). States: `ATTRIBUTED_AS_DISTRIBUTION`, `UNATTRIBUTABLE` (outside every label's envelope, or no reference label observed by that date), `NOT_ATTRIBUTED` (gate closed). |
| 5 control | Commit dates shuffled across reference commits (R = 40); the date-prior statistic should fall. Added: a dates-only baseline (marks ignored), so the date prior's gain can be split from the marks'. |

`--choices` prints the 12 `[CHOICE n]` decisions the specification left open.

## Run, 2026-11-15

Repos (HEAD, commits read with `--all`): Bio-Grid-American-Manufacturing-
9af3f9ddd1, Noise-as-Information-Sensor 4dd23212f1, Polyhedral-Intelligence
859cd4982f, chain-position-detectability 015eb8fc78, decision-aperture
38d6b1b125, differential-frame-core f169b09109, drift-archive-audit 2ecb26596c,
explorative-math 3b8e9abfed, hands-lie-detector eedf547f1a, method-layer
466d6f21d9, orbital-phycom 5ac081aa74, simulators 38a77bc81b, study-aperture
15a0e92642. Five clones were unshallowed first (`git fetch --unshallow`); no
repository content was changed.

Units 9909: reference 8046, target 1813, ambiguous 50.

| kind | labels | commit-out (stat / null q95) | repo-out (stat / null q95) | gate |
|---|---|---|---|---|
| py | 10 | 0.1175 / 0.1231 DOES_NOT_SEPARATE | 0.1476 / 0.1577 DOES_NOT_SEPARATE | closed |
| md | 9 | 0.1276 / 0.1128 SEPARATES | 0.1711 / 0.1589 SEPARATES | open |
| json | 7 | 0.1547 / 0.2055 DOES_NOT_SEPARATE | 0.2692 / 0.2907 DOES_NOT_SEPARATE | closed |
| other | 8 | 0.1298 / 0.1712 DOES_NOT_SEPARATE | 0.2040 / 0.2922 DOES_NOT_SEPARATE | closed |

Date control (leave-one-commit-out, first-seen recomputed without the held commit):

| kind | marks only | dates only | marks + true dates | marks + shuffled dates (median) | state |
|---|---|---|---|---|---|
| py | 0.1175 | 0.1796 | 0.2143 | 0.1219 | DEGRADES |
| md | 0.1276 | 0.2380 | 0.2582 | 0.1648 | DEGRADES |
| json | 0.1547 | 0.3169 | 0.3081 | 0.1595 | DEGRADES |
| other | 0.1298 | 0.2166 | 0.2506 | 0.0965 | DEGRADES |

Target units: py 522, json 328, other 169 `NOT_ATTRIBUTED` (gate closed).
md 794: 318 `ATTRIBUTED_AS_DISTRIBUTION`, all dated 2026-07 or later; 476
`UNATTRIBUTABLE`, of which 422 have no reference label observed on or before
their date (every md unit before 2026-07, including the whole 2025 paste era)
and 54 fall outside every label's envelope. Per-unit records are in the
`--json` output, which is regenerable and not committed.

## Readings stated, not interpreted

- The gate is closed for three of four kinds. For markdown it opens at 0.1711
  against a null 95th percentile of 0.1589.
- The date control degrades in every kind, as specified. The dates-only
  baseline is within 0.04 of marks-plus-dates for py, md and other, and above
  it for json.
- The earliest label in the reference set is first seen 2026-07-02. No unit
  before that date has a candidate, so nothing older is attributed.

## Limits

- **Labels are trailer self-reports.** A trailer is transport evidence: the
  tool that committed names itself. It is not a fact about who wrote the text,
  which is the same distinction `CORRECTION-001` draws for the author field.
- **Label is confounded with date, repo and topic.** Leave-one-repo-out is the
  partial guard; nothing separates model from task.
- **Manus and Perplexity are small** (26 py / 26 md Manus units), and Manus
  branch labels cover only `manus/` merges.
- **First-seen is not release.** A model in use before its first trailer in
  this corpus is excluded by the prior before that date.
- **Interface prior UNDECLARED.** Step 1's interface half is empty until the
  operator fills `interfaces.json`.
- **Features are a word list and ratios.** The stock-phrase list is declared;
  a paraphrase steps around it. z-scoring is done once over the whole
  reference set, so a held-out commit leaks into the scaling (stated in code).
- **Paste-era content** (`CORRECTION-001`: model output pasted from chat) is
  the material the specification is aimed at, and the reference set has no
  label covering it.
