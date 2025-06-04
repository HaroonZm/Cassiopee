from functools import reduce
from operator import mul

n, m = map(int, (__import__('sys').stdin.readline().split()))
a = list(map(int, (__import__('sys').stdin.readline().split())))
b = list(map(int, (__import__('sys').stdin.readline().split())))

f = lambda s: reduce(lambda x, y: x + y, s, 0)
print(reduce(mul, map(f, (a, b)), 1))