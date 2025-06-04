from functools import reduce
from operator import add

def fancy_counter(x, y):
    perms = list(map(lambda i: (i, x[i], y[i]), range(4)))
    hits = sum(map(lambda a: a[1]==a[2], perms))
    blows = sum(map(lambda a: (a[1]!=a[2]) and (a[1] in y), perms))
    return hits, blows

from itertools import count, islice

for _ in iter(lambda:1,0):
    m, n = map(str, raw_input().split())
    if m == "0":
        break
    print(*fancy_counter(m, n))