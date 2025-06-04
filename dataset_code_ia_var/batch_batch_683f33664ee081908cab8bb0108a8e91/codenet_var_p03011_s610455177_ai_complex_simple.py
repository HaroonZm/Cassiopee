import itertools
import functools
import operator

a = list(map(int, input().split()))
*_, m = sorted((v, i) for i, v in enumerate(a))
idx = m[1]
b = (x for i, x in enumerate(a) if i != idx)
print(functools.reduce(operator.add, b, 0))