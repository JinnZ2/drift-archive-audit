# oral-record

Status: PROPOSED, co-authored, CC0. One case: a reconstruction from first
principles (Stage A), corrected by an old oral tradition's holder (Stage B),
then rebuilt (Stage C). Not established: any Stage C reading; the bench test
has not run and its outcome slots are VOID.

- `oral_record_case_01.json`: the record (source of truth).
- `oral_record_case_01.md`: rendered from the JSON; never edited by hand.
- `case_check.py`: `--write` renders; bare run checks md == render plus the
  record rules (no identity-bearing keys, origins VOID or allowed, LOST not
  filled, bench outcomes VOID, observer slots null); `--selftest` plants one
  defect per rule.
