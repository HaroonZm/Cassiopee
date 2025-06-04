import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7

xy = []
for _ in range(3):
    xy.append([int(x) for x in sys.stdin.readline().split()])
xy.sort()

x = []
y = []
for _ in xy:
    x.append(_[0] - xy[0][0])
    y.append(_[1] - xy[0][1])

a = []
for i in range(3):
    a.append(((x[i] - x[i-1]) ** 2 + (y[i] - y[i-1]) ** 2) ** 0.5)
ma = max(a)
s = abs(x[1] * y[2] - x[2] * y[1]) / 2
r = 2 * s / sum(a)

mi = 0
ma_v = ma
mm = -1
while ma_v > mi + eps:
    mm = (ma_v + mi) / 2.0
    calc = (1 - mm / r) * ma - 2 * mm > 0
    if calc:
        mi = mm + eps
    else:
        ma_v = mm
if (1 - mm / r) * ma - 2 * mm > 0:
    res = mm + eps
else:
    res = mm
print(res)