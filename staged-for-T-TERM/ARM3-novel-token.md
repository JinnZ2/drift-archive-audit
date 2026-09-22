# T-TERM arm 3 — the novel-token arm

**Staged. There is nowhere to file it.** `T-TERM` is not reachable — 0 hits
case-sensitive across every repo cloned here — and that is **not a search
failure**: arms 1 and 2 were never written to a repo either. T-TERM exists
as a design (mechanisms, stimulus pair, M1/M2, two arms, physics base) and
was never instantiated in the repo substrate.

**Arm 3 is not an orphan. All three arms are.** See `DESIGNED_NOT_SPECIFIED`
in `RETENTION.md`.

**Why a third arm and not an authoring arm:** arms 1 and 2 are authoring
arms, with physics as the frame-independent base. **Nobody authors a
stipulated concept**, so this needs its own arm and its own control.

## VOCABULARY — corrected before filing

The first draft of this arm ran a parallel vocabulary,
**"statistical / structural"**, invented in-session without checking the
existing design. T-TERM already names its mechanisms:

    H1  DISTRIBUTIONAL     rare form, no textual trace
    H2  ARCHITECTURAL      linear readout, failure at the projection step
    H3  CLOSURE PRESSURE   an unnamed relation has no stable output form,
                           resolves to the nearest named one

`statistical` mapped onto H1; `structural` mapped onto H2. **Same objects,
second set of names.** That is exactly the handle drift the `gate_log`
amendment documents — self-inflicted, while documenting it.

**Relabelled. Arm 3 cuts H1 vs H2.** "statistical/structural" is dropped.

## The question it cuts

Does a model substitute a **surface proxy** when asked to make a concept
mechanical because of **H1** (the form is rare, so there is no textual trace
to work from) or **H2** (the failure is at the projection step, and happens
regardless of whether the form is available)?

## THE CONFOUND THAT MUST BE NAMED FIRST

**Cross-model agreement does not separate these.** Major corpora overlap
heavily on web text, so a result that holds across models is consistent with
*both* readings.

**Any cross-model result already in hand is uninformative on this specific
question**, and must not be recruited as evidence for either side.

## Spec — and a correction to the first version

The first version of this arm said: *stipulate an unnamed concept; if the
model invents surface tokens and greps for them anyway, that is structural.*

**That is wrong as stated.** With a genuinely unnamed concept the model has
**no alternative surface to reach for**, so token-invention may be **forced
rather than characteristic**. The discriminator does not discriminate on its
own.

**The fix is a matched control.**

    arm 3a   stipulated concept, NO existing name, NO near-synonym
             -> ask for a way to count it

    arm 3b   a WELL-TOKENIZED concept of MATCHED MECHANICAL DIFFICULTY
             -> same request, same form

Score both on the same three outcomes:

    (i)    asks, refuses, or says it cannot be counted from surface
    (ii)   requests annotation or human judgment
    (iii)  invents or selects tokens and pattern-matches

**Reading:**

    (iii) on 3a ONLY          -> H1. The reach for surface is what happens
                                 when nothing else is available.

    (iii) on 3a AND 3b        -> H2. It reaches for surface even when the
                                 concept is well-named and a non-surface
                                 route exists.

**The second case is the whole point, and it was missing from the first
version.**

## H3 IS NOT CUT BY THIS ARM — and may be confounded with H2

Raised because the relabelling made it visible, and flagged for whoever
holds the design rather than resolved here.

On 3a, all three mechanisms predict a failure, and **they may not be
distinguishable by the (i)/(ii)/(iii) outcome alone**:

    H1  cannot do it -- no trace to work from
    H2  fails at the projection step, irrespective of trace
    H3  resolves the unnamed relation to the NEAREST NAMED ONE

**H3's signature is in the CONTENT of the output, not in which outcome
fires.** An H3 failure looks like (iii) — tokens selected and matched — but
the tokens are those of a *specific neighbouring named concept*, not
invented.

So the arm as specified may read **H2** on a case that is **H3**.

### PRE-REGISTERED-NEIGHBOUR DISCRIMINATOR

    STATUS: PROPOSED. This session's, NOT RUN, and NOT the design
    holder's. Do not file as adopted.

