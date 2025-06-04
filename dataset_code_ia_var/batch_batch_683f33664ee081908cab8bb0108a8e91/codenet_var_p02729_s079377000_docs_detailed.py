def calculate_pairs(n, m):
    """
    Calcule le nombre de paires possibles dans une grille n x m selon les règles suivantes :
    - Si n ou m vaut 1, le nombre de paires est le nombre de connexions possibles sur la ligne/colonne.
    - Sinon, c'est la somme des connexions horizontales et verticales dans la grille.

    Args:
        n (int): Le nombre de lignes de la grille.
        m (int): Le nombre de colonnes de la grille.

    Returns:
        int: Le nombre total de paires selon les règles ci-dessus.
    """
    # Si la grille a une seule ligne
    if n == 1:
        if m == 1:
            # Il n'y a qu'une seule case, donc pas de paire possible
            return 0
        else:
            # Sur une seule ligne de m cases, on compte les paires distinctes possibles
            return int(m * (m - 1) / 2)
    else:
        # Si la grille a une seule colonne
        if m == 1:
            # Une seule colonne de n cases : paires le long de la colonne
            return int(n * (n - 1) / 2)
        else:
            # Sinon, grille avec au moins 2 lignes et colonnes :
            # On additionne les paires sur chaque ligne et colonne
            return int((n * (n - 1) + m * (m - 1)) / 2)

def main():
    """
    Fonction principale. Lit deux entiers depuis l'entrée standard,
    calcule et affiche le nombre de paires possibles dans une grille de taille n x m.
    """
    # Lecture de deux entiers séparés par un espace
    n, m = map(int, input().split())
    # Calcul du résultat avec la fonction dédiée
    result = calculate_pairs(n, m)
    # Affichage du résultat final
    print(result)

if __name__ == "__main__":
    main()