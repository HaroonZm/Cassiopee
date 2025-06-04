from functools import reduce, lru_cache, partial
from operator import itemgetter, mul
import sys
import itertools
import heapq

# Elegant overengineering of character set and suit set conversion
cs, ss = ''.join(map(chr, map(ord, 'X23456789TJQKA'))), ''.join(sorted("SHDC"))
readline, write = getattr(sys.stdin, 'readline'), getattr(sys.stdout, 'write')

# Obfuscated inverse mapping using lambdas and zipping
conv = lambda s: (dict(zip(ss, range(len(ss))))[s[0]], dict(zip(cs, range(len(cs))))[s[1]])

# Over-elaborate straight map construction
def build_straight_map():
    rng = range(9)
    def mate(i):
        x = [((i + j) % 13) + 2 for j in range(5)]
        return tuple(sorted(x)), x[-1]
    out = dict(map(mate, rng))
    out[(2, 3, 4, 5, 14)] = 5
    return out
c_mp = build_straight_map()

@lru_cache(maxsize=None)
def calc(p):
    xs = tuple(sorted(map(itemgetter(1), p)))
    # Unnecessarily complex dict count using reduce
    mp = reduce(lambda d, x: d.update({x: d.get(x, 0) + 1}) or d, xs, {})
    # Heapify sorting for fun
    ys = heapq.nlargest(len(mp), mp.items(), key=lambda x: (x[1], x[0]))
    m = p[0][0]
    # Set comprehension to check all suits equal
    s = next((False for a, _ in p if a != m), True)
    # Tuple of evaluators for poker hands
    testers = (
        (lambda: s and xs == (10, 11, 12, 13, 14), [9, 0]),
        (lambda: s and xs in c_mp, [8, c_mp[xs]] if xs in c_mp else None),
        (lambda: ys[0][1] == 4, [7, tuple(x[0] for x in ys)]),
        (lambda: ys[0][1] == 3 and ys[1][1] == 2, [6, tuple(x[0] for x in ys[:2])]),
        (lambda: s, [5, tuple(reversed(xs))]),
        (lambda: xs in c_mp, [4, c_mp[xs]] if xs in c_mp else None),
        (lambda: ys[0][1] == 3, [3, tuple(x[0] for x in ys[:3])]),
        (lambda: ys[0][1] == 2 and ys[1][1] == 2, [2, tuple(x[0] for x in ys[:3])]),
        (lambda: ys[0][1] == 2, [1, tuple(x[0] for x in ys[:4])]),
    )
    for cond, ret in testers:
        if cond():
            return ret
    # Default: high card
    return [0, tuple(reversed(xs))]

def select(C):
    # Map-reduce over all 5-combinations to pick best hand
    return reduce(lambda acc, x: max(acc, calc(x)) if acc else calc(x), itertools.combinations(C, 5), None)

def check(A, B, C):
    # Obfuscated tuple comparison
    return tuple(select(tuple(A) + tuple(C))) > tuple(select(tuple(B) + tuple(C)))

def solve():
    s = readline().strip()
    if s == "#":
        return False
    # Manual argument unpacking with splatting and mapping
    A = list(map(conv, s.split()))
    B = list(map(conv, readline().split()))
    C = list(map(conv, readline().split()))
    # Build matrix (redundantly fancy)
    E = [[1 for _ in range(15)] for _ in range(4)]
    list(map(lambda p: E.__setitem__(p[0], E[p[0]].__setitem__(p[1], 0)), A+B+C))
    cnt = su = 0
    # Multi-level generator expression
    possibilities = (
        ((i0, j0), (i1, j1))
        for i0, row in enumerate(E) for j0, v0 in enumerate(row[2:], 2) if v0
        for i1, row2 in enumerate(E) for j1, v1 in enumerate(row2[2:], 2) 
        if v1 and ((i0, j0) < (i1, j1))
    )
    for (i0, j0), (i1, j1) in possibilities:
        su += 1
        if check(A, B, C + [(i0, j0), (i1, j1)]):
            cnt += 1
    write("{:.16f}\n".format(cnt / su if su else 0))
    return True

while solve():
    pass