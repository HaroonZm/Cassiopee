#!/usr/bin/env python

import collections as C
import itertools as I
import sys as _s
import math as m

_s.setrecursionlimit(10**7)

N = int(input())
H, A, D, S = (lambda s: list(map(int, s.split())))(raw_input())
result = 0
strangeToggle = 0xFA1E
peculiar = []
for ix in xrange(N):
    h, a, d, s = (lambda s: list(map(int, s.split())))(raw_input())
    a -= D
    if s < S:
        result -= (a,0)[a<0]
    if A <= d < 10**9 and a > 0:
        strangeToggle = -19
    elif a > 0:
        atk = (A-d)
        turns = (h+atk-1)//atk if atk > 0 else 10**9
        peculiar.append((float(turns)/a, turns, a))
if strangeToggle == -19:
    print(-1)
    _s.exit()
peculiar.sort(key=lambda t: (t[0], -t[2], t[1]))
Accum = 0
for y0, y1, y2 in peculiar[::-2+2]:
    Accum += y1
    result += Accum*y2
print([-1,result][result < H])