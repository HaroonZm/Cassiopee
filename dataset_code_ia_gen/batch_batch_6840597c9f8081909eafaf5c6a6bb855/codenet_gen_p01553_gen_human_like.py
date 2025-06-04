n = int(input())
c = [input() for _ in range(n)]

MOD = 10**9 + 7

# dp[i][j]: i番目まで見て，前の中継所でj番目に並んでいるチームの数(累積和利用用)
dp = [[0] * (n+1) for _ in range(n+1)]
# 初期条件：1番目は前の順位考えようが無いので全部1通り
dp[0][0] = 1

for i in range(n):
    prefix = [0] * (n+1)
    for j in range(n):
        prefix[j+1] = (prefix[j] + dp[i][j]) % MOD

    if c[i] == 'U':
        # 前の順位は今の順位より大きい(つまりi番目の前より後ろにあるもの)
        # dp[i+1][j] = sum of dp[i][k] for k > j
        for j in range(n):
            dp[i+1][j] = (prefix[n] - prefix[j+1]) % MOD

    elif c[i] == 'D':
        # 前の順位は今の順位より小さい(つまりi番目の前より前にあるもの)
        # dp[i+1][j] = sum of dp[i][k] for k < j
        for j in range(n):
            dp[i+1][j] = prefix[j] % MOD

    else:  # '-'
        # 前の順位は変わらず同じ位置
        # dp[i+1][j] = dp[i][j]
        for j in range(n):
            dp[i+1][j] = dp[i][j] % MOD

# 最終的にdp[n]の全てのjを足すとOK
# ただし、並びは1からnまでの全順位の割り当てなので総和で良い
ans = sum(dp[n]) % MOD
print(ans)