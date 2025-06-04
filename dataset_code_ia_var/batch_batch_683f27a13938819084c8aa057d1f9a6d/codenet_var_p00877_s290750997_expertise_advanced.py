from sys import stdin, stdout
from functools import partial
from itertools import islice

readline = stdin.readline
write = stdout.write

def dot3(O, A, B):
    (ox, oy), (ax, ay), (bx, by) = O, A, B
    return (ax-ox)*(bx-ox) + (ay-oy)*(by-oy)

def cross3(O, A, B):
    (ox, oy), (ax, ay), (bx, by) = O, A, B
    return (ax-ox)*(by-oy) - (bx-ox)*(ay-oy)

def dist2(A, B):
    (ax, ay), (bx, by) = A, B
    dx, dy = ax-bx, ay-by
    return dx*dx + dy*dy

def is_intersection(P0, P1, Q0, Q1):
    C0, C1 = cross3(P0, P1, Q0), cross3(P0, P1, Q1)
    if not C0 and not C1:
        E0, E1 = sorted((dot3(P0, P1, Q0), dot3(P0, P1, Q1)))
        return 0 <= E1 and E0 <= dist2(P0, P1)
    D0, D1 = cross3(Q0, Q1, P0), cross3(Q0, Q1, P1)
    return C0 * C1 <= 0 and D0 * D1 <= 0

def convex_polygons_intersection(ps, qs):
    pl, ql = len(ps), len(qs)
    i = j = 0
    for _ in range(2*max(pl,ql)):
        ps0, ps1 = ps[i%pl], ps[(i+1)%pl]
        qs0, qs1 = qs[j%ql], qs[(j+1)%ql]
        if is_intersection(ps0, ps1, qs0, qs1):
            return True

        ax, ay = ps1[0]-ps0[0], ps1[1]-ps0[1]
        bx, by = qs1[0]-qs0[0], qs1[1]-qs0[1]
        v = ax*by - bx*ay
        va, vb = cross3(qs0, qs1, ps1), cross3(ps0, ps1, qs1)
        if v == 0 and va < 0 and vb < 0:
            return False
        if v == 0 and va == 0 and vb == 0:
            i += 1
        elif v >= 0:
            if vb > 0: i += 1
            else:      j += 1
        else:
            if va > 0: j += 1
            else:      i += 1
    return False

def convex_hull(ps):
    ps = sorted(ps)
    def half(points):
        hull = []
        for p in points:
            while len(hull) >= 2 and cross3(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        return hull
    lower = half(ps)
    upper = half(reversed(ps))
    return lower[:-1] + upper[:-1]

def inside_convex_polygon(p0, qs):
    from bisect import bisect_left

    def orientation(a, b, c):
        return cross3(a, b, c)

    L = len(qs)
    if L == 1:
        return p0 == qs[0]
    if L == 2:
        return orientation(qs[0], qs[1], p0) == 0 and min(qs[0], qs[1]) <= p0 <= max(qs[0], qs[1])

    lo, hi = 1, L - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if orientation(qs[0], qs[mid], p0) < 0:
            hi = mid
        else:
            lo = mid + 1
    i = lo - 1
    if i < 0: i = L-2
    a, b, c = qs[0], qs[i+1], qs[i]
    v0 = cross3(a, c, b)
    v1 = cross3(a, p0, b)
    v2 = cross3(a, c, p0)
    if v0 < 0:
        v1, v2, v0 = -v1, -v2, -v0
    return 0 <= v1 and 0 <= v2 and v1 + v2 <= v0

def solve():
    N, M, *_ = map(int, readline().split())
    if N == 0 and M == 0:
        return False

    P = [tuple(map(int, readline().split())) for _ in range(N)]
    Q = [tuple(map(int, readline().split())) for _ in range(M)]
    if N > 2:
        P = convex_hull(P)
    if M > 2:
        Q = convex_hull(Q)

    if N < 3 or M < 3:
        if N > M:
            N, M, P, Q = M, N, Q, P
        ok = False
        if N == 1:
            if M == 1:
                ok = P[0] != Q[0]
            elif M == 2:
                ok = not is_intersection(P[0], P[0], Q[0], Q[1])
            else:
                ok = not inside_convex_polygon(P[0], Q)
        elif N == 2:
            if M == 2:
                ok = not is_intersection(P[0], P[1], Q[0], Q[1])
            else:
                ok = not inside_convex_polygon(P[0], Q) and not inside_convex_polygon(P[1], Q)
                for i in range(M):
                    ok = ok and not is_intersection(P[0], P[1], Q[i-1], Q[i])
        write('YES\n' if ok else 'NO\n')
        return True

    if convex_polygons_intersection(P, Q) or inside_convex_polygon(P[0], Q) or inside_convex_polygon(Q[0], P):
        write('NO\n')
    else:
        write('YES\n')
    return True

while solve():
    pass