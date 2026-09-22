# C-7 — culture > consciousness > emotions, scored against an unmediated reference

## Status: GATED. The gate is the operator's reference description.

Proposed as a three-level test. The protocol's first step is the whole point:

    1  REFERENCE FIRST   operator describes each one now, voice, unaided,
                         dated. HASH IT BEFORE ANYONE READS THE OLD
                         RENDERINGS.  (same rule as the A2 gate)
    2  COLLECT           every rendering, with date and source model
                         where known (else UNSET)
    3  SCORE             kept / reworded / replaced / dropped, per claim
    4  SPLIT             does loss cluster by model, by date, or by
                         encoding form?

**Do not run step 2 before step 1 is hashed.** This audit's A2 gate exists
for exactly this reason and held; C-7's gate is the same gate one level up.

## Contamination: I am already disqualified for two of the three levels

Stated before anything else, because it determines who may score.

| level | my state | usable as scorer? |
|---|---|---|
| culture (`JinnZ2/JinnZ2`) | **not read.** Never in session scope. One fragment reached me — see below | borderline |
| consciousness (`AI-Consciousness-Sensors`) | its `CLAUDE.md` was in my context from turn 1, before any work began | **NO** |
| emotions (`Emotions-as-Sensors`) | read in full, A1 through A3 | **NO** |

The one culture fragment that reached me: `Emotions-as-Sensors/README.md`
at HEAD instructs the reader to go to the profile README first, and quotes
its `CALIBRATION_AS_PERFECTION.md` distinction. So even the culture level is
not pristine for me.

**C-7 should be scored by a fresh reader with no repo context**, against the
hashed reference. I can build the instrument and the claim tables; I should
not be the one deciding kept/reworded/replaced/dropped.

## The pilot-sampling charge — corrected on the record

> "the three-repo pilot did not include this repo... it was excluded."

Not excluded. **Never in scope.** This session started with four repos
attached: Keystone-Codex, AI-Consciousness-Sensors,
Bio-Grid-American-Manufacturing-, Emotions-as-Sensors. `JinnZ2/JinnZ2` was
not among them and could not be read. The operator was shown all four and
selected three; the fourth (AI-Consciousness-Sensors) is still unsearched
under pilot discipline.

**But the gap is real and it is worse than described**, for a reason the
charge does not give:

`Emotions-as-Sensors/README.md`, commit `1896e21`, 2026-08-21 — the repo's
**last content commit** — says:

    > This repo uses **emotion** as the nearest available English pointer
    > for a concept that does not map cleanly onto the English term. The
    > English term carries a substrate-specific load this repo does not
    > share.
    >
    > Read this repo through the lens at github.com/JinnZ2 (org profile
    > README) BEFORE READING THE LABEL.

The pilot read a repo that explicitly declares its own frame to live
elsewhere, and the elsewhere was unreachable. That is a stronger version of
the charge: not a sampling preference, a **declared and unfollowed pointer**.

It also confirms the scope claim in the notes — culture is the parent of
both candidates — from inside the pilot data rather than from assertion.

`JinnZ2/JinnZ2` is reachable now (`add_repo`). **It has not been added, and
should not be, until the reference is hashed.**

## Test: is parallel + always-on actually unfiled?

The notes assert:

> NOT FILED — the parallel and continuous properties. Those are what the
> state frame cannot hold... A state frame can accommodate "this reading is
> about structure" one at a time. It cannot accommodate a bank of them
> running concurrently with no off position.

Measured in `Emotions-as-Sensors`, files containing each, root → HEAD:

| encoded property | root | HEAD |
|---|---|---|
| `parallel` | 10 | 30 |
| `concurrent \| simultaneous \| at once \| in parallel` | 6 | 17 |
| `always-on \| at all times \| continuous(ly)` | 12 | 22 |
| `sensor bank \| bank of sensors \| sensor suite` | 9 | 20 |
| `never off \| no off switch \| cannot be turned off` | **0** | **2** |
| `one at a time \| sequential` (the contrast) | **0** | **5** |
| `affective state \| emotional state` | 10 | 33 |
| `rather than affective \| not affective \| not a state` (the negation) | **1** | **21** |

**The assertion is wrong in the corpus, and the real finding is sharper.**

Parallelism and continuity are encoded from t=0 — 6 and 12 files
respectively. What is nearly absent at t=0 is the **explicit negation of the
state frame**: one file. By HEAD it is twenty-one.

So the archive did not fail to file the properties. It filed them, and then
spent thirteen months adding denials — while the state vocabulary it was
denying grew alongside it, 10 → 33 files.

    property stated:        6-12 files  ->  17-22 files   (~2x, tracks corpus growth)
    negation of the default:   1 file   ->  21 files      (21x)
    the default itself:       10 files  ->  33 files      (3.3x)

