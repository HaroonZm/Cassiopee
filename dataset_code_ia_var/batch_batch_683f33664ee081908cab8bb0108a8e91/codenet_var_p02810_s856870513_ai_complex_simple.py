from functools import reduce
from operator import itemgetter,add
import sys

sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline()

N,X=map(int,input().split())
L=sorted(map(int,input().split()),reverse=True)
mod=10**9+7

G=lambda d=None: [[0]*(X+1) for _ in range(N//2+2 if d is None else N//2+1)]
D=G();D[1][L[0]]=1

for l in L[1:]:
    ND=G(1)
    idx=lambda _n:filter(lambda z:z[2]>0,((_c,_s,D[_c][_s]) for _c in range(1,N//2+1) for _s in range(X+1)))
    for c,s,k in idx(None):
        ψ= lambda f,*a,**ka: f(*a,**ka)
        T=lambda a,b,v: ND[a][b].__setitem__(slice(None),[(ND[a][b]+v)%mod])
        ζ=min
        if s+l+c<=X and c+1<=N//2:ψ(T,c+1,s+l,k*(c+1))
        ψ(T,c,s,k*(s-c*(l-1)))
        list(map(lambda i:ψ(T,c,s+i,k*2*c),range(1,ζ(X-s-c+2,l+1))))
        if c==1:continue
        list(map(lambda i:ψ(T,c-1,s+i,k*(c-1)*(l-i+1)),range(1,ζ(X-s-c+3,l+1))))
    D=ND

print(reduce(add,D[1][X:X+1]))