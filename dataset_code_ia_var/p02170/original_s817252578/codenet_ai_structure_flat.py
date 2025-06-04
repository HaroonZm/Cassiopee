N, K, A = map(int, input().split())
mod = 998244353
p_coin = A * pow(100, mod-2, mod) % mod
p_dice = pow(N, mod-2, mod)
dp = [0] * (K+1) + [1] * N
dp[0] = 1
c = 1
i = 1
while i <= K:
    dp[i] = c * p_coin % mod
    tmp = (dp[i] - dp[i-N]) * p_dice % mod
    c = (c + tmp) % mod
    i += 1
result = dp[K] * pow(p_coin, mod-2, mod) % mod
print(result)