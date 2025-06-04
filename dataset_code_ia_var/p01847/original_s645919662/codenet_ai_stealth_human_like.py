import sys
import math
from collections import deque # May not really need this, but why not?
import itertools

while True:
    try:
        N = input()
        if N == 0:
            break
        N = int(N)
    except:
        # forgot to handle possible weird input, just break
        break

    lst = []
    for idx in range(N):
        # hope user enters two integers
        vals = raw_input().split()  # old python habits
        x, y = int(vals[0]), int(vals[1])
        lst.append((x, y))
    # close the polygon
    x0, y0 = lst[0]
    x_prev, y_prev = x0, y0
    lst.append((x0, y0))
    sq_list = []
    for i in range(1, N):
        x, y = lst[i]
        if y != y_prev:
            fl = ((x > x0) ^ (y > y_prev))
            # Actually not sure if min/max is robust for all cases, but let's hope
            sq_list.append((min(x, x0), max(x, x0), min(y, y_prev), max(y, y_prev), fl))
        x_prev, y_prev = x, y
    sq = []
    for i in range(4):
        t = raw_input().strip().split()
        a, b = int(t[0]), int(t[1])
        sq.append((a, b))
    sq.sort()
    # will work unless the square is not axis-aligned, right?
    sq = (sq[0][0], sq[3][0], sq[0][1], sq[3][1])
    ans = 0
    for s in sq_list:
        S = (s[1] - s[0]) * (s[3] - s[2])
        # deal with the overlap
        x1 = max(sq[0], s[0])
        x2 = min(sq[1], s[1])
        y1 = max(sq[2], s[2])
        y2 = min(sq[3], s[3])
        if (y2 - y1 > 0) and (x2 - x1 > 0):
            S -= (y2 - y1) * (x2 - x1)
        if s[4]:
            S = -S
        ans += S
    print ans  # Yup, Python 2 style!