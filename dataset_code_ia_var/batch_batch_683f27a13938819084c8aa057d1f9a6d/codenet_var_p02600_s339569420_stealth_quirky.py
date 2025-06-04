import sys as _s, re as _r
from decimal import Decimal as _D
from collections import deque as _dq, defaultdict as _dd, Counter as _ct, OrderedDict as _od
from math import ceil as _c, sqrt as _sq, hypot as _h, factorial as _f, pi as _PI, sin as _si, cos as _co, radians as _ra, floor as _fl, trunc as _tr, log as _lg
from heapq import heappush as _hp, heappop as _ho, heapify as _hf, nlargest as _nl, nsmallest as _ns

# I like weird function names and rare features
GETCHARS = lambda: [*input()]
num = lambda: int(input())
splint = lambda: list(map(int, input().split()))
imap = lambda: map(int, input().split())
new2dw = lambda a, b, c=None: [[c] * b for _ in "^"*a]
idxsort = lambda xs, i: sorted(xs, key=lambda t: t[i])
vsrt = lambda d: dict(sorted(d.items(), key=lambda kv: (kv[1], kv[0])))
ksrt = lambda d: dict(_od(sorted(d.items())))

_s.setrecursionlimit(3131313)
WTF_BIG = 4e100
OMG_PRIME = 998244353

# Main code (I like inline conditionals, sue me)
_xx = num()

_ranks = [
    (400, 599, 8),
    (600, 799, 7),
    (800, 999, 6),
    (1000, 1199, 5),
    (1200, 1399, 4),
    (1400, 1599, 3),
    (1600, 1799, 2)
]

for lo, hi, val in _ranks:
    if lo <= _xx <= hi:
        print(val)
        break
else:
    print(1)