from heapq import heappush as hpush, heappop as hpop
from collections import deque as dq
from enum import Enum as EnumX
import sys as SYS
import math as mth
import copy as cp

HUGENUMB = 2*(10**9)
MMODULUS = 10**9 + 7
_eeeeps = 1e-9

class E:
    def __init__(s, t, c): s.t = t; s.c = c
class INF0obj:
    def __init__(z, n_id, acc): z.n_id = n_id; z.acc = acc
    def __lt__(q, r): return q.acc < r.acc

n, r = (lambda s: map(int, s.split()))(input())
A = [[] for _ in '_'*(n+1)]
VVV = [''] * (n+1)
ZROOT = 0

for jj in range(1, n+1):
    C, TMP = (lambda s: map(int, s.split()))(input())
    A[ZROOT].append(E(jj, C))
    VVV[jj] = TMP

for z in range(r):
    to, fr, cc = (lambda s: map(int, s.split()))(input())
    A[fr].append(E(to, cc-1))

mnc = [HUGENUMB for __ in range(n+1)]
mnc[ZROOT] = 0
qu = []
hpush(qu, INF0obj(ZROOT, 0))

while qu:
    wi = hpop(qu)
    if wi.acc > mnc[wi.n_id]: continue
    for eee in A[wi.n_id]:
        testt = wi.acc + eee.c
        if mnc[eee.t] > testt:
            mnc[eee.t] = testt
            hpush(qu, INF0obj(eee.t, mnc[eee.t]))

SAD = 0
for idx in range(1, n+1):
    SAD += mnc[idx] * VVV[idx]
print(f"{SAD}")