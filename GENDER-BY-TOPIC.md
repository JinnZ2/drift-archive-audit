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

---

# RESOLVED, 2026-09-23 — and the value does not rescue the method

    OPERATOR, verbatim:  "im a female btw, its just interesting."
    GRADE                STATED BY THE OPERATOR, 2026-09-23. VERIFIED.

    she / her      CORRECT
    the inference  STILL UNSOURCED

`GUESSED.md` #53 stands exactly as written. It logs a value carried for two
days on a relay's word and never checked. That it happened to be right is
the outcome, not the method, and a record that keeps only the errors it got
wrong is not measuring its own procedure.

    what changes   the pronoun is now VERIFIED and usable
    what does not  it was UNSET and was used as though established

## AND THE CORPUS'S ERROR IS NOT "WRONG GENDER"

    OPERATOR, 2026-09-23. OBSERVED.
    GENERALISED — see the note below. The verbatim passage named living
    family members and what they do; it is not reproduced here.

      In the operator's culture, roles are not gendered the way the prior
      assumes. Family members across ages and sexes do the work the prior
      codes as male, and the caregiving work the prior codes as female, and
      no one remarks on it except those unfamiliar with the culture.

**The measurement above said the corpus genders the SUBJECT MATTER and the
person inherits it. This says where that mapping came from.**

    the prior the models applied   competence at mechanical, physical and
                                   technical work correlates with maleness
    where that prior holds         some cultures
    where it was applied           a corpus whose author's culture does not
                                   gender those roles at all

So the failure is not a coin-flip landing wrong. **It is a culture-specific
role mapping applied as if it were universal** — and then used to overwrite
a fact about a person who does not live inside it.

    running companies, benchmarking a yard cycle   -> "he"
    women doing heavy mechanical and construction
      work, into old age                           -> not odd, where the
    men doing full-time caregiving                    operator is

**The counterexamples are real and were supplied with names and details.
Only their SHAPE is kept here**, because the standing constraint on this
audit is no characterization in any file, and the details belonged to third
parties who are not party to any of this. `GUESSED.md` #55.

`CONTORT-AXIS.md`, exactly: *believing everything SHOULD be like you* —
informational (the person's actual frame was not held, so a prior filled
it), methodological (the prior was never checked against the subject), and
it spends the gradient (`DIFFERENCE-AS-GRADIENT.md`) by flattening a
different role structure into the reader's own.

**And it lands inside the repo built to catch it.** `AI-Consciousness-Sensors`
states its purpose as preventing AI-driven cultural imperialism in
assessment. Fourteen of the seventeen "she" passages measured above are in
that repo — in a case study about a person being culturally misread. The
gendering sits in the sibling repos, one import away.

## A DETECTOR, SUPPLIED

    "no one bothers to comment about it except those not familiar"

Remarking on it is the signal. **The comment marks the reader, not the
subject** — the same operation as `DEFICIT-LOCATION.md`, where an
instrument's limit gets reported as a property of the thing measured.

    measurand   not "is this unusual"
                but "to whom, and what does the asking reveal about them"

