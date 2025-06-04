# Solution Python pour vérifier si deux lignes sont parallèles, orthogonales ou aucune de ces conditions

def is_parallel(dx1, dy1, dx2, dy2):
    """
    Deux vecteurs (dx1, dy1) et (dx2, dy2) sont parallèles si et seulement si
    leur produit vectoriel est nul : dx1*dy2 - dy1*dx2 == 0
    """
    return dx1 * dy2 == dy1 * dx2

def is_orthogonal(dx1, dy1, dx2, dy2):
    """
    Deux vecteurs sont orthogonaux si leur produit scalaire est nul :
    dx1*dx2 + dy1*dy2 == 0
    """
    return dx1 * dx2 + dy1 * dy2 == 0

def main():
    q = int(input())
    for _ in range(q):
        # lecture des coordonnées : x_p0, y_p0, x_p1, y_p1, x_p2, y_p2, x_p3, y_p3
        x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())

        # vecteurs directionnels des droites s1 et s2
        dx1 = x1 - x0
        dy1 = y1 - y0
        dx2 = x3 - x2
        dy2 = y3 - y2

        # Vérifier parallélisme
        if is_parallel(dx1, dy1, dx2, dy2):
            print(2)
        # Vérifier orthogonalité
        elif is_orthogonal(dx1, dy1, dx2, dy2):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()