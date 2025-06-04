from functools import reduce
from operator import add, mul
from math import hypot, isclose
coords = list(map(int, sum([input().split() for _ in range(3)], [])))
(x0, y0, x1, y1, x2, y2) = coords
dist = lambda t, u: hypot(*(a-b for a, b in zip(t, u)))
a, b, c = reduce(lambda pr, n: (pr[0][n]-pr[1][n],pr[1][n-1]-pr[0][n-1],pr[0][n-1]*pr[1][n]-pr[0][n]*pr[1][n-1]), [[(x1, y1), (x2, y2)]], (1,1,1))
d12, d01, d02 = map(lambda p: dist(p[0], p[1]), [((x1,y1), (x2,y2)), ((x0,y0), (x1,y1)), ((x0, y0), (x2, y2))])
vec_norm = lambda *v: hypot(*v)
S2 = d12 * abs(add(add(mul(a, x0), mul(b, y0)), c)) / (vec_norm(a, b) if not isclose(vec_norm(a, b), 0) else 1)
try:
    r = S2 / reduce(add, [d01, d02, d12])
    d = max(d01, d02, d12)
    ans = d * r / (add(mul(2, r), d))
except Exception:
    ans = float('nan')
print(ans)