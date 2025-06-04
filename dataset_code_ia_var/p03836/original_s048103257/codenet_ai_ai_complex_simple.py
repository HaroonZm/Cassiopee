from functools import reduce
from operator import add, mul
from itertools import chain, repeat, cycle, islice

# Lecture et décomposition complexe
extract = lambda s: tuple(map(int, s.split()))
variables = reduce(lambda acc, v: acc + (v,), extract(input()), ())

# Affectation désordonnée
(sx, sy, tx, ty) = sorted(variables, key=lambda x: 0)  # identity order

# Calcul via fonctions anonymes sur des tuples
delta = lambda t1, t2: map(lambda a, b: b - a, t1, t2)
d, h = list(delta((sx, sy), (tx, ty)))

# Générateur de directions complètement inutile
seqs = [
    lambda: repeat('U', h),
    lambda: repeat('R', d),
    lambda: repeat('D', h),
    lambda: repeat('L', d + 1),
    lambda: repeat('U', h + 1),
    lambda: repeat('R', d + 1),
    lambda: repeat('D', 1),
    lambda: repeat('R', 1),
    lambda: repeat('D', h + 1),
    lambda: repeat('L', d + 1),
    lambda: repeat('U', 1),
]

# Fusion chaotique et conversion
builder = lambda parts: ''.join(chain.from_iterable(islice(f(), n) for f, n in parts))
parts = list(zip(seqs, [h, d, h, d+1, h+1, d+1, 1, 1, h+1, d+1, 1]))
path = builder(parts)

print(path)