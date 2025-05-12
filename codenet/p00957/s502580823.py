l,k = map(int,input().split())
dp = [[0,0] for i in range(l+1)]
dp[1][0] = 1
if k <= l:
    dp[k][0] = 1
for h in range(1,l):
    dp[h+1][0] += dp[h][1]
    dp[h+1][1] += dp[h][0]
    if h+k <= l:
        dp[h+k][1] += dp[h][0]
ans = 0
for b,w in dp:
    ans += b
print(ans)