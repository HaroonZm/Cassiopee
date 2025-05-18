#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n = I()
lst = []
for _ in range(n):
    a = input().split(".")
    if len(a) == 1:
        a[0] = a[0] + '0' * 9
        lst.append(int(a[0]))
    else:
        l = len(a[1])
        tmp = a[0] + a[1] + '0' * (9 - l)
        lst.append(int(tmp))

two = []
five = []
for i in lst:
    j = i
    cnt = 0
    while j % 2 == 0:
        j //= 2
        cnt += 1
    two.append(cnt)
    j = i
    cnt = 0
    while j % 5 == 0:
        j //= 5
        cnt += 1
    five.append(cnt)

a = [[0] * 100 for _ in range(100)]
for i, j in zip(two, five):
    a[i][j] += 1

S = [[0] * 100 for _ in range(100)]
for i in range(1, 100):
    for j in range(1, 100):
        S[i][j] = a[i-1][j-1] + S[i][j - 1] + S[i - 1][j] - S[i - 1][j - 1]

ans = 0
for i, j in zip(two, five):
    if 18 - i < 0:
        i = 18
    if 18 - j < 0:
        j = 18
    ans += S[-1][-1] - S[-1][18 - j] - S[18 - i][-1] + S[18 - i][18 - j]
    if i + i >= 18 and j + j >= 18:
        ans -= 1
print(ans // 2)