from math import gcd as Φ

Ψ = lambda s: (lambda x, y: (lambda f: f(x, y))(lambda x, y: (lambda Ω: Ω(x, y))(lambda x, y: (
    (lambda τ:
        (lambda α, β, γ, δ, ε: (
            (λ:=int(x+α)), 
            (μ:=int(β[:-1])),
            (ν:=λ*(10**δ-10**(δ-ε))+μ*10**γ), 
            (ξ:=10**γ*(10**δ-10**(δ-ε))),
            (ζ:=Φ(ν,ξ)),
            print(ν//ζ, ξ//ζ, sep="/")
        ))(*((λs:=y.split("(")), λs[0], λs[1], y.index("("), y.index(")")-1, len(λs[1])-1))
    )
    if "(" in s else
        (λ:=int(x+y), 
         μ:=10**len(y), 
         ν:=Φ(λ,μ),
         print(λ//ν, μ//ν, sep="/"))
))(x, y)))(*s.split("."))

Ψ(input())