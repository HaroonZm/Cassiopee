import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

"""
(1+x+...+x^a) をたくさんかける
(1-x^{a+1}) をかけて、(1-x)^{-1}をかける
"""

import numpy as np
MOD = 10 ** 9 + 7
N,K = map(int,input().split())
dp = np.zeros(K+1, dtype=np.int64)
dp[0] = 1

for a in map(int,input().split()):
    # numpyのバージョン違いにより
    prev = dp.copy()
    dp[a+1:] -= prev[:-(a+1)]
    np.cumsum(dp, out=dp)
    dp %= MOD

answer = dp[K]
print(answer)