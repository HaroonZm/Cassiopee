import sys
input=sys.stdin.readline

M,N=map(int,input().split())
P=[int(input()) for _ in range(M)]
boxes=[tuple(map(int,input().split())) for _ in range(N)]

P.sort(reverse=True)

dp=[float('-inf')]*(M+1)
dp[0]=0
for c,e in boxes:
    for i in range(M-c,-1,-1):
        val=sum(P[i:i+c]) - e
        if dp[i]+val>dp[i+c]:
            dp[i+c]=dp[i]+val

print(max(0,max(dp)))