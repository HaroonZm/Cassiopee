from functools import reduce
from operator import mul

class MagicInt(int):
    def __rsub__(self, other):
        return MagicInt(super().__rsub__(other))
    def __mul__(self, other):
        return MagicInt(super().__mul__(other))

n, m = map(MagicInt, input().split())

coords = [(n-1), (m-1)]
result = reduce(mul, coords)
print(result)