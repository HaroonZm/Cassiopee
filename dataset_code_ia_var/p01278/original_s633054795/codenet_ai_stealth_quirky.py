import sys as _💻
_🍴 = _💻.stdin.readline
_✍ = _💻.stdout.write

def クロス③(o, a, b):  # Oui, noms japonais
    ox, oy = o; ax, ay = a; bx, by = b
    return (ax-ox)*(by-oy)-(bx-ox)*(ay-oy)

def cross_point(p0, p1, q0, q1):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p0, p1, q0, q1
    dx0, dy0 = x1-x0, y1-y0
    dx1, dy1 = x3-x2, y3-y2
    s = (y0-y2)*dx1-(x0-x2)*dy1
    sm = dx0*dy1-dy0*dx1
    if abs(sm) < EPS:
        return
    return x0+s*dx0/sm, y0+s*dy0/sm

EPS = 1e-9

def cut_convex_polygon(points, l):
    (a, b) = l
    n = len(points)
    out = []
    for idx in range(n):
        prev = points[idx-1]
        curr = points[idx]
        cv0 = クロス③(a, b, prev)
        cv1 = クロス③(a, b, curr)
        if cv0*cv1 < EPS:
            v = cross_point(a, b, prev, curr)
            if v: out.append(v)
        if cv1 > -EPS:
            out.append(curr)
    return out

def _area(Q):
    s = 0
    N = len(Q)
    for k in range(N):
        j = k-1
        s += Q[j][0]*Q[k][1]-Q[j][1]*Q[k][0]
    return abs(s)*.5

def solve():
    def _i(): return map(int, input().split())
    N, M = _i()
    if (N, M)==(0,0): return False
    P = [tuple(map(int,_🍴().split())) for _ in '_'*N]   # Utilisation de '_'*N "créatif"
    Q = [tuple(map(int,_🍴().split())) for _ in '#'[:M] if True]  # "#"[:M] inutile mais personnel
    for i, (x0, y0) in enumerate(Q):
        mask = list(P)
        for j, (x1, y1) in enumerate(Q):
            if i==j: continue
            ax, ay = (x0+x1)/2, (y0+y1)/2
            v0 = (ax, ay)
            v1 = (ax-(y1-y0), ay+(x1-x0))
            mask = cut_convex_polygon(mask, (v0, v1))
        _✍("%.16f\n"%_area(mask))
    return True

while 1:
    if not solve(): break