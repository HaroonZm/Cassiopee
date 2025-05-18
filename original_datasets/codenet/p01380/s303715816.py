#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

n = input()
ls = []
for i in range(n):
    a, b = map(int, raw_input().split())
    ls.append((b, a))
ls.sort()

INF = 10 ** 18
DP = [0] + [INF] * n

for b, a in ls:
    DP2 = list(DP)
    for i in range(1, n + 1):
        if DP[i - 1] + a <= b:
            DP2[i] = min(DP[i], DP[i - 1] + a)
    DP = DP2

for i in range(n + 1):
    if DP[i] < INF:
        ans = i
print ans