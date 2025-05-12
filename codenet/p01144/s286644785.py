import sys

while True:
    n,m = [int(i) for i in input().split()]
    if n == 0 and m == 0:
        sys.exit()
    dp = []
    ans = 0
    for i in range(n):
        dp.append([int(j) for j in input().split()])
    dp.sort(key=lambda x:x[1],reverse=True)
    for i in range(n):
        if dp[i][0] <= m:
            m -= dp[i][0]
        elif m > 0:
            ans += dp[i][1] * (dp[i][0] - m)
            m = 0
        else:
            ans += dp[i][1] * dp[i][0]
    print(ans)