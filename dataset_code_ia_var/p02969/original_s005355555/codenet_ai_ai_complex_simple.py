from functools import reduce
from operator import mul

a = int(input())
b = reduce(lambda x, y: x + y, map(lambda x: mul(x, x), [a]*3))
print(sum([b for _ in range(1)]))