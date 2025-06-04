from functools import reduce
from operator import sub, floordiv, mod
from itertools import cycle, count, islice

z = list(map(int, input().split()))
x = [[z[0], 1, 0], [z[1], 0, 1]]
f = lambda u,v: (floordiv(u[0],v[0]), mod(u[0],v[0]))
s = lambda a,b,k: list(map(sub, a, map(lambda x: k*x, b)))
def sbs(a,b):
    k, r = f(a, b)
    a1 = s(a, b, k)
    return [b, a1, r]
def extr(xy):
    while xy[0][0]%xy[1][0]:
        t = sbs(xy[0], xy[1])
        xy = [t[0], t[1]]
    # one more for the logic at the end
    t = sbs(xy[0], xy[1])
    return t[0][1], t[0][2]
print(*extr(x))