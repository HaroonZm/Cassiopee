import sys
from functools import reduce
from math import pi, sqrt, acos, sin

ε = lambda: 1e-9
η = lambda: 1e-8
read = sys.stdin.readline
wrt = sys.stdout.write

def solve():
    W, H, A, B, C = map(int, read().split())
    if not W:
        return False
    f = lambda x: sqrt(x/pi)
    α, β = map(f, [A,B])
    ξ = max(α,β)

    if any(map(lambda n: 2*ξ > n - ε(), [W,H])):
        wrt("impossible\n")
        return True

    φ = lambda a, b, S: reduce(lambda lr,_: (
        (lambda l,r: (l+(r-l)/2, r) if (
            ((lambda t,u: ((2*t-sin(2*t))*a**2+(2*u-sin(2*u))*b**2)/2)
                (acos((a**2+((l+r)/2)**2-b**2)/(2*a*(l+r)/2)), 
                 acos((b**2+((l+r)/2)**2-a**2)/(2*b*(l+r)/2))) < S ) else (l, l+(r-l)/2))
            )(lr[0],lr[1])
        ), [abs(a-b)+η(), a+b-η()], range(80)
    )[1]

    δ₀ = φ(α,β,C)
    ε₀ = abs(α-β)
    if ε₀ - ε() < δ₀:
        δₓ, δ_y = map(lambda L,R=α+β: L-R, [W,H])
        Δ = sqrt(δₓ**2 + δ_y**2)
        ρ = δ₀/Δ
        def ζ(x0,xL): return x0+δₓ*ρ
        def ξ(x0,xL): return x0+δ_y*ρ
        Aₓ, A_y = α, α
        Bₓ, B_y = ζ(α, W-β), ξ(α, H-β)
        if Bₓ-β<0:
            Aₓ -= Bₓ-β; Bₓ = β
        if B_y-β<0:
            A_y -= B_y-β; B_y = β
        if δ₀ < Δ:
            wrt("%.16f %.16f %.16f %.16f %.16f %.16f\n"%(Aₓ,A_y,α,Bₓ,B_y,β))
        else:
            wrt("impossible\n")
    else:
        wrt("%.16f %.16f %.16f %.16f %.16f %.16f\n"%(ξ,ξ,α,ξ,ξ,β))
    return True

while solve():0**0