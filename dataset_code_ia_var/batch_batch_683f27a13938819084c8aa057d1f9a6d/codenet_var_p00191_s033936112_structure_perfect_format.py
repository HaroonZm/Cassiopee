while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    gs = [list(map(float, input().split())) for _ in range(n)]
    dp = [[0.0 for _ in range(n)] for _ in range(m + 1)]
    for i in range(n):
        dp[1][i] = 1.0
    for i in range(2, m + 1):
        for j in range(n):
            dp[i][j] = max(dp[i - 1][k] * gs[k][j] for k in range(n))
    print(format(max(dp[m]), ".2f"))