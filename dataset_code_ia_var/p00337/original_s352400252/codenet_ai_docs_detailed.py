import sys

def graham_scan(vertices: list):
    """
    Implémente l'algorithme de Graham Scan pour calculer l'enveloppe convexe d'un ensemble de points.

    Args:
        vertices (list): Liste des sommets, chaque sommet étant une liste ou un tuple contenant au moins deux coordonnées et un identifiant (x, y, ...).

    Returns:
        list: Liste ordonnée des sommets qui forment l'enveloppe convexe, dans le sens antihoraire.
    """
    from math import atan2
    from operator import itemgetter

    # Trie les points par ordonnée croissante (puis abscisse en cas d'égalité)
    vertices.sort(key=itemgetter(1))
    # Le point de référence (le plus bas, voire le plus à gauche en cas d'égalité)
    base_x, base_y = vertices[0][:2]

    # Trie les autres points selon l'angle polaire par rapport à ce point de référence
    vertices = sorted(vertices[1:], key=lambda p: atan2(p[1]-base_y, p[0]-base_x)) + vertices[:1]
    convex = vertices[-1:] + vertices[:1]  # Démarrage de la pile de l'enveloppe (back + first)
    pop, append = convex.pop, convex.append
    last_x, last_y = convex[-1][:2]

    # Parcours chaque point trié par ordre angulaire
    for point, (x, y, *_) in zip(vertices[1:], vertices[1:]):
        # Tant que les trois derniers points ne forment pas un tournant à gauche, on retire l'avant-dernier
        while ((x - last_x) * (convex[-2][1] - last_y) -
               (y - last_y) * (convex[-2][0] - last_x) < 0):
            pop()
            last_x, last_y = convex[-1][:2]
        append(point)
        last_x, last_y = x, y

    # Retourne les sommets de l'enveloppe sans répéter le premier/dernier
    return convex[:-1]


def kruskal(v_count: int, edges: list, border_edges: list) -> int:
    """
    Implémente l'algorithme de Kruskal pour calculer le coût d'un arbre couvrant minimal,
    intégrant obligatoirement certains arêtes frontières (edges de la frontière de l'enveloppe convexe).

    Args:
        v_count (int): Nombre total de sommets.
        edges (list): Liste des arêtes disponibles au format (poids, sommet1, sommet2).
        border_edges (list): Liste des arêtes obligatoires (issues de l'enveloppe convexe).

    Returns:
        int: Coût total de l'arbre couvrant minimal incluant les arêtes frontières.
    """
    from itertools import islice

    tree = [-1] * v_count  # Structure de l'arbre pour l'union-find (disjoint-set)

    def get_root(x) -> int:
        """
        Trouve la racine de l'ensemble d'un sommet, avec compression de chemin.

        Args:
            x (int): Indice du sommet.

        Returns:
            int: Indice de la racine de l'ensemble.
        """
        if tree[x] < 0:
            return x
        tree[x] = get_root(tree[x])
        return tree[x]

    def unite(a) -> bool:
        """
        Réalise l'union des ensembles contenant deux sommets, si différents.

        Args:
            a (tuple): Triple (x, y, z), où y et z sont les sommets à unir.

        Returns:
            bool: True si une union a eu lieu, False sinon.
        """
        x, y = get_root(a[1]), get_root(a[2])
        if x != y:
            big, small = (x, y) if tree[x] < tree[y] else (y, x)
            tree[big] += tree[small]
            tree[small] = big
        return x != y

    cost = 0

    # Intègre d'abord toutes les arêtes imposées par l'enveloppe convexe (frontières)
    for c, s, t in border_edges:
        cost += c
        unite((0, s, t))
    # Met à jour le nombre de sommets à relier dans l'arbre restant
    v_count -= len(border_edges) - 1

    # Parcourt les autres arêtes dans l'ordre croissant des poids
    # et ajoute celles qui relient deux composantes différentes (arbre couvrant)
    for w, _s, _t in islice(filter(unite, sorted(edges)), v_count - 1):
        cost += w
    return cost


if __name__ == "__main__":
    from math import hypot

    # Lecture des paramètres d'entrée (nombre de sommets et de liaisons)
    V, R = map(int, input().split())

    # Lecture des coordonnées de sommets, chaque sommet ayant une position et un identifiant unique
    vertices = [list(map(int, sys.stdin.readline().split())) + [i] for i in range(V)]

    # Lecture des arêtes potentielles, calcul de leur poids (distance euclidienne entre les sommets concernés)
    edges = [
        (hypot(vertices[s-1][0] - vertices[t-1][0], vertices[s-1][1] - vertices[t-1][1]), s-1, t-1)
        for l in sys.stdin for s, t in (map(int, l.split()),)
    ]

    # Calcul de l'enveloppe convexe pour déterminer les sommets sur le bord
    convex = graham_scan(vertices)

    # Génération de la liste des arêtes formant la frontière de l'enveloppe convexe
    border_edges = [
        (hypot(x1 - x2, y1 - y2), s, t)
        for (x1, y1, s), (x2, y2, t) in zip(convex, convex[1:] + convex[:1])
    ]

    # Calcul du coût minimal de l'arbre couvrant qui intègre obligatoirement les arêtes de la frontière
    cost = kruskal(V, edges, border_edges)

    # Affichage du résultat
    print(cost)