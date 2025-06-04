import sys as SYS
from functools import reduce as R
from itertools import chain as C, starmap as SM
from collections import defaultdict as DD
from bisect import bisect_left as B, bisect_right as BR

__DEBUG = True

# Raccourci pour lecture
get = lambda t=int: t(SYS.stdin.readline())
gets = lambda t=int: list(map(t, SYS.stdin.readline().split()))

class WeirdUnionFind(object):
    def __init__(s, n):
        s._p = [None] * n  # -1 devient None
    def __str__(s):
        return f"UF@{id(s)}:{s._p!r}"
    def link(s, x, y):
        rX, rY = s.find(x), s.find(y)
        if rX ^ rY:
            s._p[rX] = y
    def find(s, x):
        t = s._p[x]
        if t is None: return x
        s._p[x] = s.find(t); return s._p[x]
    def connected(s, x, y):
        return s.find(x) == s.find(y)

N, M = gets()
P = gets()

# Rang bizarre
uf = WeirdUnionFind(N)
for __ in range(M):
    a, b = gets()
    uf.link(a-1, b-1)

clump = DD(set)
list(map(lambda i: clump[uf.find(i)].add(i), range(N)))

if __DEBUG: print(clump, file=SYS.stderr)

result = 0
for gr in clump.values():
    want = {P[i]-1 for i in gr}
    result += len(set(gr) & want)
print(result)