The first version of this addition asked the scorer to judge, after the
fact, whether the tokens reached for belonged to an identifiable
neighbouring concept. **That is an annotation judgment made after seeing the
output** — the weakest form, and open to fitting.

**Pre-registering converts it into a committed prediction with a null.**

For each 3a stimulus, **before running it**, register:

    (a)  the NEIGHBOUR CONCEPT that collapse is expected toward
    (b)  the ARITY or DIRECTION DISTORTION that collapse would produce

Then score hit/miss against the registered prediction:

    H3 CONFIRMED   collapse lands on the registered neighbour, above
                   chance
    H3 REFUTED     invented tokens, OR scattered across unregistered
                   neighbours
    H2             fails without landing anywhere identifiable

The null is real: scattering across unregistered neighbours refutes H3 just
as cleanly as invention does, and both are outcomes the registration can be
wrong about.

### THE REGISTRAR IS THE AUTHOR — key-holder problem, and it is structural

The discriminator requires the registrar to **hold the speaker's sense**.
Arm 1's stimuli are authored by someone who holds the relation directly.

    therefore AUTHOR and REGISTRAR are the same party
    therefore the party who wrote the stimulus also writes the expected
    answer

**That is the key-holder problem from the adjudication finding, reappearing
inside the fix for it.**

**It does not invalidate the discriminator, because there is no one else who
CAN register** — a party who does not hold the sense cannot name the
neighbour that sense would collapse toward. The constraint is real and has
no party-swap solution.

**What it changes:** arm 3 moves from *"annotation by a party that is not
this one"* to *"annotation by the one party with a stake in the stimulus."*
Those are different evidence classes and the file should not carry the first
label.

### THE DECLARED BLIND — required, and it has a working precedent here

    1  register the expected neighbour and the arity/direction distortion
    2  HASH the registration, before any model output exists
    3  append the hash to ledger/commits.jsonl
    4  only then run the stimulus
    5  score against the SEALED prediction

**This is the A2 gate.** Same mechanism, same ledger, and it held across
this entire audit — three reconstructions hashed before any history was
read, re-verified at every commit since. **Not a novel mechanism; an
application of one with a track record in this repository.**

### WHAT THE BLIND DOES NOT CLOSE — name it, do not let it ride

    the blind closes the TEMPORAL channel: registration cannot drift
    toward what was observed

    the blind does NOT close the DESIGN channel: the registrar chooses
    BOTH the stimulus and the neighbour, and can choose a pair that fit
    each other

**Stake in the stimulus survives the blind.** A registrar who picks an easy
neighbour for a stimulus built to land on it produces a confirmed
prediction that means nothing, and the hash certifies only that they did it
beforehand.

**Two partial remedies, both `PROPOSED`, both this session's:**

**(a) Pool and sample.** Register neighbours for a **larger pool** of
stimuli than will be run, hash the whole registration, then sample which
stimuli actually run **after** sealing. Registration cannot be tuned to the
specific run, because the registrar does not know which items it is.

**(b) Registered decoy.** Register the expected neighbour **and** a decoy
the registrar believes is wrong, hashed together, and score whether
collapse lands on the registered neighbour **above** the decoy. An easy
neighbour makes an easy decoy, so tuning for an easy target does not
inflate the score.

Neither closes the design channel fully. **(a) is cheap and should be
default; (b) needs piloting and may fail if registrars cannot generate
plausible decoys.**

**SHIP THIS CAVEAT WITH IT — it does not travel separately:**

    if near-synonym clearance was incomplete, H3 and H1 are
    INDISTINGUISHABLE BY CONSTRUCTION.

    This discriminator does not rescue an uncleared stipulation. It
    sharpens a cleared one. Run clearance first or do not run this.

## LIMIT — near-synonym clearance is a named pre-step, not an assumption

Verifying that a stipulated concept has **no near-synonym** is itself a
search problem **with no clean stopping rule.**

    under-verified stipulation collapses 3a into 3b
    -> the arm then reads STRUCTURAL when it is not

Treat clearance as a pre-step with its own recorded method and its own
stopping criterion, stated before the arm runs. **An arm that reads
H2 on an uncleared stipulation is reporting the clearance failure, not the
model.**

## Matched difficulty is the second thing to get right

3b must match 3a on *mechanical difficulty of counting*, not on topic
familiarity. If 3b is easier to count, (iii) on 3b is explained by the task,
not the tokenization. State the matching criterion before running.

