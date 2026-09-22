#!/usr/bin/env python3
"""A zero that cannot be reported without a positive control in the same call.

WHY THIS EXISTS, and it is not because the rule was forgotten.

The rule was written down, in capitals, in two files:

    POSITIVE CONTROL BEFORE TRUSTING ANY PATTERN-MATCHED ZERO

It was then violated in the same repository that states it (`GUESSED.md`
#18: four controls run, all on corpus-side detectors; zero demanded of any
instrument on the institutional side). And the class the rule guards against
has seven logged instances, two of which occurred INSIDE instruments written
after the class was named and in order to avoid it.

**Naming the hazard did not lower the rate.** So this file stops documenting
it and makes it structural: there is no code path here that returns an
unguarded zero. The caller does not remember to run a control. The caller
cannot obtain a result without one.

    search(...)              -> TypeError. There is no such function.
    guarded_count(q, ctrl)   -> the only way in. ctrl is positional and
                                required.

THREE ROUTES TO A FALSE ZERO, and the third was added 2026-09-22:

    DIALECT MISMATCH     the engine parses the pattern differently than
                         written                    -> a WRONG reading
    MATCH-UNIT MISMATCH  the matcher's unit is not the author's unit
                                                    -> a WRONG reading
    TIMEOUT              the detector does not return at all
                                                    -> NO reading

**The third is structurally different and it was a gap in this guard's own
domain rather than a bug in it.** Everything above operates on a reading. A
non-terminating detector produces none, so there is nothing to intercept, and
a zero reported downstream is indistinguishable from a measured absence.

`deadline_s` closes it: a counter that does not return inside its budget
yields DETECTOR_TIMEOUT, which like DETECTOR_BLIND is not equal to 0, cannot
be cast to a number, and has no truth value. Observed once, in this
programme's own enum sweep.

If the control returns zero, the detector is proven blind and the query's
zero is NOT REPORTED AS ZERO -- it is returned as DETECTOR_BLIND, which is a
different value and does not compare equal to 0.

CC0. Stdlib only.
"""

import signal
import subprocess


class DetectorTimeout(Exception):
    """The counter did not return inside its budget."""


def _run_with_deadline(fn, arg, deadline_s):
    """Call fn(arg) under a wall-clock budget. None means no budget.

    SIGALRM, deliberately. The first design here assumed a signal could not
    interrupt a catastrophic backtrack inside CPython's C-level `re`, and was
    about to document that as a limitation. **It was tested instead of
    asserted, and the assumption was false** -- SIGALRM fires and the match
    aborts. A fabricated technical caveat was one line from the record.

    Real limits, stated: POSIX only, main thread only, and a C extension that
    never reaches a signal check can still block past the deadline.
    """
    if deadline_s is None:
        return fn(arg)

    def _fire(_sig, _frm):
        raise DetectorTimeout()

    previous = signal.signal(signal.SIGALRM, _fire)
    signal.setitimer(signal.ITIMER_REAL, deadline_s)
    try:
        return fn(arg)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


class Reading:
    """A count, or the fact that the detector could not be trusted to produce one.

    Deliberately not an int. `Reading(0, ...) == 0` is False, so a blind
    detector's zero cannot be summed into a table, used in an f-string as a
    number, or compared against a threshold without the caller noticing.
    """

    __slots__ = ('value', 'status', 'query', 'control', 'control_hits')

    def __init__(self, value, status, query, control, control_hits):
        self.value = value
        self.status = status
        self.query = query
        self.control = control
        self.control_hits = control_hits

    def __repr__(self):
        if self.status == 'DETECTOR_TIMEOUT':
            return ('<DETECTOR_TIMEOUT  query=%r  the detector did not '
                    'return. No reading exists to guard.>' % (self.query,))
        if self.status == 'DETECTOR_BLIND':
            return ('<DETECTOR_BLIND  query=%r  control=%r returned 0 -- the '
                    'query result is NOT a finding>' % (self.query, self.control))
        if self.status == 'ZERO_GUARDED':
            return ('<0  query=%r  GUARDED: control %r returned %d>'
                    % (self.query, self.control, self.control_hits))
        return '<%d  query=%r>' % (self.value, self.query)

    def __int__(self):
        if self.status == 'DETECTOR_TIMEOUT':
            raise ValueError(
                'refusing to convert a DETECTOR_TIMEOUT reading to a number. '
                'The query %r did not return inside its budget, so nothing '
                'was measured. A timeout is the THIRD route to a false '
                'zero and the only one that produces no reading at all.'
                % (self.query,))
        if self.status == 'DETECTOR_BLIND':
            raise ValueError(
                'refusing to convert a DETECTOR_BLIND reading to a number. '
                'The control %r returned 0, so the query %r measured nothing. '
                'Fix the detector or report the blindness -- not the zero.'
                % (self.control, self.query))
        return self.value

    def __eq__(self, other):
        # A blind reading equals nothing, including itself-as-zero. This is
        # the whole point: `if result == 0:` must not silently take the
        # branch that treats blindness as absence.
        if self.status in ('DETECTOR_BLIND', 'DETECTOR_TIMEOUT'):
            return False
        return isinstance(other, int) and other == self.value

    def __bool__(self):
        if self.status == 'DETECTOR_TIMEOUT':
            raise ValueError(
                'refusing a truth value for a DETECTOR_TIMEOUT reading '
                '(query %r). Non-termination is not falsity.' % (self.query,))
        if self.status == 'DETECTOR_BLIND':
            raise ValueError(
                'refusing a truth value for a DETECTOR_BLIND reading (query '
                '%r, control %r returned 0). An untrusted detector has no '
                'truthiness.' % (self.query, self.control))
        return bool(self.value)

    def is_finding(self):
        """True only for a zero that a working detector produced."""
        return self.status == 'ZERO_GUARDED'


