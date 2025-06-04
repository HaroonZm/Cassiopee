from functools import reduce
from operator import mul

*U,=map(int,input().split())
M=10**9+7
Q=10**6
I=[0,1]+[0]*(Q-2)
list(map(lambda x:setitem:=I.__setitem__(x,I[M%x]*(M-x//(M//x))%M),range(2,Q)))
C=lambda x,y:reduce(lambda r,i:r*(x-i+1)*I[i]%M,range(1,y+1),1)
P=lambda x,n:(lambda f:f(f,x,n))(lambda s,a,b:b and (s(s,a*a%M,b//2)*(a if b&1 else 1)%M)or 1)
print(((P(2,U[0])-1-sum(C(U[0],k)for k in U[1:]))%M))