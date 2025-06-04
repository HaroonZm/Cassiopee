def cross(z1, z2):
    """
    Calcule le produit vectoriel (cross product) de deux nombres complexes vus comme des points dans le plan.

    Args:
        z1 (complex): Premier point complexe.
        z2 (complex): Deuxième point complexe.

    Returns:
        float: Valeur du produit vectoriel (z1, z2).
    """
    return z1.real * z2.imag - z1.imag * z2.real

def ccw(p1, p2, p3):
    """
    Détermine si les trois points forment un angle orienté dans le sens anti-horaire (counter-clockwise).

    Args:
        p1 (complex): Premier point.
        p2 (complex): Deuxième point.
        p3 (complex): Troisième point.

    Returns:
        bool: True si les points forment un angle orienté anti-horaire, False sinon.
    """
    return cross(p2 - p1, p3 - p1) > 0

def triangle_area(p1, p2, p3):
    """
    Calcule l'aire signée du triangle défini par trois points.

    Args:
        p1 (complex): Premier sommet.
        p2 (complex): Deuxième sommet.
        p3 (complex): Troisième sommet.

    Returns:
        float: Aire signée du triangle.
    """
    return cross(p2 - p1, p3 - p1) / 2

from sys import stdin

# Entrée des données
file_input = stdin

# Lecture du nombre de points
N = int(file_input.readline())

# Liste des points (représentés comme complexes)
P = []
# Dictionnaire pour retrouver l'indice d'origine d'un point
M = {}

for i in range(1, N + 1):
    # Lecture des coordonnées d'un point, conversion en entier
    x, y = map(int, file_input.readline().split())
    z = x + y * 1j   # Stockage sous forme de nombre complexe
    P.append(z)
    M[z] = i         # Association du point à son indice d'entrée (1-based)

# Lecture du nombre de requêtes
Q = int(file_input.readline())

# Lecture des tailles recherchées pour les polygones convexes
query = [int(file_input.readline()) for _ in range(Q)]

# Taille maximale de polygone à construire (plus grande taille demandée - 2)
ql = max(query) - 2

# On trie les points par ordonnée, puis abscisse
P.sort(key=lambda x: (x.imag, x.real))

# Définition pratique : aire maximale possible (assure l’init de la recherche min)
max_area = 20000 * 20000
CP_area = [max_area for _ in range(ql)]   # Pour chaque taille de polygone, la plus petite aire trouvée (initialisée au max)
CP_points = [None for _ in range(ql)]     # Liste des points constituant le meilleur polygone pour chaque taille

from cmath import phase
from itertools import combinations

# Parcours de tous les points comme point de base bp pour construire des triangles & polygones
for i, bp in enumerate(P[:-2], start=1):
    tP = P[i:]  # Points à droite dans l’ordre
    tP.sort(key=lambda x: phase(x - bp))  # Triés par angle par rapport à bp
    
    pn = N - i  # Nombre de points restants
    
    # tM associe un id (local) à chaque point de tP
    tM = dict(zip(range(pn), tP))
    
    # Création de tous les triangles possibles avec bp et deux autres points formant un angle strictement croissant
    t_rec = [[None for _ in range(pn)] for _ in range(pn)]
    for j, k in combinations(range(pn), 2):
        pj, pk = tM[j], tM[k]
        ta = triangle_area(bp, pj, pk)
        t_rec[j][k] = [ta, [bp, pj, pk]]  # Stocke aire et liste de points
        if ta < CP_area[0]:
            CP_area[0] = ta
            CP_points[0] = [bp, pj, pk]
    
    # Préparation à l'extension des triangles en polygones convexes de taille > 3 avec dp
    prev = t_rec.copy()   # 'prev' garde les polygones trouvés à la taille précédente
    cur = [[None for _ in range(pn)] for _ in range(pn)]
    
    # Pour chaque taille de polygone >= 4 (i commence à 1, donc polygone de taille 4)
    for l in range(1, ql):
        for j, k, s in combinations(range(pn), 3):
            pre_cp = prev[j][k]
            if pre_cp:
                pj, pk, ps = tM[j], tM[k], tM[s]
                # On vérifie que l’ajout du point ps conserve la convexité
                if ccw(pj, pk, ps):
                    ta = pre_cp[0] + t_rec[k][s][0]
                    # Si un meilleur polygone (plus petite aire) est trouvé pour cette terminaison, on remplace
                    if not cur[k][s] or cur[k][s][0] > ta:
                        cur[k][s] = [ta, pre_cp[1] + [ps]]
                        if ta < CP_area[l]:
                            CP_area[l] = ta
                            CP_points[l] = cur[k][s][1]
        # Passage à la taille suivante de polygone
        prev = cur.copy()
        cur = [[None for _ in range(pn)] for _ in range(pn)]

# Sortie des résultats pour chaque requête
for q in query:
    # Si un polygone correspondant a été trouvé, on renvoie la liste des indices d'origine des sommets
    if CP_points[q-3]:
        print(' '.join(map(lambda x: str(M[x]), CP_points[q-3])))
    else:
        # Sinon, on indique qu'aucune solution n'existe
        print("NA")