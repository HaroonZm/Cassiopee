import sys

def read_points(n):
    """
    Lit n points à partir de l'entrée standard, chaque point étant une liste de deux entiers [x, y].
    
    Args:
        n (int): Le nombre de points à lire.

    Returns:
        List[List[int]]: Une liste des points lus.
    """
    points = []
    for _ in range(n):
        line = sys.stdin.readline()
        coords = [int(x) for x in line.split()]
        points.append(coords)
    return points

def min_squared_distance_between_points(polygon1, polygon2):
    """
    Calcule la distance minimale au carré entre tous les sommets entre deux polygones.
    
    Args:
        polygon1 (List[List[int]]): Liste des sommets du premier polygone.
        polygon2 (List[List[int]]): Liste des sommets du second polygone.

    Returns:
        float: La distance minimale au carré entre tous les sommets.
    """
    min_dist_sq = float('inf')
    for x1, y1 in polygon1:
        for x2, y2 in polygon2:
            r = (x1 - x2) ** 2 + (y1 - y2) ** 2
            if r < min_dist_sq:
                min_dist_sq = r
    return min_dist_sq

def min_squared_distance_point_to_edges(points, poly_edges):
    """
    Calcule la distance minimale au carré d'un ensemble de points à chaque arête définie par deux sommets consécutifs d'un polygone.

    Pour chaque point de `points`, et pour chaque segment d'arête dans `poly_edges`, calcule la distance perpendiculaire au segment
    si la projection du point est entre les extrémités du segment.

    Args:
        points (List[List[int]]): Liste de points sous forme [x, y].
        poly_edges (List[List[int]]): Liste de sommets du polygone, l'arête considered est entre poly_edges[i] et poly_edges[i+1].

    Returns:
        float: La distance minimale au carré rencontrée.
    """
    m = len(poly_edges) - 2  # Le nombre initial de sommets retiré de 2, car on a ajouté deux points sentinelles
    min_dist_sq = float('inf')
    for x, y in points:
        for i in range(m + 1):
            p, q = poly_edges[i]      # Premier sommet du segment
            s, t = poly_edges[i + 1]  # Second sommet du segment
            # Calcul des vecteurs de l'arête
            a = t - q
            b = p - s
            # Vérifie si la projection du point sur la droite du segment tombe effectivement sur le segment
            if (b * (s - x) - a * (t - y)) * (b * (p - x) - a * (q - y)) < 0:
                # Si oui, calculer la distance perpendiculaire de ce point à l'arête
                c = -a * p - b * q
                d = (a * x + b * y + c) ** 2
                d /= (a ** 2 + b ** 2)  # Division par la norme au carré du vecteur directeur
                if d < min_dist_sq:
                    min_dist_sq = d
    return min_dist_sq

def main():
    """
    Point d'entrée principal du script.
    Lit les deux polygones depuis stdin, ajoute des points sentinelles, puis calcule
    et affiche la distance minimale entre les polygones.
    """
    # Lire le nombre de sommets du premier polygone
    n = int(sys.stdin.readline())
    p1 = read_points(n)
    # Ajouter les points sentinelles conformément à la logique du problème
    p1.insert(0, [0, 0])        # Ajoute le point [0,0] au début (coin inférieur gauche)
    p1.append([1000, 0])        # Ajoute le point [1000,0] à la fin (coin inférieur droit)

    # Lire le nombre de sommets du second polygone
    m = int(sys.stdin.readline())
    p2 = read_points(m)
    # Ajouter les points sentinelles pour le second polygone
    p2.insert(0, [0, 1000])     # Ajoute [0,1000] (coin supérieur gauche)
    p2.append([1000, 1000])     # Ajoute [1000,1000] (coin supérieur droit)

    # Initialisation de la distance minimale à l'infini
    ans = float('inf')

    # Calcul des distances entre tous les sommets des deux polygones
    ans = min(ans, min_squared_distance_between_points(p1, p2))

    # Calcul de la distance minimale entre chaque sommet du premier polygone
    # et chaque arête du second polygone
    ans = min(ans, min_squared_distance_point_to_edges(p1, p2))

    # Calcul de la distance minimale entre chaque sommet du second polygone
    # et chaque arête du premier polygone
    ans = min(ans, min_squared_distance_point_to_edges(p2, p1))

    # Afficher la racine carrée de la distance minimale trouvée
    print(ans ** 0.5)

if __name__ == "__main__":
    main()