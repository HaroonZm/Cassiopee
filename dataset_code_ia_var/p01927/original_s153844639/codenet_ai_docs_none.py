from math import sin, cos, tan, radians
from heapq import heappush, heappop
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def dot3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)
def cross3(O, A, B):
    ox, oy = O; ax, ay = A; bx, by = B
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)
def dist2(A, B):
    ax, ay = A; bx, by = B
    return (ax - bx) ** 2 + (ay - by) ** 2
def is_intersection(P0, P1, Q0, Q1):
    C0 = cross3(P0, P1, Q0)
    C1 = cross3(P0, P1, Q1)
    if C0 == C1 == 0:
        E0 = dot3(P0, P1, Q0)
        E1 = dot3(P0, P1, Q1)
        if not E0 < E1:
            E0, E1 = E1, E0
        return E0 <= dist2(P0, P1) and 0 <= E1
    D0 = cross3(Q0, Q1, P0)
    D1 = cross3(Q0, Q1, P1)
    return C0 * C1 <= 0 and D0 * D1 <= 0
def convex_hull(ps):
    qs = []
    n = len(ps)
    for p in ps:
        while len(qs) > 1 and cross3(qs[-1], qs[-2], p) >= 0:
            qs.pop()
        qs.append(p)
    t = len(qs)
    for i in range(n-2, -1, -1):
        p = ps[i]
        while len(qs) > t and cross3(qs[-1], qs[-2], p) >= 0:
            qs.pop()
        qs.append(p)
    return qs
def cross2(p, q):
    return p[0]*q[1] - p[1]*q[0]
def dot2(p, q):
    return p[0]*q[0] + p[1]*q[1]
def dist1(p):
    return p[0]**2 + p[1]**2
def segment_line_dist_d(x, p0, p1):
    z0 = (p1[0] - p0[0], p1[1] - p0[1])
    z1 = (x[0] - p0[0], x[1] - p0[1])
    if 0 <= dot2(z0, z1) <= dist1(z0):
        return cross2(z0, z1)**2 / dist1(z0)
    z2 = (x[0] - p1[0], x[1] - p1[1])
    return min(dist1(z1), dist1(z2))
def polygon_contain(x, ps):
    if len(ps) == 1:
        return 0
    pl = len(ps)
    return (
        all(cross3(ps[i-1], ps[i], x) > 0 for i in range(pl)) or
        all(cross3(ps[i-1], ps[i], x) < 0 for i in range(pl))
    )
def convex_polygon_contain(p0, qs):
    L = len(qs)
    if L < 3:
        return False
    left = 1; right = L
    x0, y0 = q0 = qs[0]
    while left+1 < right:
        mid = (left + right) >> 1
        if cross3(q0, p0, qs[mid]) <= 0:
            left = mid
        else:
            right = mid
    if left == L-1:
        left -= 1
    qi = qs[left]; qj = qs[left+1]
    v0 = cross3(q0, qi, qj)
    v1 = cross3(q0, p0, qj)
    v2 = cross3(q0, qi, p0)
    if v0 < 0:
        v1 = -v1; v2 = -v2
    return 0 <= v1 and 0 <= v2 and v1 + v2 <= v0
def convex_polygons_intersection(ps, qs):
    pl = len(ps); ql = len(qs)
    if pl == 1 or ql == 1:
        return 0
    i = j = 0
    while (i < pl or j < ql) and (i < 2*pl) and (j < 2*ql):
        px0, py0 = ps0 = ps[(i-1)%pl]; px1, py1 = ps1 = ps[i%pl]
        qx0, qy0 = qs0 = qs[(j-1)%ql]; qx1, qy1 = qs1 = qs[j%ql]
        if is_intersection(ps0, ps1, qs0, qs1):
            return 1
        ax = px1 - px0; ay = py1 - py0
        bx = qx1 - qx0; by = qy1 - qy0
        v = (ax*by - bx*ay)
        va = cross3(qs0, qs1, ps1)
        vb = cross3(ps0, ps1, qs1)
        if v == 0 and va < 0 and vb < 0:
            return 0
        if v == 0 and va == 0 and vb == 0:
            i += 1
        elif v >= 0:
            if vb > 0:
                i += 1
            else:
                j += 1
        else:
            if va > 0:
                j += 1
            else:
                i += 1
    return 0
def find_tangent(p0, qs):
    L = len(qs)
    d = L//3
    gx = (qs[0][0] + qs[d][0] + qs[2*d][0]) / 3
    gy = (qs[0][1] + qs[d][1] + qs[2*d][1]) / 3
    g = (gx, gy)
    ma = -1; mi = 2; k0 = 0; k1 = 0
    for i in range(L):
        v = cross3(p0, qs[i], g) / (dist2(p0, g) * dist2(p0, qs[i]))**.5
        if v > ma:
            k1 = i
            ma = v
        if v < mi:
            k0 = i
            mi = v
    return k0, k1
def tangent_polygon_dist(ps, qs):
    Lp = len(ps); Lq = len(qs)
    pi, qi = find_tangent(qs[0], ps)
    pj, qj = find_tangent(ps[0], qs)
    if qi < pi:
        qi += Lp
    if qj < pj:
        qj += Lq
    res = dist2(ps[pi], qs[pj])
    if pj < qj:
        for i in range(pi, qi+1):
            x = ps[i-Lp]
            for j in range(pj, qj+1):
                res = min(res, segment_line_dist_d(x, qs[(j-1)%Lq], qs[j-Lq]))
    if pi < qi:
        for j in range(pj, qj+1):
            x = qs[j-Lq]
            for i in range(pi, qi+1):
                res = min(res, segment_line_dist_d(x, ps[(i-1)%Lp], ps[i-Lp]))
    return res**.5
def polygons_dist(ps, qs):
    if (convex_polygons_intersection(ps, qs)
            or convex_polygon_contain(ps[0], qs)
            or convex_polygon_contain(qs[0], ps)):
        return 0
    return tangent_polygon_dist(ps, qs)
def solve():
    N = int(readline())
    if N == 0:
        return False
    P = [[] for i in range(N)]
    H = [0]*N
    for i in range(N):
        k, h, *ps = map(int, readline().split())
        H[i] = h
        Pi = P[i]
        for j in range(k):
            x, y = ps[2*j:2*j+2]
            Pi.append((x, y))
    theta, phi = map(int, readline().split())
    r_theta = radians(theta)
    r_phi = radians(90 - phi)
    dx = -cos(r_theta)*tan(r_phi)
    dy = -sin(r_theta)*tan(r_phi)
    sx, sy, tx, ty = map(int, readline().split())
    for i in range(N):
        Pi = P[i]
        hi = H[i]
        for j in range(len(Pi)):
            x, y = Pi[j]
            Pi.append((x + hi*dx, y + hi*dy))
        Pi.sort()
        P[i] = convex_hull(Pi)[:-1]
    P.append([(sx, sy)])
    P.append([(tx, ty)])
    E = [[0]*(N+2) for i in range(N+2)]
    dist = [10**18]*(N+2)
    for i in range(N+2):
        for j in range(i+1, N+2):
            E[i][j] = E[j][i] = polygons_dist(P[i], P[j])
    que = [(0, N)]
    dist[N] = 0
    while que:
        cost, v = heappop(que)
        if dist[v] < cost:
            continue
        for w in range(N+2):
            n_cost = cost + E[v][w]
            if n_cost < dist[w]:
                dist[w] = n_cost
                heappush(que, (n_cost, w))
    print("%.16f" % dist[N+1])
    return True
while solve():
    ...