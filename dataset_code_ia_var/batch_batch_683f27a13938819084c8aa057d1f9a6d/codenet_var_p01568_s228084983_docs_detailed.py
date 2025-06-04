from collections import deque
import sys

# Aliases for input/output functions for efficiency
readline = sys.stdin.readline
write = sys.stdout.write

def dot3(O, A, B):
    """
    Calcule le produit scalaire de deux vecteurs OA et OB.

    Parameters:
        O (tuple): Point d'origine (ox, oy).
        A (tuple): Premier point (ax, ay).
        B (tuple): Second point (bx, by).

    Returns:
        int: Produit scalaire de OA et OB.
    """
    ox, oy = O
    ax, ay = A
    bx, by = B
    return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)

def cross3(O, A, B):
    """
    Calcule le déterminant vectoriel (produit vectoriel 2D) de OA et OB.

    Parameters:
        O (tuple): Point d'origine (ox, oy)
        A (tuple): Premier point (ax, ay)
        B (tuple): Second point (bx, by)

    Returns:
        int: Valeur du déterminant vectoriel.
    """
    ox, oy = O
    ax, ay = A
    bx, by = B
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)

def dist2(A, B):
    """
    Calcule la distance au carré entre deux points.

    Parameters:
        A (tuple): Premier point (ax, ay).
        B (tuple): Second point (bx, by).

    Returns:
        int: Distance euclidienne au carré entre A et B.
    """
    ax, ay = A
    bx, by = B
    return (ax - bx) ** 2 + (ay - by) ** 2

def is_intersection(L1, L2):
    """
    Détermine si deux segments (L1, L2) s'intersectent.

    Parameters:
        L1 (tuple): Segment 1, sous forme (x0, y0, x1, y1).
        L2 (tuple): Segment 2, sous forme (x2, y2, x3, y3).

    Returns:
        bool: True si les segments se croisent, False sinon.
    """
    P0 = L1[:2]
    P1 = L1[2:]
    Q0 = L2[:2]
    Q1 = L2[2:]
    C0 = cross3(P0, P1, Q0)
    C1 = cross3(P0, P1, Q1)
    D0 = cross3(Q0, Q1, P0)
    D1 = cross3(Q0, Q1, P1)
    if C0 == C1 == 0:
        # Segments colinéaires, pas d'intersection unique
        return False
    return C0 * C1 <= 0 and D0 * D1 <= 0

def cross_point(L1, L2):
    """
    Calcule le point d'intersection de deux segments (supposés sécants).

    Parameters:
        L1 (tuple): Segment 1, sous forme (x0, y0, x1, y1).
        L2 (tuple): Segment 2, sous forme (x2, y2, x3, y3).

    Returns:
        tuple: Coordonnées (x, y) du point d'intersection.
    """
    x0, y0, x1, y1 = L1
    x2, y2, x3, y3 = L2
    dx0 = x1 - x0
    dy0 = y1 - y0
    dx1 = x3 - x2
    dy1 = y3 - y2

    s = (y0 - y2) * dx1 - (x0 - x2) * dy1
    sm = dx0 * dy1 - dy0 * dx1
    if s < 0:
        s = -s
        sm = -sm
    if s == 0:
        # Intersection au début du segment
        x = x0
        y = y0
    elif s == sm:
        # Intersection à la fin du segment
        x = x1
        y = y1
    else:
        x = x0 + s * dx0 / sm
        y = y0 + s * dy0 / sm
    return x, y

