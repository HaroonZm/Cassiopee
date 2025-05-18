N = int(input())    

A = [[0] * N for _ in range(N)]
Al = [[0] * (N+1) for _ in range(N+1)]
Ar = [[0] * (N+1) for _ in range(N+1)]

for i in range(N) :
    a = [int(i) for i in input().split()]
    for j in range(N) :
        if i < j :
            A[i][j] = a[j-1]
        elif i > j :
            A[i][j] = a[j]

for i in range(N) :
    for j in range(i+1, N) :
        Al[j][i+1] = Al[j][i] + A[j][i]
        Ar[i][j] = Ar[i-1][j] + A[i][j]

dp = [[float('inf')] * (N+1) for _ in range(N+1)]
dp[0][0] = 0
        
for i in range(N+1) :
    for j in range(i, N+1) :
        if dp[i][j] == float('inf') :
            continue
        l, r = 0, 0
        for k in range(j+1, N+1) :
            l += Al[k-1][i]
            r += Ar[k-2][k-1] - Ar[j-1][k-1]
            dp[j][k] = min(dp[j][k], dp[i][j] + l + r)
print(min(dp[i][N] for i in range(N+1)))