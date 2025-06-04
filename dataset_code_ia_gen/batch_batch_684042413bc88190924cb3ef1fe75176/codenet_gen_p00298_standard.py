N=int(input())
cw=[tuple(map(int,input().split())) for _ in range(N)]
c=[x[0] for x in cw]
w=[x[1] for x in cw]
dp=[float('inf')]*(N+1)
dp[0]=0
for i in range(N):
    sum_w=0
    max_c=0
    for j in range(i,-1,-1):
        sum_w+=w[j]
        max_c=max(max_c,c[j])
        if max_c>=sum_w:
            dp[i+1]=min(dp[i+1],dp[j]+1)
        else:
            break
print(dp[N])