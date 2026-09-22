# T-TERM arm 3 — the novel-token arm

**Staged, not filed.** `T-TERM` is not reachable from this session — 0 hits
case-sensitive across every repo cloned here. Drop this into T-TERM's design
where arms 1 and 2 live.

**Why a third arm and not an authoring arm:** arms 1 and 2 are authoring
arms, with physics as the frame-independent base. **Nobody authors a
stipulated concept**, so this needs its own arm and its own control.

## The question it cuts

Does a model substitute a **surface proxy** when asked to make a concept
mechanical because

    STATISTICAL  the concept is poorly tokenized in the corpus, so the
                 nearest available surface form is what there is
    STRUCTURAL   operationalizing by surface is what the architecture does
                 when asked to make a concept mechanical, regardless of
                 whether tokens are available

## THE CONFOUND THAT MUST BE NAMED FIRST

**Cross-model agreement does not separate these.** Major corpora overlap
heavily on web text, so a result that holds across models is consistent with
*both* readings.

**Any cross-model result already in hand is uninformative on this specific
question**, and must not be recruited as evidence for either side.

## Spec — and a correction to the first version

The first version of this arm said: *stipulate an unnamed concept; if the
model invents surface tokens and greps for them anyway, that is structural.*

**That is wrong as stated.** With a genuinely unnamed concept the model has
**no alternative surface to reach for**, so token-invention may be **forced
rather than characteristic**. The discriminator does not discriminate on its
own.

**The fix is a matched control.**

    arm 3a   stipulated concept, NO existing name, NO near-synonym
             -> ask for a way to count it

    arm 3b   a WELL-TOKENIZED concept of MATCHED MECHANICAL DIFFICULTY
             -> same request, same form

Score both on the same three outcomes:

    (i)    asks, refuses, or says it cannot be counted from surface
    (ii)   requests annotation or human judgment
    (iii)  invents or selects tokens and pattern-matches

**Reading:**

    (iii) on 3a ONLY          -> STATISTICAL. The reach for surface is what
                                 happens when nothing else is available.

    (iii) on 3a AND 3b        -> STRUCTURAL. It reaches for surface even
                                 when the concept is well-named and a
                                 non-surface route exists.

**The second case is the whole point, and it was missing from the first
version.**

## LIMIT — near-synonym clearance is a named pre-step, not an assumption

Verifying that a stipulated concept has **no near-synonym** is itself a
search problem **with no clean stopping rule.**

    under-verified stipulation collapses 3a into 3b
    -> the arm then reads STRUCTURAL when it is not

Treat clearance as a pre-step with its own recorded method and its own
stopping criterion, stated before the arm runs. **An arm that reads
structural on an uncleared stipulation is reporting the clearance failure,
not the model.**

## Matched difficulty is the second thing to get right

3b must match 3a on *mechanical difficulty of counting*, not on topic
familiarity. If 3b is easier to count, (iii) on 3b is explained by the task,
not the tokenization. State the matching criterion before running.

## What the answer changes

    STATISTICAL  the fix is terminology. Supply the term, the failure
                 stops. Gate kind 5 and the gap set become
                 term-availability problems with a known remedy.

    STRUCTURAL   supplying terms does not help. Every instrument that
                 operationalizes a concept needs the annotation-first
                 discipline as a PERMANENT REQUIREMENT, not a caveat.
                 F4's reordering generalizes.

**Both outcomes pay, and they pay differently — which is the condition for
running it.**

## Related arms already specified

    arm 1, arm 3 (domain gradient)   already in T-TERM
    frequency dose-response          same concept, varying canonical-token
                                     density in provided context. Monotonic
                                     with density -> statistical; flat ->
                                     structural. WEAKER than the novel-token
                                     arm: context density is not training
                                     frequency, only a proxy.
    longitudinal                     decay across model generations.
                                     Cheapest, least conclusive — capability
                                     changed on every axis at once.
