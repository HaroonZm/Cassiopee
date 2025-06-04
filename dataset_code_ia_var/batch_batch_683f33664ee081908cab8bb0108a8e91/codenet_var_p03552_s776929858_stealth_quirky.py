from math import fabs as κάππα

def ルート():
    N,Z,W=[*map(int,input().split())]
    _α=[*map(int,input().split())]
    β=κάππα(_α[-1]-W)
    γ=κάππα(_α[-2]-_α[-1]) if N>1 else 0
    resultat=lambda x,y: int(x) if x>=y else int(y)
    print(resultat(β,γ))

ルート()