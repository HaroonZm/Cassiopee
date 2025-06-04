from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

sys.setrecursionlimit(1000000)
mod = 998244353

m, n, k = [int(x) for x in sys.stdin.readline().split()]
if n < k:
    print(0)
elif m < k:
    print(0)
else:
    ans = pow(m, n, mod)
    p = [pow(i, n, mod) for i in range(k + 1)]
    c = m
    comb = []
    for i in range(k + 1):
        comb.append([0] * (i + 1))
    comb[0][0] = 1
    i = 0
    while i < k:
        j = 0
        while j < i + 1:
            comb[i + 1][j] += comb[i][j]
            comb[i + 1][j + 1] += comb[i][j]
            j += 1
        i += 1
    i = 1
    while i < k:
        s = 0
        j = i
        while j >= 1:
            if (i + j) & 1:
                s -= comb[i][j] * p[j]
            else:
                s += comb[i][j] * p[j]
            j -= 1
        s *= c
        c *= (m - i)
        c *= pow(i + 1, mod - 2, mod)
        c %= mod
        ans -= s
        ans %= mod
        i += 1
    print(ans)