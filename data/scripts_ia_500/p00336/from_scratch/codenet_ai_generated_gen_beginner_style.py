t = input()
b = input()

mod = 1000000007
len_t = len(t)
len_b = len(b)

# dp[i][j] = nombre de façons de trouver b[:j] dans t[:i]
dp = [[0] * (len_b + 1) for _ in range(len_t + 1)]

for i in range(len_t + 1):
    dp[i][0] = 1  # une façon de trouver la sous-chaîne vide

for i in range(1, len_t + 1):
    for j in range(1, len_b + 1):
        dp[i][j] = dp[i-1][j]
        if t[i-1] == b[j-1]:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= mod

print(dp[len_t][len_b] % mod)