#!/usr/bin/env python

from collections import Counter
from functools import cmp_to_key
import sys


def split_小韻號(小韻號: str) -> tuple[int, str]:
    if 小韻號[-1].isalpha():
        return int(小韻號[:-1]), 小韻號[-1]
    else:
        return int(小韻號), ''


def cmp_小韻號(x: str, y: str) -> int:
    if x == '+':
        if y == '+':
            return 0
        return 1
    elif y == '+':
        return -1
    split_x = split_小韻號(x)
    split_y = split_小韻號(y)
    if split_x == split_y:
        return 0
    elif split_x < split_y:
        return -1
    else:
        return 1


def cmp_row(x: list[str], y: list[str]) -> int:
    return cmp_小韻號(x[1], y[1])


def cmp_group(x: list[list[str]], y: list[list[str]]) -> int:
    return cmp_row(x[0], y[0])


def main():
    filepath = 'scripts/ambi.csv'

    with open(filepath) as fin:
        header = next(fin).rstrip()

        小韻號_counts: Counter[str] = Counter()

        groups: dict[str, list[list[str]]] = {}
        for line in fin:
            row = line.rstrip().split(',')
            groups.setdefault(row[0], []).append(row)
            if row[1] != '+':
                小韻號_counts[row[1]] += 1

    for 小韻號, count in 小韻號_counts.items():
        if count > 1:
            print(f'W: duplicate 小韻號 {小韻號}', file=sys.stderr)

    for group in groups.values():
        group.sort(key=cmp_to_key(cmp_row))

    groups_sorted = sorted(groups.values(), key=cmp_to_key(cmp_group))

    with open(filepath, 'w', newline='') as fout:
        print(header, file=fout)
        for group in groups_sorted:
            for row in group:
                print(','.join(row), file=fout)


if __name__ == '__main__':
    main()
