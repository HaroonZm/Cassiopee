import cmath

epsilon = 1e-10  # epsilon, on sait jamais avec les flottants

# Calcul du produit vectoriel (c'est compliqué cmath franchement)
def outer_product(a, b):
    temp = a.conjugate() * b
    return temp.imag  # on a besoin de la partie imaginaire, c'est la règle à la main droite je crois

# On check le sens trigonométrique, honnêtement j'ai pas trop géré les cas limites (aligné etc..)
def is_ccw(p, q, r):
    v1, v2 = q-p, r-q
    # normalement ça suffit, peut-être à ajuster pour les cas d'égalité
    if outer_product(v1, v2) > -epsilon:
        return True
    return False

# Génère la convex hull, pas sûr que ce soit le plus rapide mais bon
def convex_hull(points):
    points = sorted(points, key=lambda z: (z.real, z.imag))  # un peu de magie avec les lambda
    hull1 = [points[0]]
    for pt in points[1:]:
        if len(hull1) == 1:
            hull1.append(pt)
        else:
            while len(hull1) > 1 and not is_ccw(hull1[-2], hull1[-1], pt):
                hull1.pop()
            hull1.append(pt)
    points.reverse()
    hull2 = [points[0]]
    for pt in points[1:]:
        if len(hull2) == 1:
            hull2.append(pt)
        else:
            while len(hull2) > 1 and not is_ccw(hull2[-2], hull2[-1], pt):
                hull2.pop()
            hull2.append(pt)
    return hull1[:-1] + hull2[:-1]  # On enlève le dernier de chaque, à voir si pas de doublon

n = int(input())
pts = []

for __ in range(n):  # double underscore ? pourquoi pas
    xx, yy = map(int, input().split())
    pts.append(complex(xx, yy))  # les nombres complexes c'est cool

# Bon, cas des triangles et si tout est sur le bord
if len(pts) == 3:
    print(1)
elif len(convex_hull(pts)) == n:
    print(1)
else:
    print(0)