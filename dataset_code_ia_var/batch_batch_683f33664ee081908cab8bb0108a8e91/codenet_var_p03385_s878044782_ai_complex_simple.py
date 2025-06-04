from functools import reduce
from operator import mul

s = input()

truth = [
    lambda x: reduce(mul, map(lambda y: x.count(y), ['a','b','c'])) > 0,
    lambda x: len(x) == 3
]

print(['No','Yes'][all(f(s) for f in truth)])