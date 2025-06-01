import sys
from math import sqrt, hypot

def _hypot(p1, p2):
    """
    Calcule la distance euclidienne entre deux points 2D.

    Args:
        p1 (tuple): Coordonnées (x, y) du premier point.
        p2 (tuple): Coordonnées (x, y) du second point.

    Returns:
        float: La distance entre p1 et p2 calculée avec la formule de l'hypoténuse.
    """
    # Utilisation de hypot pour obtenir la distance (racine carrée de la somme des carrés des différences)
    return hypot(p2[0] - p1[0], p2[1] - p1[1])

def heron(p1, p2, p3):
    """
    Calcule l'aire d'un triangle défini par trois points en 2D
    en utilisant la formule de Héron.

    Args:
        p1 (tuple): Coordonnées (x, y) du premier sommet du triangle.
        p2 (tuple): Coordonnées (x, y) du second sommet du triangle.
        p3 (tuple): Coordonnées (x, y) du troisième sommet du triangle.

    Returns:
        float: L'aire du triangle formé par p1, p2 et p3.
    """
    # Calcul des longueurs des côtés du triangle
    e1 = _hypot(p1, p2)
    e2 = _hypot(p2, p3)
    e3 = _hypot(p1, p3)
    # Calcul du demi-périmètre du triangle
    z = (e1 + e2 + e3) / 2
    # Application de la formule de Héron pour calculer l'aire
    return sqrt(z * (z - e1) * (z - e2) * (z - e3))

# Lecture des points depuis l'entrée standard
# Chaque ligne est supposée contenir deux valeurs flottantes séparées par une virgule
a = [tuple(map(float, l.split(","))) for l in sys.stdin]

# Initialisation d'un accumulating variable pour l'aire totale
result = 0

# On additionne les aires des triangles formés par le premier point et chaque paire de points successifs
# Ceci correspond à une méthode pour calculer l'aire d'un polygone triangulé à partir du premier sommet
for p1, p2 in zip(a[1:], a[2:]):
    result += heron(a[0], p1, p2)

# Affichage de l'aire totale calculée
print(result)