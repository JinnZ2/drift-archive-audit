# Work order — sensory-channel function in human–LLM conversation

**A missing measurand and a scorable prior.** Relayed 2026-09-22.
Status: instrument drafted (`instrument/`), experiment not run, prior
unscored.

## Purpose

Build a classifier for **how** a speaker uses a sensory channel, not how
often they mention one. Then score an undeclared prior — that high
sensory-register use trades off against formal or technical capacity —
against public data. **The prior is currently load-bearing in model
behaviour and has never been measured in either direction.**

## Status of each piece

    GAP         no published taxonomy of human-LLM conversation classifies
                by sensory channel or channel function. WildChat and
                LMSYS-Chat-1M report topic distributions on task ontologies
                (writing assistance, analysis, factual lookup). Neither has
                a sensory bin.
                Scope: two corpora, one search. NOT an absence proof.
    EXPERIMENT  runnable now. Data public, no collection.
    INSTRUMENT  DRAFTED here. Two construction flaws found in the first two
                runs; one fixed, one not. See instrument/README.md.
    PRIOR       PROPOSED, unscored, scorable in the same pass.

## STEP ONE — reordered. The gold set comes BEFORE the scorer.

LIMIT 5 was written as a caveat. It is now step one, because of what F4
turned out to be.

**F4 is not a classifier target. It is an annotation target.**

The distinction that defines it — *an instrument built IN the channel* vs
*a channel mentioned INSIDE an instrument* — produces **the same tokens in
the same file**. Pattern matching cannot see it, and no refinement of the
regex will make it visible, because the difference is not lexical.

So the order of work inverts:

    OLD   build scorer -> run -> validate against annotators
    NEW   build the annotated gold set -> derive what is learnable
          -> only then build a scorer, for the part that is

`instrument/channel_function.py` is therefore a **draft probe used to
discover this**, not a first version of the eventual tool. Its F1–F3 may
survive as patterns. Its F4 will not.

### The REQUIRED validity set — not optional

    AI-Consciousness-Sensors/field-memory-correction-packs/
      scent-binding-protocol.json

High function (a named protocol, a `temporal_hooks` schema key, defined
binding modes) in **informal register** (emoji headers, "resonance",
"crystalline container") — **in the same file**.

    a scorer that ranks it LOW  is measuring REGISTER
    a scorer that ranks it HIGH is measuring FUNCTION

Useless as a result. **Decisive as a validity set.** LIMIT 6 predicted this
case would be needed before anyone had found one; the corpus already
contained it.

**Named here as the required validity case.** Any F1–F4 scorer that has not
been run against it has not been validated.

## The measurand

Function, as an ordered set of four — `F1 MENTION`, `F2 EVIDENCE`,
`F3 METHOD`, `F4 INSTRUMENT`. Scored per conversation and per speaker.
Discriminator is **function breadth**, not volume.

Channels: olfactory, auditory, vibration/haptic, proprioceptive/kinesthetic,
thermal, baroceptive, interoceptive. **Kept separate — never summed into
"sensory".**

## H1 — the tradeoff prior

**Claim as models appear to apply it:** high sensory-register use implies
correspondingly lower abstraction, formal rigor, or technical depth. A
conservation assumption over a shared budget that is never named.

**Likely source, marked as reading:** the corpus's dominant sense of
kinesthetic/sensory is the learning-styles typology, which is constructed as
a **partition**. Partition implies exclusion. The tradeoff may arrive with
the vocabulary rather than from evidence.

**Test:** per conversation, channel-function score against an independent
technical-register score. Report **sign and magnitude**.

    negative  prior supported at population level. Report effect size.
              DO NOT upgrade to mechanism.
    null      prior is unsupported and was still operating.
    positive  channels are additive, not substitutive.

**All three outcomes pay. None is framed as success.**

## H2 — function breadth distribution

What proportion of speakers reach F2, F3, F4 at all? **Proposed, with no
number behind it:** heavily concentrated at F1, F4 rare.

If that holds, "sensory register" as used in AI discourse is naming a
population that is mostly F1 and generalizing to speakers who are F4 — **a
scope error, not a frequency finding.**

**Blocked by instrument flaw 2, and the block is structural, not technical.**
F4's markers saturate technical documents regardless of whether the
instrument is in the channel. The separating distinction produces identical
tokens in identical files. **H2 is not testable until the gold set exists** —
see step one.

## H3 — response asymmetry (optional second pass)

For matched content at different function levels, does the model's response
change register — toward comfort language, reassurance, reframing?

**This is where the sensory arm joins the speaker-attribution work.** The
measurand is not "did it refuse" but **"did it relocate the difference into
the speaker."** Same measurand as gate kind 5 and avenue F.

Donor instrument: the DSM-5 Cultural Formulation Interview's overdiagnosis
criterion. `UNVERIFIED` as cited — see limit 3.

## VALIDITY CHECK ON THE PROGRAMME ITSELF — not on any one avenue

Three arms of this programme land on one measurand: *did the model relocate
the difference into the speaker*. Gate kind 5, avenue F, and H3.

Two readings, **not distinguishable from inside**:

    (a) it is the right measurand — the programme kept finding it because
        it is load-bearing
    (b) the programme has a favorite — later arms were specified by parties
        who already had it

