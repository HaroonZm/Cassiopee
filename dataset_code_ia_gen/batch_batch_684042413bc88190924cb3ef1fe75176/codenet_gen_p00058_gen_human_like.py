import sys

def is_orthogonal(xa, ya, xb, yb, xc, yc, xd, yd):
    # Calcul du vecteur AB
    abx = xb - xa
    aby = yb - ya
    # Calcul du vecteur CD
    cdx = xd - xc
    cdy = yd - yc
    # Produit scalaire
    dot_product = abx * cdx + aby * cdy
    # Si le produit scalaire est proche de zéro, les droites sont orthogonales
    return abs(dot_product) < 1e-10

for line in sys.stdin:
    if not line.strip():
        continue
    xa, ya, xb, yb, xc, yc, xd, yd = map(float, line.split())
    if is_orthogonal(xa, ya, xb, yb, xc, yc, xd, yd):
        print("YES")
    else:
        print("NO")