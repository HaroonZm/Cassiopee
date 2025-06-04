from bisect import bisect
from itertools import product
from sys import stdin

def solve():
    while True:
        try:
            n_lmt = next(stdin)
        except StopIteration:
            break
        n, lmt = map(int, n_lmt.split())
        if n == 0:
            break
        p = [int(next(stdin)) for _ in range(n)] + [0]
        pset = sorted(set(map(sum, product(p, repeat=2))))
        s = bisect(pset, lmt)
        print(max(i + pset[bisect(pset, lmt - i) - 1] for i in pset[:s]))

solve()