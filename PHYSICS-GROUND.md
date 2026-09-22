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
