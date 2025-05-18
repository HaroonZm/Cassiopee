#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

def koch(n, sx, sy, gx, gy):
    if n == 0:
        print gx, gy
        return
    vx = gx - sx
    vy = gy - sy
    x1 = sx + vx / 3
    y1 = sy + vy / 3
    x3 = gx - vx / 3
    y3 = gy - vy / 3
    vx60 = vx / 2 - math.sqrt(3) * vy / 2
    vy60 = math.sqrt(3) * vx / 2 + vy / 2
    x2 = x1 + vx60 / 3
    y2 = y1 + vy60 / 3
    koch(n - 1, sx, sy, x1, y1)
    koch(n - 1, x1, y1, x2, y2)
    koch(n - 1, x2, y2, x3, y3)
    koch(n - 1, x3, y3, gx, gy)

n = input()
print 0, 0
koch(n, 0.0, 0.0, 100.0, 0.0)