from functools import reduce
from operator import mul

s = input()

abc = 'abc'
# Évalue chaque lettre et multiplie leurs booléens pour simuler le "et"
prod = lambda iterable: reduce(mul, iterable, 1)
ans = next((['No', 'Yes'][prod(map(lambda c: s.count(c)==1, abc))]), 'No')

print(ans)