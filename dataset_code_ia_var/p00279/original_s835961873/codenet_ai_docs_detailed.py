import sys
import operator
import math

def triangle(a, b, c):
    """
    Calcule l'aire du triangle formé par trois points du plan complexe.

    Args:
        a (complex): Premier sommet du triangle.
        b (complex): Deuxième sommet du triangle.
        c (complex): Troisième sommet du triangle.

    Returns:
        float: Aire orientée du triangle (valeur positive ou négative selon l'orientation).
    """
    return cross(b - a, c - a) / 2

def cos(a, b):
    """
    Calcule le cosinus de l'angle entre deux vecteurs du plan complexe.

    Args:
        a (complex): Premier vecteur.
        b (complex): Deuxième vecteur.

    Returns:
        float: Cosinus de l'angle entre les deux vecteurs.
    """
    return dot(a, b) / (abs(a) * abs(b))

def dot(a, b):
    """
    Calcule le produit scalaire de deux vecteurs du plan complexe.

    Args:
        a (complex): Premier vecteur.
        b (complex): Deuxième vecteur.

    Returns:
        float: Produit scalaire de a et b.
    """
    return a.real * b.real + a.imag * b.imag

def cross(a, b):
    """
    Calcule le produit vectoriel (orientation) de deux vecteurs du plan complexe.

    Args:
        a (complex): Premier vecteur.
        b (complex): Deuxième vecteur.

    Returns:
        float: Résultat du produit vectoriel (déterminant).
    """
    return a.real * b.imag - a.imag * b.real

def solve(xyi, xy):
    """
    Trouve pour chaque k (3 <= k <= max(q)) le plus petit polygone convexe d'aire minimale
    construit à partir du point xyi et des autres points xy, en ajoutant ce point à tous
    les polygones construits avec les autres points.

    Args:
        xyi (complex): Point d'origine à inclure dans chaque polygone.
        xy (list of complex): Autres points.

    Returns:
        list: Pour chaque k, tuple (aire min, tuple des sommets). Indice k.
    """
    # Tri des points par ordre trigonométrique autour de xyi (par rapport à l'axe Ox positif)
    # On tri par le cosinus de l'angle avec l'axe (1, 0)
    xy = sorted(xy, key=lambda a: (a.real - xyi.real) / abs(a - xyi), reverse=True)

    # Initialisation de la table des aires minimales
    # area[i][j][k] : aire min et sommets pour le polygone de taille i, se terminant aux indices j, k
    area = [[[(float('inf'),) for _ in range(len(xy))] for _ in range(len(xy))] for _ in range(max(q) + 1)]

    # Remplissage de la table pour les triangles (base de la récurrence dynamique)
    for j in range(len(xy) - 1):
        for k in range(j + 1, len(xy)):
            # Triangle formé par xyi, xy[j], xy[k]
            area[3][j][k] = (triangle(xyi, xy[j], xy[k]), (xyi, xy[j], xy[k]))

    # Construction dynamique pour polygones plus grands (carrés, pentagones, etc.)
    for i in range(4, max(q) + 1):
        for j in range(len(xy)):
            for k in range(j + 1, len(xy)):
                for s in range(k + 1, len(xy)):
                    # Si aucune solution pour ce sous-polygone, on saute
                    if math.isinf(area[i - 1][j][k][0]):
                        continue
                    # Vérifie que le nouveau triangle (pour convexitée) est convexe
                    if triangle(xy[j], xy[k], xy[s]) <= 0:
                        # Si pas convexe, on saute la combinaison
                        continue
                    # Calcule l'aire totale d'ajouter le triangle [xy[k], xy[s]] à la plus petite aire précédente
                    tmp = area[3][k][s][0] + area[i - 1][j][k][0]
                    # On garde la meilleure solution, i.e. la plus petite aire
                    if not math.isnan(area[i][k][s][0]) and area[i][k][s][0] < tmp:
                        continue
                    area[i][k][s] = (tmp, area[i - 1][j][k][1] + (xy[s],))

    # Recherche, pour chaque taille de polygone, la plus petite aire trouvée
    min_space = [(float('inf'),)] * (max(q) + 1)
    for i in range(3, max(q) + 1):
        # On récupère le tuple (aire, sommets) correspondant à l'aire minimale
        min_space[i] = min([y for x in area[i] for y in x], key=operator.itemgetter(0))

    return min_space

# ----- Lecture des données et prétraitement -----

f = sys.stdin

# Lecture des points
# Chaque point est défini par ses coordonnées x et y
xy = [[int(i) for i in f.readline().split()] for _ in range(int(f.readline()))]

# Lecture des requêtes : pour chaque requête on veut le plus petit polygone de taille q[i]
q = [int(f.readline()) for _ in range(int(f.readline()))]

# On convertit chaque point en nombre complexe pour simplifier les calculs géométriques
xy = [x + y * 1j for x, y in xy]

# On conserve un dictionnaire pour convertir les objets complexes en indices pour l'affichage
id = {xyi: i + 1 for i, xyi in enumerate(xy)}

# Tri du tableau de points pour un ordre de traitement cohérent (d'abord imaginaire, puis réel)
xy.sort(key=operator.attrgetter('imag', 'real'))

# Initialisation de la liste des meilleures aires pour chaque valeur de q
min_space = [(float('inf'),) for _ in range(max(q) + 1)]

# On considère chaque point comme origine une seule fois, puis supprime ce point pour éviter répétition
while len(xy) > 2:
    xyi = xy.pop(0)  # Point d'origine du polygone courant
    # Mise à jour de la liste des meilleures aires : on compare chaque solution et garde la meilleure (plus petite aire)
    min_space = [
        min(i, j, key=operator.itemgetter(0))
        for i, j in zip(min_space, solve(xyi, xy))
    ]

# ----- Affichage des résultats -----

for qi in q:
    # Si aucune solution possible pour ce qi (polygone impossible), on affiche NA
    if math.isinf(min_space[qi][0]):
        print('NA')
    else:
        # Sinon, on affiche les indices des sommets du polygone de plus petite aire
        print(*[id[i] for i in min_space[qi][1]])