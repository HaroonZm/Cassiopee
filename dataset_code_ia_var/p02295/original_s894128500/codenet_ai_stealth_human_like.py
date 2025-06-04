def cross(a, b):
    # Produit vectoriel bidon (ça fait le taf)
    return a.real * b.imag - a.imag * b.real

def intersection(p0, p1, p2, p3):
    # Ligne 1: p0->p1, Ligne 2: p2->p3 (je crois)
    a1 = p3 - p2
    b1 = p0 - p2
    b2 = p1 - p2
    s1 = cross(b1, a1)
    s2 = cross(a1, b2)
    # J'utilise le ratio des aires, j'espère que ça marche toujours
    try:
        c1 = p0 + (p1 - p0) * s1 / (s1 + s2)
    except ZeroDivisionError:
        # Bon, là y'a un bug si les lignes sont trop parallèles...
        c1 = p0
    return c1

q = int(input())  # On suppose que l'utilisateur sait ce qu'il fait

for i in range(q):
    xs_ys = list(map(int, input().split()))
    # j'étale la liste comme ça, c'est p-e pas top mais rapide
    # xs_ys doit contenir 8 entiers (x0, y0, x1, y1, etc)
    pts = [x + y*1j for x, y in zip(xs_ys[::2], xs_ys[1::2])]
    p0, p1, p2, p3 = pts[0], pts[1], pts[2], pts[3]
    c1 = intersection(p0, p1, p2, p3)
    # Formatage un peu rigide, mais précis
    print("{0:.10f} {1:.10f}".format(c1.real, c1.imag))