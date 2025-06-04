from math import hypot, fsum, isclose, prod

def cross(P0, P1, P2):
    M = [[P1[i] - P0[i], P2[i] - P0[i]] for i in range(2)]
    return fsum([M[0][0]*M[1][1], -M[1][0]*M[0][1]])

def dot(P0, P1, P2):
    v1, v2 = tuple(map(lambda Q: tuple(map(lambda x, y: x - y, Q, P0)), (P1, P2)))
    return fsum(map(prod, zip(v1,v2)))

def dist2(P0, P1):
    return fsum(map(lambda a, b: (a - b) ** 2, P0, P1))

def collision(S0, S1, T0, T1):
    f = lambda A,B,C: cross(A,B,C)
    return all(map(lambda t: t < 0, [f(S0,S1,T0)*f(S0,S1,T1), f(T0,T1,S0)*f(T0,T1,S1)]))

def dist_lp(S, E, P):
    dd = dist2(S, E)
    proj = dot(S, E, P)
    if 0 <= proj <= dd:
        numer = abs(cross(S, E, P))
        return numer / hypot(*(e-s for e,s in zip(E,S)))
    return min(hypot(*(p-s for p,s in zip(P,S))), hypot(*(p-e for p,e in zip(P,E))))

def dist_ll(S0, S1, T0, T1):
    if collision(S0, S1, T0, T1):
        return 0
    dists = [dist_lp(S0, S1, T0), dist_lp(S0, S1, T1), dist_lp(T0, T1, S0), dist_lp(T0, T1, S1)]
    return min(dists)

def contain(PS, A):
    seq = [cross(PS[i], PS[(i+1)%len(PS)], A) for i in range(len(PS))]
    products = [seq[0]*v for v in seq]
    return all(x >= 0 for x in products)

from functools import reduce

def input_ints():
    return list(map(int, input().split()))

c = 0
while True:
    c += 1
    n = int(input())
    if not n:
        break
    sx, sy, ex, ey = input_ints()
    S, E = (sx, sy), (ex, ey)
    cannot = False
    ans = 1e9

    for _ in range(n):
        minx, miny, maxx, maxy, h = input_ints()
        pts = tuple(zip(*[((minx, miny), (minx, maxy)), ((maxx, maxy), (maxx, miny))]))
        PS = (pts[0][0], pts[0][1], pts[1][1], pts[1][0])
        cannot |= any(contain(PS, p) for p in (S, E))
        for j in range(4):
            jj = (j-1)%4
            cannot |= collision(PS[jj], PS[j], S, E)
            d = dist_ll(S, E, PS[jj], PS[j])
            x = (h**2+d**2)/(2*h) if h <= d else d
            ans = min(ans, x)

    print("0" if cannot else "{0:.8f}".format(ans))