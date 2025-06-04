import sys
M,N,m0,md,n0,nd=map(int,sys.stdin.read().split())
m=[0]*(M)
n=[0]*(N)
m[0]=m0
for i in range(M-1):
    m[i+1]=(m[i]*58+md)%(N+1)
n[0]=n0
for i in range(N-1):
    n[i+1]=(n[i]*58+nd)%(M+1)
from collections import Counter
cm=Counter(m)
cn=Counter(n)
# Calculate min pairs of carrot type and kiwi type counts
ans=0
for k in cm:
    ans+=min(cm[k],cn.get(k,0))
print(ans)