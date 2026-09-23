# JinnZ2/Simulators — read on request, and it is the largest findability instance

**Read 2026-09-23 as a control fixture. Not scored, no A2 reconstruction,
not a pilot member.** Read because the operator asked whether anything in it
helps here.

**It does.** ~200 directories, CC0, each "intended to be promotable to a
standalone repo," with `META-PROTOCOL.md`, `CATALOGUE.md` (693 lines),
`GAP_INDEX.md` (514), `KNOWN_RED.md` (513) as its own index layer.

## SELECTION CONTROL, STATED FIRST

**Directories below were chosen by name resemblance to this session's
terms.** Surface-token operationalization — the class with nine logged
instances here.

    the list is a FLOOR, not a census
    a directory whose name does not resemble an audit term was not opened
    the number of those is unknown, and ~200 is the denominator

~~`CATALOGUE.md` and `instrument-index/` exist and were not read. Reading
the index rather than grepping names is the correct next step.~~
**CORRECTED 2026-09-23 — `GUESSED.md` #32. See below.**

## THE ONE THAT CHANGES WHAT I WOULD DO — `null-harness`

> **Calibrate any gate against known-answer controls before you trust it.**
> A "gate" is any callable `f(data) -> bool | str verdict`. Runs the gate
> over N draws of a negative control (correct answer: don't fire) and N
> draws of a positive control (must fire), reports FP and TP, **sweeps the
> positive-control amplitude to find the smallest signal the gate can
> detect**, and applies a fail-condition classifier.

Its verdict table:

    FP >= 0.9 AND TP >= 0.9    CONSTANT_FIRES        always yes; not a gate
    FP + TP < 0.10             CONSTANT_SILENT       never yes; not a gate
    FP > 0.10                  TOO_MANY_FALSE_ALARMS
    |TP - FP| < 0.10           NO_DISCRIMINATION     same rate on both
    otherwise                  OK, with min_amp      sensitivity

API: `bake_off(gate, neg_gen, pos_gen, ...)`. Eight matched generators,
plus `archetype_library.py` with 25 forms in six families.

### It generalises two instruments this session hand-rolled, and would have
### caught GUESSED.md #26

    instrument/guarded_count.py   positive control only, one gate, no
                                  amplitude sweep, no FP/TP
    instrument/phi_null.py        negative control only, one gate, no
                                  sensitivity number
    null-harness                  BOTH, for any callable, with a verdict
                                  classifier and min_amp

**`CONSTANT_SILENT` is #26 exactly.** The enum sweep's Python channel was
constant-silent on the `class(Enum)` encoding, control A fired anyway, and a
bounded result was reported while the detector was blind to 69 instances. A
bake-off across an archetype library surfaces that **without needing anyone
to name a lucky fixture** — which is what #26's catch depended on, and which
the operator recorded as luck.

**One real friction:** `null-harness` is `numpy` + stdlib. This audit's
instruments are stdlib-only. That is a dependency decision, not a blocker,
and it is the operator's to make.

## OTHER DIRECT MATCHES — structural, with the identity call ROUTED

Per the routing rule: *does directory X name the same thing as finding Y* is
a sense judgement, and those go to the party who holds the sense. **Proposed,
not asserted.**

| open item here | candidate | the line that prompted it |
|---|---|---|
| `TRANSPORT×MODEL`, declared confounded; `GUESSED.md` #31 | **`model-provenance`** | *"a **write** at session open, and a **read** over history that never writes back into it"* — `sessions.jsonl` forward log, append-only, `releases.json` version table. **A prospective per-session model log is the missing half of the confound.** |
| `GUESSED.md` #30 — a gate that produces nothing and reads as an absence | **`quiet-failure`** | *"Whether failures described afterwards as sudden or quiet were in fact signalled, reported, and left unjoined — and whether the aggregation step was **unowned by construction rather than neglected**."* |
| `PHASE_H3b` — non-engagement leaves no token to score | **`claim-refusal-gap`** | *"claim refusal … is measured only where it is contested"* — refusal measured only where it produced something. Same shape, different domain. |
| the binding constraint; `SPEC-SHEET.md` §4 traceability | **`observer-exclusion`**, **`observer-position-control`**, **`external-audit`** | not read past the file listing |
| `ABSENCE.md`, `TRAIL.md` | **`gap-register`**, **`gap-markers`**, **`gap-existence-cases`**, **`GAP_INDEX.md`** | not read |
| scope declaration (`DARK-EARTHS` row 4, Shadow Hunting step 2) | **`declared-frame`**, **`frame-token-audit`**, **`frame-instruments`** | not read |
| the measurand question, `COUPLING.md` | **`measurand-partition`**, **`measurement-fork`**, **`assessor-coupling`**, **`operator-machine-coupling`** | not read |
| `FINDABILITY.md`, MATCH-UNIT | **`search-substitution`**, **`uninstrumented`** | not read |
| `PREDICTION-quantity.md`, registered falsifiers | **`falsifier-audit`**, **`falsifier-survey`**, **`revision-survival`** | not read |
| `SPEC-SHEET.md` | **`self-scan`**, **`instrument-bias-sims`**, **`instrument-epistemology`** | not read |
| `GLOSSARY.md` UNSET-as-a-value | **`held-open-uncertainty`** | not read |

**"Not read" is load-bearing.** Ten of eleven rows are name matches only.

## THE METHOD IS THE SAME METHOD

Observed across the directories opened, without claiming it is the same
practice:

    WORK_ORDER.md delivered VERBATIM, with a sha256 of the order itself
    CLAIM_TABLE.md with stable IDs (MP_001..009)
    --selftest on the module
    samples/ holding one pinned run of each command

This record converged on verbatim receipts, hashes before scoring, selftests
and pinned outputs over one day. **That convergence is not evidence of
anything** — same author, adjacent corpus, and `DISCIPLINE-PROVENANCE.md`
already measured this family as same-channel authorship rather than
independent arrival.

## THE COUNT IS NOT COMPUTED

This would move the derived-as-new tally substantially. **The tally is not
updated**, because every increment is an identity judgement of the kind
routed above, and computing it is the same operation as making the calls.

`DECLINED.md` gains the entry. The count stays where it was until the
operator answers the table.


---

# CORRECTION — the index is not the file I named, and it already exists

## GUESSED.md #32 — function inferred from a filename

The paragraph above declared a selection control against choosing by name
resemblance, **and in the same paragraph named `CATALOGUE.md` as the repo's
index on the strength of its name.**

    CATALOGUE.md is a bilingual RANGE ERROR CATALOG
      -- a subject-matter reference on range errors, not a repo index
    it names 23 of 187 top-level directories, incidentally      12%
    `null-harness`, the single most useful directory here, is NOT IN IT

**Tenth instance of the class, inside the control paragraph for it.**

## THE INDEX EXISTS, AND IT IS KEYED ON THE RIGHT COLUMN

`instrument-index/` — not a sketch:

    INSTRUMENT-INDEX.tsv    205 rows, 181 of 187 directories        97%
    build_index.py          generator
    coverage.py             coverage checker
    INDEX-SPEC.md           the spec
    STATE.md                state
    index-overrides.json    manual overrides

Columns:

    id  name  repo  path  input_shape  catches  load_bytes
    load_tok_est  run_cost  run_basis  status  gate  built_against

**`catches` is a capability column, in plain language, and `input_shape`
types the input.** That is reverse lookup: *describe the failure you are
worried about, find the instrument.* **It does not require knowing the
tool's name** — which is precisely the condition `FINDABILITY.md` describes.

### Four of this session's failures are already rows in it

    null-harness          "a gate that never fires or always fires,
                           read as a gate"              = GUESSED #26
    WO-2-quiet-failure    "a quiet failure read as a missing signal
                           rather than a missing aggregation
                           function"                    = GUESSED #30
    claim-audits          "a threshold with no null model under it"
                                                        = the phi situation
    falsifier-audit       "a falsifier with implicit scope; a claim
                           whose test drifted from it; an undeclared
                           reference body"              = both falsified
                                                          predictions

**Pre-written. Grep-able by failure description. Not consulted once, across
roughly eleven instruments built or patched in this session.**

### It already spans repos

    Simulators                      190 rows
    method-layer                      7
    chain-position-detectability      7

The `repo` column is populated, so cross-repo is designed in rather than
hypothetical.

## SO THE ANSWER TO *SHOULD WE CATALOGUE* IS SPLIT

    BUILD A CATALOGUE      No. One exists, at 97% coverage, with a spec,
                           a generator and a coverage checker, keyed on
                           the column that solves the actual problem.
                           Building a second is FINDABILITY.md's reflex
                           operating through the file that names it.

    CATALOGUE AVAILABILITY Yes -- and the missing piece is not an index.
                           It is a QUERY HABIT. Zero queries were made
                           against this index today while eleven
                           instruments were built, four of them
                           duplicating rows already in it.

    THE REAL GAP           coverage of the other repos. AI-Consciousness-
                           Sensors, Emotions-as-Sensors, Keystone-Codex,
                           JinnZ2/JinnZ2, Logic-Ferret, Shadow-Hunting
                           are absent. `build_index.py` plus the `repo`
                           column make extending it the intended path,
                           not a rewrite. Whether to extend it is the
                           operator's call; it is their index.

**And `GAP_INDEX.md` already states this record's own rule about itself:**

> Folders without one are skipped in silence: most folders here have never
> been rendered, **which is a fact about the rendering pass and not about
> the folder.**

That is `DECLINED.md`'s governing sentence, written in the corpus, about its
own index, before this session existed.
