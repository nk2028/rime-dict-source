from glob import iglob


def do(file_path):
    s = set()

    with open(file_path) as f:
        for line in f:
            line = line.rstrip('\n')

            if not line:
                continue

            word, romans, *extras = line.split('\t')
            s.add((word, romans, tuple(extras)))

    s = sorted(s, key=lambda xyz: (len(xyz[0]), *xyz))

    with open(file_path, 'w') as f:
        for ch, roman, extras in s:
            print(ch, roman, *extras, sep='\t', file=f)


for file_path in iglob('*.tsv'):
    do(file_path)
    print(f'done: {file_path}')
