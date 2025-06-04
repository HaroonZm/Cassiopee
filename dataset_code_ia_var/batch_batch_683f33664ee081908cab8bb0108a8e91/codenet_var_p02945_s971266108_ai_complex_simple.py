from functools import reduce
from operator import add, sub, mul

A, B = map(int, input().split())
ops = [add, sub, mul]

res = reduce(lambda x, y: x if x > y else y, map(lambda f: f(A, B), ops))
print(res)