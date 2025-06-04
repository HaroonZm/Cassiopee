MOD=10**9+7
N,L=map(int,input().split())
x=list(map(int,[input() for _ in range(N)]))
a=list(map(int,[input() for _ in range(N)]))
min_pos=[0]*N
max_pos=[0]*N
min_pos[0]=x[0]
for i in range(1,N):
    min_pos[i]=max(min_pos[i-1]+1,x[i])
max_pos[-1]=x[-1]+a[-1]*( (L-1 - x[-1])//a[-1] if a[-1]>0 else 0 )
for i in range(N-2,-1,-1):
    if a[i]==0:
        max_pos[i]=x[i]
    else:
        max_move=(max_pos[i+1]-1 - x[i])//a[i]
        max_pos[i]=x[i]+max_move*a[i]
        if max_pos[i]<min_pos[i]:
            print(0)
            exit()
dp=[[0]*(L+1) for _ in range(N+1)]
dp[0][0]=1
for i in range(N):
    prefix=[0]*(L+2)
    for pos in range(min_pos[i],max_pos[i]+1,a[i] if a[i]>0 else 1):
        prefix[pos+1]=(prefix[pos]+dp[i][pos])%MOD
    for pos in range(L+1):
        left=min_pos[i]
        right=max_pos[i]
        if pos<left or pos>right or (pos - x[i])% (a[i] if a[i]>0 else 1)!=0:
            dp[i+1][pos]=0
        else:
            dp[i+1][pos]=prefix[pos+1]-prefix[pos]
            dp[i+1][pos]%=MOD
    for pos in range(min_pos[i],max_pos[i]):
        dp[i+1][pos+1]+=dp[i+1][pos]
        dp[i+1][pos+1]%=MOD
res=0
for pos in range(L+1):
    res=(res+dp[N][pos])%MOD
print(res)