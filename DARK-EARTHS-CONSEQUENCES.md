# What the dark-earths file does to this record

Companion to `DARK-EARTHS.md`, filed verbatim. Everything here is the
receiving session's.

## 1. IT LANDS ON THE PILOT — verified against the files, not relayed

`Keystone-Codex` carries `data/ecological/terra_preta.json`. Checked:

    region                 "Amazon Basin"        -- West Africa absent
    replication_regions    3                     -- REGIONS NOT NAMED
    evidence e4            "Modern biochar amendment trials reproducing
                           the fertility and carbon-retention effect on
                           degraded tropical soils outside Amazonia"
                           type: replication_record

**The entry's only replication evidence is modern biochar trials.** Under the
received file's Row 3, that is replication at the **recognition level** — the
literature that went looking — and not at the **practice level**. The one
documented independent pre-modern instance, still in continuous use, is not
in the entry.

### And the corpus already holds West Africa — in the wrong entries

`terra_preta.unlocks` = `regenerative_agriculture`, `carbon_sequestration`,
`circular_waste_systems`. All three exist as entries. All three name West
Africa in their `region` field:

    carbon_sequestration      Global (Amazonia, West Africa, East Asia...)
    regenerative_agriculture  Global (Amazon Basin, West Africa, South...)
    circular_waste_systems    Global (Japan, China, India, West Africa...)
    terra_preta               Amazon Basin

**West Africa is recorded as a property of the downstream global families and
not of the independent origin.** That is precisely the practice/recognition
split the received file drew, reproduced inside the corpus without anyone
intending it. The corpus knows about West African soil practice. It files it
as modern adoption.

### The scoring gap this exposes, which is structural

`rules/keystone_rules.json` v1.1:

    longevity      ">= 300 years durable or revivable; WHERE THE FIGURE IS
                    NOT DERIVABLE FROM THE ERA, THE ENTRY MUST DECLARE A
                    longevity_basis"                          weight 0.18
    replication    ">= 2 regions INDEPENDENTLY"               weight 0.14

**Longevity has a declared provenance field. Replication has none.** Checked:
`longevity_basis` appears in 7 entries; **no `replication_basis` exists
anywhere** — not in the schema, not in an entry, not in `validate.py`.
`src/prove.py::_c_replication` reads the integer and compares it to 2.

The word carrying the entire load is **"independently"**, and the received
file spent a whole document showing how hard that word is to establish. In
the corpus it is an unbacked hand-typed integer worth **0.14 of a 0.70 pass
threshold.**

**This is the defect v1.1's own revision note diagnoses**, and it was only
half fixed:

> v1.0 scored only what an author asserted about a technology (longevity,
> regions, unlocks, decentralization) and never scored the evidence behind
> the assertion, so an entry could reach 1.0 on four numbers typed by hand.

v1.1 added three evidence criteria **alongside** the four assertion metrics.
It did not back them. `replication_regions` is still one of the four numbers
typed by hand — and now it has a case where the number is 3, the regions are
unnamed, and an independent region exists uncited.

**REPORTED, NOT FIXED.** This audit is read-only on source repos and nothing
here is committed to `Keystone-Codex`. Whether to add a `replication_basis`
field, and what `terra_preta`'s three regions actually are, is that repo's
call.

## 2. The audit did not find this, and the reason is a scope statement

This session read `Keystone-Codex` repeatedly, scored it, and used
`terra_preta` as one of three positive controls. **It never looked at whether
a scored metric had evidence behind it**, because its measurand was *drift in
renderings over time*, not entry quality.

That is not an error — it is the declared scope. But note the shape: **the
finding arrived from outside the audit's measurand entirely, carried by a
literature search about soil.** Same shape as Row 4's outcome arm, now
operating on this audit. **Fourth instance of the disciplinary seam in this
run, and the first with the audit as the party holding the verdict.**

## 3. The first CLOSED case in the register — and the trap inside it

Every instance in `ABSENCE.md`, `DEFICIT-LOCATION.md` and `CALIBRATION.md`
MODE 3 is an absence still in force. The mechanism is inferred from the gap's
shape because the gap has never been seen to close.

**Row 4 is a closed one**, with all three arms recoverable: what held it
shut, what moved it, what it cost.

    held shut by   a nutrient measurand with no column for carbon; a
                   natural/anthropogenic binary applied AT INTAKE;
                   observations in one discipline never joined to another
    moved by       a category supplied from a different continent's
                   literature
    cost           ≥ the 1990 Zech remark to the Fairhead & Leach chapter

**THE TRAP, and it is stated because this session would otherwise walk into
it.** The part of Row 4 that confirms `DEFICIT-LOCATION.md` — *"not
anthropogenic" was the default returned by an instrument whose scope was not
declared* — is the part the received file marks **scope limit 3: DERIVED,
this session's, not stated in the source.**

    sourced      the misrecognition, and the nutrient-vs-carbon
                 attention gap
    inferred     that a scope limitation PRODUCED a classification
                 verdict

**The confirming half is the inferred half.** It is not admissible as support
for a frame this pair already believes. Recorded as `UNRATED`, and the
distinction is kept because collapsing it is how a frame gets confirmed by
its own restatement.

## 4. Undeclared instrument scope — now three instances, two of them sourced

    WALS               counts grammaticalized evidentials only. Africa
                       reads absent. Scope declared IN THE FILE, 150
                       lines from the row it governs.
    African soil       measured nutrients, no channel for carbon.
      analysis         Anthropogenic soils read natural. Scope NOT
                       declared.
    this programme     four positive controls, all corpus-side; none
                       demanded of an institutional instrument. Scope
                       not declared until GUESSED.md #18.

**The pattern is not that instruments have limited scope. It is that the
scope does not travel with the reading.** A number leaves its instrument and
arrives somewhere as a finding, with the inclusion criterion left behind.

That is the same operation as `d_type D3` — *status field dropped* — one
level up, in the literature rather than in a rendering. **Flagged and not
adopted: seventh tidy correspondence from this pair, measured survival 0 in
5.**

## 5. A possible escape from the binding constraint — untested

`STUDY.md` declares the binding constraint: five tasks terminate on **a
second party who holds the speaker's senses.**

Row 4 closed without one. What unblocked it was **a category supplied by a
different literature** — not a sense-holder, a frame-holder. That is a
different resource, and it is abundant where sense-holders are scarce.

    ROUTE      a second DISCIPLINE, holding a category the first lacks
    EVIDENCE   one closed case, sourced
    UNTESTED   whether it reaches THIS programme's blockages. Four of
               the five are annotation and sense-holding tasks, where a
               borrowed category does not obviously substitute for a
               sense. The fifth -- error-count interpretation -- might.

**Not offered as a solution.** Offered as the one documented case of a
constraint of this family being cleared, with the mechanism recorded, so that
it can be tested rather than hoped at.

## 6. The convergence instrument has now returned three different values

    RUN 1  data-sovereignty frameworks    FAILED
    RUN 2  grammatical evidentiality      PARTIAL
    RUN 3  the material record            SUPPORTED at practice level,
                                          CITATION-LINKED at recognition
                                          level

**An instrument that returns three different verdicts on three channels is
discriminating.** This programme has spent the day unable to demonstrate that
property for most of its own instruments; here it is, three times, with the
failure recorded first and the selection defect declared in each file's own
scope limits.

The received file's scope limit 6 states the correct reading and it is not
improved on here: *three runs, three channels — that is a pattern across
three cases, not a result.*
