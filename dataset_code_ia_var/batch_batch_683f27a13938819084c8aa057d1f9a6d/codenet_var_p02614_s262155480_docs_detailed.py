from itertools import product

def count_ways_to_paint(H, W, K, grid):
    """
    Calcule le nombre de façons de peindre des lignes et colonnes dans une grille de taille H x W,
    de sorte que K cases contenant '#' restent découvertes après la peinture.

    Args:
        H (int): Le nombre de lignes de la grille.
        W (int): Le nombre de colonnes de la grille.
        K (int): Le nombre exact de '#' qui doivent rester non peints.
        grid (List[str]): Les lignes de la grille sous forme de liste de chaînes de caractères.

    Returns:
        int: Le nombre de sélections de lignes et colonnes dont la suppression laisse exactement K '#'.
    """
    ans = 0  # Compteur pour stocker le résultat final

    # Génère toutes les combinaisons possibles de lignes à peindre ou non (0 = non-peint, 1 = peint)
    for row in product([0, 1], repeat=H):
        # Génère toutes les combinaisons possibles de colonnes à peindre ou non
        for col in product([0, 1], repeat=W):
            cnt = 0  # Compteur pour le nombre de '#' découverts restants

            # Parcourt toutes les cases de la grille
            for i in range(H):
                for j in range(W):
                    # On compte un '#' seulement s'il n'est pas recouvert par une ligne ou une colonne peinte
                    if row[i] == 0 and col[j] == 0 and grid[i][j] == '#':
                        cnt += 1

            # Si on obtient exactement K '#' restants, c'est une combinaison valide
            if cnt == K:
                ans += 1

    return ans

def main():
    """
    Lit l'entrée standard, puis calcule et affiche le nombre de façons de peindre les lignes et colonnes
    de la grille en laissant exactement K '#' non peints.
    """
    # Lecture des entiers H (lignes), W (colonnes), K (cibles)
    H, W, K = map(int, input().split())
    # Lecture de la grille de H lignes
    grid = [input().strip() for _ in range(H)]
    # Calcul du résultat
    result = count_ways_to_paint(H, W, K, grid)
    # Affichage du résultat
    print(result)

# Lancement du programme principal
if __name__ == "__main__":
    main()