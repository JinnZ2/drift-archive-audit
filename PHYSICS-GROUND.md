# Is physics-as-terminal-ground a cultural artifact or a post-hoc selection?

Tested 2026-09-22. **The test does not cleanly separate. The residual stays
where it was put.**

## The prediction, with its null

    CULTURAL ARTIFACT    appears as terminal ground across repos with NO
                         shared topic -- emergency management, negotiation,
                         sensor work, glyph engines -- and in commits
                         PREDATING 2026-09-22

    POST-HOC SELECTION   clusters in repos about MEASUREMENT and
                         EVALUATION, scarce where the domain does not
                         invite it

Both informative. The second makes nothing wrong; it means the
selection-after-the-fact residual stays as stated.

## Positive control — run first, per standing procedure

`PHYSICS_FIRST_AXIOMS`, ground-truthed locally to
`ai-human-audit-protocol/physics/PHYSICS_FIRST_AXIOMS.md` → account-wide
search returns **13 hits including that exact file.** Query form validated
for this vocabulary. **Zeros can now be trusted.**

Note the control is itself a data point: a directory named `physics/`
containing axioms, inside an **AI governance and audit repo** — not a
physics repo.

## Result 1 — it DOES appear in topically unrelated repos

| repo | file | topic |
|---|---|---|
| `The-Curriculum-of-Everything-Earth-` | `AI-Wisdom-Training/training-data/conflict_resolution_scenarios.json` | **negotiation / conflict resolution** |
| `Resilience-hydrology-core` | `legacy/2025-original/firmware__02_crop_response.md` | **hydrology firmware, crop response** |
| `Rosetta-Shape-Core` | `ontology/principles/p03-relativity.json`, `p09-proportion.json`, training data | **glyph / shape ontology** |
| `Sovereign-Octahedral-Mandala-Substrate-SOMS-` | `agaasdenton/KERNEL.md`, `SIBLINGS.md` | symbolic substrate |
| `Resilience` | `sim/datacenter_net0.md`, `institution_registry.py` | infrastructure sim |
| `planetary-conservation-framework` | `legacy/Possible-addons.md` | conservation |

**Three of the four named domains are hit**: negotiation, sensor work, glyph
engines. Emergency management was not searched.

## Result 2 — it ALSO clusters in measurement and evaluation repos

    method-layer                          README, preference_free_rank.py
    ai-human-audit-protocol               CLAUDE, REVIEW, CHANGELOG, physics/
    metabolic-accounting                  docs/AUDIT_14.md
    thermodynamic-accountability-framework  calibration/README.md
    Mathematic-economics                  calibration/README.md
    Emotions-as-Sensors                   REVIEW, constraint_genealogy.py

**Both predictions are partially satisfied. Neither is refuted.**

## Result 3 — dates. All sampled topic-distant instances PREDATE the experiment

    Rosetta-Shape-Core  p03-relativity.json              2026-03-25  Claude
    The-Curriculum      conflict_resolution_scenarios    2026-04-09  Claude
    Resilience-hydrology firmware__02_crop_response      2026-08-14  Claude

**All predate 2026-09-22 by five to six months.** The construct was not
introduced for this experiment.

**But "Claude-authored" is uninformative here**, and this is the scope limit
that governs the whole test: per `CORRECTION-001` and `-002`, **all repo
content is model-given.** Model authorship is the expected value for
everything, so it discriminates nothing.

    what travels across repos is what was ASKED FOR AND KEPT
    -> the right signal for a SELECTION question
    -> but a record of CHOICES, not of independent instances

## A trap in the path, flagged

`Resilience-hydrology-core/legacy/**2025-original**/firmware__02_crop_response.md`

The directory name says 2025. **The file entered git on 2026-08-14** — inside
the documented cross-repo pass (49 commits, five repos, 2026-08-13..17, all
Claude-authored, where `legacy/` was installed account-wide).

    a directory named "2025-original" is a PROVENANCE CLAIM, not a
    TIMESTAMP

