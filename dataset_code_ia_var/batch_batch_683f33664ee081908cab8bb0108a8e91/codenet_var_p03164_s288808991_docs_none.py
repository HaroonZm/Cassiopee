N, W = map(int, input().split())
wv = []
for _ in range(N):
    wv.append(list(map(int, input().split())))
INF = 10**10
v_max = 10**5
dp = [[INF]*(v_max+1) for _ in range(N+1)]
dp[0][0] = 0
ans = 0
for i in range(N):
    for j in range(v_max+1):
        if j >= wv[i][1]:
            dp[i+1][j] = min(dp[i][j], dp[i][j-wv[i][1]]+wv[i][0])
        else:
            dp[i+1][j] = dp[i][j]
        if i+1 == N and dp[i+1][j] <= W:
            ans = j
print(ans)