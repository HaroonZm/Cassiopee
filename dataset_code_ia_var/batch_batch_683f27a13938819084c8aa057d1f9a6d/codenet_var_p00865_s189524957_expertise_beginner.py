while True:
    n, m, k = map(int, raw_input().split())
    if n == 0:
        break

    dp = []
    for i in range(n):
        dp.append([0] * (m * n + 1))

    for j in range(1, m + 1):
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, m * n + 1):
            total = 0
            for x in range(max(j - m, 0), j):
                total += dp[i - 1][x]
            dp[i][j] = total

    s = 0
    for value in dp[n - 1]:
        s += value

    ans = 0.0
    for i in range(1, m * n + 1):
        ans += 1.0 * dp[n - 1][i] / s * max(1, i - k)

    print("%.10f" % ans)