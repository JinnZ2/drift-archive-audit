# Proposal for Keystone-Codex — one type change, not a note

**Staged, not applied. Nothing in this directory has been committed to
`Keystone-Codex`, and the audit remains read-only on source repos.** Whether
to take it is that repo's call.

**The disposition changed, and the change is the point.** The audit first
filed this as *reported, not fixed*. That is the wrong disposition for a
defect that is fixable by one type change — "reported" and "here is the
patch and its measured cost" are different things to hand someone.

## The defect

    rules/keystone_rules.json v1.1
      replication   ">= 2 regions INDEPENDENTLY"     weight 0.14

    src/prove.py::_c_replication
      v = x["metrics"].get("replication_regions", 0)
      return v >= thr

The word carrying the load is **INDEPENDENTLY**. Establishing it for a single
entry — `terra_preta` — took two filed documents and still came back split
into a *practice level* and a *recognition level* that disagree.

**A schema that accepts a bare integer for that quantity is the surface-token
class at the schema level.** The criterion is operationalized by the variable
that is easy to store, which is the same failure this audit logged seven times
in its own instruments.

## Measured, read-only, against the live corpus

    entries with metrics                     42
    rely on replication (rep >= 2)           37
    of those, carrying any basis              0
    would become NOT_EVALUABLE               37   (88%)
    would become FAIL                         0

**Every changed verdict moves `PASS -> NOT_EVALUABLE`. None moves to `FAIL`.**
Nothing here says an entry misses the bar. It says the bar was never applied.

Run it: `python3 replication_not_evaluable.py /path/to/Keystone-Codex`

### A crude pointer, marked as crude

Ten entries assert `replication_regions >= 2` while their `region` string
enumerates no second place — `apprenticeship_systems` (12) and
`reciprocity_norms` (12) are the extremes, both with region strings of the
form *"Global (every documented …)"*.

**That count comes from counting commas in a string, which is exactly the
surface-token operationalization this proposal is about.** It is a pointer
for a human to look at, not a finding. `UNRATED`.

## The change

    schema/keystone.schema.json
      replication_basis : string
      REQUIRED when metrics.replication_regions >= 2

    src/prove.py::_c_replication
      returns PASS / FAIL / NOT_EVALUABLE
      NOT_EVALUABLE when the count is asserted and the basis is absent

`NOT_EVALUABLE` is **not** `FAIL`. Same distinction as
`instrument/guarded_count.py`'s `DETECTOR_BLIND`, for the same reason: a
missing measurement must not be usable as a value. A `NOT_EVALUABLE`
criterion must not silently score 0 — that penalises an entry for a missing
field — and must not score its weight, which is today's behaviour. **The
aggregate becomes `NOT_EVALUABLE` until the basis exists.** That is the
no-PASS-state move applied to a rule set.

## Why a documentation fix would not hold

v1.1's own `revision_note` is the diagnosis:

> v1.0 scored only what an author asserted about a technology (longevity,
> regions, unlocks, decentralization) and never scored the evidence behind
> the assertion, so an entry could reach 1.0 on four numbers typed by hand.

**v1.1 fixed it by adding three evidence criteria ALONGSIDE the four, not by
backing them.** The naming was correct, the diagnosis was correct, and the
rate did not move — `replication_regions` is still one of the four numbers
typed by hand. See `../REMEDIES.md`: of seven logged instances of the
surface-token class in this programme, **naming prevented zero.**

## The precedent is already in the same file

    longevity   ">= 300 years durable or revivable; WHERE THE FIGURE IS NOT
                 DERIVABLE FROM THE ERA, THE ENTRY MUST DECLARE A
                 longevity_basis"

`longevity_basis` exists in seven entries. **The mechanism is already built
and was applied to one metric of four.** This proposal extends it to the
second, and the same argument applies to `unlocks_lineage` and
`decentralization_score`, which are not addressed here.

## What this does not decide

- What `terra_preta`'s three regions actually are. That is an entry-level
  question and the audit has no standing to answer it.
- Whether the West African dark-earth practice belongs in that entry. See
  `../DARK-EARTHS-CONSEQUENCES.md` §1 — the evidence is filed, the decision
  is not the audit's.
- Whether 88% `NOT_EVALUABLE` is acceptable during a transition. A staged
  rollout is a maintainer's call; the number is given so the call can be
  made with it rather than around it.
