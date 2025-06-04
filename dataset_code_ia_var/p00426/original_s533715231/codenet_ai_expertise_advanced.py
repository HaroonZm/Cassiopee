from sys import stdin
from functools import cache

def solve():
    while True:
        n_m = stdin.readline()
        if not n_m:
            break
        n, m = map(int, n_m.split())
        if n == 0:
            break

        cups = [None] * n
        for tray in 'ABC':
            line = stdin.readline().split()
            for idx in map(int, line[1:]):
                cups[idx - 1] = tray

        @cache
        def rec(i):
            if i == 0:
                return 0
            match cups[n - i]:
                case 'A':
                    return rec(i - 1)
                case 'B':
                    return 2 * 3 ** (i - 1) - 1 - rec(i - 1)
                case _:  # 'C'
                    return rec(i - 1) + 2 * 3 ** (i - 1)

        total_moves = rec(n)
        min_moves = min(total_moves, 3 ** n - 1 - total_moves)
        print(min_moves if min_moves <= m else -1)

solve()