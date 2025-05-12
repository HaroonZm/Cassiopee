#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys

def main():
    while True:
        N, M = read_ints()
        if (N, M) == (0, 0):
            break
        A = read_ints()
        W = read_ints()
        print(solve(N, M, A, W))

def solve(N, M, A, W):
    weights = set([])
    for w in W:
        wl = list(weights)
        weights.add(w)
        for w0 in wl:
            if w0 + w > 0:
                weights.add(w0 + w)
            if w0 - w > 0:
                weights.add(w0 - w)
            if w - w0 > 0:
                weights.add(w - w0)

    rest = set()
    for a in A:
        if a not in weights:
            rest.add(a)

    if not rest:
        return 0

    rest = list(rest)
    cands = None
    for w in rest:
        r = set([w])
        for w0 in weights:
            r.add(w0 + w)
            if w0 - w > 0:
                r.add(w0 - w)
            if w - w0 > 0:
                r.add(w - w0)
        if cands is None:
            cands = r
        else:
            cands &= r

    if not cands:
        return -1
    return min(cands)

###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = 'DEBUG' in os.environ

def inp():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(inp())

def read_ints():
    return [int(e) for e in inp().split()]

def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()