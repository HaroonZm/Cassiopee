p=[]
for i in range(2,1121):
    for j in range(2,int(i**0.5)+1):
        if not i%j:break
    else:p+=[i]
dp=[[0]*1121 for _ in range(15)]
dp[0][0]=1
for x,y in enumerate(p):
    for i in range(min(x+1,14),0,-1):
        for j in range(y,1121):
            dp[i][j]+=dp[i-1][j-y]
while 1:
    n,k=map(int,input().split())
    if n==0:break
    print(dp[k][n])