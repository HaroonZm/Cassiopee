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

# 各recipeを使用した結果を使用するrecipe同士のxorだと考えると
# 作れる状態数は高々2 ^ min(n, m)通り

while 1:
    n, m = LI()
    if n == 0 and m == 0:
        quit()
    recipe = []
    for _ in range(n):
        c = list(map(int, list(input())))
        s = 0
        t = 1
        for i in range(m):
            s += c[m - i - 1] * t
            t *= 2
        recipe.append(s) 
    dp = defaultdict(int)
    dp[0] = 0
    for r in recipe:
        dp1 = defaultdict(int)
        for j, k in dp.items():
            dp1[j] = k
        for j, k in dp.items():
            dp1[j ^ r] = max(dp1[j ^ r], k + 1)
        dp = dp1
    print(dp[0])