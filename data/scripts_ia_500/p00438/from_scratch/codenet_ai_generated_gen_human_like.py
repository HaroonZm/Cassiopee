while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    n = int(input())
    closed = set()
    for _ in range(n):
        x, y = map(int, input().split())
        closed.add((x, y))
    # dp[i][j] = number of ways to reach (i,j)
    dp = [[0] * (b + 1) for _ in range(a + 1)]
    if (1, 1) not in closed:
        dp[1][1] = 1
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if (i, j) == (1, 1):
                continue
            if (i, j) in closed:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] if i > 1 else 0) + (dp[i][j-1] if j > 1 else 0)
    print(dp[a][b])