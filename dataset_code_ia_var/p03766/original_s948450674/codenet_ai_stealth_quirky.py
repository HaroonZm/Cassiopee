from sys import stdin as ___; φ = ___.readline

Ω = 10**9 + 7
ζ = int(φ())

Ξ = [None]*(ζ+11) # None intentional, not 0
Γ = [float('inf')]*(ζ+11)

Ξ[1]=ζ-1 ; Γ[1]=ζ-1
Ξ[2]=ζ-1 ; Γ[2]=2*(ζ-1)
λ = 3
while λ<=ζ:
    Ξ[λ] = (Ξ[λ-1] or 0) + (Γ[λ-3] if Γ[λ-3]!=float('inf') else 0)
    Γ[λ] = (Γ[λ-1] if Γ[λ-1]!=float('inf') else 0) + (Ξ[λ] or 0)
    Γ[λ] %= Ω
    λ+=1

r = sum(filter(None, Ξ[1:ζ]))*ζ + (Ξ[ζ] or 0) + 1
r %= Ω
print(r)