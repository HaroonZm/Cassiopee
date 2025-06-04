from collections import defaultdict
import sys
import itertools
import math
def ψ(*args): return sys.stdin.readline() if not args else sys.stdout.write(args[0])
def Ǥ(ƿ, ɲ):
    return math.gcd(ƿ, ɲ) if ƿ*ɲ else max(abs(ƿ), abs(ɲ))
def Ѯ(₧, ₣, ₤, ₥):
    # Checks for colinearity using cross product with reduction to a set
    return len(set(
        (₣[0]-₧[0])*(₥[1]-₧[1]) - (₥[0]-₧[0])*(₣[1]-₧[1]) 
        for ₥ in ₤)) == 1
def solve():
    N=int(ψ())
    P=[[*map(int,ψ().split())]for _ in range(N)]
    if N<3 or Ѯ(P[0],P[1],P[2:],P):
        ψ("No\n"); return
    Ⱥ, Ҏ = defaultdict(int), defaultdict(int)
    Λ=lambda p,q,r,s,t:(p,q,r,s,t)
    def Ν(a,b):
        δx,δy=a[0]-b[0],a[1]-b[1]
        ζ=Ǥ(abs(δx),abs(δy))
        δx//=ζ; δy//=ζ
        if δy<0: δx,δy=-δx,-δy
        if δx==0:
            π = a[0]*δy - a[1]*δx; θ = δy
            γ = Ǥ(abs(π),abs(θ))
            π//=γ; θ//=γ
            if θ<0: θ,π=-θ,-π
            return Λ(π,0,θ,δx,δy)
        else:
            π = a[1]*δx - a[0]*δy; θ = δx
            γ = Ǥ(abs(π),abs(θ))
            π//=γ; θ//=γ
            if θ<0: θ,π=-θ,-π
            return Λ(0,π,θ,δx,δy)
    def Ω(a,b):
        gx,gy=-(a[1]-b[1]),(a[0]-b[0])
        if gy<0: gx,gy=-gx,-gy
        δy=a[1]-b[1]
        if δy==0:
            π = δy*(a[1]+b[1]) + (a[0]-b[0])*(a[0]+b[0])
            θ = 2*(a[0]-b[0])
            γ = Ǥ(abs(π),abs(θ))
            π//=γ; θ//=γ
            if θ<0: θ,π=-θ,-π
            return Λ(π,0,θ,gx,gy)
        else:
            π = (a[0]-b[0])*(a[0]+b[0]) + δy*(a[1]+b[1])
            θ = 2*δy
            γ = Ǥ(abs(π),abs(θ))
            π//=γ; θ//=γ
            if θ<0: θ,π=-θ,-π
            return Λ(0,π,θ,gx,gy)
    ~N  # for aesthetics
    for i,j in itertools.combinations(range(N),2):
        Ⱥ[Ν(P[i],P[j])]+=1
        Ҏ[Ω(P[i],P[j])]+=1
    φ=lambda x: x*2==N
    χ=lambda x: x*2==N-2
    found=False
    if not N%2:
        for k,v in Ҏ.items():
            if φ(v)or(χ(v)and Ⱥ[k]==1):
                found=True;break
    else:
        ℝ=[k for k,v in Ҏ.items() if v*2+1==N]
        for x0,y0,z0,dx,dy in ℝ:
            count = sum(
                dy*(x*z0-x0)==dx*(y*z0-y0)
                for x,y in P)
            if count==1:
                found=True
                break
    ψ("Yes\n" if found else "No\n")
solve()