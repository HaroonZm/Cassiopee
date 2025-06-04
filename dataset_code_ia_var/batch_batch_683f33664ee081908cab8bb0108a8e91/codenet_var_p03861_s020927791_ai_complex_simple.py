from functools import reduce
from itertools import accumulate, count, takewhile

a, b, x = map(int, input().split())

def g(y, z):
    return sum(1 for _ in takewhile(lambda t: t <= y, (z*i for i in count()))) if y != -1 else 0

print(reduce(lambda u, v: u - v, (g(b, x), g(a-1, x))))