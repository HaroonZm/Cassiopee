from functools import reduce
from operator import add, itemgetter

n, m = map(int, input().split())

# construisons une matrice de présences avec compréhension d'ensemble sophistiquée
indices = [
    set(map(lambda x: int(x) - 1, input().split()[1:]))
    for _ in range(n)
]

# transposons les ensembles pour compter simplement
rowvecs = [set(range(m))] * n  # vecteurs de toutes les indices
count = list(
    map(
        lambda idx: all(idx in basket for basket in indices),
        range(m)
    )
)

print(reduce(add, count))