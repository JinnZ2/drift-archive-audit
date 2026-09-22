# Instrument — commit-size distribution as a transport fingerprint

**Status: measured in this pilot, prediction confirmed, generalization
untested.**

Reads the transport regime **without trusting the git author field.** That
independence is the point: `CORRECTION-001` established the author field
names the pusher, not the content author. This recovers the same boundary
from a channel that authorship metadata does not touch — so it is
independent evidence, not a downstream consequence of the correction.

## The measurement

Files added per commit, three pilot repos, split at each repo's transport
boundary (Bio-Grid 2026-06-02; Keystone and Emotions 2026-03-22).

    size   paste era   agent era
       1          48          47
       2           0          14
       3           0           7
       4           0           5
       5           0           2
       6           0           2
       7           0           1
       8           0           2
      11           0           1
      16           1           0
      20           0           1
      32           0           1
      67           1           0
     172           1           0
    total         51          83

## The prediction, and it held

Stated follow-on: *the bimodal paste-era shape should have a gap at every
intermediate size, not just 2–9. Check 10–30.*

**Confirmed, and the result is stronger than the prediction.**

    paste-era sizes observed   {1, 16, 67, 172}      4 distinct sizes
    agent-era sizes observed   {1,2,3,4,5,6,7,8,11,20,32}   11 distinct

The paste era has **no intermediate sizes anywhere** — nothing between 2 and
15, nothing between 17 and 66, nothing between 68 and 171. The three sizes
above 1 are the three bulk imports, one per repo.

So the paste-era distribution is not merely bimodal. It is **degenerate: a
point mass at 1, plus isolated bulk events.** 48 of 51 adding commits are
exactly one file.

The agent era is continuous from 1 through 8 and scattered above.

## Structure of the claim, stated honestly

    paste era  =  48 commits of exactly 1 file
                + 3 bulk imports (16, 67, 172 — one per repo, each the
                  repo's initial publication)

The "no intermediate sizes" result rests on 48 non-import commits **all**
being exactly 1. There is no intermediate-size commit to explain away,
which is what makes it clean — but it is 48 observations from one sender on
one channel, not a population.

The single paste-era entry in the 10–30 bucket is Keystone's 16-file root
import, not a counterexample.

## Mechanism

A hand-paste channel has no operation that produces "three files together."
One code block becomes one file. An accumulated batch is dumped at once.
There is nothing in between, because nothing in the channel can express it.

An agent commits whatever set a change touched, which lands naturally
across 2–9 — 33 times here.

## Reusable, untested

If the fingerprint holds, it generalizes past this corpus: **any repository
where a human transported model output under one-at-a-time constraints
should show the same degenerate size distribution.** That makes it an
instrument, not a fact about these three repos.

What would falsify or bound it:

- a paste-era repo showing a continuous size distribution → the fingerprint
  is about this operator's workflow, not the channel
- an agent-era repo showing a degenerate one → the signal is confounded with
  something else (project maturity, commit discipline, CI)
- a repo with known mixed transport showing no boundary → the instrument
  lacks resolution
- it may simply track **tooling** (web UI vs git client) rather than
  transport-as-channel; this pilot cannot separate those, because the same
  boundary changes both

**It does not separate transport from model change.** It confirms the
transport half of that confound is real and dateable. Nothing more.
