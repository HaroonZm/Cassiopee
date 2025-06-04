import sys

def dot(c1, c2):
    """
    Calcule le produit scalaire de deux nombres complexes considérés comme des vecteurs 2D.

    Args:
        c1 (complex): Premier vecteur sous forme complexe.
        c2 (complex): Second vecteur sous forme complexe.

    Returns:
        float: Résultat du produit scalaire.
    """
    # Produit scalaire : (x1 * x2 + y1 * y2)
    return c1.real * c2.real + c1.imag * c2.imag

def cross(c1, c2):
    """
    Calcule le produit vectoriel (aire du parallélogramme) de deux nombres complexes considérés comme des vecteurs 2D.

    Args:
        c1 (complex): Premier vecteur sous forme complexe.
        c2 (complex): Second vecteur sous forme complexe.

    Returns:
        float: Résultat du produit vectoriel.
    """
    # Produit vectoriel : (x1 * y2 - y1 * x2)
    return c1.real * c2.imag - c1.imag * c2.real

def string_to_complex(s):
    """
    Convertit une chaîne de caractères contenant deux entiers séparés par un espace en nombre complexe.

    Args:
        s (str): Chaîne de caractères 'x y'.

    Returns:
        complex: Le nombre complexe x + yj.
    """
    # Extraction et conversion des coordonnées
    x, y = map(int, s.split())
    return x + y * 1j

def contains(polygon, point):
    """
    Détermine la position d'un point par rapport à un polygone donné (sur le bord, à l'intérieur ou à l'extérieur).
    Basé sur l'algorithme de croisement de segments.

    Args:
        polygon (List[complex]): Liste ordonnée des sommets (complexes) du polygone, où le dernier sommet est identique au premier.
        point (complex): Point à tester.

    Returns:
        int: 0 si le point est à l'extérieur, 
             1 si le point est sur le bord,
             2 si le point est à l'intérieur.
    """
    flag = False  # Indicateur du nombre d'intersections avec les arêtes du polygone
    for v1, v2 in zip(polygon[0:], polygon[1:]):
        # Vecteurs allant du point testé aux sommets v1 et v2
        a = v1 - point
        b = v2 - point
        # On ordonne pour que a.imag <= b.imag
        if a.imag > b.imag:
            a, b = b, a
        cross_ab = cross(a, b)
        # Cas particulier : le point est exactement sur un segment du polygone
        if cross_ab == 0 and dot(a, b) <= 0:
            return 1
        # Test de croisement de la demi-droite horizontale sortant du point
        if a.imag <= 0 < b.imag and cross_ab > 0:
            flag = not flag
    # Retourne 2 si le nombre de croisements est impair (point à l'intérieur), sinon 0
    return 2 if flag else 0

# --- Programme principal ---

# Utilisation de l'entrée standard pour la lecture des données
file_input = sys.stdin

# Lecture du nombre de sommets du polygone
n = int(file_input.readline())

# Construction de la liste des sommets du polygone sous forme complexe
polygon = [string_to_complex(file_input.readline()) for _ in range(n)]
# Fermeture du polygone en rajoutant le premier point à la fin
polygon.append(polygon[0])

# Lecture du nombre de points à tester
q = int(file_input.readline())

# Pour chaque point à tester, lire sa position, puis afficher où il se trouve par rapport au polygone
for line in file_input:
    t = string_to_complex(line)
    print(contains(polygon, t))