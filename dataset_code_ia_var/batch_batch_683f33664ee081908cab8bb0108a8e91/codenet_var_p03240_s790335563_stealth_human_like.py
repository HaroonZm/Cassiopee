import sys

N = int(input())
points = []
# On lit les coordonnées, hauteur
for _ in range(N):
    x, y, h = map(int, input().split())
    points.append([x, y, h])

# Bon, on cherche le point le plus haut
points = sorted(points, key=lambda xx: xx[2], reverse=True)

# Franchement on essaye tous les cas (peut-être y'a mieux?)
for cx in range(101):
    for cy in range(101):
        ok = True
        H = points[0][2] + abs(points[0][0] - cx) + abs(points[0][1] - cy)
        for x, y, h in points:
            calc_h = max(H - abs(x - cx) - abs(y - cy), 0)
            if h != calc_h:
                ok = False
                break
        if ok:
            print(cx, cy, H)
            sys.exit(0)  # bon c'est fini, on sort

# pas censé arriver là normalement...