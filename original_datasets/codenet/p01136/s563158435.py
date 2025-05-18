import heapq
while True:
    N = int(input())
    if not N:
        break
    f = [0] * N
    for i in range(N):
        f[i] = list(map(int,input().split()[1:]))

    dp = [ [0] * 51 for i in range(51) ]

    for i in range(N):
        for j in range(N):
            dp[j][i] = 1<<i
    for i in range(1,31):
        ds = [ j for j in range(N) if i in f[j]]
        for d1 in ds:
            for d2 in ds:
                dp[i][d1] |= dp[i-1][d2]
        for j in range(N):
            dp[i][j] |= dp[i-1][j]
    ans = 40
    for i in range(31):
        for j in range(N):
            if dp[i][j] == (1<<N)-1:
                ans = min( (ans,i) )
    if ans > 30:
        print(-1)
    else:
        print(ans)