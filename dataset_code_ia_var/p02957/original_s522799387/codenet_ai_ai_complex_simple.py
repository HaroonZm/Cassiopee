from functools import reduce
from operator import add, mod, floordiv

s = list(map(lambda x: int(x), input().split()))
parity_check = lambda lst: reduce(mod, [reduce(add, lst), 2])
means = lambda lst: reduce(floordiv, [reduce(add, lst), 2])
print([means(s), 'IMPOSSIBLE'][parity_check(s)])