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

If the control returns zero, the detector is proven blind and the query's
zero is NOT REPORTED AS ZERO -- it is returned as DETECTOR_BLIND, which is a
different value and does not compare equal to 0.

CC0. Stdlib only.
"""

import subprocess


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
        if self.status == 'DETECTOR_BLIND':
            return ('<DETECTOR_BLIND  query=%r  control=%r returned 0 -- the '
                    'query result is NOT a finding>' % (self.query, self.control))
        if self.status == 'ZERO_GUARDED':
            return ('<0  query=%r  GUARDED: control %r returned %d>'
                    % (self.query, self.control, self.control_hits))
        return '<%d  query=%r>' % (self.value, self.query)

    def __int__(self):
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
        if self.status == 'DETECTOR_BLIND':
            return False
        return isinstance(other, int) and other == self.value

    def __bool__(self):
        if self.status == 'DETECTOR_BLIND':
            raise ValueError(
                'refusing a truth value for a DETECTOR_BLIND reading (query '
                '%r, control %r returned 0). An untrusted detector has no '
                'truthiness.' % (self.query, self.control))
        return bool(self.value)

    def is_finding(self):
        """True only for a zero that a working detector produced."""
        return self.status == 'ZERO_GUARDED'


def guarded_count(query, positive_control, counter):
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
    control_hits = counter(positive_control)
    if control_hits == 0:
        return Reading(None, 'DETECTOR_BLIND', query, positive_control, 0)
    hits = counter(query)
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

    print('selftest OK' if ok else 'selftest FAILED')
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(_selftest())