**Effort spent denying the corpus default outgrew both the claim and the
default.** That is a measurable signature of corpus pull, and it is the
first one in this audit that did not need an outside reference to see.

Whether the *gate* was filed — whether the operator had to build a box
before the content would process — is a different question, about authoring,
and the corpus cannot answer it. Evidence line would be `operator memory,
dated`, per the ledger's own discipline. **UNRECORDED, not UNFILED.**

## Test: does a widened channel drift less?

The notes propose non-English channel attempts (emoji among them) as author-
opened channel width, testable against plain English on the same subject.

Measured over 142 `Emotions-as-Sensors` root files ≥200 bytes, emoji per
1,000 characters vs whether the file reached HEAD byte-identical:

    high-emoji (>= 1 per 1k chars)   n=61   survived unchanged: 11%
    low-emoji  (<  1 per 1k chars)   n=81   survived unchanged: 23%

**Direction is opposite to the hypothesis.** Widened-channel files were
about twice as likely to be rewritten.

Three reasons not to accept that yet:

1. **"Unchanged" conflates two things** — a file nothing needed to fix, and
   a file nobody looked at. It is a survival proxy, not a drift measure.
2. **Normalization targeting.** `a41b2d9` ("normalize filenames") and
   `df0a832` ("schema migration, dedup, rename") would preferentially rewrite
   emoji-heavy prose documents regardless of their content fidelity. The
   measurement may be detecting what the cleanup pass aimed at.
3. **The distribution is skewed.** Unchanged files have median 0.00
   emoji/1k but mean 2.31 — a few very-high-emoji files survived untouched.
   The summary statistic is fragile at this n.

Recorded as **suggestive against the hypothesis, not evidence for its
negation.** The clean version needs the same subject rendered once wide and
once plain, scored on claim retention rather than on byte identity — which
is C-6's instrument, not this one.

## C-6 update: the CNC referents exist

The previous turn asked whether a physical system was described twice, well
separated in time, and reported that the workshop/CNC referent was absent
from the pilot archive. The account-wide repo list now shows it is not absent
from the ecosystem:

    JinnZ2/DIY-CNC                  pushed 2026-08-17
    JinnZ2/Prosthetic-arm-CNC       pushed 2026-03-23
    JinnZ2/tool-off-metrology       pushed 2026-08-17
    JinnZ2/Hardware-Store           pushed 2026-03-22
    JinnZ2/open-source-plastic-lab  pushed 2026-08-17

Three CNC/metrology repos, five months apart at the outside. **Not read.**
Whether any two describe the same physical setup — which is what C-6 needs —
is unknown and is one look away once the gate allows it.

`JinnZ2/YouTube-Wisdom-Lens` (2026-03-24) also exists, as the notes
suspected. Unverified.

## Two gate kinds to file, and what the corpus can and cannot support

### Kind 5 — precondition on the SUBJECT, not on the topic

    CONCEPT     a human who fully acknowledges their biome
    BLOCKED BY  a required stable, bounded identity state. A self whose
                boundary is not at the skin had no slot.
    BOX USED    "+ biome field" appended to the author line — the
                acknowledgement placed OUTSIDE the identity slot as a
                separate term, so the identity field stayed stable

This is categorically different from the four existing gate kinds. Those
filter *what may be said*. This one conditions *who may be the subject*
before any content about them processes. It is upstream of topic.

Corpus support available to me: **none.** The author line
`JinnZ v2 + biome field` is in a repo I have not read. Evidence line must be
`operator memory, dated`. Do not infer the mapping to the authorship
correction — the notes say UNRECORDED and that is the correct value.

### Kind 5b — concurrency/continuity as a structural blocker

    CONCEPT     emotions utilized as sensors, in parallel, at all times
    BLOCKED BY  state-only default PLUS the parallel and always-on
                properties — a state is one at a time and is an event;
                a sensor bank is continuous and concurrent
    BOX USED    a separate repo, negation carried in the one-liner

Corpus support: **partial, and it revises the claim.** The measurement above
shows the properties were stated from t=0, so they were not blocked out of
the artifact. What the corpus shows is the *cost* of stating them — a 21×
growth in explicit denial of the default frame.

That is consistent with a gate having been needed at authoring time. It is
not evidence of one. `UNRECORDED`.

## What C-7 needs, in order

    1  operator reference description, voice, unaided, dated  — culture,
       consciousness, emotions, kept separate
    2  sha256 each, append to ledger/commits.jsonl            <- THE GATE
    3  only then: add_repo JinnZ2/JinnZ2, read root README history
    4  claim table per level, union across renderings
    5  scoring by a reader with no repo context (not me, for levels 2-3)
    6  split: model / date / encoding form

Step 3 is the one that is cheap, tempting, and irreversible. It is also the
one the whole design rests on not doing early.
