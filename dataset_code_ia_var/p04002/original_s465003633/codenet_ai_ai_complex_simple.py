from functools import reduce
from operator import itemgetter

ψ = lambda: list(map(int, input().split()))
H, W, N = ψ()
Φ = [(H-2)*(W-2)] + [0]*9
Σ = {}
r = range

exec('''for _ in [0]*N:
 α, β = ψ()
 μ = lambda ζ: (α + ζ % 3, β + ζ // 3)
 Ω = (μ(ζ) for ζ in r(9))
 Λ = filter(lambda γ: 1 < γ[0] < H+1 and 1 < γ[1] < W+1, Ω)
 list(map(lambda δ: (Φ.__setitem__(Σ.setdefault(δ,0), Φ[Σ[δ]]-1), 
                    Φ.__setitem__(Σ.__setitem__(δ,Σ[δ]+1), Φ[Σ[δ]+1]+1)), Λ))
''')

print(*Φ)