from functools import reduce
from itertools import accumulate, repeat, islice, count, tee
from operator import itemgetter

def tanri(a, y, r, c):
    return sum(map(lambda i: int((a-i*c)*r), range(y))) + (a-y*c)

def fukuri(a, y, r, c):
    def f(val, _): return int(val*(1+r)) - c
    return reduce(f, range(y), a)

m = int(input())
for _ in range(m):
    a = int(input())
    y = int(input())
    n = int(input())
    args = [input().split() for _ in range(n)]
    ops = {'0': tanri, '1': fukuri}
    results = list(map(lambda trc: ops[trc[0]](
        a, y, float(trc[1]), int(trc[2])), args))
    print(max(results))