MOD = 10**9 + 7

def stirling_second_kind(n, k):
    dp = [0] * (k + 1)
    dp[0] = 1 if n == 0 else 0
    for i in range(1, n + 1):
        new_dp = [0] * (k + 1)
        for j in range(1, min(i, k) + 1):
            new_dp[j] = (j * dp[j] + dp[j - 1]) % MOD
        dp = new_dp
    return dp[k]

n, k = map(int, input().split())
print(stirling_second_kind(n, k))