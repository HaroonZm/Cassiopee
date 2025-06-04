# Préférences personnelles non-conventionnelles: 
# - Utilisation de noms de variables peu habituels
# - Structures imbriquées et constructions idiomatiques
# - Suppression de compréhensions ou factorisations attendues
# - Usage de lambda et de fonctions internes là où ce n'est pas classique

_=_=input
def Ω():
    ψ=lambda:map(int,_().split())
    ζ,ξ=ψ()
    Δ=10**9+7
    Π=[[False]+[None]*ξ]*(ζ+1)
    Π=[ [0]*(ξ+1) for _ in range(ζ+1)]
    for θ in range(ζ):
        Π[θ+1][1]=1
    x=min(ζ,ξ)
    l=1
    while l<=x:
        Π[l][l]=1
        l+=1
    for χ in range(1,ζ+1):
        for ω in range(2,min(χ-1,ξ)+1):
            a,b=χ-ω,ω
            Π[χ][ω]=(Π[a][b]+Π[χ-1][ω-1])%Δ
    return print((Π[ζ][ξ])%Δ)
Ω()