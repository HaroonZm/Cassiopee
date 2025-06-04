INF = int(1e9)

while True:
    n, m, p = map(int, input().split())
    if n == 0 and m == 0 and p == 0:
        break
    es = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        es.append((u, v, w))
        es.append((v, u, w))
    d = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            else:
                row.append(INF)
        d.append(row)
    for (u, v, w) in es:
        d[u][v] = w
    k = 0
    while k < n:
        i = 0
        while i < n:
            j = 0
            while j < n:
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                j += 1
            i += 1
        k += 1
    dp = []
    for i in range(n):
        dp.append([0] * n)
    for (u, v, w) in es:
        if d[0][u] + w + d[v][n-1] == d[0][n-1]:
            dp[u][v] = 1
    k = 0
    while k < n:
        i = 0
        while i < n:
            j = 0
            while j < n:
                dp[i][j] += dp[i][k] * dp[k][j]
                j += 1
            i += 1
        k += 1
    for _ in range(p):
        c = int(input())
        ans = 0
        if dp[0][n-1] != 0:
            ans = dp[0][c] * dp[c][n-1] / dp[0][n-1]
        print("{:.9f}".format(ans))