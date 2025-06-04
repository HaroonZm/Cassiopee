n, W = map(int, input().split())
w = []
v = []
V = 0
for i in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)
    V += b
dp = [[float('inf')] * (V+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(V+1):
        if j >= v[i]:
            dp[i+1][j] = min(dp[i][j], dp[i][j-v[i]]+w[i])
        else:
            dp[i+1][j] = dp[i][j]
ans = 0
for i in range(V+1):
    if dp[n][i] <= W:
        ans = i
print(ans)