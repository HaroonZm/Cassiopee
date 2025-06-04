import sys

class Something:
 def __init__(self, GGG):self.X=GGG+1;self.A=[0]*self.X;self.B=[0]*self.X
 def _A(self,ARR,k,V):
  k+=1
  while k<self.X:ARR[k]+=V;k+=k&-k
 def _B(self,B,k):
  k+=1;z=0
  while k:z+=B[k];k-=k&-k
  return z
 def f(self,a,b,c):
  self._A(self.A,a,-c*(a-1));self._A(self.A,b,c*(b-1));self._A(self.B,a,c);self._A(self.B,b,-c)
 def g(self,a,b):
  return self._B(self.B,b-1)*(b-1)+self._B(self.A,b-1)-self._B(self.B,a-1)*(a-1)-self._B(self.A,a-1)

sys.setrecursionlimit(1000000000)
INF=float("inf")
MOD=10**9+7
get=lambda:sys.stdin.readline().strip()
int1=lambda: int(get())
mpI=lambda : map(int, get().split())
def LIST(n=None):return list(mpI()) if n is None else [int1() for _ in range(n)]
y=lambda:print('Yes')
n=lambda:print('No')
Y=lambda:print('YES')
N=lambda:print('NO')
def L2(a,b,k):return [[k]*b for _ in range(a)]
def L3(a,b,c,v):return [[[v]*c for __ in range(b)] for _ in range(a)]
def CEIL(x,y=1):return int(-(-x//y))
def L4(a,b,c,d,e):return [[[[e]*d for _ in range(c)] for __ in range(b)] for _ in range(a)]

A,B=[*mpI()]
F=Something(A+1)
for _ in range(B):
 c,*val=mpI()
 if not c:
  s,t,x=val
  F.f(s,t+1,x)
 else:
  s,t=val
  print(F.g(s,t+1))