def guarded_count(query, positive_control, counter, deadline_s=None):
    """Run `query`, but only after `positive_control` proves `counter` can see.

    query             the pattern whose count is wanted
    positive_control  a pattern the caller asserts IS present. Required and
                      positional -- there is no default and no keyword form,
                      so it cannot be omitted by habit.
    counter           callable(pattern) -> int

    Returns a Reading. A zero from a blind detector never comes back as 0.
    """
    if positive_control is None or positive_control == query:
        raise ValueError(
            'a positive control must be a pattern distinct from the query '
            'and asserted present. Got %r.' % (positive_control,))
    try:
        control_hits = _run_with_deadline(counter, positive_control, deadline_s)
    except DetectorTimeout:
        return Reading(None, 'DETECTOR_TIMEOUT', positive_control,
                       positive_control, None)
    if control_hits == 0:
        return Reading(None, 'DETECTOR_BLIND', query, positive_control, 0)
    try:
        hits = _run_with_deadline(counter, query, deadline_s)
    except DetectorTimeout:
        return Reading(None, 'DETECTOR_TIMEOUT', query, positive_control,
                       control_hits)
    status = 'ZERO_GUARDED' if hits == 0 else 'COUNT'
    return Reading(hits, status, query, positive_control, control_hits)


def grep_counter(paths=('.',), flags=('-r', '-o', '-E')):
    """A counter over files. The dialect is NAMED, because instances one and
    four of MATCH-UNIT MISMATCH were dialect errors -- `\\|` read as a literal
    pipe in POSIX ERE, and `(?:...)` unsupported in `git grep -E`."""
    def count(pattern):
        try:
            out = subprocess.run(['grep', *flags, '--', pattern, *paths],
                                 capture_output=True, text=True)
        except OSError:
            return 0
        return len([l for l in out.stdout.splitlines() if l])
    count.dialect = 'POSIX ERE via grep -E'
    return count


def _selftest():
    """Every branch, including the ones that must refuse."""
    corpus = {'alpha': 3, 'beta': 0, 'never': 0}
    counter = lambda p: corpus.get(p, 0)
    ok = True

    r = guarded_count('beta', 'alpha', counter)
    if not (r.is_finding() and r == 0 and r.status == 'ZERO_GUARDED'):
        print('FAIL: guarded zero did not come back as a finding'); ok = False

    b = guarded_count('beta', 'never', counter)
    if b.is_finding() or b == 0 or b.status != 'DETECTOR_BLIND':
        print('FAIL: blind detector produced a usable zero'); ok = False
    for op, name in ((int, 'int()'), (bool, 'bool()')):
        try:
            op(b)
            print('FAIL: %s on a blind reading did not refuse' % name); ok = False
        except ValueError:
            pass

    try:
        guarded_count('beta', 'beta', counter)
        print('FAIL: query accepted as its own control'); ok = False
    except ValueError:
        pass

    c = guarded_count('alpha', 'alpha3', counter)
    if c.status != 'DETECTOR_BLIND':
        # 'alpha3' is absent, so this is a blind run even though the query
        # itself would have hit. A nonzero query result does NOT rescue a
        # failed control -- the detector's trustworthiness is not a function
        # of whether this particular query happened to fire.
        print('FAIL: failed control was rescued by a nonzero query'); ok = False

    # The third route: a counter that does not return.
    def slow(_p):
        pat = __import__('re').compile(r'(?:\s*"[^"]+"\s*,?\s*)+$')
        return 1 if pat.match('"a", ' * 26 + 'X') else 0

    t = guarded_count('beta', 'alpha', slow, deadline_s=0.5)
    if t.status != 'DETECTOR_TIMEOUT' or t.is_finding() or t == 0:
        print('FAIL: a non-returning counter produced a usable value'); ok = False
    for op, name in ((int, 'int()'), (bool, 'bool()')):
        try:
            op(t)
            print('FAIL: %s on a timeout reading did not refuse' % name)
            ok = False
        except ValueError:
            pass

    print('selftest OK' if ok else 'selftest FAILED')
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(_selftest())
