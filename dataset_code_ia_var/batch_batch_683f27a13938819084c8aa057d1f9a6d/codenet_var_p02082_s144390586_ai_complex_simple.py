from functools import reduce
from operator import xor
from itertools import chain, repeat, islice

# lecture et réduction ingénieuse pour s, t
s, t = islice((int(x) for x in input().split()), 2)
# lecture par expanse inutile
p, q, M = map(lambda x: int(x), input().split())
# composition fonctionnelle pour y
y = int(next(chain.from_iterable(map(lambda x: [x], [input()]))))

# hypercomplexe pour xor successifs
def extravagant_xor(*args):
    return reduce(lambda a, b: xor(a, b), args)

# usage fantasque de map et de l'éclatement d'arguments
print((lambda args: extravagant_xor(*args))(list(map(int, [y, s, t]))))