# rime-dict-source

Dictionary of Middle Chinese, source for [building IME dictionaries in different romanizations](https://github.com/nk2028/rime-dict-builder).

## About scripts

In `scripts/`:

- `uniqsort.py`: Sorts rows in each TSV by word length, then by Unicode code points of each field.

- `check.py`: Checks if characters of each 音韻地位 in `ambi.csv` fully covers characters with that 地位 in `chars.tsv`.

  - `ambi.csv`: Lists characters with the same 音韻地位 by 小韻 (not exhaustive yet), which could possibly have different 音韻地位 in other data sources.

    Fields: 音韻地位, 小韻號 (can be `+` if it's not from 廣韻), 廣韻字頭 (and variants), 外字 (whose 音韻地位 follows the corresponding 小韻)

  - `sort_ambi.py`: Sorts rows in `ambi.csv`. Rows are grouped by 音韻地位 first. Then rows in each group are sorted by 小韻號, and groups are sorted by the smallest 小韻號 in each group.
