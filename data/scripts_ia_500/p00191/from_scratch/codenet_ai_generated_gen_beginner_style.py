while True:
    line = input()
    if line == "":
        continue
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break
    g = []
    for _ in range(n):
        row = list(map(float, input().split()))
        g.append(row)

    # dp[i][j] = 最大の苗木の大きさ i回目に肥料j(0-index)を与えた時
    dp = [[0.0]*n for _ in range(m+1)]

    # 1回目はどの肥料でも成長度は1.0
    for j in range(n):
        dp[1][j] = 1.0

    for i in range(2, m+1):
        for j in range(n):
            max_val = 0.0
            for k in range(n):
                val = dp[i-1][k] * g[k][j]
                if val > max_val:
                    max_val = val
            dp[i][j] = max_val

    ans = max(dp[m])
    print(f"{ans:.2f}")