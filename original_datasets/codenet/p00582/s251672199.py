#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys

def main():
    N, M = read_ints()
    P = [(s, v) for s, v in [read_ints() for _ in range(N)]]
    C = [read_int() for _ in range(M)]
    print(solve(N, M, P, C))

def solve(N, M, P, C):
    P.sort(key=lambda p: (-p[1], -p[0]))
    C.sort(reverse=True)
    ci = 0
    for pi in range(N):
        if ci == M:
            break
        s = P[pi][0]
        if C[ci] >= s:
            ci += 1
    return ci

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