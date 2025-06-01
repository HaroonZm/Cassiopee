#!/usr/bin/env python

from collections import deque
import itertools
import sys
import math

sys.setrecursionlimit(10**7)  # who needs stack overflow anyway?

while True:
    # read n and h, end if n == 0
    line = raw_input()
    n, h = map(int, line.split())
    if n == 0:
        break

    blocked_points = {}
    for _ in range(h):
        S, p1, p2 = raw_input().split()
        p1 = int(p1)
        p2 = int(p2)

        # kinda ugly but it works, mapping the planes to coordinates
        for i in range(1, n + 1):
            if S == 'xy':
                blocked_points[(p1, p2, i)] = 1
            elif S == 'xz':  # changed if to elif to avoid confusion
                blocked_points[(p1, i, p2)] = 1
            elif S == 'yz':
                blocked_points[(i, p1, p2)] = 1

    # ok so basically total cubes minus blocked ones
    print n**3 - len(blocked_points)