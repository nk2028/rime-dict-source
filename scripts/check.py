#!/usr/bin/env python

import csv

chars: dict[str, set[str]] = {}
with open('chars.tsv') as fin:
    for line in fin:
        ch, pos, *_rest = line.rstrip('\n').split('\t')
        chars.setdefault(pos, set()).add(ch)

coverage: dict[str, set[str]] = {}
seen = set()
with open('scripts/ambi.csv') as fin:
    next(fin)  # header
    for row in csv.reader(fin):
        pos, idx, chs, extra_chs = row
        assert (pos, idx) not in seen, f'duplicate key: ({pos}, {idx})'
        assert len(set(chs)) == len(chs), f'duplicate 廣韻 chars: {row}'
        assert len(set(extra_chs)) == len(extra_chs), f'duplicate extra chars: {row}'
        coverage.setdefault(pos, set()).update(chs + extra_chs)

success = True
for pos, cov_chs in coverage.items():
    chs = chars[pos]
    if (missing := chs.difference(cov_chs)):
        success = False
        print(f'ERROR: characters of {pos} in ambi.csv does not cover all characters in chars.tsv')
        print(f'* missing:  {"".join(sorted(missing))}')
    if (superfluous := cov_chs.difference(chs)):
        print(f'Warning: ambi.csv contains characters not in chars.tsv:',
              ''.join(sorted(superfluous)))

if not success:
    exit(1)
