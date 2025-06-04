#!/usr/bin/env python

import sys
import math
import itertools as it
from collections import deque

sys.setrecursionlimit(10000000)

x, y, r = map(float, raw_input().split())

q = input()

for loop in range(q):
    x1, y1, x2, y2 = map(float, raw_input().split())
    vx = x2 - x1
    vy = y2 - y1
    norm = vx * vx + vy * vy
    inn = vx * (x - x1) + vy * (y - y1)
    xc = x1 + vx * inn / norm
    yc = y1 + vy * inn / norm
    rem = math.sqrt(max(0, r ** 2 - (xc - x) ** 2 - (yc - y) ** 2))
    dx = vx / math.sqrt(norm) * rem
    dy = vy / math.sqrt(norm) * rem
    ans = sorted([
        (xc + dx, yc + dy),
        (xc - dx, yc - dy)
    ])
    print "%.10f %.10f %.10f %.10f" % (
        ans[0][0], ans[0][1], ans[1][0], ans[1][1]
    )