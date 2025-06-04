from functools import reduce
from operator import add

n, h, w = map(int, input().split())
l = [tuple(map(int, input().split())) for _ in range(n)]
ans = reduce(add, map(lambda t: ((h <= t[0]) & (w <= t[1])), l))
print(ans)