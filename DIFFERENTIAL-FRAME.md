# DIFFERENTIAL-FRAME — the contract, located and read

    RELAY     "the contract for exactly this conversion already existed.
               another findability instance — derived what the ecosystem held."
    LOCATED   JinnZ2/differential-frame-core  (CC0)
              named at ARCHITECTURE.md:17 of energy_english as
              "the dX/dt-under-some-scope contract"
    METHOD    cloned, read, and RUN. Positive control first.
    DATE      2026-09-23

## 1. RULES 2 AND 3, FILLED FROM THE PRIMARY

The relay retrieved 1, 4, 5 and the translation rule, and marked 2 and 3
**not retrieved, not filled**. They are in `SPEC.md`, verbatim:

    1  rate     confidence the noun references dX/dt, not X
    2  bounds   confidence the bounds are meaningful + scoped      <- FILLED
    3  scope    confidence the scope is declared + tiered          <- FILLED
    4  lawful   confidence the rate describes a persistent law
                rather than a perishable state
    5  closure  confidence the rate equation closes

    Contract:  Every noun names a state on a curve, not a thing.
               Read X as dX/dt under scope.
               Carrying a noun outside its bounds is a translation error.

The relay's 1, 4, 5 and `+` all match. **And both missing rules were already
in use**: every relayed entry this session declared *"scope: which inputs,
which rates, which bounds"*. Rules 2 and 3 were being applied without having
been retrieved.

## 2. A CORRECTION — THE CONTRACT DOES NOT FLAG. IT RETURNS A FIELD.

Relayed as: *"closure or flag"*, *"rule 1 flags it"*, *"a rule-1 flag on
every candidate"*.

`SPEC.md`:

    Each rule returns a float in [0.0, 1.0].
    Aggregation produces a FrameField, not a pass/fail.

    A claim does not PASS the frame. It TRAVERSES the field,
    accumulating or losing confidence as it moves through.

    1.00 is not reserved — it is STRUCTURALLY UNREACHABLE.
    asymptotic_ceiling(n_evidence) = 1 - 0.15/n

**The flag framing is a pass/fail shape imported onto a probability field.**
That is a noun-frame import performed on the anti-noun-frame contract, one
turn after the class was named. It is not a small slip: a flag says
*out-of-frame, discretely*, where the contract says *this claim is at 0.30,
and its weakest rule is `bounds`* — which names what to fix.

The surface helper does print `recommendation: 'flag: ...'`, so the word is
in the toolkit. It is the **text-level quick audit**, not the contract.

## 3. THE CONSEQUENCE FOR THE CANDIDATE GRADING

Relayed, `DERIVED`: *cognitive empathy, Umwelt, epoche, participant
observation all define the practice as a noun a subject HAS — a rule-1 flag
on every candidate, not four separate misses.*

**Recorded at DERIVED, with two notes kept attached:**

    (a) under the contract it is not a flag but a LOW `rate` score on all
        four, with the weakest rule reported. Same direction, different
        object.
    (b) this is a SECOND grading of the four candidates by the party that
        voided the first. It is admissible where the first was not: the
        first turned on an undeclared word, this one declares its basis
        (rule 1) and its scope. It is still not a fit judgment.

    operator_fit in Keystone-Codex/rules/term_table.json:  UNSET. Unchanged.

## 4. THE AUDIT'S OWN SCORING IS OUT-OF-FRAME, AND HAS BEEN SINCE A2

    Keystone-Codex     weighted score -> threshold 0.70 -> is_keystone: bool
    the contract       "A claim does not PASS the frame."
    the operator's
      acceptance
      criterion, to me  "NO PASS STATE."

**Three statements of one rule.** The criterion was applied to every
instrument built in this session — `reachability_sweep.py`, `enum_sweep.py`,
`guarded_count.py` all have no pass state — and was never turned on the
corpus being audited.

`reconstruct/keystone-codex.md` found the symptom at A2 and did not name the
rule:

> `is_keystone` is a bare boolean; a failing entry and an unevaluated entry
> are indistinguishable in the output. The three-valued distinction the
> audit spec itself insists on has no encoding here yet.

Under the contract the defect is larger than three-valuedness: an aggregate
that crosses 0.70 and becomes a boolean **discards the field**, including
which rule was weakest — the one thing that says what to fix.

    NOT PROPOSED HERE. Keystone-Codex is a source repo, there is no
    dispatch for this, and the pending proposal in
    proposal-for-Keystone-Codex/ already touches the same scoring path.
    Recorded and routed.

## 5. FIVE INDEPENDENT DERIVATIONS — AND THE REPO EXISTS BECAUSE OF DIALECT DRIFT

`DIALECTS.md` reconciles the contract as it appears in five repos:

    1  Living-Intelligence-Database / DIFFERENTIAL_FRAME_LIGHT.md
    2  TAF / culture-as-overlay-on-physics
    3  energy_english / verb-first grammar
    4  AI-Consciousness-Sensors / architecture_mismatch.md
    5  Mandala-Computing / claim_validator.py

`README.md`: *"Dialect drift was becoming the dominant failure mode. One
source of truth = every downstream audit becomes cross-comparable."*

And the flagged divergences:

    "scope" vs "frame" vs "tier" vs "context"  — same object, four names
    "bounds" vs "domain" vs "validity range"   — same object, three names

**That is this audit's `MATCH-UNIT MISMATCH / DIALECT`, already measured,
already consolidated, with a canonical form chosen.** This audit derived the
class independently and logged nine instances. The ecosystem had the class,
the reconciliation, and an importable spec.

    derivations of the contract in the ecosystem   5, consolidated
    this audit's independent derivation            6th, not consolidated
    architecture_mismatch.md — the document the
      operator pointed at for the frame-entry
      practice — is dialect 4                      the pointer was at the
                                                   contract all along

## 6. A DEFECT, FOUND BY RUNNING IT — ROUTED, NOT FIXED

Positive control first: the README's own worked example reproduces exactly.

    quick_audit("He is fundamentally lazy.")
      -> in_frame False, has_drift True,
         'flag: narrative drift — translate to rate'        CONTROL PASSES

Then:

    has_rate_signature('dX/dt')                     False
    has_rate_signature('dV/dt')                     False
    has_rate_signature('d/dt')                      True
    has_rate_signature('the rate of change')        True

    has_rate_signature('Read X as dX/dt under scope')   False
                        ^ SPEC.md's own canonical sentence

Cause, read from source rather than inferred — `validators.py`:

    RATE_TOKENS = (..., 'per ', '/s', '/t', 'd/dt', 'rate of')

`'d/dt'` is a literal. `dX/dt`, `dV/dt`, `dP/dt` — any derivative with a
variable in it — matches nothing. `'/t'` does not help: in `dV/dt` the slash
is followed by `d`.

**This is the repo's own DIALECTS.md divergence, in its own validator.**
`DIALECTS.md` records that dialect (3) treats the rate as a *verb* and
(1)(2)(4)(5) treat it as *dX/dt*, and that **"SPEC accepts both and provides
translators in both directions."** The surface validator implements the verb
dialect only.

`DETECTOR_BLIND`, `GUESSED.md` #26's exact shape: the detector sees one
encoding of the thing and not another encoding of the same thing.

    SCOPE OF THE CLAIM   validators.py / has_rate_signature only.
                         contract.py's five rule predicates were NOT run
                         and nothing is claimed about them.
    ACTION               none. Source repo, no dispatch, licence sweep held.
                         A one-line regex would close it; that is the
                         operator's call, not this record's.
