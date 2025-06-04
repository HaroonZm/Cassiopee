def main():
    """
    Fonction principale qui lit la taille N de la grille puis, pour chaque requête, 
    lit deux entiers a et b représentant une position sur la grille et calcule
    une valeur basée sur la distance minimale à partir des bords, modulo 3, puis affiche le résultat.
    """
    # Lit la taille de la grille (N)
    N = input()
    # Lit le nombre de requêtes (Q)
    Q = input()
    # Pour chaque requête
    for _ in [1] * Q:
        # Lit les coordonnées a et b séparées par un espace
        a, b = map(int, raw_input().split())
        # Calcule la distance minimale aux bords pour a et b
        min_dist_a = min(a - 1, N - a)  # Distance ligne du bord le plus proche
        min_dist_b = min(b - 1, N - b)  # Distance colonne du bord le plus proche
        min_layer = min(min_dist_a, min_dist_b)
        # Le résultat est le numéro de la couche modulo 3, plus 1 (pour avoir des valeurs de 1 à 3)
        result = (min_layer % 3) + 1
        # Affiche le résultat pour cette case
        print(result)

# Appel de la fonction principale si ce script est exécuté directement
if __name__ == "__main__":
    main()