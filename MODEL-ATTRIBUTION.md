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

---

# Training-era marks

Status: **PROPOSED**, co-authored; outputs **DERIVED**. Run once, 2026-11-15,
on the same 13 clones. What is established: on this corpus the marks give
only weak lower bounds (2019-2021) on any writer's cutoff, the removed-API
inference is testable for one mark of eight, and no Python unit before
2026 carries a mark. Every date in the table is CARRIED from Claude's memory
and unverified.

Code: `instrument/era_marks.py` (imports `model_attribution` for units and
labels); table: `instrument/era_marks.json`; selftest
`python3 instrument/era_marks.py --self-test`; output
`era-marks-2026-11-15.txt`.

## Delivered specification

```
TRAINING-ERA MARKS (PROPOSED)
  library versions, API calls, deprecated functions,
  syntax features a model used → bounds its knowledge
  cutoff, independent of commit date
  e.g. code calling a function removed in 2024 → written
  by a model trained before that change
  calibrate on labeled commits first (same gate)
```

## What was built

- **Table** (`era_marks.json`): 22 marks. 14 INTRODUCED (Python 3.8–3.12
  syntax and stdlib: `:=`, `list[int]`, `removeprefix`, `functools.cache`,
  `zoneinfo`, `match`, `X | None`, `except*`, `tomllib`, `typing.Self`,
  `type X =`, PEP 695 generics, `typing.override`, `itertools.batched`).
  7 REMOVED (`collections.Mapping` aliases, NumPy scalar aliases,
  `distutils`, `imp`, `asyncore`, `openai.ChatCompletion.create`, `cgi`) and
  1 DEPRECATED (`datetime.utcnow`). Each row carries version and date,
  source CARRIED.
- **Matching:** Python units only, with comments, single-line strings and
  complete triple-quoted blocks stripped first, so a file that names a
  pattern does not fire (the table and this module are tested for that).
- **Two kinds, not symmetric.** INTRODUCED(D) puts the writer's cutoff on or
  after D (lower bound; can still be copied from context). REMOVED(D) is the
  specification's example: cutoff before D. That inference fails if models
  trained after the change still emit the old API, so it is tested first.
- **Gates, on labeled commits first:**
  - lower bounds: TABLE_CONSISTENT if no labeled unit uses an INTRODUCED mark
    dated after its own commit;
  - upper bounds, per mark: a label REACHES a removed mark when its own
    INTRODUCED marks put its cutoff on or after the removal date. A reaching
    label that still uses the mark is a COUNTEREXAMPLE. Reached and unused
    is NO_COUNTEREXAMPLE. Reached by no label is NOT_TESTED, and the mark
    gives no upper bound, because the test could not have failed on it;
  - label separation on era marks (the same repo-out calibration as the tool
    marks): reported. This module emits no label probabilities, so it gates
    nothing here.
- **Output per unlabeled unit:** marks present, `cutoff_at_least`,
  `cutoff_before_candidate` (only from NO_COUNTEREXAMPLE marks), withheld
  upper marks with their state, and whether the lower bound falls after the
  unit's own commit date. No label. Status DERIVED.

## Run, 2026-11-15

Python units 2793: reference 2268 (162 with any mark), target 522.

| check | result |
|---|---|
| marks in reference | `list[int]` 153, `X \| None` 59, `utcnow` 3, `:=` 3, `openai.ChatCompletion` 1 |
| marks in target | `list[int]` 16, `X \| None` 9, `utcnow` 10 |
| lower-bound gate | TABLE_CONSISTENT, 0 contradictions |
| label lower bounds | latest is 2021-10-04 (`X \| None`), for Opus 4.7, Opus 5, Opus 5.5, Manus, Perplexity; no labeled unit uses any 3.11 or 3.12 mark |
| upper-bound gate | `collections.Mapping` aliases NO_COUNTEREXAMPLE (reached by 5 labels, 0 uses); the other 7 NOT_TESTED, since no label's lower bound reaches 2022-12 or later. `openai.ChatCompletion` (1 use) and `utcnow` (3 uses) appear in labeled 2026 code, but no label's own marks place its cutoff after those dates, so they are not counterexamples |
| label separation on era marks | DOES_NOT_SEPARATE (repo-out 0.3439 vs null q95 0.49; commit-out 0.2816 vs 0.3419) |
| target | 27 MARKED, 495 NO_ERA_MARK. All 27 pre-2026 Python units (2025) carry no mark. The 17 units with a lower bound are dated 2026, bounds 2020-10-05 to 2021-10-04, none after its own commit date. The 10 `utcnow` units have their upper candidate withheld (NOT_TESTED) |

## Readings stated, not interpreted

- The marks that appear are all 2021 or older; none of the 3.11 / 3.12
  marks occur anywhere in this corpus, labeled or not. So lower bounds stop
  at 2021-10-04 for every writer.
- The removed-API inference was testable on one mark and not falsified
  there. On the other seven it was not testable here.
- `openai.ChatCompletion.create` and `datetime.utcnow` appear in labeled
  2026 commits. Whether that falsifies "removed → trained before" depends
  on those models' cutoffs, which this corpus does not bound late enough.

## Limits

- **Table dates are CARRIED, unverified** (release notes not reachable). A
  wrong date moves every bound that rests on it.
- **A mark can be copied** from code the writer was given; INTRODUCED is a
  lower bound on what reached the output, not proof of training data.
- **Absence is not a bound.** NO_ERA_MARK says nothing about cutoff.
- **Project constraints suppress marks.** Several of these repositories
  require Python 3.8 or 3.9 compatibility, which forbids exactly the newer
  syntax the lower bounds would need.
- **Patterns are regexes** over stripped text; multi-line strings that open
  outside the added lines are not stripped.
