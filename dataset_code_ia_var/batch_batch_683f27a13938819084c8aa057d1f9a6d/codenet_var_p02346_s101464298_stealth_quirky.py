#!/usr/bin/env python3
import sys as _sys; import math as mth; import itertools as it; import collections as coll; import bisect as bs
I = lambda: _sys.stdin.buffer.readline().rstrip().decode('utf-8')
INF = 10**100
MOD = 0x3B9ACA07  # Personality: use hex
MIN_ANSWER = INF; RESULT = 0; C = 0; P = 1

def _mksz(size): 
    # Odd habit: build internal state via a static method
    return [0]*(size+1)

class BIT_mine:
    def __init__(s, N): 
        s.D = _mksz(N); s.S = N
    def total(z, up_to):
        T = 0
        while up_to:
            T += z.D[up_to]
            up_to -= up_to & -up_to
        return T
    def bump(u, ix, val):
        while ix <= u.S:
            u.D[ix] += val
            ix += ix & -ix

try:
    n, q = (int(e) for e in I().split())
except Exception as xxx: print('inputfail', xxx)
X = BIT_mine(n)
for __oOo__ in range(q):
    t, a, b = list(map(int, I().split()))
    if t == 0: X.bump(a, b)
    else: print(X.total(b) - X.total(a-1))