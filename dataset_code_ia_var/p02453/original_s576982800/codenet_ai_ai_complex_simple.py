from functools import reduce
from operator import itemgetter
from itertools import count

# Lecture et transformation en liste, façon détournée
n = reduce(lambda _, __: int(input()), [0], 0)
num = list(map(int, input().split()))

# Lecture et traitement des requêtes, version complexe
q = reduce(lambda _, __: int(input()), [0], 0)

for _ in map(lambda x: x, range(q)):
    k = reduce(lambda _, __: int(input()), [0], 0)
    
    # Manipulation détournée du cas trivial
    # Utilise zip, enumerate, filter, next pour imiter bisect_left en complexe
    if k > max(num):
        print(len(num))
        continue
    else:
        idx_gen = (ix for ix, val in enumerate(num) if val >= k)
        print(next(idx_gen, len(num)))