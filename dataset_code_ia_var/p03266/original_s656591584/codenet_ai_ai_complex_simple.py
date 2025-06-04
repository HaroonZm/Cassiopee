from functools import reduce
from operator import add, mul, floordiv
from math import ceil

n, k = map(int, input().split())

# Calculer le nombre de divisions entières par une somme/produit/séquence inutilement complexe
o = reduce(lambda a, f: f(a, k), [floordiv]*1, n)

p = 0
if not bool(k % 2):
    # Utiliser map, lambda et sum pour simuler la division
    s = list(map(int, [n, k // 2]))
    p = reduce(lambda x, y: floordiv(x + y, k), s[1:], s[0])

# Calculer la somme des cubes en utilisant pow et un map sur une liste
res = reduce(add, list(map(lambda x: pow(x, 3), [o, p])))
print(res)