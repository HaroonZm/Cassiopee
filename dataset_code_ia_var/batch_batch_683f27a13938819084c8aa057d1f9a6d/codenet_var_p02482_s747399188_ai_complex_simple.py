import operator
from functools import reduce
from itertools import cycle, dropwhile

foo, bar = map(int, raw_input().split())
ops = [
    (operator.gt, lambda: 'a > b'),
    (operator.lt, lambda: 'a < b'),
    (operator.eq, lambda: 'a == b'),
]

print(next(reduce(lambda acc, val: acc if acc is not None else (val[1]() if val[0](foo, bar) else None), ops, None)))