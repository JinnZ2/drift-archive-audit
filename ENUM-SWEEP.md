# Enum sweep — FIND converted into a reading task

**Run 2026-09-22 on the operator's instruction: cheapest first, positive
control first.** Instrument: `instrument/enum_sweep.py`. Output artifact:
`enum-sweep-2026-09-22.txt`.

## POSITIVE CONTROL — fired

Per standing rule, before any result. The sweep had to recover the one enum
already known to have been missed: `Keystone-Codex`'s evidence-type enum,
whose non-assertion members are what should have produced the `ENACTED`
provenance grade hours before it was derived as new.

    POSITIVE CONTROL: FIRED.

    recovered, in full, and visible in the list body:
      archaeological_record, peer_reviewed_study, ethnographic_record,
      primary_text, engineering_record, replication_record,
      radiocarbon_date, standards_spec, field_measurement,
      oral_tradition_encoded

**The run aborts and prints nothing if this does not fire.** A sweep that
cannot recover a known instance says nothing by returning few — the failure
this record has logged three times as a false zero.

## BOUNDEDNESS — the claim under test, and it holds

    roots swept                               4
    enum occurrences found                   70
    distinct member sets                     63
    removed by the declared member criterion 12
    DISTINCT SETS TO READ                    51

**51 lines is a few minutes of reading.** That is what decides whether this
instrument works, and it is reported before the list rather than after.

The removed 12 are prose constants and regex tables the Python channel caught
— module-level string collections that are not closed sets. **The criterion is
on FORM** (member length ≤ 60, no sentence punctuation, no newline), **was
statable before the run**, and both counts are printed so the filtering stays
auditable rather than becoming a tuning step.

## WHAT THIS DOES TO THE CONSTRAINT

    FIND, before   needs a party fluent in BOTH vocabularies
                   -> declared the scarcest constraint on the list,
                      strict subset of DEFINE's population, silent
                      failure mode
    FIND, after    needs a party who will read 51 lines
                   -> READER-SIDE. Substitutable.

**An enum does not need a term to find.** It is a closed set someone wrote
down because the distinctions in it mattered enough to enumerate. That is why
it is reachable from a vocabulary that does not contain any of its members.

## THE CLASS GOES TO n = 3, WITH A MECHANISM

Third member of the substitutable-party class, after arm-H3b coding and
cache-dependency sufficiency. **And the operator's point is that this is a
mechanism rather than a resemblance:**

    all three hand a party a BOUNDED OBJECT and a RULE STATED BEFORE
    THEY SEE IT

      H3b coding            a pre-registered coding rule, coder blind to
                            condition
      cache sufficiency     read a section, report where you stop
      enum sweep            read 51 lines, report what you recognise

**That is why the party is substitutable: nothing in any of the three
requires this particular reader.** The rule does the work the reader's
identity would otherwise have to do.

**FLAGGED.** The promotion from resemblance to mechanism at n=3 is exactly
the reading `SPEC-SHEET.md` §2 says this instrument returns — it leaves the
record tidier. The claim is the operator's; **the acceptance would be this
session's, which is `GUESSED.md` #22's lesson.** Held `PROPOSED, n = 3`.

## A CONSTRUCTION FAILURE, RECORDED — eighth MATCH-UNIT instance

The first version of the Python channel used a nested-quantifier regex:

    ((?:\s*["\'][^"\']+["\']\s*,?\s*)+)

It backtracked catastrophically on a long non-matching line and **hung the
run past 120 seconds.** Replaced with a linear two-stage scan; the dead regex
is kept in the source with a comment rather than deleted.

**Eighth instance of the MATCH-UNIT family, and its failure mode is one this
record had not logged: cost, not correctness.** The pattern was not wrong. It
never finished.

**And a detector that never finishes returns nothing, which is
indistinguishable from an absence.** A timeout manufactures a false zero by a
different route than a bad pattern does — and `guarded_count`'s protection
does not cover it, because no reading is produced to guard.

**Third time this class has recurred inside an instrument built after it was
named**, in this case the instrument built to make FIND cheap.

## THE LIST IS HANDED OVER UNREAD FOR SIGNIFICANCE

`enum-sweep-2026-09-22.txt` is in this repo. **This session has not picked out
which of the 51 matter, and will not.**

Judging significance is the part that needs the other vocabulary. Pointing at
candidates would be this session applying its corpus sense to terms that may
not carry it — `GUESSED.md` #23, which happened today, in a tool.

**The control instance is the only one this session can vouch for**, because
it was already known. Everything else in the list is a reading task for a
party who can do it, and that is not a limitation of the sweep. **It is the
sweep working as specified:** it produces the bounded object; it does not
produce the reading.

## THE THREE-ITEM LIST — one item is not in this session's context

The instruction arrived as an ordered list. **Item 2 is not present in what
reached this session.** Items received:

    1  enums          -- bounded, mechanical to collect. RUN, this file.
    2  [NOT RECEIVED] -- recorded as a gap, not inferred
    3  imperative lines -- must, never, abort, refuse, requires, before.
                        Design constraints are written as commands
                        regardless of domain vocabulary, and that is
                        where scope declarations actually live.

**Item 2 is left as an empty slot rather than reconstructed.** Filling it by
inference is the thing this record forbids, and a three-item list arriving
with one item missing on the receiving side is itself a reachability instance.

### Item 3 is SPECIFIED, NOT INSTANTIATED — deliberately

The design is stated above and is buildable. **It was not built this turn.**

`FINDABILITY.md`'s finding was that the reflex to build an instrument is the
wrong response to a gap, in a session that built four instruments in one day.
**Building item 3 immediately, unasked, having just recorded that, would be
the reflex operating through the file that names it.**

The instruction was an ordering — *cheapest first is 1* — and 1 is done.
Item 3 waits for a word.