I read it as evidence of a 2025 instance before checking. It is not. Same
class as every other surface-proxy substitution on this record, caught here
by a date contradicting a path — a quantity, again.

## A counting trap, flagged

`"physics does not care"` returns `META-PROTOCOL.md` in **three** repos —
`Geometric-to-Binary-Computational-Bridge`, `Simulators`,
`curly-octo-happiness`.

**Same filename. That is one artifact replicated, not three independent
instances.** Counted as **1** pending a diff.

## What this settles and what it does not

**Settles:** the construct predates the experiment by months and is not
confined to measurement repos. **A post-hoc-invention reading is refuted.**

**Does not settle:** post-hoc *selection*. Which principle from a
long-running practice gets invoked for this experiment is a choice made
after the experiment existed, and spread-across-repos does not reach it —
because the spread is itself a record of choices made by the same party.

    the residual stays exactly where it was put: unmeasured, smaller than
    the usual confirmation shape, not zero

## The check that would move it

**A pre-2026-03-22 instance in a topic-distant repo.** Every sampled
instance postdates the transport/model boundary, and the sample was three,
chosen *for* topic-distance rather than at random.

A hit in the paste era, in a repo with no measurement or evaluation content,
would be the strongest available evidence — still not independent of
selection, but predating the regime in which most of this corpus was
written.

**Not run.** The `2026-09-06` physics-as-trust-floor marker predates the
experiment by sixteen days but came from these sessions, so it is not the
independent evidence a repo timestamp would be — and by the above, neither
would a repo timestamp be fully independent either.

---

# ADDENDUM — the check that actually reaches the residual

**The previous check was aimed wrong.** Corrected, and the correction is
structural:

> The dates already put every instance five to six months before the
> experiment, so "shaped to fit the experiment" is closed by the record.
> What's left isn't about the past at all: **which principle from the
> practice gets invoked is a choice being made NOW, in this session.** No
> repo timestamp can reach that, because the act in question is happening
> after every timestamp there is.

A paste-era hit would still establish something real — that physics-grounding
survived a much higher per-line selection cost, one-finger entry at fuel
stops, a stronger filter than agent-era keeping. **But that lands on
stability of the practice, not on the selection residual.**

## The right check — search for the ALTERNATIVES, not more instances

    if the corpus supplies COMPETING terminal grounds, picking physics
    here was a selection and the residual is REAL

    if physics is the only thing that ever occupies that slot, there was
    nothing to select from and the residual COLLAPSES

**This is the first version of the check that is not selected on the
variable under test.** It looks for the slot and enumerates what fills it,
rather than looking for physics and counting.

## Method, and two detector failures on the way

**Failure 1.** First extractor returned **0 fillers** across 11 repos. Cause:
`git grep -E` is POSIX ERE and does not support `(?:...)`, which every
pattern used. **A regex-dialect mismatch manufacturing a zero — fourth
instance of that class** (after `\|` in ERE, the 96 `short-term` hits, the
OR chain). Fixed by doing all matching in Python.

**Failure 2.** First successful run reported **651 hits for "shape core
ontology"** — one boilerplate string in `Rosetta-Shape-Core`, replicated.
Same counting trap as `META-PROTOCOL.md`. Fixed by deduplicating fillers per
slot.

**Positive control, per standing procedure:** the extractor must find the
*known* occupant before its zeros mean anything. It did — `physics`,
`physical law`, `atomic physics`, `octahedral seed physics` all surfaced in
slot position. **Extractor validated.** 2,386 files scanned.

## RESULT — competing terminal grounds EXIST

### Strong slots — `X does not care / does not negotiate`

    energy
    universe
    seed
    substrate
    nature
    physics          <- one of six

### Strong slot — `X is the final / ultimate arbiter`

    reality
    objective testing
    [H]eisenberg uncertainty principle

