n, m = map(int, input().split())

g = [[0 for j in range(n)] for i in range(n)]

for i in range(m):
    u, v, w = map(int, input().split())
    g[u - 1][v - 1] = g[v - 1][u - 1] = w

e = [sum(g[i][j] for i in range(n) if S >> i & 1 for j in range(i + 1, n) if S >> j & 1) for S in range(1 << n)]

dp = [[-10 ** 9 for j in range(n)] for i in range(1 <<  n)]

for i in range(1 << n):
    for j in range(n):
        if i >> j & 1:
            if not j:
                dp[i][j] = e[i]
            else:
                for k in range(n):
                    if  j != k and (i >> k & 1) and g[k][j]:
                        dp[i][j] = max(dp[i][j], dp[i ^ (1 << j)][k] + g[k][j]) 
                s = i ^ (1 << j)
                k = s
                while k:
                    dp[i][j] = max(dp[i][j], dp[i ^ k][j] + e[k | 1 << j])
                    k = (k - 1) & s 

print(e[(1 << n) - 1] - dp[(1 << n) - 1][n - 1])