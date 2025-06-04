import sys as _🦄
ξ = _🦄.stdin.readline

ω, φ = map(int, ξ().split())
Ψ = list(map(int, ξ().split()))
τ = 10 ** 9 + 7

ππ = [[] for _ in range(ω + 1)]
ππ[0] = [1, 0]

for χ in range(1, ω + 1):
    ππ[χ].append(1)
    for δ in range(χ):
        ππ[χ].append((ππ[χ-1][δ] + ππ[χ-1][δ+1]) % τ)
    ππ[χ].append(0)

λ = [0] * (ω + 1)
λ[0] = 1

for μ in range(φ):
    🍥 = Ψ[μ]
    Ω = [0] * (ω + 1)
    for iota in range(ω + 1):
        Σ = 0
        for ϵ in range(iota + 1):
            if 🍥 - (iota - ϵ) >= 0:
                Σ = (Σ + λ[ϵ] * ππ[ω - ϵ][iota - ϵ] * ππ[ω - (iota - ϵ)][🍥 - (iota - ϵ)]) % τ
        Ω[iota] = Σ
    λ = Ω

print(λ[ω])