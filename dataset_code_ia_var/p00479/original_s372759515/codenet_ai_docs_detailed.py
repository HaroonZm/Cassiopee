def main():
    """
    Fonction principale qui lit deux entiers depuis l'entrée standard :
    - N : un entier représentant la taille d'une séquence ou d'une grille.
    - M : un entier représentant le nombre de requêtes à traiter.

    Pour chaque requête, lit deux entiers a et b, effectue un calcul sur ces valeurs
    selon leur position par rapport aux bords (supposé d'une grille N x N), puis
    affiche un entier entre 1 et 3 inclus (calculé via une opération modulo).
    """
    # Lecture de la taille, supposée être la taille d'une grille ou d'une séquence
    N = int(input())

    # Lecture du nombre de requêtes à traiter
    M = int(input())

    # Chaque requête prend les valeurs (a, b)
    for _ in range(M):
        # Lecture de deux entiers a et b
        a, b = map(int, input().split())

        # Calcul de la distance minimum aux bords pour les coordonnées a et b
        dist_a = min(a - 1, N - a)
        dist_b = min(b - 1, N - b)

        # Prend la valeur minimale entre la distance à un bord vertical ou horizontal
        min_dist = min(dist_a, dist_b)

        # Le résultat est la valeur minimale modulo 3, plus 1 (pour être dans [1, 3])
        result = (min_dist % 3) + 1

        # Affiche le résultat pour la requête en cours
        print(result)

# Appel de la fonction principale uniquement si le script est exécuté directement
if __name__ == "__main__":
    main()