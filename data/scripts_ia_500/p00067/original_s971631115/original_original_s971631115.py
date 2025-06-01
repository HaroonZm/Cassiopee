#!/usr/bin/env python

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

def solve(L):
    n = 0
    sets = set()
    for y in range(12):
        for x in range(12):
            if not L[y][x]:
                continue
            elif y and L[y-1][x]:
                L[y][x] = L[y-1][x]
            elif x and L[y][x-1]:
                L[y][x] = L[y][x-1]
            else:
                n += 1
                sets.add(n)
                L[y][x] = n
        for x in range(10, -1, -1):
            if L[y][x] and L[y][x+1] and L[y][x] != L[y][x+1]:
                sets.discard(L[y][x])
                L[y][x] = L[y][x+1]
    return len(sets)

s = '\n'
sep = '\n'
while s:
    L = []
    for i in range(12):
        L.append([int(s) for s in stdin.readline().rstrip()])
    print(solve(L))
    s = stdin.readline()