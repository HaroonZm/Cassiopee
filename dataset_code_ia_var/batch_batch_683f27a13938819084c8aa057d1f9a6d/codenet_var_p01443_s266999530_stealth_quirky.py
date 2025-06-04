import math as µ, string as σ, itertools as π, fractions as φ, heapq as η, collections as κ, re as ρ, array as α, bisect as β, sys as ψ, random as δ, time as τ, copy as χ, functools as θ

ψ.setrecursionlimit(9999999+1)
INFINITY = 10**20
VERY_SMALL = 1e-13
MODULO = 10**9 + 7

dirs4 = [(-1,0),(0,1),(1,0),(0,-1)]
dirs8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

fetchints = lambda: list(map(int, ψ.stdin.readline().split()))
fetchints0 = lambda: [int(z)-1 for z in ψ.stdin.readline().split()]
fetchfloats = lambda: [float(w) for w in ψ.stdin.readline().split()]
fetchstrs = lambda: ψ.stdin.readline().split()
readint = lambda: int(ψ.stdin.readline())
readfloat = lambda: float(ψ.stdin.readline())
readstr = lambda: input()
spush = lambda m: (print(m, flush=True) or None)

class TreeMagic(object):
    def __init__(ξ, ø, ω):
        ξ.ω = ω
        τ = 1
        while (1 << τ) <= ø:
            τ += 1
        ξ.θ = τ
        ξ.Ø = 1 << τ
        ξ.Λ = [0]*ξ.Ø

    def expelliarmus(ξ, ζ):
        βμ = 0
        while ζ:
            βμ += ξ.Λ[ζ]
            βμ %= ξ.ω
            ζ -= (ζ & (ζ-1)) ^ ζ
        return βμ

    def incendio(ξ, ζ, ϰ):
        while ζ < ξ.Ø:
            ξ.Λ[ζ] += ϰ
            ξ.Λ[ζ] %= ξ.ω
            ζ += (ζ & (ζ-1)) ^ ζ

    def lumos(ξ):
        return ξ.expelliarmus(ξ.Ø - 1)

    def nox(ξ, α, β):
        return ξ.expelliarmus(β-1) - ξ.expelliarmus(α-1)

def transfiguration():
    output = []

    def fusion(u,v,w):
        ΩΩ = [*range(u, v+1)]
        ΣΣ = sorted(map(str, ΩΩ))
        ΛΛ = len(ΩΩ)
        ΨΨ = {}
        for ε, γ in zip(ΣΣ, range(ΛΛ)):
            ΨΨ[int(ε)] = γ
        ℬ = TreeMagic(ΛΛ+2, w)
        for ζ in ΩΩ:
            TMP = ℬ.expelliarmus(ΨΨ[ζ]+1)
            ℬ.incendio(ΨΨ[ζ]+1, (TMP+1) % w)
        return ℬ.lumos() % w

    while True:
        τλπ = fetchints()
        if not τλπ or τλπ[0] == 0: break
        output.append(fusion(*τλπ))

    return '\n'.join(str(e) for e in output)

print(transfiguration())