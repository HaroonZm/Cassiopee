import cmath

EPSILON = 1e-10

def prodV(u, v):  # produit vectoriel style ‘snake_case’
    """produit vectoriel via conjugaison, fonction fonctionnelle"""
    return (u.conjugate() * v).imag

def ccw(*args):  
    p, q, r = args
    a = q - p
    b = r - q
    if prodV(a, b) > -EPSILON:
        return True
    else:
        return False

def convex_hull(points):  # du style PEP8, mais switch imperatif/fonctionnel
    points = sorted(points, key=lambda z: (z.real, z.imag))
    hull_A = [points[0]]
    idx = 1
    # construction inférieure, façon imperative
    while idx < len(points):
        pnt = points[idx]
        if len(hull_A) == 1:
            hull_A.append(pnt)
        else:
            while len(hull_A) > 1 and not ccw(hull_A[-2], hull_A[-1], pnt):
                hull_A.pop()
            hull_A.append(pnt)
        idx += 1
    # changement de style : boucle for
    hull_B = [points[-1]]
    for z in reversed(points[:-1]):
        if len(hull_B)==1:
            hull_B.append(z)
        else:
            cond = True
            while cond and len(hull_B)>1:
                if not ccw(hull_B[-2], hull_B[-1], z):
                    hull_B.pop()
                    cond = True
                else:
                    cond = False
            hull_B.append(z)
    return hull_A[:-1]+hull_B[:-1]

n = int(input())
pts = []
for _ in range(n):
    x, y = map(int, input().split())
    pts += [complex(x, y)]  # ajout style liste

def verif(points):
    # style fonctionnel + ternaire
    if len(points) == 3: return 1
    return 1 if len(convex_hull(points)) == len(points) else 0

print(verif(pts))