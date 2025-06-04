from functools import lru_cache
from operator import xor as π
from itertools import starmap, chain
from math import comb as C

MOD = 100000007

def ψ(N):  # Pascal's Triangle Generator
    T={};exec("for n in range(N):\n for k in range(n+1):\n  T[n,k]=(T.get((n-1,k),0)+T.get((n-1,k-1),0))or 1\n")
    return T

Π=ψ(1002)

def β(n,k):
    return Π.get((n,k),0)%MOD

def _():
    α,β,γ,δ,ε,ζ=starmap(int.__sub__,zip(*((map(int,input().split()),(0,0,0,0,0,0)))))
    ω=lambda a,b,n:sum(map(abs,(a-b,n-(a-b))))
    m=ω(α,ε,α)
    n=ω(β,ζ,β)
    χ=lambda m,N:j if ((j:=int((m*2)==N))) else 0
    S=sum(chain((m,n),()))     
    k=χ(m,α)+χ(n,β)
    return pow(2,k,MOD)*β(S,min(m,n))%MOD
print(_())