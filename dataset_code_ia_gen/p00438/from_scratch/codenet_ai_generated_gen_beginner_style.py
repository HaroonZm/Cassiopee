while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    n = int(input())
    closed = set()
    for _ in range(n):
        x, y = map(int, input().split())
        closed.add((x, y))

    dp = [[0] * (b + 1) for _ in range(a + 1)]
    dp[1][1] = 1 if (1, 1) not in closed else 0

    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if (i, j) in closed or (i == 1 and j == 1):
                continue
            ways = 0
            if i > 1:
                ways += dp[i - 1][j]
            if j > 1:
                ways += dp[i][j - 1]
            dp[i][j] = ways

    print(dp[a][b])