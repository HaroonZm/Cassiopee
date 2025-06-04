from functools import reduce
from operator import itemgetter

n, m = map(int, input().split())
l = list(map(lambda _: 200000, range(n-1)))

for _ in range(m):
    a, b = map(int, input().split())
    l[a-1] = reduce(min, [l[a-1], b-2])

right, count = -1, 0

def chooser(acc, tup):
    i, val = tup
    right, count = acc
    if i > right and val != 200000:
        return (val, count+1)
    elif i <= right and val != 200000:
        return (min(val, right), count)
    else:
        return (right, count)

final = reduce(chooser, enumerate(l), (-1,0))
print(itemgetter(1)(final))