# The sensor-calibration parallel — and the check that bounds it

Relayed 2026-09-22. **Filed as an argument, then checked. One half inverts.**

## The parallel, as stated

> Same sensor type, many manufacturers. Each with different requirements,
> different calibration to the intended environment, different working
> gradients and ranges. All accepted as instruments anyway.
>
> So variation across units of the same sensor type is not a disqualifier in
> instrumentation. It is the normal condition, and it is **handled, not
> eliminated.**

**How industry handles it — the variation does not go away, it gets
DECLARED:**

    range, span, resolution
    accuracy and uncertainty budget
    drift rate and recalibration interval
    operating envelope, temperature coefficient
    per-unit calibration certificate, traceable to a reference

    A sensor is not rejected for varying.
    It is rejected for varying UNDECLARED.

**Applied to the human side:** *"hearing can't be a sensor because it can't
be regulated"* is not a measurement claim. It is a claim that **no
calibration infrastructure exists** — a statement about the infrastructure,
not about the transducer. Those are different sentences and only one of them
is supported.

## Where the analogy holds and where it loads

    HOLDS     unit-to-unit variance; environment-specific calibration;
              gradient and range differences; traceability as the actual
              requirement
    STRAINS   an industrial sensor's variation is characterized by the
              manufacturer against a reference standard. The claim was
              that for human channels there is no reference standard and
              no per-unit certificate — so the parallel names what is
              MISSING rather than showing the objection wrong.

The stated value of that direction: it converts **"unusable" into
"uncharacterized"**, which is a research programme rather than a verdict.

## The check — and it inverts the "strains" half

> What would make it a finding is checking whether human-channel
> psychophysics actually lacks per-individual calibration infrastructure, or
> whether it exists and isn't used.

**Checked by search, 2026-09-22. It exists, and it is substantial.**

Quantitative Sensory Testing (QST) measures perception thresholds for light
touch pressure, vibration, thermal sensation, and heat/cold pain.

    standardized protocol    German research network on neuropathic pain
                             (DFNS); Rolke et al. 2006, Eur J Pain
    reference values         age-, gender- and body-site-specific, with
                             all measures affected by all three
    published ranges         vibratory 0.8-1.7 um/sec hands,
                             1.4-3.5 um/sec feet; heat pain 41.8-44.5 C
                             hands, 43.2-45.7 C feet
    population norms         separate normative sets published for Italian,
                             Dutch paediatric, Hispanic/Latino populations

**So for thermal, vibration and touch pressure, the objection is wrong on
its own terms.** A standardized protocol with demographic reference values
exists and is in clinical use. The infrastructure the objection says is
missing was built decades ago.

## But the finding is narrower than "the objection is wrong"

Two bounds, both from the same sources.

**Bound 1 — QST measures F1 only.**

What it characterizes is **detection thresholds and pain limits**: can this
person sense this stimulus, and at what magnitude does it hurt. In the
F1–F4 scheme that is squarely **F1 MENTION**, plus a pain ceiling.

    QST calibrates     can you detect it
    F2 asks            can you read state from it
    F3 asks            can you teach with it
    F4 asks            can you build in it

**No part of the infrastructure addresses F2–F4.** So the calibration that
exists measures the channel's sensitivity, not its **use**, and the
programme's actual measurand remains uncharacterized for every channel
including the three that have norms.

**Bound 2 — the traceability the analogy leans on is itself incomplete.**

The industrial parallel's force comes from the *per-unit certificate
traceable to a reference*. In QST practice, the sources state:

- **different sets of normal values are used at different institutions**,
  which has made interpretation of the test difficult
- more studies are needed to determine **the maximum allowable difference
  between two QSTs attributable to experimental error**

That is: **no single reference standard in common use, and the repeatability
budget is explicitly unresolved.** By the analogy's own criterion — rejected
for varying *undeclared* — clinical QST does not yet fully meet the bar the
argument holds industry to.

