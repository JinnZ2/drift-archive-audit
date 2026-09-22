# Remedies — sorted by whether anything enforces them

**Produced by a cross-party observation, 2026-09-22:**

> Naming the class did not lower the rate. Two of seven instances sit inside
> instruments written after the class was named, to avoid it. Most of this
> programme's remedies are naming. If naming doesn't move the rate, the
> remedies that do are the structural ones — no PASS state, aborts on
> control failure, returns a set the reader didn't pick. **Build the
> property into the tool, don't document the hazard.**

## The test applied

    STRUCTURAL   a code path refuses, aborts, or returns a DIFFERENT VALUE
                 when the rule is broken. The user of the tool cannot
                 proceed incorrectly by forgetting.
    SEMI         a detector exists, but invoking it is discretionary.
                 Forgetting to run it restores the hazard in full.
    NAMING       a sentence in a document. Enforcement is memory.
    RECORD       counts what happened. Prevents nothing, and is not
                 supposed to -- listed so it is not miscounted as a remedy.

## The inventory

| remedy | kind | violated? |
|---|---|---|
| A2 hash gate — nothing scored before the reconstruction is hashed | SEMI | no, ~28 verifications |
| never edit an A2 file after hashing | SEMI | no (hash would show it) |
| **positive control before trusting any pattern-matched zero** | **NAMING** | **YES — `GUESSED.md` #18** |
| `UNSET`/`UNCLEAR`/`UNRECORDED` are values, never filled by inference | NAMING | not recorded |
| a guessed row is worse than an empty row | NAMING | not recorded |
| every claim carries a provenance label | NAMING | by omission, per `GLOSSARY.md` |
| no verdicts on content | NAMING | not recorded |
| edit the claim, not the data | NAMING | not recorded |
| a registered prediction is not reread after the result | NAMING | no — it held, and falsified the prediction |
| `reachability_sweep` has **no PASS state** | STRUCTURAL | — |
| `reachability_sweep` aborts on any of four control failures | STRUCTURAL | — |
| `reachability_sweep` key-unit control (no fragment keys) | STRUCTURAL | — |
| `guarded_count` — a zero is unobtainable without a live control | STRUCTURAL | — |
| `GUESSED.md` retraction ledger | RECORD | — |
| the three-column catch ledger (self / operator / cross-party) | RECORD | — |
| `PREDICTION-quantity.md` | RECORD | **both predictions falsified, 2026-09-22; the population was defective — `GUESSED.md` #19** |

    STRUCTURAL  4    three of them written on 2026-09-22
    SEMI        2
    NAMING      7
    RECORD      3

**Most of this programme's remedies are naming, as stated.**

## The number that matters

Of the seven logged instances of MATCH-UNIT MISMATCH (`CONTROLS.md`):

    prevented by the rule that names the class        0 of 7
    caught by a structural mechanism                  1 of 7   (C10, by the
                                                      corpus's own
                                                      falsification suite --
                                                      a process that RUNS)
    caught by a magnitude violating expectation       4 of 7
    caught by reading a diagnostic list               2 of 7

**Zero preventions from naming.** Instances six and seven occurred inside an
instrument written to avoid the class, by a party holding the class
definition in working memory while writing it.

That is the case for the reframe. It is not an argument that the naming was
wasted — the names are how the instances got *recognised as one class* — but
recognition after the fact is a `RECORD`, and this file exists to stop
`RECORD` being counted as `REMEDY`.

## Acceptance criteria for an instrument in this programme

Stated by the operator as three properties; taken here as **criteria a tool
must meet**, not advice it should follow.

    1  NO PASS STATE         no input can produce an all-clear. The output
                             is a list, a set, or a refusal.
    2  ABORTS ON CONTROL     a failed control stops the run. It does not
       FAILURE               warn and continue.
    3  RETURNS A SET THE     the reader does not choose the membership.
       READER DID NOT PICK   Recognising a member is then a real event
                             rather than a confirmation.

### Current instruments against the criteria

| instrument | 1 | 2 | 3 |
|---|---|---|---|
| `reachability_sweep.py` | ✔ | ✔ | ✔ |
| `guarded_count.py` | ✔ | ✔ | n/a — returns one reading |
| `channel_function.py` | ✖ **prints `PASS`/`FAIL` per case** | ✖ **self-test reports a ratio and continues** | ✖ scores inputs the caller chose |

`channel_function.py` fails all three and already carries two documented
construction flaws. **It is not repaired here.** Repairing it would mean
rebuilding the F1–F4 scorer around a different output shape, and the reason
to do that is not that this file says so — it is that the instrument's
findings currently arrive as a score the reader can accept. Filed as the
first item below.

Note what its own self-test says: *"passing a self-test authored with the
scorer proves"* nothing. **That is criterion 3, stated in the tool and then
not built into it** — the exact failure this file is about, in the instrument
that names it.

## Work-order consequence

For `STUDY.md`. Not an avenue — a constraint on every avenue.

    Any remedy proposed for an inside-party defect must state which kind it
    is. A NAMING remedy proposed for a class that already has a name is not
    a remedy; it is a second name.

Ranked by what they would have caught:

    1  rebuild channel_function.py to the three criteria    fails all 3
    2  make the A2 verification non-discretionary            SEMI -> STRUCTURAL
    3  a provenance label the tools require, not request     NAMING -> ?
    4  route every count in future work through
       guarded_count                                        already built
    5  run the unsatisfiable-requirement test AT THE MOMENT
       A REQUIREMENT IS ISSUED                               NAMING -> ?

**Item 5 comes from X-3** (`UNSATISFIABLE-REQUIREMENT.md`). The detector is
not missing: three of five open requirements in this repo were already routed
around correctly, each by naming the mechanism first. The one that failed had
its mechanism named **an hour earlier, by the same party, in the same
session** — and the requirement was issued anyway.

**So the gap is not knowledge and not naming. It is that nothing runs the
check at issue time.** Whether that can be made structural is open: a tool
would have to recognise a requirement as a requirement. Same difficulty as
item 3.

~~**Item 3 is open and may not be buildable.** A label cannot be enforced by
a tool that does not know what a claim is. Recorded as a limit, not a task:
**some hazards have no structural form, and for those, naming is what there
is.**~~ **WITHDRAWN 2026-09-22 — `GUESSED.md` #20.**

**The argument is refuted by an existence proof and the generalisation never
had support.** Obligatory evidential systems enforce a source-of-knowledge
field at the level of the **utterance**: the grammar does not classify a
claim, an unmarked assertion is simply ungrammatical. Same design as
`guarded_count`'s required positional control — a required field, not a
classifier — arrived at independently and deployed at the scale of whole
languages. See `EVIDENTIALITY.md` row 5 and `EVIDENTIALITY-CONSEQUENCES.md`.

    item 3   NAMING -> ?   becomes
             NAMING -> A STRUCTURAL FORM EXISTS. THIS CHANNEL DOES NOT
                       IMPLEMENT IT.

*Some hazards have no structural form* was stated from one hard case with no
search for a counterexample — **difficulty read as impossibility**, which is
the emptiness-implies-value error with the sign flipped.

The error is not naming — it is *counting a name as a fix and stopping
there.* And, added by #20: it is also **counting a hard conversion as an
impossible one and stopping there.**
