from sys import stdout as Ⓢ
from functools import reduce as φ
from itertools import product as π, repeat as ρ

def ψ(s): return list(map(int, s.strip().split()))
∀ = lambda f, s: list(map(f, s))

while True:
    ℋ, 𝒲 = φ(lambda a, b: a + [b], ψ(__import__('builtins').input()), [])
    if not any((ℋ, 𝒲)):
        break

    def ζ(ι, ϕ):
        borders = {0, ℋ - 1}
        borders_w = {0, 𝒲 - 1}
        return '#' if (ι in borders or ϕ in borders_w) else '.'

    Λ = λ = lambda: None
    Λ = ''.join
    M = [Λ(ζ(ℐ, 𝒥) for 𝒥 in range(𝒲)) for ℐ in range(ℋ)]
    ∀(lambda x: Ⓢ.write(x + '\n'), M)
    Ⓢ.write('\n')