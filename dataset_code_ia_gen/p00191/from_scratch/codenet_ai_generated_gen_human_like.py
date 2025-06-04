while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    g = [list(map(float, input().split())) for _ in range(n)]

    # dp[i][j]: i回目に肥料j+1を与えた時の苗木の最大サイズ
    # 1回目はどの肥料でも成長度1.0
    dp = [[0.0] * n for _ in range(m)]
    for j in range(n):
        dp[0][j] = 1.0

    for i in range(1, m):
        for j in range(n):      # 今回与える肥料 j+1
            max_val = 0.0
            for k in range(n):  # 前回与えた肥料 k+1
                val = dp[i - 1][k] * g[k][j]
                if val > max_val:
                    max_val = val
            dp[i][j] = max_val

    ans = max(dp[m - 1])
    print(f"{ans:.2f}")