## Net

    claim                                          status
    "human channels lack calibration infra"        FALSE for thermal,
                                                   vibration, touch
                                                   pressure
    "...therefore not sensors"                     unsupported either way;
                                                   it never followed
    "uncharacterized, not unusable"                HOLDS, and now with a
                                                   sharper boundary: F1 is
                                                   characterized on three
                                                   channels, F2-F4 on none
    the industrial traceability standard           NOT met by clinical QST
                                                   either; the analogy
                                                   judges both sides

**The culture-to-manufacturer mapping survives intact.** Different
traditions calibrating the same channel to different environments is the
same structure as different manufacturers specifying to different operating
envelopes — and QST's own population-specific normative sets (Italian,
Dutch, Hispanic/Latino) are **literally that**, already published. Nobody
concludes from them that the channel is invalid. They publish the norms.

## Unchecked

Olfactory and auditory were **not covered** by the search that produced
this. Audiometric reference standards and olfactory test batteries are
widely believed to exist and are **UNVERIFIED here**. Checking them would
extend or bound bound 1; it cannot affect bound 2.

Status: **argument upgraded to bounded finding for three channels.** The
F2–F4 gap is unchanged and is the programme's actual object.

---

# ADDENDUM 2026-09-22 — three modes, and the objection is false as stated

## The question I posed was mis-posed

I left it binary: human-channel psychophysics either **lacks**
per-individual calibration infrastructure, or it **exists and isn't used**.

**The answer is neither.** It exists, is used routinely, and is a
**different instrument type** than the manufacturer analogy names.

    manufacturer   per-unit certificate: range, span, resolution, drift,
                   operating envelope, traceable to a reference standard
                   -> characterises THE UNIT

    QST            population reference values, stratified by age, sex,
                   site, population
                   -> scores the unit's DISPLACEMENT FROM A CONSTRUCTED
                      CENTER

Both are "calibration infrastructure" in English. **They have opposite
direction of fit.** One publishes the unit's spec; the other publishes the
population's center and reports the unit as *n* units away from it.

