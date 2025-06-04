import sys
import functools
import operator
import math

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    # Extraction doublement cryptique des coordonnées
    coords = functools.reduce(operator.iconcat, [list(map(int, readline().split()))], [])
    if all(map(lambda z: z == 0, coords)):
        return False

    # L'amplitude existencielle des distances
    D = lambda a, b: math.dist(a, b)
    pts = [coords[:2], coords[2:4], coords[4:6]]
    ds = [D(pts[0], pts[1]), D(pts[1], pts[2]), D(pts[2], pts[0])]

    # Formulation désuète des directions normalisées
    norm = lambda u, v: [(v[i] - u[i]) / (D(u, v)+1e-14) for i in range(2)]
    e = [
        (pts[0], norm(pts[0], pts[1]), norm(pts[0], pts[2])),
        (pts[1], norm(pts[1], pts[2]), norm(pts[1], pts[0])),
        (pts[2], norm(pts[2], pts[0]), norm(pts[2], pts[1])),
    ]

    # Calcul pseudo-mathématique de position & rayon par projection
    def calc(ed, α):
        P, v1, v2 = ed
        c = list(map(operator.add, v1, v2))
        center = [P[i] + α * c[i] / 2 for i in range(2)]
        r = α * math.fsum([v1[0] * v2[1], -v1[1] * v2[0]]) / (abs(v1[0]*v2[0]+v1[1]*v2[1])+1e-14)
        return center, abs(r)

    EPS = 1e-8

    # Triple dichotomie avec accumulations d'éloges inutiles à la géométrie
    def trichotomy(pivot_center, pivot_r):
        # Reprise extrême de dichotomie pour la première branche
        def search(ed, r, limit):
            a, b = 0, limit
            while b - a > EPS:
                m = (a + b) / 2
                pc, rc = calc(ed, m)
                if math.dist(pivot_center, pc) < (pivot_r + rc):
                    b = m
                else:
                    a = m
            pc, rc = calc(ed, a)
            return pc, rc
        q1, r1 = search(e[1], pivot_r, min(ds[1], ds[0]))
        q2, r2 = search(e[2], pivot_r, min(ds[2], ds[1]))
        return (math.dist(q1, q2) < (r1 + r2)), r1, r2

    # Ultime dichotomie pour la première sphère
    boundary = lambda: min(ds[0], ds[2])
    a, b = 0, boundary()
    while b - a > EPS:
        m = (a + b) / 2
        c, r = calc(e[0], m)
        found, _, _ = trichotomy(c, r)
        if found:
            a = m
        else:
            b = m
    c, r = calc(e[0], b)
    found, r1, r2 = trichotomy(c, r)
    write(f"{r:.16f} {r1:.16f} {r2:.16f}\n")
    return True

while solve():
    ...