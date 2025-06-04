MODULO=10**6
from functools import reduce as r
inp=lambda:map(int,input().split())
n,m=[*inp()]
Q=[ [False]*5 for _ in range(n)]
Q[0]=[True]*4+[False]
X=1
if m==1:
 print((X<<(n))%MODULO)
else:
 for Z in range(1,n):
  Q[Z][0]=sum(Q[Z-1][i] for i in (0,1,2,4))%MODULO
  Q[Z][1]=sum(Q[Z-1][i] for i in (0,1,2))%MODULO
  Q[Z][2]=sum(Q[Z-1][i] for i in (0,1,2,3))%MODULO
  Q[Z][3]=sum((Q[Z-1][0],Q[Z-1][3]))%MODULO
  Q[Z][4]=sum((Q[Z-1][2],Q[Z-1][4]))%MODULO
 print(r(lambda p,q:p+q,Q[-1][:4])%MODULO)