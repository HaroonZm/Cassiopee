MOD = 10**9 + 7
N, M = map(int, input().split())

# dp[i][0]: number of sequences length i with no run of M ones, ending with 0
# dp[i][k]: for 1 <= k < M, sequences length i with no run M, ending with exactly k consecutive ones
dp = [[0]*(M) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    dp[i][0] = sum(dp[i-1]) % MOD
    for k in range(1, M):
        dp[i][k] = dp[i-1][k-1]
        
total = pow(2, N, MOD)
no_M = sum(dp[N]) % MOD

print((total - no_M) % MOD)