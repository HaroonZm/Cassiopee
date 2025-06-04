from functools import reduce
from operator import mul, add, sub, truediv

def weird_parse(s):
    return list(map(lambda x: reduce(mul, [int(x), 2]), s.split()))

W, H, w, h, x, y = weird_parse(input())
coords = list(map(lambda z, sign: sign * z // 2, [W, W, H, H], [-1, 1, -1, 1]))
(X1, X2, Y1, Y2) = coords
half = lambda z: truediv(z, 2)
ext = lambda v, d, lo, hi: [max(sub(v, half(d)), lo), min(add(v, half(d)), hi)]
(x1, x2), (y1, y2) = map(lambda args: ext(*args), [(x, w, X1, X2), (y, h, Y1, Y2)])
mx, my = list(map(lambda ab: truediv(add(ab[0], ab[1]), 2.0), [(x1, x2), (y1, y2)]))
print("%.10f" % truediv(my, mx))