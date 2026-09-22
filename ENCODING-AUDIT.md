# Encoding audit — the rule from #26, applied to every instrument here

**The rule is worth more than the catch that produced it**, and the catch was
luck. So the rule gets tested on the instrument set rather than left as a
sentence.

    CONTROL EVERY ENCODING THE CONCEPT TAKES, NOT EVERY CONCEPT.

    The same failure waits wherever a concept has two syntaxes and the
    detector knows one.
                                              -- operator, 2026-09-22

## #26 AMENDED — the catch was luck, and it is recorded as luck

> My part was luck. I named two fixtures I expected to exist; one happened to
> sit in the encoding the sweep couldn't see. No design, no prediction.

**So #26 is not evidence that naming fixtures is a reliable method.** It is
one draw. The record previously said the catch surfaced "only because the
operator named a control fixture that happened to live in the missing
encoding" — accurate, but it sat next to a control-discipline argument and
could be read as method. **It was not method.**

**What survives is the rule**, which does not depend on how it was found.

## THE AUDIT

For each instrument: the concept it detects, the syntaxes that concept takes,
and which of them the instrument knows.

### `instrument/enum_sweep.py` — concept: A CLOSED SET

| encoding | known? | present in the 5 roots? |
|---|---|---|
| JSON Schema `"enum": [...]` | **yes** | yes — control A |
| Python `NAME = (...)` literal collection | **yes** | yes |
| Python `Literal[...]` | **yes** | — |
| Python `class X(Enum)` | **yes**, added by #26 | yes — control B, 69 in pilot repos |
| YAML `enum:` | **no** | **0** — 9 yaml files exist, channel works. Guarded zero |
| JSON Schema `oneOf` + `const` | **no** | **0** across 813 json files. Guarded zero |
| JS/TS union type literals | **no** | **0** — no `.ts` files at all. Zero is trivially explained, not a finding |
| JS `Object.freeze({...})` as enum | **no** | **0** across 22 `.js` files with 239 `const` declarations. Guarded zero |
| Markdown "one of:" table rows | **no** | **1** |

**The blind encodings happen to be empty in this corpus. That is a fact
about this corpus, not about the instrument.** The sweep remains blind to
five encodings of its own target concept, and a sixth repo could carry any of
them.

**Zeros above are guarded**, per standing rule: the file types exist and the
grep channel is demonstrated working on a known-present token in each. The
`.ts` row is the exception and is marked as trivially explained rather than
counted.

### The rest of the instrument set — asserted from the code, not measured

| instrument | concept | syntaxes it knows | syntaxes it does not |
|---|---|---|---|
| `reachability_sweep.py` | *a term a reader must look up* | backticked spans; ALL-CAPS runs | `**bold**` terms; headings; plain prose; hyphenated multiword terms. **DEFECT 1 in that file is one symptom of this**, already logged |
| `phi_null.py` | *a phi-adjacent ratio in data* | adjacent ratios, orientation-free | all-pairs ratios; running-sum ratios; windowed ratios; directed ratios (already noted in the file) |
| `guarded_count.grep_counter` | *a pattern occurrence* | POSIX ERE via `grep -E` | PCRE; fixed-string; word-boundary dialects. **The dialect is named in the code** because instances 1 and 4 were dialect errors |
| `channel_function.py` | *channel function F1–F4* | keyword regexes | everything else. Two construction flaws already documented; fails all three acceptance criteria |

**Marked as asserted, not measured.** Counting the missed instances for each
would take the same work the enum row took, and it has not been done.

## WHAT THE RULE COSTS, STATED

A control per concept is one fixture. **A control per encoding is one fixture
per syntax**, and the syntax list is open — nobody can enumerate every way a
concept can be written.

    so the rule is NOT "achieve complete encoding coverage"
    it IS   "the encodings you control are the encodings you can
             report a zero for"

**A zero is reportable exactly as far as the controls reach.** The enum sweep
can now report a zero for four encodings and cannot report one for five,
which is a narrower and truer claim than the bounded-at-51 it made yesterday.
