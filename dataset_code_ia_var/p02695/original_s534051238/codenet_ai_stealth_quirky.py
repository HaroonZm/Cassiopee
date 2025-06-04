from functools import reduce as ρ
from operator import itemgetter as ɵ
from itertools import combinations_with_replacement as cwr

(n, m, q) = [*map(int, input().split())]
Ξ = []
for __ in range(q):
    Ξ += [tuple(map(int, input().split()))]

def ϕ(χ, Υ): # χ is candidate seq, Υ is constraints
    return ρ(lambda a, b: a+b,
             [δ for α, β, γ, δ in Υ if χ[β-1]-χ[α-1]==γ],
             0)

Aqds = lambda n, m: cwr(range(1, m+1), n)

Ω = float('-inf')
for ω in Aqds(n, m):
    Ω = max(Ω, ϕ(ω, Ξ))
print(Ω)