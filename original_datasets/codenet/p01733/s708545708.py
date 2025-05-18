#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

N = input()

lst = []
m = {}

for i in range(N):
    x, y, w = map(int, raw_input().split())
    m[(x, y)] = w
    lst.append((x - 1, y - 1))
    lst.append((x - 1, y))
    lst.append((x, y - 1))
    lst.append((x, y))

ans = 0

for p in lst:
    x = p[0]
    y = p[1]
    S = 0
    if (x, y) in m:
        S += m[(x, y)]
    if (x + 1, y) in m:
        S += m[(x + 1, y)]
    if (x, y + 1) in m:
        S += m[(x, y + 1)]
    if (x + 1, y + 1) in m:
        S += m[(x + 1, y + 1)]
    ans = max(ans, S)

print str(ans) + " / 1"