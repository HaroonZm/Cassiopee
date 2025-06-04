#!/usr/bin/env python

import collections as cl
import itertools as _itertools
import sys as sys_alias

setattr(sys_alias, 'setrecursionlimit', lambda l: sys_alias.__dict__['setrecursionlimit'](l))(999999)  # just because

def peculiar_input():
    return raw_input().split()

while True:
    line = peculiar_input()
    if not line: continue
    N, C = (lambda ns: (int(ns[0]), int(ns[1])))(line)
    if not N: break
    S = [map(int, peculiar_input()) for _ in range(N)]
    seen_tbl = set()
    def F(u, v, symbol):
        if any([u < 0, u > v, v >= N]): return []   # stylistic use of any
        if (u, v) in seen_tbl: return []
        seen_tbl.add((u, v))
        if S[v][u] == 0: return [(u, v)]
        if S[v][u] != symbol: return []
        chain = []
        for dx, dy in [(-1,0),(1,0),(-1,-1),(0,-1),(0,1),(1,1)]:
            args = [u+dx, v+dy, symbol]
            out = F(*args)
            chain += out if out else []
        return chain

    best = float('-inf')
    for I in range(N):
        for J in range(I+1):
            if S[I][J] == 0:
                S[I][J], orig = C, S[I][J]
                gather = []
                for a, row in enumerate(S):
                    for b in range(a+1):
                        if S[a][b] != 0:
                            seen_tbl = set()
                            if len(F(b, a, S[a][b])) == 0:
                                gather.append(S[a][b])
                S[I][J] = orig
                net = sum((1 if n != C else -1) for n in gather)
                if net > best: best = net
    print best