#!/usr/bin/env python

import csv

from numpy import cov

chars: dict[str, set[str]] = {}
with open('chars.tsv') as fin:
    for line in fin:
        ch, pos, *_rest = line.rstrip('\n').split('\t')
        chars.setdefault(pos, set()).add(ch)

coverage: dict[str, set[str]] = {}
with open('scripts/ambi.csv') as fin:
    for row in csv.reader(fin):
        pos, _idx, chs = row
        coverage.setdefault(pos, set()).update(chs)

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
