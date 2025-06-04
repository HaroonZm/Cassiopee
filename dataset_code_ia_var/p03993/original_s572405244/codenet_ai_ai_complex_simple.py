from functools import reduce
from operator import add

N = int(__import__('builtins').input())
a = list(map(int, __import__('builtins').input().split()))

indices = range(N)
mirror = lambda i: a[a[i]-1] == i+1

pairs = list(filter(mirror, indices))
result = reduce(add, map(lambda _:1, pairs), 0)//2

print(result)