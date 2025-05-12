#!/usr/bin/python3

import array
from fractions import Fraction
import functools
import itertools
import math
import os
import sys

def main():
    H, W = read_ints()
    S = [inp() for _ in range(H)]
    print(solve(H, W, S))

def solve(H, W, S):
    o_table = [[0] * W for _ in range(H)]
    for y in range(H):
        c = 0
        for x in range(W - 1, -1, -1):
            if S[y][x] == 'O':
                c += 1
            o_table[y][x] = c

    i_table = [[0] * W for _ in range(H)]
    for x in range(W):
        c = 0
        for y in range(H - 1, -1, -1):
            if S[y][x] == 'I':
                c += 1
            i_table[y][x] = c

    ans = 0
    for y in range(H):
        for x in range(W):
            if S[y][x] == 'J':
                ans += o_table[y][x] * i_table[y][x]

    return ans

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