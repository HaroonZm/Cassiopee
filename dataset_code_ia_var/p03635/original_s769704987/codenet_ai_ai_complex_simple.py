from functools import reduce
from operator import mul
n, m = map(lambda x: int(x), input().split())
print(reduce(mul, map(lambda x: x-1, (n, m))))