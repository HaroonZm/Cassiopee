import numpy as np
from functools import reduce
from operator import add, mul
from collections import Counter
from itertools import product, chain, groupby

n, k = map(int, input().split())

# Création ingénieuse du compteur périodique
x = Counter(map(lambda y: y % k, range(1, n + 1)))
x = dict(map(lambda t: (t, x.get(t, 0)), range(k)))

def triplets(k):
    # Générer les triplets (a, b, c) dans [0, k-1]^3 avec a + b + c ≡ 0 mod k
    return filter(lambda t: sum(t) % k == 0, product(range(k), repeat=3))

# 'ans' par la somme de tous les triplets valides pondérée par leur effectif
ans = sum(reduce(mul, map(x.get, t), 1) for t in triplets(k) if len(set(t)) == 1 or t[1] == (k - t[0]) % k and t[2] == (k - t[0]) % k)

print(ans)