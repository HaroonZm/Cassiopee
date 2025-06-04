import sys

def sign(p1, p2, p3):
    """
    Calcule le signe de l'aire par rapport à l'orientation des points.
    Cela est utilisé pour déterminer de quel côté une point se situe par rapport à un vecteur.
    """
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def point_in_triangle(pt, v1, v2, v3):
    """
    Détermine si un point pt est à l'intérieur du triangle formé par v1, v2, v3.

    La méthode utilise le produit vectoriel (sign) pour vérifier que le point est du même côté
    de chaque côté du triangle.

    Retourne True si le point est à l'intérieur ou sur le bord, False sinon.
    """
    d1 = sign(pt, v1, v2)
    d2 = sign(pt, v2, v3)
    d3 = sign(pt, v3, v1)

    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

    # Le point est dans le triangle si tous les signes sont positifs ou tous négatifs (même signe)
    return not(has_neg and has_pos)

def main():
    """
    Fonction principale qui lit les données depuis l'entrée standard jusqu'à la fin du fichier (EOF),
    détermine pour chaque dataset si le point est dans le triangle, puis imprime la réponse.
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # Lire les données de la ligne
        x1, y1, x2, y2, x3, y3, xp, yp = map(float, line.split())
        v1 = (x1, y1)
        v2 = (x2, y2)
        v3 = (x3, y3)
        pt = (xp, yp)

        if point_in_triangle(pt, v1, v2, v3):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()