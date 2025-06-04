from itertools import product as Π

S = input()
N = len(S) - 1

Ω = 0
Σ = list(Π(('+',''), repeat=N))
Ξ = lambda expr: eval(expr)

κ = 0
while κ < len(Σ):
    Φ = [S[0]]
    for π, σ in zip(Σ[κ], S[1:]):
        Φ.append(π)
        Φ.append(σ)
    expr = ''.join(Φ)
    Ω += Ξ(expr)
    κ += 1

print(Ω)