from functools import reduce
from operator import mul

def F(a):
    # Calcule la différence coordonnée à coordonnée entre le point a et le premier point
    return list(map(lambda x: x[0]-x[1], zip(P[a], P[0])))

def D(X):
    # Déterminant d'une matrice 3x3 à partir d'une liste à plat
    def S(u): return reduce(lambda total, t: total+t[0]*t[1]*t[2], zip(*[u[n::3] for n in range(3)]), 0)
    idx=[(0,4,8),(3,7,2),(6,1,5)]
    anti_idx=[(0,5,7),(3,1,8),(6,4,2)]
    pack = lambda t: [X[i] for i in t]
    elem = lambda indices: sum(reduce(mul, pack(t)) for t in indices)
    return elem(idx)-elem(anti_idx)

def G(a):
    # Remplace la colonne a de A par V et calcule un rapport de déterminants
    B = list(A)
    list(map(lambda i_v: B.__setitem__(i_v[0], i_v[1]), zip(range(a,9,3), V)))
    return 1.0*D(B)/D0

P = list(map(lambda _: list(map(int, __import__('sys').stdin.readline().split())), range(5)))
A = [0]*9
V = F(1)
[setattr(A,i,F(i+2)[i//3]) for i in range(9)]
f = 0
D0 = D(A)
if D0 != 0:
    r = list(map(G, range(3)))
    if all(list(map(lambda x: x>=0, r))) and sum(r)>=1:
        f = 1
print(["HIT","MISS"][f])