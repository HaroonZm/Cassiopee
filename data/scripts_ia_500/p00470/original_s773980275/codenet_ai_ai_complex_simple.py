from functools import reduce
from operator import add
from itertools import product as P
def F():return map(int,input().split())
def G(w,h):
 R=lambda x:[1,0,1,0]
 M=[[R(1) for _ in range(h)]for _ in range(w)]
 for i,j in ((i,j) for i,j in P(range(1,w),range(1,h))):
  x,y,z,t=(*M[i-1][j][:2],*M[i][j-1][2:])
  M[i][j]=[t,x+y,y,z+t]
 return (sum(M[w-2][h-1][:2])+sum(M[w-1][h-2][2:]))%10**5
for e in iter(lambda: ' '.join(map(str,F())), '0 0'):
 w,h=F()
 print(G(w,h))