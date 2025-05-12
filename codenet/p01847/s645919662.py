#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

while True:
    N = input()
    if N == 0:
        break
    lst = []
    for i in range(N):
        x, y = map(int, raw_input().split())
        lst.append((x, y))
    x0, y0 = lst[0]
    x_pre, y_pre = lst[0]
    lst.append((x0, y0))
    sq_list = []
    for i in range(1, N):
        x, y = lst[i]
        if y != y_pre:
            flag = ((x > x0) ^ (y > y_pre))
            sq_list.append((min(x, x0),max(x, x0),min(y, y_pre),max(y, y_pre),flag))
        x_pre = x
        y_pre = y
    sq = []
    for i in range(4):
        x, y = map(int, raw_input().split())
        sq.append((x, y))
    sq.sort()
    sq = (sq[0][0], sq[3][0], sq[0][1], sq[3][1])
    ans = 0
    for s in sq_list:
        S = (s[1] - s[0]) * (s[3] - s[2])
        x1 = max(sq[0], s[0])
        x2 = min(sq[1], s[1])
        y1 = max(sq[2], s[2])
        y2 = min(sq[3], s[3])
        if y2 - y1 > 0 and x2 - x1 > 0:
            S -= (y2 - y1) * (x2 - x1)
        if s[4]:
            S *= -1
        ans += S
    print ans