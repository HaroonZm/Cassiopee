from functools import reduce
from operator import add

n = int(__import__('builtins').input())
a = list(map(int, __import__('builtins').input().split()))
_max, _min = reduce(lambda x, y: (x[0] if x[0] > y else y, x[1] if x[1] < y else y), a, (a[0], a[0]))
S = set(range(_min, _max+1))
def cost(m, seq):
    return reduce(add, map(lambda x: (x-m)**2, seq), 0)
costs = (cost(m, a) for m in S)
print(reduce(lambda x, y: x if x < y else y, costs))