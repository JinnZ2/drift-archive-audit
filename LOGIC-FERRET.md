# Logic-Ferret — read as a control fixture, and it holds two counterexamples

**Read-only. Not a pilot repo, not scored, no A2 reconstruction exists.**
Read because the operator named it as a positive-control fixture; the
observations below are factual, not verdicts.

## #7 — THE COUNTEREXAMPLE. Scope DOES travel here, and it is not bolted on

`README.md`, its own named section, quoted in full because the wording is the
finding:

> ## Honest limits
>
> The sensors match keywords and patterns. They have no idea what a text is
> about.
>
> Run the article check on the shipped example and you can watch them
> over-fire: `Peripheral Signals` goes RED on "Engineers say" and "Veterans
> say" — ordinary attribution verbs — and `Systemic Alignment` goes RED on
> "budget" and "spending". **A high score means "this text uses flagged
> vocabulary densely", which is *evidence about* camouflage, not a verdict on
> it.** A real emergency contains urgency words.
>
> **This is why the human half exists, and why the comparison runs in that
> order.**

**Three things are attached to the number, not one:**

    THE INCLUSION CRITERION   what a high score actually means
    THE FAILURE MODE          named, with worked examples the reader can
                              reproduce from the shipped sample
    THE DESIGN CONSEQUENCE    the human half exists BECAUSE of this, and
                              the ordering is specified

### What this does to this record's generalization

`DARK-EARTHS-CONSEQUENCES.md` §4 proposed: **the scope does not travel with
the reading.** Three instances. That generalization was already weakened
this afternoon when the operator's own self-flag prompted a check showing the
three were not three instances of one thing.

**This is a positive counterexample, and it is stronger than the weakening.**

    an instrument in this corpus attaches its scope to its number,
    names its own failure mode with reproducible examples, and derives
    a design consequence from it

**So scope-travelling is a VARIABLE, not a constant.** Some instruments carry
it; some do not; one in this corpus carries it better than anything this
audit produced today. The generalization is not repaired by a caveat — the
thing it asserted about instruments in general is false of an instrument
sitting in the corpus it was asserted about.

`GUESSED.md` #28.

## #8 — SignatureMismatch: contract drift as a FAILURE, not a report

`schema_contract.py`:

```python
class SignatureMismatch(Exception):
    """Raised when a consumer's pinned signatures don't match this contract."""

def assert_signatures(expected):
    """Fail loud if the consumer's pinned signatures have drifted from ours.
    TAF's ferret_fieldlink.py keeps its own SIGNATURES copy and calls this
    on import. Any drift -> SignatureMismatch, naming every offending key."""
```

    siblings mirror the contract and hand back pinned signatures
    drift RAISES -- it does not warn, and it does not silently pass
    called ON IMPORT, so nothing downstream runs against a drifted contract

**This is `REMEDIES.md`'s entire thesis, built and shipped in the corpus.**

    REMEDIES.md, written today   "build the property into the tool, don't
                                  document the hazard" -- and it counted
                                  4 structural remedies against 7 naming
    schema_contract.py           a structural remedy for contract drift.
                                 Not a note saying "keep signatures in
                                 sync."

**Sixth derived-as-new**, by this record's count. And it is the closest one
yet to the audit's own subject: **the audit is named for drift**, and a
drift-detection mechanism that fails loud rather than reporting was already
in the corpus.

## The reader-side class — corrected, and the correction is exact

The operator's point, and it lands:

> The machine half and human half are meant to be used against each other.
> The human half needs **a** person, not **the** person. That's reader-side,
> and it's the fourth member of that class — **and unlike the three I listed,
> it exists.**

**Checked against the three this record listed:**

| member | reader-side half | has it ever been performed? |
|---|---|---|
| arm-H3b coding | code ENGAGED / NON-ENGAGED | **no.** `SPECIFIED_NOT_INSTANTIATED`. No stimulus set exists |
| cache-dependency sufficiency | read a section, report where you stop | **no.** Prescribed this morning, never run |
| enum sweep | read the list, report what you recognise | **no.** The list is produced and committed, and sits unread |
| **Logic-Ferret's human half** | **run the comparison against the machine reading** | **YES. Built, shipped, documented, with the ordering specified** |

**All three of this record's members are designs awaiting a reader.** The
fourth is operating. That is not a fourth data point for the class — **it is
the only one that demonstrates the class works.**

`PROPOSED, n = 4` — but the members are not equivalent and the table above is
the reason. **Three specifications and one instance is not four instances.**

## Observation, not a finding

`shadow_catalog.py` and every other module under `knowledge/` carries the
header comment `# RECONSTRUCTED (see CLAUDE.md): same damage pattern as the
other knowledge/ modules`, and `recontextualizer.py` records the one judgment
call made during reconstruction. **A repair log kept in the repaired file.**
Noted; not scored, and no claim is made here about what the damage was.
