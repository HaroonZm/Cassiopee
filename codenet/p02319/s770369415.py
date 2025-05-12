import bisect

n,W = map(int,input().split())
b = [list(map(int, input().split())) for i in range(n)]
dp = [float("INF") for i in range(10001)]
dp[0] = 0
for v,w in b:
    for i in range(10001):
        if 10000-i+v < 10001:
            dp[10000-i+v] = min(dp[10000-i+v], dp[10000-i]+w)
for i in range(1,10000):
    dp[10000-i] = min(dp[10000-i], dp[10001-i])
print(bisect.bisect_right(dp,W)-1)