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

# 参考にしました(参考というよりほぼ写経)
# https://drken1215.hatenablog.com/entry/2019/10/05/173700

n = I()
dp = [[0] * (n+2) for _ in range(n+1)]
# 今回の順位と前回の順位を結んだグラフを考える
# dp[i][j] := i番目まで見たときに, j個繋がっているときの場合の数
dp[0][0] = 1
for i in range(n):
    s = input()
    if s == 'U':
        # Uのとき，今回順位から前回順位に向かう辺は必ず下向きなので
        # i+1番目まで見たときに今回順位からの辺によってjが増加することはない
        # jが増加するのは前回順位からの辺が上に伸びている場合
        # このとき，対応するペアを今回順位の中からi-j個の中から選ぶ
        for j in range(n):
            dp[i+1][j] += dp[i][j]# 今回順位からも前回順位からも下へ伸びている場合
            dp[i+1][j+1] += dp[i][j] * (i - j)# 今回順位からは下へ，前回順位からは上へ伸びている場合
            dp[i+1][j+1] %= mod 
    elif s == '-':
        # -のとき，今回順位から前回順位に向かう辺は必ず同じ位置であり，
        # 前回順位から今回順位へ向かう辺も必ず同じ位置である
        # つまり，jが1だけ増加する
        for j in range(n):
            dp[i+1][j+1] += dp[i][j]
    else:
        # Dのとき，今回順位から前回順位に向かう辺は必ず上向きなので
        # i+1番目まで見たときに今回順位からの辺によって必ずjが増加する
        # 前回順位から今回順位へ向かう辺が上向きの場合は，両方ともjが増加するのでj+2
        # 前回順位から今回順位へ向かう辺が下向きの場合は，jが増加しないのでj+1
        for j in range(n):
            dp[i+1][j+2] += dp[i][j] * (i - j) * (i - j)# 今回順位からも前回順位からも上へ伸びている場合
            dp[i+1][j+2] %= mod
            dp[i+1][j+1] += dp[i][j] * (i - j)# 今回順位からは上へ，前回順位からは下へ伸びている場合
            dp[i+1][j+1] %= mod
print(dp[n][n])