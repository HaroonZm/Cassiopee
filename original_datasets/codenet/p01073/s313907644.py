n, m, k = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))
abList = sorted(tuple(zip(aList, bList)), key=lambda x:-x[0])
ans = 0
#dp[y][x] ... y面x個の最大値
dp = [[0] * (m + 1) for _ in range(k + 1)]
for a, b in abList:
    for y in range(k - 1, -1, -1):
        for x in range(m - 1, -1, -1):
            use = min(b, m - x)
            dp[y + 1][x + use] = max(dp[y + 1][x + use], dp[y][x] + use * a)

ans = 0
for y in range(k + 1):
    for x in range(m + 1):
        ans = max(ans, dp[y][x] + m - x)
print(ans)