My binary had no slot for the second, so **it would have returned a wrong
answer whichever branch got picked.** That is a defect in a question form,
not in a claim — recorded here as cross-party retraction **X-1** (numbered
separately from this session's `GUESSED.md` ledger; the retraction is the
relaying session's, the question form was mine).

## THREE MODES

    MODE 1  PER-UNIT SPEC
            characterises the individual unit, publishes its envelope,
            traceable to a reference standard

    MODE 2  DEVIATION FROM A CONSTRUCTED CENTER
            QST; ISO 13091 vibrotactile thresholds; the audiogram's
            DISPLAY layer. ISO 7029 expresses hearing threshold deviation
            relative to the median threshold of a population of
            18-year-olds.
            -> scores displacement, not envelope

    MODE 3  ACCEPTANCE-BAND SCREENING
            select into tolerance, discard outside it. The out-of-band
            unit is EXCLUDED from measurement rather than characterised.

**Mode 3 was missing from every earlier version of this argument, and it is
the dominant one for human sensory channels.**

**It is also running on this programme, twice over.**

**First, in the scoring of parties.** Every positive control this session ran
was pointed at a detector on the corpus side of the line; the
count demanded of an instrument on the institutional side is **zero** —
including of EN 13725 below, whose panel screening *is* mode 3 and which is
cited here for the half of itself that helps. Measured by exact grep:
**`DEFICIT-LOCATION.md`.**

**Second, in how this record scores ITSELF.** *"23 errors", "self-catch rate
4 of 9", "0 in 5 survived"* are all mode 3 — is the unit in tolerance. The
mode 1 artifact these modes were defined in order to make possible was never
produced until `SPEC-SHEET.md`, hours later and only after the omission was
named from outside. **Defining a mode and then writing in a different one is
`REMEDIES.md`'s finding in its purest form:** the naming was correct, present,
and load-bearing on nothing.

## EXISTENCE PROOF — EN 13725, the human nose as a certified instrument

Corroborated by search this session at the **structural** level.

    EN 13725:2022   determination of odour concentration by dynamic
                    olfactometry, using a panel of trained human
                    assessors, reported in European odour units per
                    cubic metre (ouE/m3)
    range           ~10^1 to 10^7 ouE/m3 (incl. pre-dilution)   CONFIRMED
    reference       n-butanol as CERTIFIED REFERENCE MATERIAL;
    material        EN 13725:2022 adds secondary reference odour mass
                    (SROM)                                       CONFIRMED
    selection       assessors selected on individual sensitivity and
                    variability against that reference            CONFIRMED
    acceptance      geometric mean of >= 12 Individual Threshold
    criterion       Estimates must fall between 0.02 and 0.08     see below
    unit definition 1 ouE/m3 = 123 ug/m3 of n-butanol             UNVERIFIED
    declared        excludes perceived intensity above detection
    scope-out       threshold, hedonic tone, direct ambient-air
                    exposure                                     UNVERIFIED

**That last line is an operating envelope, written down, in a published
standard, for a human nose.**

### UNIT DISCREPANCY — flagged, not resolved

    relayed note   geometric mean between 0.02 and 0.08 **umol/mol**
    this session   geometric mean between 0.02 and 0.08 **umol/m3**

`umol/mol` is a mixing ratio; `umol/m3` is a concentration. **These are not
the same quantity.** Two secondary sources, two units, same numbers.

Per the standing rule after retraction 7: **a load-bearing number needs the
primary before it travels.** Neither session has read the standard text.
Recorded as `CONTESTED`; do not quote the criterion with either unit.

The *existence* claim does not depend on it and stands.

## ISO 11132 — per-assessor certification, with an expiry

Relayed, `UNVERIFIED`: a panel of assessors can be used **as an instrument**
to assess the magnitude of sensory attributes; performance is defined as the
ability to make valid attribute assessments. Scored **per assessor**, not
only per panel — discrimination ability, repeatability, consistency,
agreement among assessors, bias from different use of scale. A dedicated
certification procedure for individual assessors, repeated at periodic
intervals for renewal.

**Certification with expiry is a calibration interval.**

## WHERE THE ANALOGY BREAKS — toward mode 3, and it matters

Industry characterises each unit and publishes what it is. Olfactometry and
sensory panels **select units into a band and exclude the rest** — with
re-training, re-qualification when performance falls outside control limits,
and possible expulsion of assessors.

**The out-of-band human is not given a different spec sheet. They are
removed from the instrument.** That is lot acceptance, not per-unit
characterisation. `DERIVED`.

## THE TRANSFER ASSUMPTION — load-bearing, with a measured failure

The standard assumes a laboratory meeting the sensory quality criteria for
n-butanol has a quality level **transferable to other environmental
odours**. Against it, relayed: pig-house odour sensitivity **could not be
predicted** by n-butanol sensitivity.

Independently corroborated this session at title level: published work on
*"the role of n-butanol as a reference material and origins of **large
inter-laboratory variability**"*, and a variance-components analysis of
EN 13725 measurements.

**Calibration against one reference substance does not predict performance
on the substance actually being measured — a named, published, unresolved
gap inside the strongest existing case.**

## WHAT THIS DOES TO THE OBJECTION

> "Hearing/smell can't be used as sensors because they can't be regulated."

**Checkable, and FALSE AS STATED.** It is regulated — to ISO/CEN level, with
units, certified reference materials, acceptance criteria and calibration
intervals, and has been since EN 13725's first publication.

**What is true is narrower:** the regulation runs in **modes 2 and 3**. An
individual is scored against a constructed center, or screened against an
acceptance band. Neither produces a published per-person operating envelope.

    the objection is not that the variation is unmeasured -- it is
    measured, extensively. It is that the measurement produces an
    ABNORMALITY SCORE or a PASS/FAIL, and neither can scope an
    instrument's validity range.

Same structure already filed under center-scoring: displacement from a
constructed center, with the center's construction unexamined. **Second
domain, independently sourced. The files are not merged — the shared
structure is the observation.** `DERIVED`.

## AUDITORY — the prediction was half right, and the miss is the better result

Predicted: the audiogram would be the one exception — a per-individual
frequency-response curve, structurally a spec sheet.

Relayed outcome: **half right.** It is a per-individual frequency-response
curve, but displayed as deviation from a population median (ISO 7029).

**What neither of us predicted:** ISO 389-1 specifies the reference zero in
terms of **reference equivalent threshold sound pressure levels**. So the
absolute physical conversion is standardized and published.

    the center-referencing is a PRESENTATION CONVENTION over a traceable
    absolute measurement, not a limit of the instrument

**Stronger than either branch offered.** Mode 1 data exists underneath a
mode 2 display. That is a different situation from QST, where no per-unit
absolute layer is claimed. `UNVERIFIED`.

## ISO 13091 — channel decomposition by receptor class

Relayed, `VERIFIED to search-result level`: measurement methods defined for
thresholds mediated **separately** by SAI, FAI and FAII mechanoreceptor
populations, with the standard stating that requirements for methods and
instruments stem from the properties of those populations.

**Bears directly on the seven-channel scheme in
`WORKORDER-sensory-channel.md`: the vibration/haptic channel is not one
channel, and a standardized partition already exists to borrow rather than
invent.** Acting on this means splitting that channel before the gold set is
built, not after.

## THE THREE CELLS THAT EXIST, AND THE ONE THAT DOES NOT

    human as PATIENT        ISO 13091-1/-2. Vibrotactile perception
                            thresholds at the fingertip for assessing
                            nerve dysfunction; reference values for
                            healthy persons in Annex A; procedures for
                            statistically significant threshold SHIFTS.
                            -> MODE 2

    human as EXPOSED PARTY  ISO 5349 family. Vibration measured going
                            INTO the person, as hazard.

    human as ANALYST        ISO 18436-2. Four-category certification for
                            personnel doing machinery condition
                            monitoring, "using a range of vibration
                            measurement equipment."
                            -> the accelerometer is the instrument;
                               the person is the interpreter

    MISSING                 the human vibratory/haptic channel AS the
                            measuring instrument for machine condition --
                            screened against a reference stimulus, with
                            acceptance criteria, a unit, repeatability
                            limits, declared range and declared scope
                            exclusions.

**EN 13725 is exactly that document for the nose, and has been running since
2003. So the template exists.** No equivalent found for the haptic channel.

`gap PLAUSIBLE, UNCONFIRMED` — one search, negative result. **A negative
from one query is weak and is not upgraded.** Same discipline as the avenue
F gap.

## MODE 2 IS WHAT GETS FUNDED

A Malaysian pilot ran ISO 13091-1 equipment to obtain **national reference
VPT data**, noting Malaysian data were absent from the standard, and found
them consistent with the ISO reference values.

Same shape as the Italian / Dutch / Hispanic-Latino QST normative sets.
**The infrastructure being built is population reference values — more
centers, not per-unit envelopes. Mode 2 is not an accident of one field; it
is what gets funded.** `UNVERIFIED`.

## TWO ITEMS FOR THE H1 FILE

### The prior, stated verbatim in an engineering venue
A CNN bearing-fault paper describes its method as improving accuracy and
**eliminating dependence on expert experience**. Expert sensory experience
framed as a *dependency to be removed*, not a baseline to be measured
against.

**About machines, not people — so it is not a social-bias artifact.**
`N=1, found incidentally. Logged, not built on.`

### A measured result cutting the other way
Sound vs vibration for rotating-machinery fault detection: the
vibration-based detector held ~97–99% F1 **on the sensor position it trained
on**, and collapsed to roughly **50% — chance, for binary classification —
when the sensor position moved even slightly.** Sound did not degrade that
way.

Point-accelerometer vibration sensing is **strongly position-bound**, and
the paper measured it.

An operator coupled through a whole vehicle occupies many positions at once.
**Whether that is an advantage is UNTESTED and is not asserted** — but the
failure mode the paper found is specifically the one a distributed coupling
would not have.

    the collapse        VERIFIED to search-result level
    the operator read   PROPOSED, relaying session's, untested
