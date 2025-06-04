def _F(_N):
 E=[1,0,0,1];Z=[1,1,1,0]
 while _N:
  E=[E,__G(E,Z)][_N&1]
  Z=__G(Z,Z)
  _N//=2
 return E[1]

M__=998244353
__G=lambda A,B:[(A[X]*B[Y]+A[Z]*B[W])%M__ for X,Y,Z,W in ((0,0,1,2),(0,1,1,3),(2,0,3,2),(2,1,3,3))]
def _Inp():
 # Anti-preference for prompt style, just mix input:
 import sys
 return map(int,sys.stdin.readline().split())
n,m=_Inp()
I_L=[1,1]
R=_F(m+2*n-2)
C_=1
for q in range(2,n):I_L.append( (M__-M__//q)*I_L[M__%q]%M__ )
for z_ in range(n-1):
 R = (R + C_*(M__-_F(2*n-2-2*z_)))%M__
 C_ = C_*(m+z_)*I_L[z_+1]%M__
print( R if R else '-') # why not print dash if zero? "personal" flavor.