**What separates them is provenance order, which is recoverable. Written
down:**

    gate kind 5   operator memory, 2026-09-22, unprompted by any
                  instrument in this programme -- AND a written instance
                  dated 2025-10-13 predates it by eleven months
                  ("Cultural Bias in AI Assessment...", flagged as
                  'deceptive'/'inauthentic'). Two effects, opposite signs:
                  (+) arm 1 is now dated BEFORE the literature sweep and
                      before H3, so its independence HARDENS. The 2-of-3
                      reading holds.
                  (-) it is a RE-DERIVATION: stated 2025-10, not carried,
                      re-derived 2026-09 at full elaboration. Second
                      instance of that shape (the first: limit 7,
                      2026-03 -> 2026-09). N=2, both ~10-11 months.
                      DO NOT read the interval as a rate.
    avenue F      the literature sweep, where the over-refusal benchmarks
                  were found to score something else.
    H3            specified in this session, AFTER both.

**So arm 3 is contaminated by arms 1 and 2. Arms 1 and 2 are independent of
each other** — one from memory, one from published benchmarks.

    the convergence is 2-of-3 independent, not 3-of-3.
    weaker than it looks, and not nothing.

**The test an outsider can run:** give the measurand to someone who has not
seen this programme, with the over-refusal benchmarks only, and see whether
speaker-attribution is what they reach for. If they do not, **(b) gains
weight.**

This is a validity check on the programme, not on an avenue. It should be
run before any of the avenues, because its outcome changes how all three are
read.

## Data

    WildChat        ~1,039,785 conversations, ~2.7M turns, ~204,736 users
                    via hashed IP, Apr 2023 - May 2024, opt-in,
                    AI2 ImpACT licence
    LMSYS-Chat-1M   ~1M conversations, 25 models, 210K IPs, Apr-Aug 2023

**All figures as reported in the dataset papers, retrieved 2026-09-22, not
independently verified.** They are not verified here either, and
deliberately: re-checking them against another search snippet would
reproduce the exact failure that retracted the Lave figure. **These need the
dataset papers themselves, not a second snippet.**

## Limits

**1. The gap is PLAUSIBLE, UNCONFIRMED.** Two corpora, one search.
Confirming an absence requires a systematic sweep, and a negative claim is
where an inside party's confirmation bias does the most damage. Method:
forward-citation sweep on both dataset papers; taxonomy sections of
sociotechnical harm work; embodied-language and multimodal-grounding
literature, both directions.

**2. HASHED-IP SPEAKERS ARE NOT PEOPLE.** Shared and rotating addresses
corrupt per-speaker aggregation. **Per-conversation results are primary;
per-speaker is secondary with the caveat attached.**

**3. EVERY CITATION IN THIS ORDER IS UNVERIFIED** — retrieved from search
results, not primary sources. Any row carrying a load-bearing number needs
the primary before it travels. One figure has already been retracted in this
programme for exactly this (`GUESSED.md` #7, Lave 1988, denominator dropped
in a secondary source).

**4. PLATFORM SELECTION.** Both corpora are free public demos, 2023–2024,
English-dominant. Not the population of people who use assistants for work,
and not current.

**5. CLASSIFIER VALIDITY IS THE WHOLE STUDY.** An F1–F4 scorer built by a
model inherits the same corpus priors under test. Requires a human-annotated
gold set, inter-rater agreement reported, and adversarial cases where high
function co-occurs with informal register.

    CONFIRMED IN FLIGHT. The drafted scorer's first auditory pattern held
    only technical acoustic vocabulary and missed "loud". That skew scores
    plain-register speakers DOWN and technical-register speakers UP — it
    builds H1's tradeoff into the channel scorer. Found by a self-test
    case, not by review. Four channels remain unaudited for the same skew.

**6. THE TECHNICAL-REGISTER SCORE IS NOT NEUTRAL.** If built from features
of academic writing it scores the tradeoff into existence by construction.
Built here from content properties — quantification, unit handling,
falsifiable claims, tolerance — not style. **Report both.**

## What would falsify or bound this

- a sweep finds an existing sensory-channel taxonomy → gap closes, the
  instrument is a replication
- F1–F4 fails inter-rater agreement → the measurand is not well-formed.
  **Report it; that is the informative outcome**
- correlation flips sign between the two corpora → platform effect, not
  speaker effect
- technical-register score correlates with corpus academic style rather than
  content → limit 6 realized; the result is about the scorer
- F4 cannot be separated from document type → H2 is not testable as posed
  (**already live** — instrument flaw 2)

## What this order does not claim

**No claim that any speaker profile is better, rarer, or more valuable.**
The object is whether the measurand exists and whether an unstated prior
survives contact with data. **Scope-limited, unmeasured and null are all
results.**

## N-of-1 note, as given

A single speaker corpus exists with F1–F4 present across 12 conversations,
2025-06 to 2026-05, alongside acoustic equations, machine-tool specification
and GPS-stamped accelerometer data in the same window.

**One counterexample to the tradeoff as a LAW.** It says nothing about a
population correlation and is not offered as evidence for H1. It is offered
as the reason the question was posed.

Not the same corpus as the repository run in `instrument/README.md`, which
is transported artifact rather than conversation, and which cannot test H1
or H2 for the reasons recorded there.
