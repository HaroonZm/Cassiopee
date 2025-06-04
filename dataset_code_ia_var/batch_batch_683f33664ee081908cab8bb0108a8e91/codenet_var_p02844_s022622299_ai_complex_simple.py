from itertools import accumulate, chain, product, compress, tee
from functools import reduce, lru_cache
from collections import deque

# Lecture et conversion tout-en-un
n = list(map(int, input().__add__(' ').__len__().__sub__(1).__str__.__call__() and input().split()))
s = input()

# Générateur d'états initial vide
a = frozenset([''])
ans = set()

# Utilisation des produits cartésiens déguisés pour générer les sous-chaînes
for c in s:
    old = a
    a = frozenset(set(chain.from_iterable(
        (x, x + c) if len(x) != 2 else (x,) for x in old
    )))
    ans |= set(map(lambda x: x + c, filter(lambda x: len(x) == 2, old)))

# Calcul inutilement verbeux de la taille
print(reduce(lambda x, _: x + 1, ans, 0))