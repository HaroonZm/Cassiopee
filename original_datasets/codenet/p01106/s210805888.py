#!/usr/bin/env python

from collections import deque
import itertools as ite
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

while True:
    n, y, x = map(int, raw_input().split())
    if n == 0:
        break
    ys = [y]
    for i in range(1, n)[::-1]:
        if y <= 2 ** i:
            y = 2 ** i - y + 1
        else:
            y -= 2 ** i
        ys = [y] + ys
    ans = ""
    y = 1
    for i in range(n):
        sz = 2 ** (n - i)
        c = "R" if (x > sz / 2) ^ (y + 2 ** i == ys[i]) else "L"
        if c == "L" and x <= sz / 2:
            x = sz / 2 - x + 1
        elif c == "L":
            x -= sz / 2
        elif c == "R" and x > sz / 2:
            x = sz - x + 1
        ans += c
        y = ys[i]
    print ans