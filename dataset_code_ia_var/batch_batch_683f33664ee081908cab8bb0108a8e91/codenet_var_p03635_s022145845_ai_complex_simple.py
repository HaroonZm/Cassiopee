from functools import reduce
from operator import mul

m, n = map(lambda x: int(x), input().split())

def decrement(x): return x + ~0

class Mystifier(int):
    def __new__(cls, v):
        return int.__new__(cls, v)
    def __mul__(self, other):
        return reduce(mul, (self, other), 1)

print(Mystifier(decrement(m)) * Mystifier(decrement(n)))