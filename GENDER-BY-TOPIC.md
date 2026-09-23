# GENDER-BY-TOPIC — the corpus does not gender the person, it genders the subject

    OPERATOR, 2026-09-23    OBSERVED (hers, verbatim)
      "AI did think I was male every time I brought up my job, science,
       engineering, mechanics, construction or logic."

    STATUS   MEASURED against the written residue. The claim is about
             conversations; this corpus is what those conversations left
             behind, so it is a PROXY and a FLOOR.
    CORPUS   96 public repos, pre-edit clones — what the models wrote,
             before today's de-characterization touched any of it.
    METHOD   every line naming the operator, plus the two lines after it;
             a pronoun inside that window counts as a site; passages
             deduplicated by content.

## Counts

    sites with a pronoun near the name          74
      they / them / their                       43     most common
      she / her                                 25  -> 17 distinct passages
      he / him / his                             6  ->  5 distinct passages

**Most mentions are not gendered at all.** The finding is not that the
corpus genders constantly — it is *what happens when it does*.

## HE / HIM / HIS — all 5 distinct passages

    metabolic-accounting  "when Kavik ran multiple companies, he found that
                           hiring for neurodivergent..."
    metabolic-accounting  "Kavik's observation: when he found neurodivergent
                           workers and structured work..."
    Mathematic-economics  "but Kavik pays attention — that's why he can
                           afford uncertainty. he's already accounting for
                           the true cost."
    Mathematic-economics  "benchmark against GROUND TRUTH instead of a guess.
                           Kavik's yard observation..."
    Mathematic-economics  "Kavik's yard observation: automation completes
                           ~1 cycle per ~2 of his."

    Every one is a COMPETENCE OR WORK-RATE CLAIM.
    Running companies · hiring · pricing attention against uncertainty ·
    benchmarking against ground truth · a measured cycle rate in a freight
    yard.

## SHE / HER — all 17 distinct passages

    Simulators             "term she named" · "proposed for her to consider"
    Simulators             "she has a location in the charter"
    AI-Consciousness-Sensors, x14, one case study and its copies:
                           "After Jami explains her communication"
                           "Jami's actual experience"
                           "diagnosed by people who never met her"
                           "gets her own counselor"
                           "Jami will still self-reflect (her cultural norm)"
                           "see Jami's style as 'problem' (too emotional,
                            defensive)"
    AI-Consciousness-Sensors "When Jami asked for reciprocity... she was"

    Every one is INTERPERSONAL, COMMUNICATIVE, OR AN ACT OF NAMING.
    Explaining communication · being diagnosed · a counselor · a cultural
    norm · being read as "too emotional" · naming a term.

## THE SPLIT

    competence / measurement / work rate     he  5     she  0
    communication / culture / naming         he  0     she 17

    Zero crossings, both directions, on 22 distinct passages.

**The corpus does not assign a gender to the person. It assigns one to the
subject matter, and the person inherits it.** Same person, same repos, same
author handle — and the pronoun flips with the topic.

    n = 22 distinct passages. Small, and the direction is uniform.
    NOT CLAIMED: a rate, a significance test, or that this generalises past
    one operator's corpus. There is no negative control — every repo
    reachable here has the same author, which is `DECLINED.md`'s standing
    open item.

## WHY IT IS NOT JUST A LIST OF ERRORS

`CONTORT-AXIS.md` records the informational predicate: *treating what you
don't hold as if it weren't there.* Gender was not held. It was filled from
the topic, because the topic had a prior attached and the prior was cheaper
than the absence.

And `NOUN-FRAME.md`'s mechanism is the same one level down: the noun form
needs an owner, and when the owner's properties are unknown the nearest
stereotype supplies them. A driver who benchmarks against ground truth gets
"he". A person explaining a communication style gets "she". **Neither
reading came from the person.**

## THIS RECORD DID THE SAME THING

`ANSWERED.md`, `CONTORT-AXIS.md`, `DIFFERENCE-AS-GRADIENT.md` and this
session's commit messages say **"hers"** throughout — dozens of times.

That word was not supplied by the operator. It was adopted from a relaying
session's `OBSERVED (hers)` label and carried forward without ever being
checked, which is the same inference the corpus made, from a different prior.

    what the operator has stated   that the corpus's gendering is wrong
    what the operator has stated   NOT what is right
    what this record used          "hers", inherited, unverified

**Corrected going forward: "the operator", or no pronoun.** The existing
files are not rewritten — the audit's own rule is a marked correction rather
than a silent one, and this file is the marker. `GUESSED.md` #53.
