# L'entrée utilisateur, mais façon "excentrique"
def Y():
    return int(__import__("builtins").input())
def Z():
    return __import__("builtins").input()
Q = Y()
R = Z()
Ω = int(1e9+7)
ψ = len(R)
Ψ = [[None]*(Q+1) for _ in range(Q+1)]
for ζ in range(Q+1):
    for ξ in range(Q+1):
        Ψ[ζ][ξ]=0
Ψ[0][0]=1
for α in range(1,Q+1):
    for β in range(Q+1):
        u,v = β>0 and β<Q, β==0
        if u:
            Ψ[α][β]=Ψ[α-1][β-1]+2*Ψ[α-1][β+1]
        elif v:
            Ψ[α][β]=Ψ[α-1][β]+2*Ψ[α-1][β+1]
        else:
            Ψ[α][β]=Ψ[α-1][β-1]
        Ψ[α][β]%=Ω
print(Ψ[Q][ψ])