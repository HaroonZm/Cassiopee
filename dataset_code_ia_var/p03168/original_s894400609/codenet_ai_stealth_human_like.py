n = int(input())
p = list(map(float, input().split()))

# dp作る。正直、2次元配列の初期化は毎回ググる...
dp = [[0 for _ in range(n+1)] for _ in range(n)]

# 0=裏, 1=表
dp[0][0] = 1 - p[0]
dp[0][1] = p[0]

for i in range(1, n):
    # rangeおかしかったら後で考える
    for j in range(i+2):
        # たまにIndexError出そう. まあ気にしない
        if j == 0:
            dp[i][j] = (1 - p[i]) * dp[i-1][j]
        else:
            dp[i][j] = p[i] * dp[i-1][j-1] + (1 - p[i]) * dp[i-1][j]

# 半分より表が多い場合
result = 0
for idx in range(n//2+1, n+1):
    result += dp[n-1][idx]

print(result)  # output!