T, __ = [], lambda *args: None
exec("for _____ in range(3):T+=[[*map(int, input().split())]]")
def Δ(x,y): return (x-y) if x>=y else 60-(y-x)
for z in T:
    a, b, c, d, e, f = z
    S=Δ(f,c); E=e-(b+(1 if f<c else 0)); H=d-(a+(1 if f<c or e<b else 0))
    S = S if f>=c else S
    M = Δ(e, b) if f>=c else Δ((e-1), b)
    H = H if e>=b or f>=c else H-1
    print(H, M, S)