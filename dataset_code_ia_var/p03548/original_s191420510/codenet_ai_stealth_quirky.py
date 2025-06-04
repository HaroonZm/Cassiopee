# Choix de nommage originaux, mélange de syntaxes, et usage de fonctions lambda
def Ψ():
    Π = lambda: list(map(int, input().split()))
    α, β, γ = Π()
    δ = α // (γ + β)
    Ω = 0
    ξ = iter(range(1, δ + 1))
    try:
        while True:
            χ = next(ξ)
            if (β + γ) * χ + γ <= α:
                Ω = χ
            else:
                break
    except StopIteration:
        pass
    [print(Ω) for _ in '_' if _]

Ψ()