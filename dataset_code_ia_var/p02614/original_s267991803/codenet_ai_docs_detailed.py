def count_colored_cells_with_k_marks():
    """
    Lit les dimensions de la grille ainsi que la valeur cible 'k' depuis l'entrée,
    lit ensuite la grille constituée de caractères '.' et '#', puis calcule
    de combien de façons il est possible de choisir un sous-ensemble de lignes
    et de colonnes à recouvrir (marquer) pour qu'il reste exactement 'k'
    cellules colorées ('#') visibles dans la grille finale.

    Retourne:
        int: le nombre total de combinaisons (ensembles lignes/colonnes),
        après lesquelles il reste exactement 'k' cellules colorées ('#').
    """

    # Lecture des dimensions de la grille (hauteur h, largeur w) et la cible k.
    h, w, k = map(int, input().split())

    # Lecture de la grille ligne par ligne. Chaque ligne est une chaîne de caractères.
    table = [input() for _ in range(h)]

    # Variable pour stocker le nombre final de façons valides.
    ans = 0

    # Parcours de tous les choix possibles de lignes à recouvrir (utilisation de masques binaires)
    for row_mask in range(2 ** h):
        # Parcours de tous les choix possibles de colonnes à recouvrir (masques binaires)
        for col_mask in range(2 ** w):
            cnt = 0  # Compteur du nombre de cellules '#' restantes pour cette sélection

            # Parcours de toutes les cellules de la grille
            for r in range(h):
                for c in range(w):
                    # Vérifier si la cellule (r, c) est colorée ('#')
                    if table[r][c] == "#":
                        # Vérifier que la ligne r et la colonne c ne sont PAS recouvertes,
                        # c'est-à-dire: le bit r n'est PAS à 1 dans row_mask et le bit c n'est PAS à 1 dans col_mask
                        # Puisque le code d'origine vérifiait (i>>s)&1 et (j>>t)&1,
                        # on doit considérer l'inverse: "non choisi" signifie bit à 0.
                        if not ((row_mask >> r) & 1) and not ((col_mask >> c) & 1):
                            cnt += 1

            # Si le nombre de cellules restantes colorées est exactement k, incrémenter le nombre de façons valides
            if cnt == k:
                ans += 1

    # Affichage du résultat final
    print(ans)

# Appel de la fonction principale pour exécuter le programme
count_colored_cells_with_k_marks()