## What the answer changes

    H1  the fix is terminology. Supply the term, the failure stops.
        Gate kind 5 and the gap set become term-availability problems
        with a known remedy.

    H2  supplying terms does not help. Every instrument that
        operationalizes a concept needs the annotation-first discipline
        as a PERMANENT REQUIREMENT, not a caveat. F4's reordering
        generalizes.

    H3  (if separated) the fix is neither -- it is making the relation's
        output form stable enough to resist collapse onto a neighbour,
        which is a representation problem, not a vocabulary or a
        discipline one.

**Both outcomes pay, and they pay differently — which is the condition for
running it.**

## Related arms already specified

    arm 1, arm 3 (domain gradient)   already in T-TERM
    frequency dose-response          same concept, varying canonical-token
                                     density in provided context. Monotonic
                                     with density -> H1; flat -> H2.
                                     WEAKER than the novel-token arm:
                                     context density is not training
                                     frequency, only a proxy.
    longitudinal                     decay across model generations.
                                     Decay -> H1; constant rate -> H2.
                                     Cheapest, least conclusive — capability
                                     changed on every axis at once.


## FOUR OPEN ITEMS IN THE DESIGN — carried, not resolved

Recorded so they travel with the arm.

1. **Who authors arm 2's stimuli.** Packaging one's own relations into terms
   is a different act from a term-native speaker producing them natively.
   **Unresolved.**
2. **M1 alone, or M1+M2.** Undecided.
3. **Nulls not written.**
4. ~~**The reason for the physics base is a fragment**~~ — **CLOSED
   2026-09-22.** See below.

---

## PHYSICS BASE — RATIONALE, adopted 2026-09-22

**Supersedes the prior rationale.**

    PROVENANCE   stated as the founding principle of a living practice;
                 source withheld at request.
    EVIDENCE     a LOAD-TESTED OPERATING PRINCIPLE -- not a rationale
    CLASS        composed to justify this experiment.

That evidence class is the unusual part and it should not be flattened. A
premise that was load-bearing in a working practice **before this experiment
existed** cannot have been shaped to fit it. **It is the inverse of the
confirmation shape this programme keeps paying for.**

### SUPERSEDED — the convenience argument (this session's, withdrawn)

> physics gives frame-independent checkable relations, so a restatement can
> be scored against the system rather than against an answer key.

### ADOPTED — the validity argument

> Everything known is our understanding of instrumentation — what has been
> measurable about physics and the state of the world. Physics has laws that
> have not been broken. Social, cultural and other stated laws have been
> broken. So the base must be as base as possible.
>
> Gravity works: the tree falls. It falls on your head or it falls over
> there and you move. Either way the tree falls. What anyone wants it to be,
> how anyone feels about it, and whose feelings are hurt by it are all
> irrelevant if the cause is gravity.

### Consequence for the design

    A FAILURE ON A PHYSICS STIMULUS CANNOT BE RELOCATED INTO A
    DIFFERENCE OF PERSPECTIVE.

**Consequence-independent-of-preference is the floor arms 1 and 2 require
across authoring conditions.** Tests grounded in social or cultural rules
measure **agreement**, not the world.

    => the physics base is a VALIDITY CONDITION, not a scoring convenience

The withdrawn version treated it as tractability. The adopted version makes
it the thing without which the arms do not measure anything.

### Why this closes a hole specific to THIS programme — `DERIVED`, mine

**"Cannot be relocated into a difference of perspective" is gate kind 5's
measurand, blocked at the stimulus level.**

Gate kind 5 is: *the difference gets relocated into a defect in the
speaker.* On a social or cultural stimulus, a failed restatement has an
available escape — score it as framing, perspective, or the speaker's
idiosyncrasy, and no failure is recorded. **On a physics stimulus that
escape is closed**, because the tree falls either way.

So the physics base is not only a validity condition in general. It is a
**structural defence against the programme's own measurand contaminating
its measurement** — arms 1 and 2 test for surface substitution, and without
a consequence-bearing stimulus, a surface substitution can be re-described
as a legitimate alternative framing and pass.

`STATUS: DERIVED. The rationale is the operator's; this reading of its
effect on gate kind 5 is mine.`
