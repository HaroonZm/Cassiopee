def find_max_distance_between_B(H, W, grid):
    """
    Calcule la distance de Manhattan maximale entre toutes les paires de cases contenant 'B' dans une grille donnée.

    Paramètres :
    - H (int) : nombre de lignes de la grille.
    - W (int) : nombre de colonnes de la grille.
    - grid (List[List[str]]) : grille sous forme de liste de listes de caractères.

    Retourne :
    - int : la distance de Manhattan maximale entre deux cases contenant 'B'.
    """
    Bs = []  # Liste pour stocker les coordonnées de toutes les cases contenant 'B'

    # Parcours de la grille pour trouver les positions des 'B'
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "B":
                Bs.append((i, j))  # On ajoute la position (i, j) si c'est un 'B'

    ans = 0  # Initialisation de la distance maximale

    # On considère toutes les paires possibles de positions contenant 'B'
    for e0 in Bs:
        for e1 in Bs:
            # On calcule la distance de Manhattan entre les deux positions
            distance = abs(e0[0] - e1[0]) + abs(e0[1] - e1[1])
            # On met à jour la distance maximale trouvée jusqu'à présent
            ans = max(ans, distance)

    return ans  # On retourne la distance maximale


def main():
    """
    Fonction principale exécutant la collecte d'entrée utilisateur,
    la préparation de la grille, puis l'affichage de la distance maximale.
    """
    # Lecture des dimensions de la grille
    H, W = [int(n) for n in input().split()]

    # Initialisation de la grille : liste de listes de caractères
    grid = []
    for _ in range(H):
        # Lecture d'une ligne, conversion en liste de caractères, ajout à la grille
        row = list(input())
        grid.append(row)

    # Calcul de la distance maximale entre deux 'B' et affichage du résultat
    ans = find_max_distance_between_B(H, W, grid)
    print(ans)

# Appel de la fonction principale
if __name__ == "__main__":
    main()