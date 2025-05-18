import sys
input = sys.stdin.readline

import numpy as np

"""
各数字ごとに左移動・右移動・そのまま使う。全部コスト1ならLIS。
左から見て、「最後にそのまま使った数、そこまでの数を並べるコスト」を持ってdp。
"""

N,A,B = map(int,input().split())
P = [int(x) for x in input().split()]

INF = 10**18
dp = np.full(N+1,INF,dtype=np.int64)
dp[0] = 0
for p in P:
    # pを置く
    dp[p] = dp[:p].min()
    # pを左移動
    dp[p+1:] += B
    # pを右移動
    dp[:p] += A

answer = dp.min()
print(answer)