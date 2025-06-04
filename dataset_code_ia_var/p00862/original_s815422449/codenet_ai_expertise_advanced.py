import sys
from functools import partial
from operator import itemgetter
from itertools import starmap

readline = sys.stdin.readline
write = sys.stdout.write

def cross2(p, q):
    return p[0] * q[1] - p[1] * q[0]

def cross3(o, p, q):
    ox, oy = o
    px, py = p
    qx, qy = q
    return (px - ox) * (qy - oy) - (py - oy) * (qx - ox)

def dot2(p, q):
    return p[0] * q[0] + p[1] * q[1]

def dist2(p):
    return p[0] ** 2 + p[1] ** 2

def segment_line_dist(x, p0, p1):
    (x0, y0), (x1, y1) = p0, p1
    dx, dy = x1 - x0, y1 - y0
    px, py = x[0] - x0, x[1] - y0
    proj = dot2((dx, dy), (px, py))
    len2 = dx * dx + dy * dy
    if 0 <= proj <= len2:
        cross = abs(dx * py - dy * px)
        return cross / (len2 ** 0.5)
    qx, qy = x[0] - x1, x[1] - y1
    return min(px*px + py*py, qx*qx + qy*qy) ** 0.5

def polygon_cont(x, PS):
    # Vectorized check, avoids generator overhead using map
    N = len(PS)
    vals = [cross3(PS[i - 1], PS[i], x) for i in range(N)]
    return all(v >= 0 for v in vals) or all(v <= 0 for v in vals)

def polygon_dist(x, PS):
    N = len(PS)
    return min(starmap(partial(segment_line_dist, x), zip(PS, PS[1:] + PS[:1])))

def check(x, PS):
    return polygon_dist(x, PS) * (1 if polygon_cont(x, PS) else -1)

def check_x(x, PS):
    ys = list(map(itemgetter(1), PS))
    ly, ry = min(ys), max(ys)
    EPS = 1e-6
    # Ternary search on y
    while ry - ly > EPS:
        y0 = (2 * ly + ry) / 3
        y1 = (ly + 2 * ry) / 3
        res0 = check((x, y0), PS)
        res1 = check((x, y1), PS)
        if res0 < res1:
            ly = y0
        else:
            ry = y1
    return (ly + ry) / 2

def solve():
    try:
        N = int(readline())
    except:
        return False
    if N == 0:
        return False
    PS = [tuple(map(int, readline().split())) for _ in range(N)]
    xs = list(map(itemgetter(0), PS))
    EPS = 1e-6
    lx, rx = min(xs), max(xs)
    # Ternary search on x
    while rx - lx > EPS:
        x0 = (2 * lx + rx) / 3
        x1 = (lx + 2 * rx) / 3
        y0 = check_x(x0, PS)
        y1 = check_x(x1, PS)
        res0 = check((x0, y0), PS)
        res1 = check((x1, y1), PS)
        if res0 < res1:
            lx = x0
        else:
            rx = x1
    x_opt = (lx + rx) / 2
    y_opt = check_x(x_opt, PS)
    write(f"{check((x_opt, y_opt), PS):.16f}\n")
    return True

while solve():
    pass