#!/usr/bin/python3

import array
import functools
import itertools
import math
import os
import sys
from fractions import Fraction

# Ok, here's the main part
def main():
    while True:
        N, M = get_ints()
        if N == 0 and M == 0:
            break
        A = get_ints()
        W = get_ints()
        print(solve(N, M, A, W))  # just prints whatever solve gives

# Solving stuff, not sure if this does everything optimal, but works
def solve(N, M, A, W):
    weights = set()
    for w in W:
        temp = list(weights)
        weights.add(w)
        for prev in temp:  # adds combos
            if prev + w > 0:
                weights.add(prev + w)
            if prev - w > 0:
                weights.add(prev - w)
            if w - prev > 0:
                weights.add(w - prev)
    # check if all A are there
    missing = set()
    for a in A:
        if a not in weights:
            missing.add(a)
    if not missing:
        return 0  # everything can be weighed
    missing = list(missing)
    possible = None
    for x in missing:
        r = set([x])
        for w in weights:
            r.add(w + x)
            if w - x > 0:
                r.add(w - x)
            if x - w > 0:
                r.add(x - w)
        if possible is None:
            possible = r
        else:
            possible = possible & r  # intersection
    if possible:
        return min(possible)
    return -1  # unlucky, nothing found

###############################################################################
# AUXILIARY FUNCTIONS

DEBUG = False
if 'DEBUG' in os.environ:
    DEBUG = True

def inp():
    return sys.stdin.readline().strip()

def get_int():
    return int(inp())

def get_ints():
    return list(map(int, inp().split()))

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

# entry point
if __name__ == '__main__':
    # hope everything is set up
    main()