import sys
import math

def dist(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

def can(x, y, sweets, t):
    # vérifier si max(distance/speed) <= t pour toutes les douceurs
    for (sx, sy, v) in sweets:
        if dist(x, y, sx, sy) / v > t:
            return False
    return True

def solve(sweets):
    # recherche binaire sur le temps minimal t
    left, right = 0.0, 150.0
    for _ in range(60):
        mid = (left + right) / 2
        found = False
        # On va chercher un point (x,y) tel que max dist/speed <= mid
        # La solution optimale se trouve à l'intersection de cercles dilatés
        # Pour simplifier on fait une recherche sur un maillage
        # mais ici on peut chercher sur des cercles de rayon mid*v autour des douceurs.
        # On essaye les points sur ces cercles intersections
        candidates = []
        for i, (x1, y1, v1) in enumerate(sweets):
            r1 = mid * v1
            candidates.append((x1, y1))
            for j in range(i + 1, len(sweets)):
                x2, y2, v2 = sweets[j]
                r2 = mid * v2
                d = dist(x1, y1, x2, y2)
                # si aucune intersection possible
                if d > r1 + r2 or d < abs(r1 - r2):
                    continue
                if d == 0 and r1 == r2:
                    # cercles égaux, prendre centre
                    candidates.append((x1, y1))
                    continue
                a = (r1*r1 - r2*r2 + d*d) / (2*d)
                h = math.sqrt(max(0.0, r1*r1 - a*a))
                xm = x1 + a*(x2 - x1)/d
                ym = y1 + a*(y2 - y1)/d
                xs1 = xm + h*(y2 - y1)/d
                ys1 = ym - h*(x2 - x1)/d
                xs2 = xm - h*(y2 - y1)/d
                ys2 = ym + h*(x2 - x1)/d
                candidates.append((xs1, ys1))
                candidates.append((xs2, ys2))
        # tester tous les candidats
        for cx, cy in candidates:
            if can(cx, cy, sweets, mid):
                found = True
                break
        if found:
            right = mid
        else:
            left = mid
    return right

input = sys.stdin.readline
while True:
    N = int(input())
    if N == 0:
        break
    sweets = [tuple(map(int, input().split())) for _ in range(N)]
    ans = solve(sweets)
    print(f"{ans:.8f}")