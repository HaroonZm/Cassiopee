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
        N, M, T, P = read_ints()
        if (N, M, T, P) == (0, 0, 0, 0):
            break
        F = [read_ints() for _ in range(T)]
        H = [read_ints() for _ in range(P)]
        print(*solve(N, M, T, P, F, H), sep='\n')

def solve(N, M, T, P, F, H):
    w = N
    h = M
    paper = [[1] * w for _ in range(h)]

    for d, c in F:
        if d == 1:
            w1 = max(c, w - c)
            npaper = [[0] * w1 for _ in range(h)]
            for y in range(h):
                for dx in range(c):
                    npaper[y][c - 1 - dx] += paper[y][dx]
                for dx in range(c, w):
                    npaper[y][dx - c] += paper[y][dx]
            w = w1
            paper = npaper
            continue

        h1 = max(c, h - c)
        npaper = [[0] * w for _ in range(h1)]
        for x in range(w):
            for dy in range(c):
                npaper[c - 1 - dy][x] += paper[dy][x]
            for dy in range(c, h):
                npaper[dy - c][x] += paper[dy][x]
        h = h1
        paper = npaper

    return [paper[y][x] for x, y in H]

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