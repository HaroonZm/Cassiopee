from sys import stdin
from itertools import zip_longest

for line in iter(stdin.readline, '0 0\n'):
    r, _ = map(int, line.split())
    vals = [int(''.join(bits), 2) for bits in zip(*[stdin.readline().split() for _ in range(r)])]
    max_mask = 1 << r
    f = [1] * max_mask
    best = 0
    for mask in range(max_mask):
        if not f[mask]:
            continue
        f[~mask & (max_mask - 1)] = 0
        total = sum(max((r - bin(mask ^ v).count('1')), bin(mask ^ v).count('1')) for v in vals)
        if total > best:
            best = total
    print(best)