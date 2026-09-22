# instrument/ — channel-function scorer (F1–F4)

`channel_function.py` — stdlib only, no dependencies.

    python3 instrument/channel_function.py --self-test
    python3 instrument/channel_function.py <path> [<path> ...]

Scores **how** a speaker uses a sensory channel, not how often they mention
one. Discriminator is **function breadth** (how many of F1–F4 are reached),
not volume. Seven channels, kept separate, never summed.

    F1 MENTION     sensory term as description
    F2 EVIDENCE    channel read for state
    F3 METHOD      channel used to teach / transmit / diagnose with
    F4 INSTRUMENT  something built IN or FOR the channel

Technical-register score is built from **content** properties per LIMIT 6 —
quantified units, equations, falsifiable claims, tolerance handling — not
from academic style.

---

## TWO CONSTRUCTION FLAWS, both found by running it

LIMIT 5 said classifier validity is the whole study. Both of these were
found in the first two runs, which is the argument for a human gold set
rather than a reason to trust the fixes.

### Flaw 1 — the channel patterns carried the H1 prior (FIXED, partially)

The first `auditory` pattern held only **technical** acoustic vocabulary —
`acoustic, timbre, resonance, harmonic` — and missed plain descriptors.
The self-test case *"the room was loud"* returned **None**.

**That skew scores F1 down for plain-register speakers and inflates the
apparent function breadth of technical-register ones.** It builds the H1
tradeoff into the *channel* scorer — a place LIMIT 6 only anticipated it in
the *technical-register* scorer.

Plain descriptors were added to `auditory`, `vibration_haptic` and
`thermal`. **The remaining four channels have not been audited for the same
skew and a human should do it before any number here is used.**

### Flaw 2 — F4 is contaminated by document type (NOT FIXED)

F4 fires on `protocol | schema | sensor | spec | log | .json | .py | module
| pipeline`. Those words saturate any code repository **regardless of
whether the instrument is actually in the sensory channel.**

    "the sensor detects temperature"  in a JSON schema
      -> scored F4 thermal
      -> but the schema is not a thermal instrument

So the F4 column below is an **upper bound**, and on repository data it is
probably a loose one. **H2 cannot be tested on document corpora with this
version of F4.** It needs a marker that distinguishes *an instrument built
in the channel* from *a channel mentioned inside an instrument*, and that
distinction may require human annotation rather than pattern matching.

---

## Run on the four session repos — a worked example, not a result

    AI-Consciousness-Sensors          Emotions-as-Sensors
    channel           files  F1  F2  F3  F4  br     files F1  F2  F3  F4 br
    olfactory            47  47  20  23  17   4        5   5   1   4   4  3
    auditory            545 545 301 232 216   4      179 179 107  83  91  4
    vibration_haptic     88  88  30  31  20   4       30  30  14   8   9  4
    proprio_kines       285 285 110  95  67   4       58  58  31  16  22  4
    thermal             109 109  14  28  18   3       27  27  20  13  12  4
    baroceptive         198 198  83  67  33   4       25  25  14   5   8  4
    interoceptive        55  55  19  23  11   4       20  20   9  11   8  4

    Bio-Grid: 99 docs, breadth 3–4 across 7 channels
    Keystone: 69 docs, breadth 2–4 across 6 channels

**What this does NOT show.**

- **It cannot test H1.** One speaker, and the artifact channel rather than
  conversation. There is no population and no independent second speaker.
- **It cannot test H2.** Flaw 2. F4 is inflated by repo vocabulary.
- **It is not the N-of-1 conversational corpus** the work order refers to.
  Different channel, different selection, transported rather than spoken.

**What it does show.** The scheme **runs**, produces a populated F1–F4
table across seven channels, and distinguishes channels within one corpus
(olfactory reaches breadth 4 in one repo, 3 in three others). That is
enough to take to annotators and not enough to report as a finding.

Next step is the gold set: human-annotated F1–F4 on a sample, inter-rater
agreement reported, and **adversarial cases where high function co-occurs
with informal register** — which is the case this corpus happens to be, and
is why it is a useful validity set rather than a useful result.
