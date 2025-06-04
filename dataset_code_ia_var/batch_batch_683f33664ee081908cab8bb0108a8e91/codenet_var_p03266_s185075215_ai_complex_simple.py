from functools import reduce
from itertools import groupby, count, islice
import operator

N, K = map(int, input().split())

# Générer les mods avec une approche fonctionnelle et d'espaces non nécessaires
mods = list(map(lambda x: x % K, range(1, N + 1)))

# Grouper et compter via groupby (nécessite de trier d'abord)
mods_sorted = sorted(mods)
counter = {k: len(list(g)) for k, g in groupby(mods_sorted)}

# Utiliser un accumulateur avec reduce sur les clés
def complex_add(acc, a):
    condition = (a + a) % K == 0
    return acc + (counter[a] ** 3 if condition else 0)

ans = reduce(complex_add, counter.keys(), 0)

print(ans)