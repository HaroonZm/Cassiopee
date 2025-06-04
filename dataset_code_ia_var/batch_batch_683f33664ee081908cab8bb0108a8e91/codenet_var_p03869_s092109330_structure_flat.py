import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7

xy = []
for _ in range(3):
    xy.append([int(x) for x in sys.stdin.readline().split()])
xy.sort()
x = [xy[i][0] - xy[0][0] for i in range(3)]
y = [xy[i][1] - xy[0][1] for i in range(3)]
s = abs(x[1]*y[2] - x[2]*y[1]) / 2
a = [((xy[i][0] - xy[i-1][0])**2 + (xy[i][1] - xy[i-1][1])**2) ** 0.5 for i in range(3)]
r = 2 * s / sum(a)
ma = max(a)

mi = 0
maval = ma
mm = -1.0
def f(i):
    return (1-i/r) * ma - 2*i > 0

while maval > mi + eps:
    mm = (maval+mi) / 2.0
    if f(mm):
        mi = mm + eps
    else:
        maval = mm
if f(mm):
    print(mm + eps)
else:
    print(mm)