from functools import reduce
from operator import mul

ＭＯＤ＝10**8+7
Ｎ＝1001

def comb(x, y):
    # Utilise de la programmation fonctionnelle et manipulation avancée de listes pour la symétrie
    mirror = (lambda a, b: (a, b) if 2*b <= a else (a, a-b))
    xx, yy = mirror(x, y)
    return (FAC[xx] * INV[yy] % ＭＯＤ) * INV[xx-yy] % ＭＯＤ

# Génère les factoriels via reduce dans une seule ligne
FAC = [1] + list(reduce(lambda acc, i: acc+[acc[-1]*i%ＭＯＤ], range(1, Ｎ+1), [1]))[1:]
# Inverses en utilisant des listes en compréhension acrobatique
INV = [1 for _ in range(Ｎ+1)]
INV[-1] = pow(FAC[-1], ＭＯＤ-2, ＭＯＤ)
[INV.__setitem__(i, INV[i+1]*(i+1)%ＭＯＤ) for i in range(Ｎ-1, 1, -1)]

parameters = tuple(map(int, input().split()))
r, c, a1, a2, b1, b2 = parameters

# Point fixe et map pour le min, tuple unpacking
row, col = map(lambda abk: min(abs(abk[0]-abk[1]), abk[2]-abs(abk[0]-abk[1])), [(b1, a1, r), (b2, a2, c)])

# Produit des facteurs conditionnels via une expression booléenne convertie en int
bonuses = (row*2 == r) + (col*2 == c)
ans = pow(2, bonuses) * comb(row+col, row) % ＭＯＤ

print(ans)