def intersection_points_with_circle(cx, cy, r, queries):
    """
    Calcule les points d'intersection entre un cercle et plusieurs segments de droites.

    Args:
        cx (int): Abscisse du centre du cercle.
        cy (int): Ordonnée du centre du cercle.
        r (int): Rayon du cercle.
        queries (List[Tuple[int, int, int, int]]): Liste de tuples représentant les extrémités des segments
                                                  sous la forme (x1, y1, x2, y2) où (x1,y1) et (x2,y2)
                                                  sont les points de départ et d'arrivée du segment.

    Returns:
        List[Tuple[float, float, float, float]]: Liste contenant pour chaque requête un quadruplet
                                                 (ix1, iy1, ix2, iy2) représentant les coordonnées
                                                 des deux points d'intersection dans l'ordre demandé.
    """
    results = []
    for x1, y1, x2, y2 in queries:
        # Vecteur du segment de droite
        dx = x2 - x1
        dy = y2 - y1

        # Vecteur du point de départ du segment vers le centre du cercle
        px = cx - x1
        py = cy - y1

        # Longueur au carré du segment (pour éviter des racines inutiles)
        s2 = dx ** 2 + dy ** 2

        # Produit scalaire entre (dx,dy) et (px,py)
        dot = dx * px + dy * py

        # Produit vectoriel (utilisé pour la distance entre centre et segment)
        crs = dx * py - dy * px

        # Discriminant sous la racine, (s2*r^2 - crs^2) > 0 garantit l'intersection
        discriminant = s2 * r ** 2 - crs ** 2

        # Calcul des deux paramètres d'intersection t1 et t2
        t1 = (dot + discriminant ** 0.5) / s2
        t2 = (dot - discriminant ** 0.5) / s2

        # On peut avoir besoin d'intervertir selon l'orientation pour garantir le bon ordre
        if (dx < 0 or (dx == 0 and dy < 0)) ^ (t1 > t2):
            t1, t2 = t2, t1

        # Calcul des coordonnées des points d'intersection sur la ligne
        ix1 = x1 + dx * t1
        iy1 = y1 + dy * t1
        ix2 = x1 + dx * t2
        iy2 = y1 + dy * t2

        results.append((ix1, iy1, ix2, iy2))
    return results


def main():
    """
    Fonction principale qui lit les entrées, effectue les calculs et affiche les résultats.
    """
    # Lecture de la première ligne : centre et rayon du cercle
    cx, cy, r = map(int, input().split())
    # Lecture du nombre de requêtes (segments)
    q = int(input())

    queries = []
    for _ in range(q):
        # Lecture des coordonnées des deux extrémités pour chaque segment
        x1, y1, x2, y2 = map(int, input().split())
        queries.append((x1, y1, x2, y2))

    # Calcul des points d'intersection pour chaque segment
    intersections = intersection_points_with_circle(cx, cy, r, queries)

    # Affichage des résultats pour chaque segment
    for ix1, iy1, ix2, iy2 in intersections:
        print(ix1, iy1, ix2, iy2)


if __name__ == "__main__":
    main()