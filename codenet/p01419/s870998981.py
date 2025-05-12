#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

R, C, M = map(int, raw_input().split())
S = []
t_cost = []
on_cost = []
off_cost = []

for loop in range(R):
    hoge = raw_input()
    S.append(hoge)

for loop in range(R):
    hoge = map(int, raw_input().split())
    t_cost.append(hoge)

for loop in range(R):
    hoge = map(int, raw_input().split())
    on_cost.append(hoge)

for loop in range(R):
    hoge = map(int, raw_input().split())
    off_cost.append(hoge)

m = {}
used = {}

for y in range(R):
    for x in range(C):
        m[(x, y)] = []

def func(x, y, gx, gy, step):
    if x < 0 or y < 0 or x >= C or y >= R:
        return False
    if (x, y) in used:
        return False
    used[(x, y)] = step
    if S[y][x] == '#':
        return False
    if x == gx and y == gy:
        m[(x, y)].append(step)
        return True
    ret = False
    ret = (ret or func(x - 1, y, gx, gy, step + 1))
    ret = (ret or func(x + 1, y, gx, gy, step + 1))
    ret = (ret or func(x, y - 1, gx, gy, step + 1))
    ret = (ret or func(x, y + 1, gx, gy, step + 1))
    if ret:
        m[(x, y)].append(step)
    return ret

sy, sx = map(int, raw_input().split())
cnt = 0
for loop in range(M - 1):
    gy, gx = map(int, raw_input().split())
    used = {}
    func(sx, sy, gx, gy, cnt)
    cnt = m[(gx, gy)].pop()
    sx, sy = gx, gy
m[(gx, gy)].append(cnt)

ans = 0
for y in range(R):
    for x in range(C):
        t = t_cost[y][x]
        on = on_cost[y][x]
        off = off_cost[y][x]

        lst = m[(x, y)]
        if len(lst) > 0:
            ans += on + off
        for i in range(len(lst) - 1):
            t1 = lst[i]
            t2 = lst[i + 1]
            ans += min(on + off, t * (t2 - t1))
#print m
print ans