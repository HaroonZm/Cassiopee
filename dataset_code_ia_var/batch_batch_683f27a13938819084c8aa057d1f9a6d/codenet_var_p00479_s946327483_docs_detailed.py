def get_minimum_color(n, a, b):
    """
    Calcule la couleur minimale assignée à une position de la grille.

    La couleur est déterminée par la formule :
    min(a-1, n-a, b-1, n-b) % 3 + 1

    Args:
        n (int): Taille de la grille (nombre de lignes/colonnes).
        a (int): Numéro de ligne (1-based).
        b (int): Numéro de colonne (1-based).

    Returns:
        int: Couleur minimale attribuée à la case.
    """
    # Calcul de la distance minimale de la case aux bords de la grille
    min_dist = min(a - 1, n - a, b - 1, n - b)
    # Calcul et renvoi de la couleur selon l'expression donnée
    return min_dist % 3 + 1


def main():
    """
    Fonction principale qui lit les entrées, traite chaque requête, et affiche le résultat.

    1. Lit la taille de la grille.
    2. Pour chaque requête, lit les coordonnées et affiche la couleur minimale de cette case.
    """
    # Lecture de la taille de la grille (N)
    N = int(input())
    # Lecture du nombre de requêtes
    Q = int(input())
    for _ in range(Q):
        # Lecture des coordonnées a et b pour chaque requête (entrée utilisateur, séparée par un espace)
        a, b = map(int, input().split())
        # Calcul et affichage de la couleur assignée
        print(get_minimum_color(N, a, b))


if __name__ == "__main__":
    main()