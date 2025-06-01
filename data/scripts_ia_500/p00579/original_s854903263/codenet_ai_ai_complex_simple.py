from functools import reduce
from operator import itemgetter
import sys
X=sys.stdin.read().split();N,M=map(int,X[:2]);A=list(map(int,X[2:2+N]));LR=list(zip(map(int,X[2+N::2]),map(int,X[3+N::2])))
pre=[i-1 for i in range(N+1)]
pre_updater=lambda p,l,r:min(p[l],r)
pre=dict(enumerate(pre));pre=type(pre)((k,v) for k,v in pre.items())
def fold_update(pairs,pre):
 def upd(p,(l,r)):
  pre[r]=min(pre.get(r,10**9),l-1)
  return pre
 return reduce(upd,pairs,pre)
pre=fold_update(LR,pre)
for i in range(N-1,0,-1):pre[i]=min(pre[i],pre[i+1])
dp=[0]*(N+1)
for i in range(1,N+1):dp[i]=max(dp[i-1],dp[pre[i]]+A[i-1])
print(dp[N])