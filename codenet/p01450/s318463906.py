N, W = map(int, input().split())
MOD = 10**9 + 7
ws = [int(input()) for i in range(N)]
ws.sort(reverse=1)
su = sum(ws)
dp = [0]*(W+1)
dp[0] = 1
ans = 0
if su <= W:
    ans += 1
for i in range(N):
    w = ws[i]
    su -= w
    ans += sum(dp[max(W+1-w-su, 0):max(W+1-su, 0)]) % MOD
    for j in range(W, w-1, -1):
        dp[j] += dp[j-w]
        dp[j] %= MOD
print(ans % MOD)