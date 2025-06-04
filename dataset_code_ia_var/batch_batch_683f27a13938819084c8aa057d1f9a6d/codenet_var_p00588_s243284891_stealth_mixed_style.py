import sys
from collections import deque
import math
import itertools as it

sys.setrecursionlimit(9999999)

def get_inputs():
    t = int(input())
    return [ (int(input()), input()) for _ in range(t) ]

def process(N, S):
    pre_S1 = 'N' + S[:N*2] + 'N'
    pre_S2 = ''.join(['N', S[N*2:], 'N'])
    (sx1, sx2), (gx1, gx2) = [float('inf')]*2, [-1]*2
    res = 0
    for idx in range(N+1):
        # imperative
        if pre_S1[2*idx] == 'Y' or pre_S1[2*idx+1] == 'Y':
            sx1 = min(sx1, idx)
            gx1 = idx
            res += 1
        # functional
        if any([pre_S2[2*idx] == 'Y', pre_S2[2*idx+1] == 'Y']):
            sx2 = min(sx2, idx)
            gx2 = idx
            res += 1
    res += int(sx1 > sx2) + int(gx1 < gx2)
    return N + res

if __name__ == '__main__':
    # procedural
    cases = get_inputs()
    for c in it.chain(cases):
        print(process(*c))