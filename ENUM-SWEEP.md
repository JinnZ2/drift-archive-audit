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

---

# RE-RUN, SAME DAY — the control was not enough, and the result was wrong

**`GUESSED.md` #26.** The run below the line was reported as control-passed and
bounded at 51. **It was blind to an entire encoding.**

## CONTROL B, and the rule it refines

Control A is a **JSON Schema** enum. It fired, and the sweep was declared
working on the strength of it.

**Control B is the same concept in a different encoding** — a Python
`class X(Enum)` with `MEMBER = "value"` members. The first version could not
see that form at all.

    class(Enum) declarations invisible to the reported sweep,
    IN THE FOUR PILOT REPOS ALONE:        69

    AI-Consciousness-Sensors   35
    Emotions-as-Sensors        34
    Keystone-Codex              0
    Bio-Grid                    0

**A list reported as the bounded set of 51 was missing more than it
contained.**

### THE REFINED STANDING RULE

    A positive control proves the detector can see THE THING IT WAS
    POINTED AT. It does not prove the detector can see A DIFFERENT
    ENCODING of the same thing.

    Control on every encoding the concept takes, not on one instance
    of it.

**Ninth MATCH-UNIT instance.** The matcher's unit was `NAME = [...]`; the
author's unit was `class X(Enum)`. Granularity sub-form. Caught by no
property of the sweep, and not by quantity: 51 looked like a plausible
number.

**THE CATCH WAS LUCK, and is recorded as luck** — cross-party, 2026-09-22:
*"I named two fixtures I expected to exist; one happened to sit in the
encoding the sweep couldn't see. No design, no prediction."* **This is one
draw, not a method**, and it sits next to a control-discipline argument where
it could otherwise be read as one.

**The rule is worth more than the catch and does not depend on it.** Applied
to the whole instrument set in `ENCODING-AUDIT.md`.

**Both controls now required. The run aborts if either fails** — verified by
running it against the four pilot roots alone, where control B's fixture does
not exist: it aborts and prints nothing, which is correct.

## BOUNDEDNESS — restated, and it still holds

    roots swept                               6
    enum occurrences found                  230
    distinct member sets                    205
    removed by the declared member criterion 51
    DISTINCT SETS TO READ                   154

**154 lines, not 51.** Still bounded — ten minutes rather than three — so the
instrument's premise survives. **What did not survive is the first report of
it.**

## FIFTH DERIVED-AS-NEW — CONFIRMED on inspection

The operator flagged this as a candidate. **It holds, and it is larger than
one instance.**

    Logic-Ferret/knowledge/scope_mapper.py
      "Maps a study's claim to its actual scope. Outputs a structured
       ScopeMap showing where the finding is load-bearing AND WHERE IT
       GOES SILENT."

    Logic-Ferret/knowledge/shadow_catalog.py
      "A growing library of silence patterns. Studies go silent in
       PATTERNED ways."

      class SilenceCategory(Enum)  -- TEN members:
        selection, measurement, temporal, causal, ontological,
        contextual, population, interpretive, structural, incentive

      SELECTION    "who got into the study"
      MEASUREMENT  "what the instrument can touch"

**`SELECTION` is the survivorship structure this record logged four separate
appearances of today.** **`MEASUREMENT` is the undeclared-scope class, the
mode-3 exclusion, and `DEFICIT-LOCATION.md`'s *not admitted to the
measurement* — all three.**

**And `scope_mapper.py` is the scope-declaration instrument** that
`DARK-EARTHS.md` Row 4 re-derived and that Shadow Hunting step 2 was named as.

    derived as new by this audit today, already in the corpus:
      the survivorship class       = SilenceCategory.SELECTION
      the undeclared-scope class   = SilenceCategory.MEASUREMENT
      scope declaration            = scope_mapper.ScopeMap
      the silence register itself  = shadow_catalog

`ABSENCE.md` has three states. **The catalog has ten categories, machine-
readable, CC0, and it was vendored into this repo's reach.**

**Operator's note, recorded verbatim in substance:** *declared as a relation
type, vendored into this repo, and I still built the thing today.* The
finding is not that the audit missed a distant repo. It is that the material
was adjacent and the audit had no term to reach it with — `FINDABILITY.md`,
fifth instance.

---

# ORIGINAL RUN — superseded above, kept as the raw reading

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

---

# ADDENDUM 2026-09-22 — the new item, and what was not built

## "Exports consumed by nothing" — SPECIFIED, NOT INSTANTIATED

    A repo exporting named entities that no other fieldlink consumes is an
    instrument with no downstream -- either genuinely terminal, or a join
    nobody made. Both are informative, and the distinction is one human
    look.

**Design recorded. Not built this turn**, for the reason stated last turn and
not weakened by a second opportunity: `FINDABILITY.md` found that the reflex
to build is the wrong response to a gap, in a session that built five
instruments today. Building unasked, twice running, would be that reflex
operating through the file that names it.

**Its control is already specified by the operator** and half of it has
already fired, in a way worth recording:

    control target 1   Logic-Ferret's scope pipeline
                       -> scope_mapper.py, CONFIRMED to exist. And the
                          enum sweep FAILED to surface it until control B
                          was added, which is exactly why this control
                          was named.
    control target 2   Noise-as-Information's falsification log
                       -> docs/FALSIFICATION_LOG.md, CONFIRMED to exist.
                          Already the source of MATCH-UNIT instance five
                          (C10).

**Both fixtures exist and are readable.** The sweep that would use them is
not built.

## The pilot gate, and why these two repos were read

`logic-ferret` and `Noise-as-Information-Sensor` are **control fixtures, not
pilot repos.**

    read      yes, read-only
    scored    NO
    A2 hash   none exists for either, and none was made

The gate this record holds is *nothing is scored before its A2 hash*, and
*do not expand the pilot until the operator reviews verification* — the three
`verify/*.txt` forms are still blank. **Neither repo is scored here.** They
are used as test fixtures for an instrument, which is a different operation
from being audited, and the distinction is stated rather than assumed.

Precedent: several non-pilot repos were already cloned read-only earlier in
this session for the same purpose.

## A transmission fact, stated not diagnosed

**Two consecutive instructions have arrived carrying item 3 of a numbered
list, with items 1 and 2 absent from this session's context.**

    previous turn   "3. Imperative lines..."    item 2 not received
    this turn       "3. Exports consumed by
                     nothing..."                items 1 and 2 not received

**The mechanism, supplied cross-party and now in `GLOSSARY.md`:**
*reconstructing an instruction from what it probably said is how a cached
field becomes an asserted one.* The rule bites hardest where the
reconstruction would obviously be right — obviousness is the shared context,
and filling the slot converts that context into a claim the record carries as
its own. **An empty slot stays legible as a gap. A filled one does not.**

Recorded as a fact about what reached this side. **Not reconstructed, not
diagnosed, and no inference drawn about cause** — filling the slots by
inference is what this record forbids, and the pattern is noted only because
a second occurrence makes it a pattern rather than an incident.
