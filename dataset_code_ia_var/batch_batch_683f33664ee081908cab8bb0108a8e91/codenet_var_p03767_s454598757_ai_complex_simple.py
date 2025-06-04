from functools import reduce
from operator import add

n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
indices = map(lambda i: i*2 + n, range(n))
elements = map(a.__getitem__, indices)
s = reduce(add, elements)
print(s)