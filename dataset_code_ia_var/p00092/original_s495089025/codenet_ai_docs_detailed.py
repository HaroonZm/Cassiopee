def read_input():
    """
    Lit un entier depuis l'entrée standard.

    Returns:
        int: L'entier lu.
    """
    return int(input())


def read_table(n):
    """
    Lit une grille de taille n x n depuis l'entrée standard.

    Args:
        n (int): La taille de la grille à lire.

    Returns:
        list of str: La grille lue, chaque case étant une chaîne de caractères.
    """
    grid = [''] * n
    for r in range(n):
        grid[r] = input()
    return grid


def largest_empty_square(table, n, dp):
    """
    Détermine la taille maximale d'un carré sans obstacle dans la grille.

    Args:
        table (list of str): La grille de caractères, '*' pour obstacle, '.' pour libre.
        n (int): Taille de la grille (n x n).
        dp (list of list of int): Tableau pour la programmation dynamique.

    Returns:
        int: La taille du plus grand carré sans obstacle.
    """
    max_size = 0  # Taille maximale du carré trouvée

    for r in range(n):
        for c in range(n):
            if table[r][c] == '*':
                # Si obstacle, pas de carré possible finissant ici
                dp[r][c] = 0
            else:
                # On cherche la taille minimale parmi les 3 cases voisines (haut, gauche, haut-gauche)
                # Elles correspondent aux coins pouvant agrandir le carré actuel
                t = dp[r-1][c-1]
                if dp[r][c-1] < t:
                    t = dp[r][c-1]
                if dp[r-1][c] < t:
                    t = dp[r-1][c]
                t += 1
                dp[r][c] = t
                if t > max_size:
                    max_size = t
    return max_size


def main():
    """
    Fonction principale du programme.
    Pour chaque grille lue, affiche la taille du plus grand carré sans obstacle.
    Arrête la lecture lorsqu'un 0 est rencontré en entrée.
    """
    # Pré-allocation de la table et du tableau dp pour des performances maximales (jusqu'à 1002 x 1002)
    table = [''] * 1002
    dp = [[0] * 1002 for _ in range(1002)]

    while True:
        n = read_input()  # Lecture de la taille de la prochaine grille
        if n == 0:
            break  # Fin des cas de test
        # Lecture de la grille
        for r in range(n):
            table[r] = input()
        # Appel à la fonction de résolution
        answer = largest_empty_square(table, n, dp)
        print(answer)


if __name__ == "__main__":
    main()