# READER-ADAPTATION — the proposal, checked against what exists

    RELAY    "readability tuned to one reader decays on every update,
              by construction. not a skill gap — a moving target."
             + invert who adapts: fixed names as keys, aliases absorb
               each reader's label, one entry point per ecosystem,
               a rename log.                                    DERIVED
    DATE     2026-09-23

## 1. THE ENTRY POINT EXISTS. SO DOES THE LOG. SO DOES THE NAMES-AS-KEYS RULE.

`JinnZ2/JinnZ2/META_INDEX.md` — **233 lines, 83 repo rows, 9 domains, a
per-repo License column** — with the proposal's semantics stated in its own
header:

> slugs are **gate keys, not descriptions** (§2, `gate_log.md`)
> each entry is a **marker, not a position** (§4)
> where the only available English word carries the wrong load, **the word
> is a pointer, the definition is in the entry** (§3)
> Reconsolidation is in progress (`LOG.md`) — apparent independence between
> the repos below is largely apparent.

    proposed                          exists as
    ------------------------------    -----------------------------------
    one entry point per ecosystem     META_INDEX.md, 83 rows, 9 domains
    keep YOUR names as keys           "slugs are gate keys, not
                                       descriptions"
    reader carries the translation    "the word is a pointer, the
                                       definition is in the entry"
    rename log, drift traceable       LOG.md, named in the header
    alias table for one contract      differential-frame-core/DIALECTS.md
                                       (scope/frame/tier/context -> `scope`)

**The pattern is not being proposed. It is being re-derived.** Second time in
two turns: yesterday the contract, today the index.

`gate_log.md` is named in that header and **was not opened.** The
`DECLINED.md` entry is `PRINCIPLED` — reading it burns C-7's reference gate
— and it stands. Referring to a file is not reading it.

## 2. THE COST IS MEASURABLE, AND IT IS IN THE KEYS

The index's own lookup keys against the actual repo names:

    META_INDEX rows                           83
      exact name match to a repo              65
      match only after normalising             9   <- lookup-key drift
      sub-repo directory, not a repo           4
      named repo, not reachable                2
      truncated name, no match                 3

    12 of 83 (14%) will not resolve by lookup.

The dominant single cause is **seven trailing hyphens**:

    Adaptive-Intelligence-Framework    -> Adaptive-Intelligence-Framework-
    Bio-Grid-American-Manufacturing    -> Bio-Grid-American-Manufacturing-
    Combine-Cognitive-Architecture     -> Combine-Cognitive-Architecture-
    Fulgerite-Antenna-Prototype        -> Fulgerite-Antenna-Prototype-
    Geometric-manifold                 -> Geometric-manifold-
    The-Curriculum-of-Everything-Earth -> The-Curriculum-of-Everything-Earth-
    Universal-Redesign-Algorithm       -> Universal-Redesign-Algorithm-

    plus  "Resilience Indigenous Worldwide"  (spaces)
          "Resilient AI-Human Collaboration" (spaces)
          three truncations: -model, -SOMS-, -repurposing-database

**None of these is a rename for a reader.** They are cosmetic tidying — a
trailing hyphen removed because it looks like a typo. The relay's mechanism
holds and the trigger is smaller than stated: **the key drifts when the name
is made to read better, and "better" includes tidier.** One of the seven is
a pilot repo of this audit.

## 3. AN INDEPENDENT CROSS-CHECK OF THE HELD LICENCE SWEEP

META_INDEX's License column is a second, independent record of the same
quantity the sweep measured. Cross-checked, 52 rows with a declared licence:

    AGREE with the measured LICENSE file      45
    DISAGREE                                   7

    Shadow-Hunting          index MIT   measured CC0   <- relicensed today;
                                                         index stale by hours
    Coop-framework          index MIT   measured CC0
    Logic-Ferret            index MIT   measured CC0   index lags a repo that
    Rosetta-Shape-Core      index MIT   measured CC0   already moved to CC0
    assumption_validator    index MIT   measured CC0

    AI-Consciousness-Sensors index CC0  measured MIT   <- index claims CC0,
    PatternBridge            index CC0  measured MIT      the file says MIT

**Five of seven are the index lagging behind repos that already moved.** The
profile README's own line — *"Not yet uniformly so — Rosetta-Shape-Core is
MIT with CC0…"*, flagged `STALE` last turn — is confirmed stale: that repo
measures CC0.

**Two run the other way and matter more.** `PatternBridge` is one of the
sweep's `STOP` flags: it carries a deliberate MIT-code / separate-DATA_LICENSE
split, and the index records it as CC0. An index that over-declares CC0 is
the failure mode a licence sweep run *from the index* would inherit.

    the sweep was run from the LICENSE files, not from the index.
    that choice is now load-bearing.

## 4. THE DENOMINATOR — NO LONGER MERELY UNVERIFIED

Last turn: *"whether 100 is all of them is not determinable from here."* The
index settles half of it.

    grounding-layers                 github.com/JinnZ2/grounding-layers
    Seed-Expander Connective Layer   github.com/JinnZ2/seed-expander

Both are named in META_INDEX with repo-root URLs. **Neither is in the 100
rows `list_repos` returned.** Checked, not assumed:

    git ls-remote https://github.com/JinnZ2/Logic-Ferret     -> refs listed
    git ls-remote https://github.com/JinnZ2/grounding-layers -> credential
    git ls-remote https://github.com/JinnZ2/seed-expander       prompt

Anonymous git cannot separate **private** from **nonexistent** — both give
that prompt. Two readings, both live:

    (a) they exist and are private -> `list_repos` is capped at 100 and its
        `has_more: false` is wrong. Three other private repos WERE listed,
        so the cap is the likelier cause.
    (b) they do not exist -> META_INDEX names two repos that were never
        created, which is the same drift class as §2 one level up.

**Not decided.** What is settled: **the sweep's 100 is not the whole set**,
and any "all JinnZ2 repos" claim from it is bounded by that.

The other four unmatched names resolve cleanly and are not repos at all:
`falsification_ledger`, `cascade_regime_audit` and
`multi_substrate_calibration` are directories inside `Simulators`;
`energy_english` is a directory inside `JinnZ2/JinnZ2`. **The index keys on
sub-repo granularity; `list_repos` keys on repos.** That is a match-unit
mismatch between two registries of the same ecosystem — `DIALECT`'s sibling,
and the ninth-plus instance.

## 5. THE NO-TERM FILE — NOT FOUND, NOT FILLED

    "the no-term file broke because it was renamed for the reader.
     it's findable now because your names went back in as keys."

Searched, case-insensitively, for `no-term` / `no_term` / `noterm` across
`jinnz2/`, `drift-archive-audit/`, `Keystone-Codex/`, `Emotions-as-Sensors/`.

    2 hits, both false positives:
      Simulators/claim-record/record.py:979    a local variable `noterm`
      Simulators/sheet-structure-scan/coupling.py:651  "NO_TERMINALS"

**No such file is reachable from here under that name** — which is
consistent with the claim (it was renamed) and does not verify it. The
example is recorded as relayed and `UNRESOLVED` on this side. Filling in
what it was would be the error the whole relay is about.

    the no-term file, by any name reachable here   UNSET
    whether the rename-and-restore happened        OBSERVED (hers),
                                                   not corroborated here
