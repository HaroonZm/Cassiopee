from sys import stdin
from itertools import accumulate

MOD = 10**9 + 7

N, M = map(int, stdin.readline().split())

pow2 = [1] + [0] * N
for i in range(1, N + 1):
    pow2[i] = pow2[i - 1] * 2 % MOD

dp = [1] + [0] * N
dp[1:M] = pow2[1:M]
if M <= N:
    dp[M] = (pow2[M] - 1) % MOD

cumsum = list(accumulate(dp[:M+1], initial=0))
for i in range(M + 1, N + 1):
    dp[i] = (2 * dp[i - 1] - dp[i - 1 - M]) % MOD
    cumsum.append((cumsum[-1] + dp[i]) % MOD)

print((pow2[N] - dp[N]) % MOD)