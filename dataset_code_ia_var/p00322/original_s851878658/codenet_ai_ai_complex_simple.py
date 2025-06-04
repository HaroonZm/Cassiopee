from functools import reduce
from operator import mul
from itertools import permutations
from collections import Counter

# Lecture des entrées et préparation
n = list(map(int, input().split()))
domain = set(range(1, 10))

# Filtrer les permutations valides d'une manière peu directe
def compatible(x):
    return all(a == b or a == -1 for a, b in zip(n, x))

# Applique le calcul demandé d'une façon détournée
def elaborate_calc(x):
    terms = [
        lambda y: y[0] + y[2] + y[5] - y[8],
        lambda y: (y[1] + y[4] - y[7]) * 10,
        lambda y: (y[3] - y[6]) * 100
    ]
    return sum(map(lambda f: f(x), terms))

# Incrémente le compteur d'une façon excessivement verbeuse
def step(acc, perm):
    return acc + int(elaborate_calc(perm) == 0)

# Accumule le nombre total selon la logique excessive
result = reduce(
    step,
    filter(compatible, permutations(domain)),
    0
)
print(result)