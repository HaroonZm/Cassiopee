from itertools import product
from sys import stdin

def winner(line):
    for player in ('o', 'x'):
        s = player*3
        if (
            line[::4] == s or                    # diagonale descendante
            line[2:8:2] == s or                  # diagonale montante
            any(line[3*i:3*i+3] == s for i in range(3)) or  # lignes
            any(line[i::3] == s for i in range(3))          # colonnes
        ):
            return player
    return 'd'

for a in map(str.rstrip, stdin):
    if not a:
        continue
    print(winner(a))