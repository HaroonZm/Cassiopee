from sys import stdin
readline = stdin.readline

def cross(a, b):
    """
    Calcule le produit vectoriel 2D de deux nombres complexes traités comme des vecteurs.

    Args:
        a (complex): Premier vecteur (point complexe).
        b (complex): Deuxième vecteur (point complexe).

    Returns:
        float: Résultat du produit vectoriel (a × b).
    """
    # Produit vectoriel en dimension 2 via parties réelle et imaginaire
    return a.real * b.imag - a.imag * b.real

def dot(a, b):
    """
    Calcule le produit scalaire de deux vecteurs représentés par des nombres complexes.

    Args:
        a (complex): Premier vecteur.
        b (complex): Deuxième vecteur.

    Returns:
        float: Le produit scalaire.
    """
    # Produit scalaire des deux vecteurs
    return a.real * b.real + a.imag * b.imag

def eq(a, b):
    """
    Détermine si deux nombres complexes sont égaux à une précision donnée.

    Args:
        a (complex): Premier nombre.
        b (complex): Deuxième nombre.

    Returns:
        bool: True si les valeurs sont considérées comme égales, False sinon.
    """
    # On utilise une tolérance pour compenser les imprécisions flottantes
    return abs(a - b) < 1e-10

def on_line(p, s, e):
    """
    Vérifie si le point p appartient au segment de droite [s, e].

    Args:
        p (complex): Point à tester.
        s (complex): Point de départ du segment.
        e (complex): Point d'arrivée du segment.

    Returns:
        bool: True si p est sur le segment [s, e], False sinon.
    """
    # Calcul du produit scalaire et vectoriel
    d = dot(p - s, e - s)
    c = cross(p - s, e - s)
    # Si cross == 0, les vecteurs sont colinéaires.
    # On vérifie alors si p est entre s et e.
    if c == 0 and 0 <= d <= abs(e - s) ** 2:
        return True
    return False

def on_polygon_line(xy, p):
    """
    Vérifie si le point xy est exactement sur un des côtés du polygone défini par p.

    Args:
        xy (complex): Point à vérifier.
        p (list of complex): Liste des sommets du polygone (dans l'ordre).

    Returns:
        bool: True si xy est sur un côté du polygone, False sinon.
    """
    # Parcourt tous les segments du polygone
    for i in range(len(p)):
        j = i - 1  # Préserve la liaison entre le dernier et le premier sommet
        if on_line(xy, p[i], p[j]):
            return True
    return False

def in_polygon(xy, p):
    """
    Détermine si le point xy se trouve à l'intérieur du polygone p à l'aide du winding number.

    Args:
        xy (complex): Point à tester.
        p (list of complex): Liste des sommets du polygone (dans l'ordre).

    Returns:
        int: Le winding number (nombre d'enroulements autour du point).
             S'il est 0, le point est à l'extérieur. Sinon, à l'intérieur.
    """
    wn = 0  # Initialisation du winding number
    for i in range(len(p)):
        j = i - 1  # Précédent sommet pour former l'arête (j, i)
        # On ignore les arêtes horizontales
        if 0 == (p[i] - p[j]).imag:
            continue
        vt = (xy - p[j]).imag / (p[i] - p[j]).imag
        tmp = p[j] + vt * (p[i] - p[j])  # Intersection potentielle avec la ligne horizontale passant par xy
        # On incrémente/décrémente en fonction de la traversée ascendante ou descendante
        if xy.real < tmp.real:
            wn += 1 if p[j].imag <= xy.imag < p[i].imag else\
                  -1 if p[i].imag <= xy.imag < p[j].imag else 0
    return wn

# Lecture du nombre de sommets du polygone
n = int(readline())
# Lecture des sommets du polygone, convertis en nombres complexes (x + yj)
p = [map(int, readline().split()) for _ in range(n)]
p = [x + y * 1j for x, y in p]

# Lecture du nombre de requêtes
q = int(readline())
for _ in range(q):
    # Lecture du point à tester
    x, y = map(int, readline().split())
    xy = x + y * 1j
    # Affiche 1 si sur le bord, 2 si à l'intérieur, sinon 0
    print(1 if on_polygon_line(xy, p) else 2 if in_polygon(xy, p) else 0)