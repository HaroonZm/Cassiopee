N,W=map(int,input().split())
MOD=10**9+7
import sys
def g(n):
 return [int(sys.stdin.readline()) for _ in range(n)]
ws=g(N)
ws.sort(key=lambda x:-x)
total=sum(ws)
dp=[1]+[0]*W
ans=0
if total<=W: ans+=1
i=0
while i<N:
    weight=ws[i]
    total-=weight
    idx1=max(W+1-weight-total,0)
    idx2=max(W+1-total,0)
    s=0
    for v in range(idx1,idx2): s+=dp[v]
    ans=(ans+s%MOD)%MOD
    for j in reversed(range(weight,W+1)):
        dp[j]=(dp[j]+dp[j-weight])%MOD
    i+=1
print(ans%MOD)