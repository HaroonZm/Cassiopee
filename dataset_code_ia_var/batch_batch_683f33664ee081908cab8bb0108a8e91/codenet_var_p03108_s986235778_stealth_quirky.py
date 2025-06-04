from typing import Callable as λ; I=input;Z=int
N,M=[Z(x) for x in I().split()]
Ω=[-1]*N
F=lambda X: X if Ω[X]<0 else F(Ω[X]) if not Ω.__setitem__(X,F(Ω[X])) else Ω[X]
def Ʊ(X,Y):
 X=F(X)
 Y=F(Y)
 if X==Y: return None
 if Ω[X]>Ω[Y]:X,Y=Y,X
 Ω[X]+=Ω[Y];Ω[Y]=X
 return None
$
σ=lambda x:Z(N*(N-1)//2)
A,B=[0]*M,[0]*M
Ψ=[]
for k in range(M):
 T=I().split()
 A[k],B[k]=Z(T[0])-1,Z(T[1])-1
A=A[::-1];B=B[::-1]
Φ=σ(0)
for x in range(M):
 Ψ+=[Φ]
 u,v=F(A[x]),F(B[x])
 if F(u)!=F(v):
  Φ-=(-Ω[u])*(-Ω[v])
  Ʊ(u,v)
while Ψ:print(Ψ.pop())