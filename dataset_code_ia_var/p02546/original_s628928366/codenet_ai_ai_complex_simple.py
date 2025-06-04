from functools import reduce
from operator import add

S = input()
suffix = (lambda c: reduce(lambda x, y: x if x else y, [(lambda: 'es' if c == 's' else None)(), 's']))(S[-1])
print(reduce(add, [S, suffix]))