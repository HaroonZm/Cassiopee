from functools import reduce
from operator import add
print(reduce(add, list(map(lambda x: int(x), input().split())), 0))