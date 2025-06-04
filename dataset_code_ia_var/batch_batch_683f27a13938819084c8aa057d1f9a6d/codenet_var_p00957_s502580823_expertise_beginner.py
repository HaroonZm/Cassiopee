l, k = input().split()
l = int(l)
k = int(k)
dp = []
for i in range(l+1):
    dp.append([0, 0])
dp[1][0] = 1
if k <= l:
    dp[k][0] = 1
h = 1
while h < l:
    dp[h+1][0] = dp[h+1][0] + dp[h][1]
    dp[h+1][1] = dp[h+1][1] + dp[h][0]
    if h + k <= l:
        dp[h+k][1] = dp[h+k][1] + dp[h][0]
    h = h + 1
ans = 0
for pair in dp:
    b = pair[0]
    w = pair[1]
    ans = ans + b
print(ans)