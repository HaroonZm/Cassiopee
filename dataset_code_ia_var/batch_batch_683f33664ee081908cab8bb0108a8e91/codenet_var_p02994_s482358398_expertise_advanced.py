from functools import reduce
from operator import add

n, l = map(int, input().split())
flavors = [l + i for i in range(n)]
excluded = min(flavors, key=abs)
result = reduce(add, flavors) - excluded
print(result)