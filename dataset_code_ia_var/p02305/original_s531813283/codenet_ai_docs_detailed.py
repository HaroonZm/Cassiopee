import math

def read_circle_input():
    """
    Lit une ligne d'entrée standard, la découpe en trois entiers pour obtenir les coordonnées du centre
    et le rayon d'un cercle.

    Returns:
        tuple: Un triplet (x, y, r) représentant respectivement l'abscisse, l'ordonnée et le rayon du cercle.
    """
    # Lire une ligne d'entrée, la découper et convertir les éléments en entiers.
    return tuple(int(i) for i in input().split())

def distance_between_points(x1, y1, x2, y2):
    """
    Calcule la distance euclidienne entre deux points du plan.

    Args:
        x1 (int): abscisse du premier point.
        y1 (int): ordonnée du premier point.
        x2 (int): abscisse du second point.
        y2 (int): ordonnée du second point.

    Returns:
        float: distance euclidienne entre les deux points.
    """
    # Application de la formule de la distance euclidienne : sqrt((x1-x2)^2 + (y1-y2)^2)
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def circles_relationship(c1, c2):
    """
    Détermine la relation géométrique entre deux cercles dans le plan.

    Args:
        c1 (tuple): triplet (x1, y1, r1) du premier cercle.
        c2 (tuple): triplet (x2, y2, r2) du second cercle.

    Returns:
        int: valeur indiquant la position relative des cercles :
            4 : les cercles sont extérieurs (aucun point commun)
            3 : les cercles sont tangents extérieurement (un point commun)
            2 : les cercles s’intersectent en deux points
            1 : les cercles sont tangents intérieurement (un point commun)
            0 : un cercle est à l’intérieur de l’autre sans intersection
    """
    x1, y1, r1 = c1
    x2, y2, r2 = c2

    # Calcul de la distance entre les centres des deux cercles.
    d = distance_between_points(x1, y1, x2, y2)

    # Somme des rayons des deux cercles.
    sum_r = r1 + r2

    # On identifie le plus grand et le plus petit rayon.
    r_big = max(r1, r2)
    r_small = min(r1, r2)

    # Test relation entre les cercles
    if d > sum_r:
        # Les cercles sont extérieurs et ne se touchent pas.
        return 4
    elif d == sum_r:
        # Les cercles sont tangents extérieurement (ils se touchent en un point extérieur).
        return 3
    elif d + r_small < r_big:
        # Un cercle est strictement à l'intérieur de l'autre, sans aucun point commun.
        return 0
    elif d + r_small == r_big:
        # Les cercles sont tangents intérieurement (ils se touchent en un seul point intérieur).
        return 1
    else:
        # Les cercles se croisent en deux points (ils sont sécants).
        return 2

def main():
    """
    Fonction principale qui lit les entrées, calcule la relation entre deux cercles et affiche le résultat.
    """
    # Lecture des paramètres du premier cercle.
    c1 = read_circle_input()
    # Lecture des paramètres du second cercle.
    c2 = read_circle_input()
    # Détermination de la situation géométrique des deux cercles.
    rel = circles_relationship(c1, c2)
    # Affichage du résultat.
    print(rel)

# Exécution du programme principal.
main()