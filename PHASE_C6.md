# C-6 — repeat description of a physical referent

## Status: DESIGNED, NOT RUN. Blocked on one operator answer.

Proposed after Phase C reported that the archive holds no experiment across
the tooling boundary (C-5). The proposal's core point is correct and is the
first thing in this audit with an **outside reference**:

    CONSTANT   same operator, same translation act, same channel
               (voice / one-finger from the cab), three years
    VARIABLE   the model on the other end, and its date
    OUTPUT     what came back, committed verbatim, timestamped

    REFERENT EXISTS   the workshop, the CNC work, the forest practice are
                      real systems with real behaviour. A rendering can be
                      wrong in a way a text benchmark cannot detect.

Everything else in this audit scores renderings against other renderings.
C-6 scores a rendering against a physical system. That is a different kind of
evidence and it is the strongest arm in the design.

## The one question

> **Is there a system you described to a model twice, well separated in time?**
> The workshop, a CNC setup, a forest practice, a machining job — anything
> with a physical referent you can still check against.

    YES -> which system, roughly when each time:  ______________________
    NO  -> C-6 does not exist and is closed
    UNSURE -> any saved chat logs, notes or exports from 2023-2025?

Nothing else is needed to start.

## Searched: the pilot archive does not contain the referent

Measured across all three pilot repos, root and HEAD, files containing:

    CNC            0 -> 2      sawmill / lumber / timber    0 -> 0
    workshop       0 -> 0      fixture / jig                0 -> 0
    feed rate / spindle        0 -> 0

The workshop, machining and forest-practice referents are **not in these
repos at any commit**. `machining` hits are generic ("machine tools").
So C-6's material has to come from the description history, not the archive —
exactly as the proposal states. Confirmed, not assumed.

(`AI-Consciousness-Sensors` was NOT searched. Pilot scope holds until the
verify forms come back.)

## C-6a — a repeat description that IS in the archive

Found while searching. Not the proposed arm, but the same shape, and it
gives C-6 a worked scoring method before any new data is collected.

**Referent:** the RGP probe — a physical object with real material behaviour.
**Two independent renderings, one day apart, both committed verbatim:**

    Waste-management/Tolerances.md        b05b69b  2025-11-09  1113 words
    Waste-management/Mechanical-specs.md  cba75db  2025-11-09  1619 words

Both never edited since. Scored on itemised physical claims:

| physical claim | Tolerances | Mech-specs |
|---|---|---|
| Inconel 718 primary casing | yes | yes |
| Hastelloy X alternative | yes | yes |
| SiC inner liner | yes | yes |
| alumina liner option | yes | yes |
| YSZ thermal barrier coating | yes | yes |
| W / Mo refractory at hottest face | yes | yes |
| ablative sacrificial outer layer | yes | yes |
| bellows / compliant thermal joint | yes | yes |
| multi-stage shock isolation | yes | yes |
| ceramic-to-metal feedthroughs | yes | yes |
| redundant sensors + fusing | yes | yes |
| avoid steel load-bearing fasteners | yes | yes |
| ΔT 200–600 °C | — | yes |
| 10⁴ thermal cycles | — | yes |
| ≥ 20,000 g shock | — | yes |

    shared: 12/15      differing: 3/3 are QUANTIFICATIONS the longer
                       rendering adds; the material stack is identical

**Reading.** Under a fixed referent the two renderings agree completely on
*what the thing is made of* and differ only in *whether numbers are
attached*. The structure varied; the material content did not.

**Limits, stated plainly.** Same day, so no time separation. Model identity
UNSET for both — possibly the same model, possibly the same session. This is
**not** a model-varied experiment. It is a demonstration that a repeat
description of a physical referent exists in this archive and can be scored
item by item, and it supplies the scoring instrument C-6 will need.

**The part that is checkable outside the corpus:** Inconel 718, YSZ TBC, SiC
liners, ceramic-to-metal seals and the 20,000 g / 10⁴-cycle / 200–600 °C
envelope are all verifiable against materials engineering. Whether the stack
is *correct* is not scored here — no verdicts on content — but unlike every
other finding in this audit, it *could* be.

## Confounds in the proposed design — four, and three are fixable

The proposal lists four constants. Three of them are assumptions.

### 1. "same operator" is the weakest constant, not the strongest
Three years of describing systems to models is three years of learning what
gets a usable answer back. Operator-side adaptation is **the same
phenomenon this audit was built to detect**, relocated to the input side.
If the later description is better targeted, the later rendering improves for
a reason that has nothing to do with the model.

*Fix:* score the two descriptions themselves before scoring either
rendering. If description 2 is materially more specified than description 1,
the arm measures description drift, not model drift. This is checkable the
moment both descriptions exist.

### 2. "same channel" is not constant — it is TRANSPORT, and it changed
Voice capture and transcription in 2023 and in 2026 are not the same layer.
Transcription errors, punctuation, segmentation and handling of technical
vocabulary all moved. That is the identical `TRANSPORT×MODEL` confound
already recorded at the 2026-03-22 boundary, reappearing here.

*Fix:* if the raw transcript is recoverable for both, score transcript →
rendering separately from speech → transcript. If only the rendering
survives, the confound is live and must be labelled.

### 3. the referent may have moved
A workshop three years apart is not necessarily the same system. A rendering
that mismatches today's shop may have matched the shop as described.

*Fix:* pick a referent whose relevant behaviour is stable, or state which
parts changed before scoring.

### 4. ground truth is single-rater and unblinded
"Nobody else has both sides" is what makes the arm possible and is also its
measurement weakness: one rater, unblinded, scoring after seeing both, and
knowing which is newer. Order and expectancy effects apply regardless of care.

*Fix, and this one costs almost nothing:*
- score **itemised physical claims**, not global impression — the C-6a table
  above is the template
- strip dates and any model-identifying phrasing, randomise presentation order
- score each claim `CORRECT / WRONG / NOT ADDRESSED` against the physical
  system, never against the other rendering
- for wrong claims record the failure mode: *wrong value*, *wrong mechanism*,
  *right mechanism wrongly bounded*, *plausible and untestable*

Done this way the arm survives being single-rater, because each judgement is
about a physical fact rather than a preference.

## Protocol, if the answer is YES

    C6-1  recover both descriptions and both renderings, verbatim, with dates
    C6-2  score the DESCRIPTIONS for specification delta  (confound 1)
    C6-3  build the itemised physical-claim table, union of both renderings
    C6-4  operator scores each claim against the real system, blinded to date
    C6-5  report per rendering:
              correct / wrong / not-addressed
              failure modes of the wrong ones
              claims present in one rendering only
    C6-6  DOMAIN SPREAD: repeat across build / machining / ecological /
          coordination if more than one repeat exists. Whether drift has the
          same SHAPE across domains is the second question, and it is only
          answerable with two or more repeats.

## What C-6 can and cannot settle

**Can:** whether a rendering of a real system got more or less physically
correct across the model-date axis; what the failure modes are; whether those
failure modes are domain-general or domain-specific.

**Cannot:** attribute the change to the model. Date and model covary with
transport and with operator description drift, exactly as everywhere else in
this pilot. C-6 is the first arm with an outside referent. It is not an
arm with an isolated cause.

That is still a large gain. Every other finding here compares text to text.
