import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
import sys
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
INF = float("INF")
ans = 1
tmp = 0
cnt = 0
ansli = []
tmpli = []
candili = []
stillset = set()
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]
ddn9 = ddn + [(0, 0)]
# Suppression des fonctions inutilisées, tout est linéaire

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
new_s = ""
idx = 0
while idx < 2 * n:
    if (2 * n - idx - 1) % 2 == 0:
        new_s += s[idx]
    else:
        if s[idx] == "B":
            new_s += "W"
        else:
            new_s += "B"
    idx += 1

lr = ""
idx = 0
while idx < 2 * n:
    if new_s[idx] == "B":
        lr += "R"
    else:
        lr += "L"
    idx += 1

rcount = 0
idx = 0
lenlr = len(lr)
tmpcnt = 0
idx = 0
while idx < lenlr:
    if lr[idx] == "R":
        rcount += 1
    idx += 1

if rcount != n:
    print(0)
    sys.exit()

lcount = 0
idx = 0
while idx < lenlr:
    if lr[idx] == "L":
        lcount += 1
    else:
        ans *= lcount
        ans %= mod
        lcount -= 1
    idx += 1

i = 1
while i <= n:
    ans *= i
    ans %= mod
    i += 1

print(ans)