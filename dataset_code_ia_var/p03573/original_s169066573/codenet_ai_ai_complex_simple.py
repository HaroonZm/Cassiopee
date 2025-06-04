from functools import reduce
from operator import xor

A, B, C = map(int, input().split())
print(reduce(lambda x, y: xor(x, y), {A, B, C} * 2))