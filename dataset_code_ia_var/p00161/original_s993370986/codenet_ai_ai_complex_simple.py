from functools import reduce
from operator import add, itemgetter
import sys

g = iter(sys.stdin.readline, '')
while True:
    n = int(next(g).strip())
    if not n: break
    w = lambda z: sum(map(lambda p: p[0]*60 + p[1], zip(*[iter(list(map(int, z[1:])))]*2)))
    data = [(w(tuple(map(int, next(g).split()))), int(next(g).split()[0])) for _ in range(n)]
    data = sorted(((lambda y: (y[0], y[1]))(x) for x in data), key=itemgetter(0))
    f = lambda d, p: print(*map(itemgetter(1), (d[0], d[1], d[-2])), sep='\n')
    f(data, None)