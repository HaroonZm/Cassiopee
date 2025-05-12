N = int(input())
C = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N)]
dp[0] = 1

MOD = 10**9 + 7

r = [-1 for _ in range(N)]
prev = [-1 for _ in range(max(C) + 1)]

for i in range(N):
    if prev[C[i]] != -1 and prev[C[i]] + 1 != i:
        r[prev[C[i]]] = i
    prev[C[i]] = i

for i in range(N - 1):
    if r[i] != -1:
        dp[r[i]] += dp[i]
        dp[r[i]] %= MOD
    dp[i + 1] += dp[i]
    dp[i + 1] %= MOD

print(dp[N-1] % MOD)