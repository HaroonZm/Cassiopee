def enumerate_painting_patterns(height, width, K, grid):
    """
    Compte le nombre de façons de choisir des ensembles de lignes et de colonnes à peindre (supprimer)
    du tableau `grid` de dimensions `height` x `width` de sorte qu'il reste exactement `K` cellules "#".

    Args:
        height (int): Nombre de lignes du tableau.
        width (int): Nombre de colonnes du tableau.
        K (int): Nombre souhaité de cellules noires restantes après peinture.
        grid (List[List[str]]): Grille contenant les caractères '#' (noir) et '.' (vide).

    Returns:
        int: Nombre de motifs de peinture possibles satisfaisant la contrainte.
    """
    count = 0  # Compteur de solutions valides

    # Créer des masques binaires pour énumérer tous les sous-ensembles de lignes
    for h_bits in range(2 ** height):
        # Déterminer les lignes qui NE seront PAS peintes, à partir des bits de h_bits (1 = non-peinte)
        painted_rows = []
        for row in range(height):
            if (h_bits >> row) & 1:
                painted_rows.append(row)

        # Énumérer tous les sous-ensembles de colonnes
        for w_bits in range(2 ** width):
            painted_cols = []
            for col in range(width):
                if (w_bits >> col) & 1:
                    painted_cols.append(col)

            black_count = 0  # Compte de cellules '#' dans la configuration résultante
            for x in painted_rows:
                for y in painted_cols:
                    if grid[x][y] == '#':
                        black_count += 1
            # Si le nombre de '#' est exactement K, c'est une solution valide
            if black_count == K:
                count += 1

    return count

def main():
    """
    Point d'entrée principal du programme.
    Lit les entrées, prépare la grille, puis appelle l'algorithme de pattern painting.
    Affiche le résultat calculé.
    """
    # Lire les dimensions et le nombre de noir désiré
    h, w, K = map(int, input().split())
    # Lire la grille : chaque ligne du tableau, convertie en liste de caractères
    grid = [list(input().strip()) for _ in range(h)]

    # Appeler la fonction principale et afficher la réponse
    result = enumerate_painting_patterns(h, w, K, grid)
    print(result)

# Démarrer le programme principal
if __name__ == "__main__":
    main()