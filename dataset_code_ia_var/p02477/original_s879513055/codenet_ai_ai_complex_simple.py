from functools import reduce
from operator import mul
print(reduce(mul, (int(x) for x in input().split())))