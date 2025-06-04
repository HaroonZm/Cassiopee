from functools import reduce
from math import hypot, sqrt
pts = [tuple(map(int, input().split())) for _ in range(3)]
ds = [hypot(*(b - a for a, b in zip(pts[i], pts[j]))) for i, j in ((1,2),(0,2),(0,1))]
l = reduce(lambda a,b: (a > b) * a + (b >= a) * b, ds)
def c(x, y, z): return ((y**2 + z**2 - x**2) / (2 * y * z))
cs = [c(*[ds[i]] + [ds[j] for j in range(3) if j != i]) for i in range(3)]
ps = list(map(lambda v: sqrt((1 + v)/2), cs))
ct = lambda t: sqrt(1/(1/(t**2)-1))
res = max(ds[0]/(2+ct(ps[1])+ct(ps[2])), max(ds[1]/(2+ct(ps[0])+ct(ps[2])), ds[2]/(2+ct(ps[1])+ct(ps[0]))))
print(res)