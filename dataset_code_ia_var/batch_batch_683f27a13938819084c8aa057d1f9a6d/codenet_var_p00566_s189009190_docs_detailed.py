def min_weighted_distance_sum():
    """
    Calcule la position (cellule) d'une grille h x w qui minimise la somme pondérée des distances
    à toutes les autres cellules en fonction des valeurs assignées à chaque cellule.
    La pondération est basée sur les valeurs des cellules (chaque valeur représente un poids associé).
    Pour chaque position possible, on calcule le coût total comme la somme pondérée des distances minimales (ville la plus proche,
    calculée via l'infini de Manhattan ou Chebyshev suivant le min entre |i-m| et |j-n|) vers chaque autre cellule.

    Entrées:
        - La première ligne contient deux entiers h et w séparés par un espace, représentant la hauteur et la largeur de la grille.
        - Les h lignes suivantes contiennent chacune w entiers représentant la valeur (poids) de chaque cellule.

    Sortie:
        - Un entier représentant la somme minimale pondérée des distances pour la meilleure cellule de la grille.
    """
    # Lecture des dimensions de la grille depuis l'entrée standard
    h, w = map(int, input().split())

    # Construction de la grille 'a' contenant les poids de chaque cellule.
    a = [list(map(int, input().split())) for _ in range(h)]

    # Initialisation de la variable qui contiendra la réponse minimale possible.
    # On choisit une valeur suffisamment grande (1e9) pour garantir qu'elle sera remplacée.
    ans = 1e9

    # On parcourt toutes les cellules possibles (i, j) de la grille
    for i in range(h):
        for j in range(w):
            cnt = 0  # Cette variable cumulera la somme pondérée des distances pour la cellule (i, j)

            # Pour chaque cellule (m, n) de la grille, on calcule sa contribution au coût total
            for m, row in enumerate(a):
                for n, x in enumerate(row):
                    # La distance considérée ici est min(|i-m|, |j-n|), puis multipliée par la valeur (poids) x de la cellule.
                    cnt += min(abs(i - m), abs(j - n)) * x

            # On conserve le coût minimal rencontré lors de l'itération sur toutes les positions
            ans = min(ans, cnt)

    # Affichage du résultat : la plus petite somme pondérée trouvée
    print(ans)

# Appel de la fonction principale pour exécuter le programme
min_weighted_distance_sum()