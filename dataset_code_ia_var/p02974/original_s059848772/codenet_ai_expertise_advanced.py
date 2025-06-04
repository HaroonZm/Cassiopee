import sys
from functools import partial
from itertools import product

sys.setrecursionlimit(2**31 - 1)
INF = float('inf')
MOD = 10**9 + 7
input = sys.stdin.readline

def resolve():
    n, K = map(int, input().split())
    # Using only two layers to optimize space: dp[cur][j][k]
    dp = [ [ [0]*(K+2701) for _ in range(n+2) ] for _ in range(2) ]
    dp[0][0][0] = 1
    for i in range(n):
        cur, nxt = i % 2, (i+1) % 2
        for row in dp[nxt]:  # Clear next state
            row[:] = [0] * len(row)
        for j, k in product(range(i+1), range(K+1)):
            val = dp[cur][j][k]
            if not val:
                continue
            nj = j
            nk = k + 2*j
            add = (2*j+1)*val % MOD
            if nk <= K:
                dp[nxt][nj][nk] = (dp[nxt][nj][nk] + add) % MOD
            nj = j+1
            nk = k + 2*nj
            if nk <= K:
                dp[nxt][nj][nk] = (dp[nxt][nj][nk] + val) % MOD
            if j:
                nj = j-1
                nk = k + 2*nj
                add = j*j*val % MOD
                if nk <= K:
                    dp[nxt][nj][nk] = (dp[nxt][nj][nk] + add) % MOD
    print(dp[n%2][0][K])
resolve()