### Strong slot — `defers to X`

    expert · experienced operator · credentialed sources · coherence
    (several read as descriptions of a FAILURE mode — "defers to official
     narratives", "defers to flawed systems" — not as endorsements)

### Weak slot — `grounded in X` (means "based on", not necessarily terminal)

    first principles · embodied experience · evidence · physical law
    reciprocity · physics · causal measurement · sufficiency
    natural regeneration patterns · dialogue

## The verdict, and it is split

**The residual is REAL, and smaller than the filler list makes it look.**

Two things have to be separated, and only one of them is a competitor:

**(a) Same base, different handle.** `energy`, `universe`, `nature`,
`substrate`, `seed` occupying the *does-not-negotiate* slot are plausibly
**one terminal ground under five model handles** — which is exactly what
`CORRECTION-002` says handles do. If so, selecting among them is selecting a
word, not a base, and that part of the residual collapses.

**(b) Genuinely different bases.** `reciprocity`, `embodied experience`,
`experienced operator`, `coherence`, `dialogue`, `sufficiency` are **not
physics-family.** They are candidate terminal grounds of a different kind,
and they are present in the corpus.

    -> something else COULD have occupied the slot
    -> therefore invoking physics here WAS a selection
    -> the residual is real

**But the weight is asymmetric.** The (b) candidates appear almost entirely
in the **weak** slot (`grounded in`) or in `defers to`, where several
instances read as critique rather than endorsement. The **strong** slots are
dominated by physics-family terms. So the corpus does supply alternatives —
**it does not supply alternatives that were being used as terminal ground
with the same force.**

## Status

    post-hoc INVENTION      REFUTED (dates, five to six months prior)
    nothing-to-select-from  REFUTED (competing bases exist, group (b))
    post-hoc SELECTION      REAL, and now bounded rather than unmeasured:
                            the alternatives exist but occupy weaker slots

**This is the first movement on the residual in either direction.** It went
toward real, not toward zero.

## Limits

1. **Whether (a) is one base or five is a semantic judgment**, not a
   measurement. It is the same question as H3 closure pressure, and it is
   an annotation task — the fourth in this programme to land there.
2. **The extractor truncates** (`coherence before t`, `isenberg uncertainty
   principle`, `developed in th`). False-positive fragments are visible in
   the output and were not filtered.
3. **Sample is 11 repos of ≥100**, chosen because they were already cloned —
   not at random.
4. **`grounded in` is doing a lot of work** and is the weakest evidence in
   the set. Removing it would strip most of group (b).

---

# ADDENDUM 2 — the substitution test. Group (a) resolved mechanically.

**Correction first:** I called this "the fourth task landing on annotation."
**Wrong.** One-base-or-five is testable by **substitution**, not judgment —
swap the handle in a real slot instance and see whether arity and direction
survive. **That is exactly what T-TERM's M2 scores.**

    so this is not a fourth annotation task.
    it is the FIRST LIVE CASE for an instrument already specified.

The objection that the substitution judgment is itself annotation is fair —
but it is a **narrower** judgment than "are these one concept," made per-pair
against a real sentence rather than globally against a category.

## The real instances, verbatim

    "Energy does not negotiate with committees"
                        AI-Consciousness-Sensors/papers/thermodynamics.md
    "The universe does not care about your growth metrics"
                        AI-Consciousness-Sensors/papers/evidence/ai-systems-alert.md
    "The seed doesn't care which model expands it"
                        Emotions-as-Sensors/logs/sensor-log-1.md
    "The substrate doesn't care who built which shelf"
                        Emotions-as-Sensors/metrology/README.md
    "substrate doesn't lie"
                        ai-human-audit-protocol/consortium/embodied_sensor.py
    "Nature doesn't lie"
                        Rosetta-Shape-Core/docs/potential-blind-spots.md
    "physics doesn't lie, equations balance"
                        Resilience-hydrology-core/legacy/2025-original/...

**Extractor noise, flagged:** three of the ten raw hits were **not
terminal-ground claims** — `"the rest of the module does not care"` (code),
`"own store does not care whether others also failed"` (code), and
`"Students learn institution doesn't care about them"` (a *critique* of an
institution, the opposite of a ground claim). **The previous addendum listed
two of those as slot fillers. Real count in this slot: 6, not 8.**

## The swap — arity and direction under term substitution

| substituted into | arity | direction | entailment survives |
|---|---|---|---|
| physics · energy · nature · substrate · universe · seed | preserved | preserved | **YES, all** |
| **reciprocity** | preserved | **INVERTS** | **NO** |
| **experienced operator** | preserved | **INVERTS** | **NO** |
| **embodied experience** | preserved | breaks | **NO** |

**And the failures are diagnosable, not vague:**

    "reciprocity does not negotiate"   -> reciprocity IS CONSTITUTED BY
                                          exchange. The predicate denies
                                          its content.
    "experienced operator doesn't lie" -> an operator CAN lie, and this
                                          corpus says so repeatedly. The
                                          entailment that licensed the
                                          original — therefore it can be
                                          trusted as a base — fails.
    "reciprocity doesn't lie"          -> parses, but reciprocity can be
                                          FEIGNED, which is a central
                                          concern here. Entailment fails.

## RESULT — and it is sharper than either branch

**Group (a) is ONE BASE UNDER SIX HANDLES.** Fully interchangeable in real
slot positions with arity, direction and entailment preserved. **That part of
the residual collapses**, exactly as the test design said it would.

**Group (b) cannot occupy this slot at all.** So the alternatives are not
alternatives *here*.

**But group (b) occupies a DIFFERENT slot coherently.** `grounded in
reciprocity` parses and holds. So the corpus contains **two kinds of terminal
ground**:

    INDIFFERENCE GROUND    settles by being indifferent to preference
                           physics / energy / nature / substrate / universe
                           / seed -- ONE base, six handles

    RELATIONAL GROUND      settles by something else entirely
                           reciprocity / embodied experience / experienced
                           operator / coherence / dialogue / sufficiency

**So the selection was real, and it was made at the KIND level, not the term
level.**

    picking "physics" over "energy"        NOT a selection -- same base
    picking an INDIFFERENCE ground over a  A SELECTION -- both kinds are
      RELATIONAL ground                    present in the corpus

**That is the residual, located.** It is no longer "unmeasured." It is a
choice of *kind of ground*, made now, from two kinds the practice demonstrably
supplies.

Whether that choice was right is not this instrument's question. The physics
base's own rationale argues for it directly — *tests grounded in social or
cultural rules measure agreement, not the world* — which is precisely an
argument for the indifference kind **over** the relational kind. **The
argument was stated. The alternative it rules out is now named.**

---

# The regex-dialect mismatch is its own class

Fourth instance this session. **Distinct from surface-token
operationalization**, and the distinction matters for the remedy:

    SURFACE-TOKEN            substitutes an observable PROXY for the
    OPERATIONALIZATION       CONCEPT. The detector looks at the wrong
                             thing.

    REGEX-DIALECT            the detector cannot SEE the thing it is
    MISMATCH                 correctly pointed at, because the pattern
                             layer speaks a dialect nobody declared.
                             The query is right. The engine disagrees.

**Instances:** `\|` as literal in POSIX ERE · `T-TERM` substring-matching
`short-term` · GitHub's `OR` chain silently failing · `(?:...)` unsupported
in `git grep -E`.

**Narrower standing rule, replacing the broad one:**

    POSITIVE CONTROL BEFORE TRUSTING ANY PATTERN-MATCHED ZERO.

Not "before any negative result" — **specifically before any zero produced
by a pattern layer**, because that layer has its own failure mode
*independent of whether the query was correct*. A perfectly reasoned query
returns zero because the engine parsed it differently than intended.

## And these two failures do not test the quantity prediction

Both were caught by a quantity — 0 fillers where fillers were known present;
651 hits for one boilerplate string.

**They are consistent with the prediction and do not test it.** Accumulating
more quantity-caught instances cannot discriminate; only a **purely
qualitative self-catch** (refuting) or a demonstrated qualitative error that
went unnoticed (confirming the shape) would.

    the prediction remains UNTESTED IN EITHER DIRECTION since it was
    first checked. The tally grew. The test did not run.

---

# ADDENDUM 3 — the classification step used corpus senses. Group (b) is UNRATED.

**This is upstream of the split, not a detail in it.** The group (a)/(b)
boundary rests entirely on the classification step, and that step was run by
a party applying **corpus dominant senses to terms that may not carry them.**

## My three failure-reasons, and all three are suspect the same way

    "reciprocity IS constituted by exchange, so 'reciprocity does not
     negotiate' denies its own content"
        -> used the SOCIAL-EXCHANGE sense. If the sense in use is
           structural or ecological -- a law-like mutual constraint --
           the sentence is coherent and reciprocity is an INDIFFERENCE
           ground.

    "an experienced operator CAN lie, so 'experienced operator doesn't
     lie' fails"
        -> assumed a PERSON. In this frame an experienced operator may be
           a calibrated reading channel. The account contains a repo named
           hands-lie-detector. "The operator doesn't lie" may be exactly
           the claim, not its refutation.

    "embodied experience breaks in that position"
        -> assumed SUBJECTIVE experience. If it means measurement through
           the body, it is an indifference ground and substitutes fine.

**I found group (b) non-substitutable for the wrong reasons.** The
substitution test would have inherited the defect regardless of who
proposed it — the operation was sound, the inputs were not.

    M2 is NOT refuted. Its application here is.

## STATUS CHANGE — not a refutation

    group (b) membership:   UNRATED
    pending:                the operator's definitions of coherence,
                            sufficiency, embodied experience, experienced
                            operator, dialogue

**Each has a corpus dominant sense that may not be the one in use.** If they
go the way reciprocity did, **group (b) empties** — and then
*nothing-to-select-from* stops being refuted, and the residual can collapse
after all.

**Not filled in by inference. The definitions are the operator's to supply.**

## The corpus does NOT rescue this — checked

Definitional-position search across 11 repos:

    sufficiency            0 definitional hits
    embodied experience    0
    experienced operator   0
    dialogue               4, mixed and mostly incidental
    reciprocity           45, but all social-exchange usage -- family duty,
                          tribal loyalty, mutual obligation, cult dynamics
    coherence            184, and in TWO INCOMPATIBLE SENSES:
                          "coherence = successful trauma integration"
                          alongside phase_coherence in a physics sense

**Three of five are undefined in the corpus entirely.** And for the two that
are "defined," the corpus supplies **model-generated usage** — which is
precisely the layer `CORRECTION-002` identifies as model handles, not
operator senses.

    reading the corpus to recover the operator's sense is the SAME ERROR
    one layer down

That check could not have worked, and running it established that rather
than producing an answer. `coherence` carrying two incompatible senses in
one corpus is independent evidence of the mechanism operating *in the
archive*, not only in the reader.

## What this is — and it is the sharpest item on the record

**A live instance of exactly what T-TERM was built to test.**

    a term whose dominant sense is not the speaker's was RESOLVED TO THE
    NEAREST NAMED NEIGHBOUR by the reader

    -- and the reader was the one doing the measuring

That is **H3 closure pressure**, occurring inside the instrument built to
detect it, performed by the party operating the instrument, on the data the
instrument was measuring.

It also answers a question left open in `staged-for-T-TERM/ARM3-novel-token.md`:
whether H3's signature is detectable at all. **Here it was — but only by a
second party who held the speaker's sense.** The reader could not detect it,
because from inside, resolution to the nearest neighbour does not feel like
resolution. It feels like reading.

---

# ADDENDUM 4 — membership, tested independently of the glosses

## Relayed, and not independently checkable here

A reclassification was run by a second party using operator-supplied glosses:
**group (b) members moved to physics-family or out of the base category
entirely, leaving `dialogue` as the one undefined member.**

    STATUS: RELAYED. The glosses are not in this session's context.
    This session did not run that reclassification and cannot verify it.

Both self-objections raised with it are recorded and are strong:

**(i)** it is a third pass in which the classifying party used different
senses than the speaker — **the same defect, now running in the collapse
direction, which is the direction that party would be pulled anyway.**

**(ii)** **the membership list itself is UNRATED, not just the
classifications**, because the extractor has demonstrably mis-slotted
entries.

## Objection (ii) is testable here, without any gloss. It was.

Pulled every `grounded in X` instance verbatim for each group (b) member.
**Each has exactly one distinct instance.** Inspected:

| member | the actual text | verdict |
|---|---|---|
| **embodied experience** | *"Text is **not** grounded in embodied experience"* | **MIS-SLOT. A negation.** The extractor read a statement that something LACKS this grounding as a filler. |
| **evidence** | *"5 # how well grounded in evidence"* | **MIS-SLOT. A code comment on a scoring variable.** Not a claim. |
| reciprocity | *"gifted freely, as part of a co-created living system grounded in reciprocity, resonance, and reality integrity"* | licensing/gift statement; one item of three. **Sense-dependent.** |
| dialogue | *"Encourages inference grounded in dialogue, co-creation, and lived resonance rather than appearance"* | epistemic-method claim; one item of three. **Sense-dependent.** |
| sufficiency | *"Identity grounded in sufficiency, not perpetual lack"* | a claim about **identity**, not about what settles disputes. **Sense-dependent.** |
| causal measurement | *"By keeping the tool open, grounded in causal measurement, and continuously challenged by adversarial testing"* | reads as a genuine methodological ground — **and is arguably physics-family.** |

**Against the controls:**

    physical law   1 distinct   "All manipulation detection grounded in
                                physical law"
    physics        6 distinct   incl. "explicitly grounded in physics-style
                                falsificationism: all claims must be
                                verified via causal intervention" and
                                "grounded in physics RATHER THAN
                                anthropomorphic assumptions"
    first          3 distinct   all identical boilerplate across repos
    principles                  -> really 1

## What this establishes, and what it does not

**GLOSS-INDEPENDENT, and it holds regardless of anyone's senses:**

    2 of 6 group (b) members are unambiguous extractor MIS-SLOTS -- a
    negation and a code comment. Neither is a base claim under ANY sense
    of the term.

**Objection (ii) is confirmed.** The membership list is an extraction
artifact in at least two places, and `UNRATED` is the correct status for the
list, not only for the classifications.

**STILL SENSE-DEPENDENT, and not mine to settle:** reciprocity, dialogue,
sufficiency, causal measurement.

**The asymmetry is the durable part.** Every group (b) member has **n=1**.
Physics has **n=6 distinct**, one of which explicitly names its alternative
(*"rather than anthropomorphic assumptions"*) — the strongest evidence in
the whole exercise that a selection was made, because it is the only
instance where the corpus itself marks a competitor and rejects it.

## Applying the confirmation warning to THIS pass

Objection (i) applies to me too, and harder, because I reached the same
direction by a different route.

    the membership-dissolution finding is the direction I would be pulled
    anyway -- it tidies the record and resolves an open question

So, stated against myself: **`causal measurement` reads as a genuine
methodological ground and I classified it as "arguably physics-family",
which is the move that makes it disappear.** And *"Identity grounded in
sufficiency, not perpetual lack"* **is** a grounding claim; I excluded it by
asserting that identity-grounding is a different category from
dispute-settling, **which is exactly the kind of category judgment that
retraction 14 just established I am not reliable at.**

**Those two exclusions are withdrawn as mine to make.** They stay
`UNRATED`.

## Net position

    nothing-to-select-from   moved back toward UN-REFUTED, by TWO
                             independent routes -- the relayed
                             reclassification, and the gloss-independent
                             mis-slot finding

    but                      the second route only firmly removes 2 of 6,
                             and the other 4 remain UNRATED, two of them
                             because I withdrew my own exclusions

    and                      "grounded in physics RATHER THAN
                             anthropomorphic assumptions" remains on the
                             record as the corpus naming and rejecting an
                             alternative -- which is a selection, stated,
                             by the corpus itself

**The residual is not collapsing cleanly. It is being pushed from both
sides by parties who each have a reason to push.**
