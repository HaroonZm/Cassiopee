from functools import reduce
from operator import mul,add
N,K=map(int,input().split())
S=reduce(lambda s,q:s.__setitem__(q[0]-1,q[1])or s,[tuple(map(int,input().split()))for _ in range(K)],[0]*N)
dp=[0]*9
x=lambda i,j:i*3+j
a,b=S[:2]
dp[:]=((a and b)*[0]*x(~-a,~-b)+(a and not b)*([1]*3+[0]*6)[:x(a,3)]+[0]*(9-x(a,3))+(not a and b)*sum(([int(i/3)==~-b]*3 for i in range(9)),[])+(not a and not b)*[1]*9)
for i in range(2,N):
 z=S[i];cur=z-1;tmp=[0]*9;R=range(3)
 if z:tmp=[sum(dp[k::3])-dp[cur*4]*(k==cur)for k in R for _ in R if _==cur else 0]
 else:
  tmp=[sum(dp[k::3])-dp[cur*4]*(k==cur)for cur in R for k in R]
  tmp=reduce(add,([tmp[i*3+j]for j in R]for i in R))
 dp=tmp[:]
print(sum(dp)%10000)