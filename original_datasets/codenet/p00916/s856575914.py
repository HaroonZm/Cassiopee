#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

while True:
    n = input()
    if n == 0:
        break
    
    lst = []
    x_lst = []
    y_lst = []

    for loop in range(n):
        l, t, r, b = map(int, raw_input().split())
        lst.append((l, t, r, b))
        x_lst += [l, r]
        y_lst += [t, b]

    x_lst = sorted(list(set(x_lst)))
    y_lst = sorted(list(set(y_lst)))

    mx = {}
    my = {}

    for i in range(len(x_lst)):
        mx[x_lst[i]] = 2 * i + 1

    for i in range(len(y_lst)):
        my[y_lst[i]] = 2 * i + 1

    wall = {}

    def func(x, y):
        if (x, y) in wall:
            return
        if x < 0 or y < 0 or x > 5 * n or y > 5 * n:
            return
        wall[(x, y)] = 1
        func(x - 1, y)
        func(x + 1, y)
        func(x, y - 1)
        func(x, y + 1)

    for sq in lst:
        sx = mx[sq[0]]
        gx = mx[sq[2]]
        sy = my[sq[3]]
        gy = my[sq[1]]
        for x in range(sx, gx + 1):
            wall[(x, sy)] = 1
            wall[(x, gy)] = 1
        for y in range(sy, gy + 1):
            wall[(sx, y)] = 1
            wall[(gx, y)] = 1

    ans = 0

    for y in range(5 * n):
        for x in range(5 * n):
            if not (x, y) in wall:
                ans += 1
                func(x, y)

    print ans