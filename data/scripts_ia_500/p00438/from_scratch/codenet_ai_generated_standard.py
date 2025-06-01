while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    n=int(input())
    blocked=set(tuple(map(int,input().split())) for _ in range(n))
    dp=[[0]*(b+1) for _ in range(a+1)]
    dp[1][1]=0 if (1,1) in blocked else 1
    for i in range(1,a+1):
        for j in range(1,b+1):
            if (i,j) in blocked or (i==1 and j==1):
                continue
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print(dp[a][b])