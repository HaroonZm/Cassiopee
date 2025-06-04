n=int(input())
mod=10**9+7
bt=bin(n)[2:]
k=len(bt)
dp=[[0]*2 for _ in range(k+1)]
dp[0][0]=1
dp[0][1]=1
for i in range(k):
    j=int(bt[k-i-1])
    if j==0:
        a,b,c=1,0,0
        d,e,f=1,1,1
    else:
        a,b,c=1,1,0
        d,e,f=0,1,2
    dp[i+1][0]=(a*dp[i][0]+b*dp[i][1]+c*pow(3,i,mod))%mod
    dp[i+1][1]=(d*dp[i][0]+e*dp[i][1]+f*pow(3,i,mod))%mod
print(dp[k][0])