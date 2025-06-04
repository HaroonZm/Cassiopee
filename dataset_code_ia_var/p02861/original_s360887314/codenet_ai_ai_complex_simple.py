from functools import reduce
from itertools import combinations,repeat
from operator import add
from math import hypot

n = int(input())
xy = [list(map(int, input().split())) for _ in repeat(None, n)]

pairs = list(combinations(xy, 2))
dists = list(map(lambda p: hypot(*(map(lambda ab: ab[0] - ab[1], zip(*p)))), pairs))
total = reduce(add, dists, 0)

print(total / (reduce(lambda a, b: a * b, (n, n - 1)) // 2) * (n - 1))