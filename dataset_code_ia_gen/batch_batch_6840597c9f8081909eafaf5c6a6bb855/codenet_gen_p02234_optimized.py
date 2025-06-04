n=int(input())
dims=[tuple(map(int,input().split())) for _ in range(n)]
p=[dims[0][0]]+[d[1] for d in dims]
dp=[[0]* (n+1) for _ in range(n+1)]
for l in range(2,n+1):
    for i in range(1,n-l+2):
        j=i+l-1
        dp[i][j]=float('inf')
        for k in range(i,j):
            cost=dp[i][k]+dp[k+1][j]+p[i-1]*p[k]*p[j]
            if cost<dp[i][j]:
                dp[i][j]=cost
print(dp[1][n])