def solve():
    """
    Solution principale du problème :
    - Lit la description des segments, obstacles, points de départ et d'arrivée.
    - Construit le graphe d'adjacence représentant les chemins sur les segments sans obstacles.
    - Effectue deux parcours en largeur pour déterminer le minimum de chemin restant ou si un chemin est bloqué.
    - Affiche la longueur totale des parties accessibles (hors obstacles et zone bloquée).

    Entrée :
        Voir description initiale (stdin).

    Sortie :
        -1 si un chemin direct existe de l'arrivée à la sortie; sinon, la longueur totale des arcs accessibles.
    """
    # Lecture du nombre de segments (N) et d'obstacles (M)
    N, M = map(int, readline().split())

    # Dictionnaire associant à chaque point son type (libre, obstacle, extrémité)
    mp = {}
    LS = []  # Liste des segments [(x1, y1, x2, y2)]

    # Lecture des segments, enregistrement des extrémités
    for i in range(N):
        x1, y1, x2, y2 = map(int, readline().split())
        mp[x1, y1] = 0  # 0 = point libre
        mp[x2, y2] = 0
        LS.append((x1, y1, x2, y2))

    # Ajout des points d'intersection entre segments
    for i in range(N):
        L1 = LS[i]
        for j in range(i+1, N):
            L2 = LS[j]
            if is_intersection(L1, L2):
                x, y = cross_point(L1, L2)
                mp[x, y] = 0

    # Lecture des obstacles et marquage (valeur 1)
    for i in range(M):
        x, y = map(int, readline().split())
        mp[x, y] = 1

    # Lecture de l'arrivée et du départ, marquage (valeur 2)
    xb, yb = map(int, readline().split())  # sortie
    mp[xb, yb] = 2
    xc, yc = map(int, readline().split())  # entrée
    mp[xc, yc] = 2

    # Construction des listes de points avec tri pour ordonner les sommets
    ps1 = list(mp.keys())
    ps1.sort(key = lambda x: (x[0], x[1]))  # tri par abscisse puis ordonnée
    mv = {e: i for i, e in enumerate(ps1)}  # mapping point -> index
    ps2 = list(mp.keys())
    ps2.sort(key = lambda x: (x[1], x[0]))  # tri par ordonnée puis abscisse

    # Les arêtes du graphe (chaque segment, subdivisé à ses intersections)
    ES = []
    ms = list(map(mv.__getitem__, ps2))  # indices relatifs à ps2 dans l'ordre trié par y,x
    ks = list(map(mp.__getitem__, ps1))  # type de chaque point dans l'ordre ps1
    K = len(ps1)  # nombre de sommets

    G = [[] for i in range(K)]  # liste d'adjacence pour les sommets

    # Construction du graphe d'adjacence
    for x1, y1, x2, y2 in LS:
        vs = []  # liste des indices des points sur le segment courant
        if x1 != x2:
            # Segment non vertical : progression par x
            if not x1 <= x2:
                x1, y1, x2, y2 = x2, y2, x1, y1  # renversement pour assurer l'ordre croissant en x
            for k, (x, y) in enumerate(ps1):
                # Point sur le segment ? Test par équation paramétrique et epsilon
                if x1 <= x <= x2 and abs((x - x1)*(y2 - y1) - (y - y1)*(x2 - x1)) < 1e-6:
                    vs.append(k)
        else:
            # Segment vertical : progression par y
            if not y1 <= y2:
                y1, y2 = y2, y1
            for k, (x, y) in zip(ms, ps2):
                if y1 <= y <= y2 and abs((x - x1)*(y2 - y1) - (y - y1)*(x2 - x1)) < 1e-6:
                    vs.append(k)
        # Création des arêtes entre les points consécutifs du segment
        for i in range(len(vs) - 1):
            k1 = vs[i]
            k2 = vs[i + 1]
            G[k1].append(k2)
            G[k2].append(k1)
            ES.append((k1, k2) if k1 <= k2 else (k2, k1))

    # Récupération des indices des points d'entrée (départ) et sortie
    s = mv[xc, yc]  # point d'entrée
    t = mv[xb, yb]  # point de sortie

    # Premier parcours : depuis l'entrée, éviter d'atteindre la sortie
    que = deque([s])
    used = [0] * K  # marque pour les sommets visités
    used[s] = 1
    e_used = set()  # arêtes traversées dans ce BFS

    while que:
        v = que.popleft()
        for w in G[v]:
            if w == t:
                # Si la sortie est accessible directement, on retourne -1
                write("-1\n")
                return
            # Marque l'arête utilisée
            e_used.add((v, w) if v <= w else (w, v))
            # Ne pas traverser les obstacles
            if not used[w] and ks[w] != 1:
                que.append(w)
            used[w] = 1

    # Second parcours : propagation à partir de la sortie, sans retraverser les arêtes déjà utilisées
    que.append(t)
    e_used1 = set()
    used = [0] * K
    used[t] = 1

    while que:
        v = que.popleft()
        for w in G[v]:
            e = (v, w) if v <= w else (w, v)
            if e in e_used:
                continue
            e_used1.add(e)
            if not used[w]:
                que.append(w)
                used[w] = 1

    # Calcul de la longueur totale des arêtes utilisables dans le graphe résultant
    ans = 0
    for k1, k2 in ES:
        if (k1, k2) in e_used1:
            continue
        x1, y1 = ps1[k1]
        x2, y2 = ps1[k2]
        ans += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    write("%.16f\n" % ans)

# Appel de la fonction principale pour résoudre le problème dès l'exécution
solve()