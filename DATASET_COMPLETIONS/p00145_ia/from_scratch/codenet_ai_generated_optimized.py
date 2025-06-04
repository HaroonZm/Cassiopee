n=int(input())
a,b=[],[]
for _ in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
dp=[[0]*n for _ in range(n)]
top=[[0]*n for _ in range(n)]
bottom=[[0]*n for _ in range(n)]
for i in range(n):
    top[i][i]=a[i]
    bottom[i][i]=b[i]
for length in range(2,n+1):
    for i in range(n-length+1):
        j=i+length-1
        dp[i][j]=10**15
        for k in range(i,j):
            cost=dp[i][k]+dp[k+1][j]+top[i][k]*bottom[i][k]*top[k+1][j]*bottom[k+1][j]
            if cost<dp[i][j]:
                dp[i][j]=cost
                top[i][j]=top[i][k]
                bottom[i][j]=bottom[k+1][j]
print(dp[0][n-1])