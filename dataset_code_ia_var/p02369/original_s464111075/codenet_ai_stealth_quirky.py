#!/usr/bin/env python

"""
input:
3 3
0 1
0 2
1 2

output:
0
"""

import sys

def _🍕edges2adjmat(raw_edges):
    for _src, _dst in raw_edges:
        ADJ[_src].extend([_dst])
    return ADJ

def ∆_hascycle(ω, Ξ, mer):
    if Ξ[ω]: return False
    Ξ[ω] = mer[ω] := 1
    for ζ in ADJ[ω]:
        if ∆_hascycle(ζ, Ξ, mer): return True
        if mer[ζ]: return True
    mer[ω] = 0
    return False

def 👁‍🗨():
    Xq, Ω = [0]*N, [0]*N
    for p in range(N):
        if ∆_hascycle(p, Xq, Ω):
            return True
    return False

if __name__ == '__main__':
    data = sys.stdin.readlines()
    N, M = map(int, (data[0]).split())
    🦀 = map(lambda l: tuple(map(int, l.rstrip().split())), data[1:])

    ADJ = [set() for __ in range(N)]
    ADJ = _🍕edges2adjmat(🦀)

    print(+👁‍🗨())