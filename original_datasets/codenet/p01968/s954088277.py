#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

N = input()
a = map(int, raw_input().split()) + [1]
DP = [[1] + [0] * (N + 1), [0] * (N + 2)]
path = [[0] * (N + 2), [0] * (N + 2)]

for i in range(N + 1):
    for j in range(i + 1):
        if DP[0][i + 1] < DP[0][j] * a[i]:
            DP[0][i + 1] = DP[0][j] * a[i]
            path[0][i + 1] = (0, j)
        if DP[0][i + 1] < DP[1][j] * a[i]:
            DP[0][i + 1] = DP[1][j] * a[i]
            path[0][i + 1] = (1, j)
        if DP[1][i + 1] > DP[0][j] * a[i]:
            DP[1][i + 1] = DP[0][j] * a[i]
            path[1][i + 1] = (0, j)
        if DP[1][i + 1] > DP[1][j] * a[i]:
            DP[1][i + 1] = DP[1][j] * a[i]
            path[1][i + 1] = (1, j)
ans = []
nex = path[0][-1]
while nex[1] != 0:
    ans += [nex[1]]
    nex = path[nex[0]][nex[1]]

ans = ans[::-1]
if len(ans) == 0:
    print 0
else:
    print len(ans)
    for num in ans:
        print num