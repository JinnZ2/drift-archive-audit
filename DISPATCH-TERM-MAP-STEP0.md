# Dispatch: TERM_MAP as a generated view — STEP 0 REPORT, STOPPED

**Step 0 says locate before building and stop if anything is missing.**
Nothing is missing. **Three other things are, and each needs a fiat call the
dispatch forbids me to make.** Nothing was built; no commit touches
`Simulators`.

## PATHS — all three found

    cooperative-substrate/term_table.py        FOUND
    tools/check_term_collision.py              FOUND
    term-drift-citation/                       FOUND
    TERM_MAP.md anywhere in the repo           DOES NOT EXIST
                                               (step 6's "if one already
                                               exists" branch is moot)

**Four more the dispatch does not name, located by the same pass:**

    tools/sourced.py                 value + source + locator, or UNRATED
    tools/validate_claim_table.py    CLAIM_TABLE.json schema validation
    tools/check_gate_drift.py
    tools/known_answer.py

## STOP 1 — `term_table.py` is not a general term table

Step 1 says *extend `term_table.py`'s schema*. **It has a different key
space.**

    TERMS       5 concepts: cost asymmetry · incentive direction ·
                accounting boundary · whether a legitimate other is
                representable · does the accounting stance preserve or
                destroy the measurement it depends on
    SUBSTRATES  5: foraging/predation ecology · multiagent AI harnesses ·
                human societies and mutual aid · morality/ethics claims ·
                nation-state sovereignty
    CELLS       (term, substrate) -> MEASURED | MISSING |
                SCOPE_DIFFERENT | UNRECORDED
    BASIS       names pack items: "E1.1-E1.3 (profitability = E /
                handling time; cost terms)", basis_status
                UNVERIFIED-FULLTEXT

**It is E7's cross-substrate evidence matrix.** Its rows are *concepts
measured in substrates*; TERM_MAP's rows are *coinages mapped to existing
English*. `operator_fit`, `coiner` and `source_kind` have no cell to attach
to — they are properties of a mapping, and there is no mapping here.

**What I said two turns ago, and it was correct as far as it went:** the
*rule* is shared — *nothing filled from memory; a non-UNRECORDED cell needs
a basis.* **The rule transfers. The table does not.**

    the fiat call I am not making:
      overload E7's evidence-pack table with a second, unrelated key
      space, OR create a new table inside that module and call it an
      extension.

## STOP 2 — step 4's premise is false, and I ran it to find out

    python3 tools/check_term_collision.py
    occurrences of "Dissonance" in the output:  0

**It is not a general collision detector.** Its `TERMS` is a hardcoded dict
of four regexes:

    "change of mind"            change[sd]?\s+of\s+mind|changed\s+...\s+mind
    "self-questioning"          self[-\s]question
    "constant re-evaluation"    \b(?:constant|continuous|ongoing)\s+re-?evaluat
    "re-evaluation (bare)"      \bre-?evaluat

Those are **PREAMBLE.md's declared TERM COLLISION note**, and the tool's job
is to find where those four appear and report which modules carry the note.
It answers *who uses the declared colliding terms*, not *which terms
collide*.

**So `Dissonance` cannot surface mechanically without first being declared
in PREAMBLE.** Reported as the dispatch asks, and the reason is structural
rather than a defect.

    the fiat call I am not making:
      decide whether to generalise the tool, or to add Dissonance to
      PREAMBLE's note so the existing tool picks it up. Those are
      different repos-worth of decision.

## STOP 3 — no push access to `Simulators`

    remote: https://github.com/JinnZ2/Simulators   read-only clone

Every step from 1 to 7 ends in a commit. **None can land.** Attaching with
push access is a call for the operator, and the last attempt in this session
was denied by the environment before later succeeding on retry.

## FINDING — step 2 is already built, and stricter

`tools/sourced.py`:

> A value and its source travel together. Three fields on every extracted
> value: the **VALUE**, the **LITERAL SOURCE TEXT** it came from, and the
> **LOCATOR** — which document, which line, which columns. Then one gate.
> **Anything entering a scoring function carries all three or the scoring
> function returns UNRATED: not zero, not clean, not a default.**

Step 2 proposes `candidate_basis = "model_recall 2026-09-22"`. **Under
`sourced.py` that string is not a basis**: no literal source text, no
locator. It returns `UNRATED` — which is the outcome step 2 wants, reached
by an existing gate rather than a new field.

**Ninth piece of existing machinery located in three turns.** The dispatch
names three; the pass found seven.

## GUESSED.md #37 — I reported these tools without running them

Two turns ago, in `TERM-MAP-RECEIVED.md`:

> `check_term_collision.py` … **is TERM_MAP's CONFUSION RISKS table, as a
> running tool. The one row there (Dissonance) is what it finds
> mechanically.**

**False. One command showed it.** The tool scans four declared phrases and
`Dissonance` is not among them.

**And the shape of the error is the one this record keeps logging.** I ran
the FIND check, located the tools, read their docstrings, and reported their
capabilities from the docstrings. **Finding is not verifying.** The check I
credited myself with — *2 of 8 found by looking* — did half the job and I
reported it as whole.

    #32   inferred a file's function from its NAME
    #37   inferred three tools' capability from their DOCSTRINGS
          -- and one of the three was running in the same repo,
             one command away, for three turns.

## THE OPERATOR'S TWO ITEMS — both recorded

**1. Whose miss.** Recorded as stated, `OBSERVED`: TERM_MAP was built
without searching the corpus, three instruments already held its parts, and
findability instance #7 originated on the operator's side. **No reading
added.**

**2. Provenance flag, and it reaches this repo.** Every `existing_term` and
`source` in both relayed tables rests on **model recall — nothing retrieved,
nothing checked.** Under `term_table.py`'s rule and `sourced.py`'s gate those
cells are `UNRECORDED`.

**Both relayed files in this repo now carry that flag in their receipts.**
The verbatim bodies are untouched; the tables still read `MATCH` and
`STRONG`, and the flag says what is under them, which is nothing yet.

## WHAT WOULD UNBLOCK EACH

    STOP 1   the operator says where a mapping table lives: a new module,
             or a second table inside term_table.py, or somewhere else
    STOP 2   the operator says generalise the tool OR declare Dissonance
             in PREAMBLE
    STOP 3   push access to JinnZ2/Simulators

**Steps 3, 5, 6 and 7 are mechanical once 1 and 3 are answered.** Step 2 may
not need building at all.
