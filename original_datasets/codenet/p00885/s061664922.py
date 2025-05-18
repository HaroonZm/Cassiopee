inf = 10**9
while True:
    n = int(input())
    if n == 0:
        break
    b = [(0,0)]
    b.extend([tuple(map(int,input().split())) for i in range(n)])
    dp = [[inf]*4 for i in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        update = False
        for j in range(4):
            if dp[i][j] is inf:
                continue
            now = b[i][0]
            nxt = b[i+1][0]
            if j<=2 and b[i][1]+abs(nxt-now)*(j+1) <= b[i+1][1] and dp[i+1][j+1] > dp[i][j]+abs(nxt-now):
                dp[i+1][j+1] = dp[i][j]+abs(nxt-now)
                update = True
            if b[i][1]+now*(j+1)+nxt <= b[i+1][1] and dp[i+1][1] > dp[i][j]+nxt+now:
                dp[i+1][1] = dp[i][j]+nxt+now
                update = True
        if not update:
            print('NG',i+1)
            break
    if update:
        print('OK',min(dp[n])+b[n][0])