import sys

def count_combinations(n, s):
    # dp[i][j][k] = 組み合わせ数: 0..i までの数字から j 個選び合計が k である組み合わせ
    dp = [[[0]*(s+1) for _ in range(n+1)] for _ in range(101)]
    dp[0][0][0] = 1

    for i in range(1, 101):
        for j in range(n+1):
            for k in range(s+1):
                # i-1番目の数字を使わない場合の組み合わせ数
                dp[i][j][k] = dp[i-1][j][k]
                # i-1番目の数字を使う場合
                if j > 0 and k - (i-1) >= 0:
                    dp[i][j][k] += dp[i-1][j-1][k - (i-1)]
    return dp[100][n][s]

for line in sys.stdin:
    n, s = map(int, line.split())
    if n == 0 and s == 0:
        break
    print(count_combinations(n, s))