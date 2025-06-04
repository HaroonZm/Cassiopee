from functools import reduce, partial
from operator import itemgetter, add, sub, mul
import sys
import itertools as it

φ = lambda x, y, z: (sub(*map(itemgetter(0), (y, z))) * sub(*map(itemgetter(1), (z, x))) 
                     - sub(*map(itemgetter(1), (y, z))) * sub(*map(itemgetter(0), (z, x))))

δ = sys.stdin.readline
ω = sys.stdout.write

def ψ():
    Λ = int(δ())
    Σ = {}
    for _ in map(lambda _:_, range(Λ)):
        κ, ν = map(int, δ().split())
        Σ.setdefault(κ, []).append(ν)
    Ω = sorted(Σ.items(), key=itemgetter(0))
    
    def α(Ω, ξ):
        Π, Θ = [], []
        ζ = 0
        Υ = [0]
        for χ, ς in Ω:
            (lambda s : s.sort(reverse=ξ))(ς)
            for υ in ς:
                π = (χ, υ)
                while len(Π) > 1 and φ(Π[-2], Π[-1], π) <= 0:
                    ζ += abs(φ(Π[-2], Π[-1], π))
                    Π.pop()
                Π += [π]
                while len(Θ) > 1 and φ(Θ[-2], Θ[-1], π) >= 0:
                    ζ += abs(φ(Θ[-2], Θ[-1], π))
                    Θ.pop()
                Θ += [π]
            Υ.append(ζ)
        return Υ
    
    β = α(Ω, 0)
    Ω = Ω[::-1]
    γ = α(Ω, 1)
    η = len(Ω)
    ξ = min(map(add, β, γ[::-1]))
    ω("%d\n" % ((ξ+1)//2))
ψ()