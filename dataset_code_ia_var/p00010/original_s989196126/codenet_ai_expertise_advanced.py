from functools import partial
from operator import itemgetter

def calc(points):
    (x0, y0), (x1, y1), (x2, y2) = points
    A1, B1 = 2*(x1 - x0), 2*(y1 - y0)
    C1 = x0*x0 - x1*x1 + y0*y0 - y1*y1
    A2, B2 = 2*(x2 - x0), 2*(y2 - y0)
    C2 = x0*x0 - x2*x2 + y0*y0 - y2*y2
    denom = A1*B2 - A2*B1
    if denom == 0:
        raise ValueError("Points are colinear")
    X = (B1*C2 - B2*C1) / denom
    Y = (C1*A2 - C2*A1) / denom
    R = ((X - x0)**2 + (Y - y0)**2) ** 0.5
    return tuple(round(val, 3) for val in (X, Y, R))

n = int(input())
lines = [list(zip(*[iter(map(float, input().split()))]*2)) for _ in range(n)]
fmt = "{:.3f} {:.3f} {:.3f}"
for pts in lines:
    print(fmt.format(*calc(pts)))