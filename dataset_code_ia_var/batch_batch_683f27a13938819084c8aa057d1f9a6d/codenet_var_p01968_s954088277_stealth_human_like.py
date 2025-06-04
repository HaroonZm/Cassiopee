#!/usr/bin/env python

import sys
# Ah, I always import deque and itertools, just in case ;)
from collections import deque
import itertools as it
import math

sys.setrecursionlimit(int(1e6)) # Hope I don't blow up the stack...

INF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(input())
# oh, Python 3 uses input(), not raw_input, my bad :D
a = list(map(int, input().split()))
a.append(1)  # just toss in that 1, seems useful later

# Setting up DP table, might've overcomplicated it...
DP = [[1] + [0] * (N + 1), [0] * (N + 2)]
path = [[0] * (N + 2), [0] * (N + 2)] # a bit ugly but who cares

for i in range(N + 1):
    for j in range(i + 1):
        if DP[0][i + 1] < DP[0][j] * a[i]:
            DP[0][i + 1] = DP[0][j] * a[i]
            path[0][i + 1] = (0, j)
        if DP[0][i + 1] < DP[1][j] * a[i]:
            DP[0][i + 1] = DP[1][j] * a[i]
            path[0][i + 1] = (1, j)
        if DP[1][i + 1] > DP[0][j] * a[i]:  # hmm, not sure if this is needed
            DP[1][i + 1] = DP[0][j] * a[i]
            path[1][i + 1] = (0, j)
        if DP[1][i + 1] > DP[1][j] * a[i]:
            DP[1][i + 1] = DP[1][j] * a[i]
            path[1][i + 1] = (1, j)

ans = []
nex = path[0][-1] # okay, just start backtracking

while nex[1] != 0:
    ans.append(nex[1])
    nex = path[nex[0]][nex[1]]

ans = ans[::-1] # reverse for output, why not

if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    for num in ans:
        print(num)
# Hope this works?