def find_min_enclosing_sphere_radius(stars):
    """
    Calcule le rayon du plus petit cercle englobant toutes les étoiles (points 3D) en utilisant une méthode heuristique.

    Args:
        stars (list of list of float): Liste des coordonnées de chaque étoile sous forme [x, y, z].

    Returns:
        float: Rayon du plus petit cercle englobant.
    """
    n = len(stars)
    # Initialisation du centre à l'origine
    center = [0.0, 0.0, 0.0]
    # Amplitude initiale du déplacement à chaque itération
    move = 0.5

    # Procédure itérative pour placer le centre approximativement
    for _ in range(500):
        for _ in range(100):
            max_dist_sq = 0  # Carré de la distance maximale centre-étoile
            idx_furthest = 0
            # Recherche de l’étoile la plus éloignée du centre courant
            for i in range(n):
                dist_sq = sum((stars[i][d] - center[d]) ** 2 for d in range(3))
                if dist_sq > max_dist_sq:
                    max_dist_sq = dist_sq
                    idx_furthest = i
            # Déplacement du centre vers l’étoile la plus lointaine selon le ratio move
            center = [
                center[d] - (center[d] - stars[idx_furthest][d]) * move
                for d in range(3)
            ]
        # Réduction du pas de déplacement pour raffiner l’estimation
        move /= 2

    # Calcul du rayon en recherchant la distance maximale au centre final
    max_dist_sq = 0
    for i in range(n):
        dist_sq = sum((stars[i][d] - center[d]) ** 2 for d in range(3))
        if dist_sq > max_dist_sq:
            max_dist_sq = dist_sq
    return round(max_dist_sq ** 0.5, 5)


def main():
    """
    Point d'entrée principal du programme.
    Lit les jeux de données depuis l'entrée utilisateur, calcule et affiche le rayon du plus petit cercle englobant pour chaque ensemble d'étoiles.
    """
    while True:
        try:
            # Lecture du nombre d'étoiles à traiter
            n = int(input())
            if n == 0:
                break  # Fin de la saisie
            # Lecture des positions des étoiles, conversion en float et stockage en liste
            stars = [list(map(float, input().split())) for _ in range(n)]
            # Calcul et affichage du rayon minimal recherché
            print(find_min_enclosing_sphere_radius(stars))
        except Exception:
            # Gestion d'une éventuelle erreur d'entrée ou d'exécution
            break


if __name__ == "__main__":
    main()