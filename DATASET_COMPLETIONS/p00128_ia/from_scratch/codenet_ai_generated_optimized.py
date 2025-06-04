def soroban(digits):
    upper_bead = ['*', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    lower_beads = [
        ['*', '*', '*', '*', '*', '*', ' ', '*', '*', '*'],
        [' ', ' ', ' ', ' ', ' ', ' ', '*', '*', '*', '*'],
        [' ', ' ', ' ', ' ', '*', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*'],
        [' ', ' ', '*', '*', '*', '*', ' ', ' ', ' ', '*'],
        [' ', ' ', '*', '*', '*', '*', '*', ' ', ' ', '*'],
    ]
    upper_row = []
    lower_rows = ['' for _ in range(5)]
    digits = digits.zfill(5)
    for d in digits:
        n = int(d)
        upper_row.append(upper_bead[n])
        for i in range(5):
            lower_rows[i] += lower_beads[i][n]
    print(''.join(upper_row))
    print('=====')
    for row in lower_rows:
        print(row)

import sys
lines = list(map(str.strip, sys.stdin.readlines()))
for i, line in enumerate(lines):
    if line == '':
        continue
    soroban(line)
    if i != len(lines)-1:
        print()