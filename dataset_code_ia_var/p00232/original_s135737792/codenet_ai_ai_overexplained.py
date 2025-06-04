def solve(X, Y, Z, V, E, A):
    # Création d'une table de programmation dynamique (DP) bidimensionnelle.
    # La première dimension correspond aux 'steps' (étapes de temps, jusqu'à Y + 10 pour marge de sécurité),
    # la seconde dimension correspond à la valeur des 'points' (on va jusqu'à 6000 inclus, d'où 6001 colonnes).
    # Chaque case dp[i][j] contiendra la probabilité d'être à l'étape i avec j points.
    dp = [[0.0] * 6001 for _ in range(Y + 11)]
    # Initialisation : avant de commencer, on a probabilité 1.0 d'être à l'étape 0 avec 0 points.
    dp[0][0] = 1.0

    # Parcours de chaque étape de temps jusqu'à l'étape finale Y (exclue).
    for i in range(Y):
        # Parcours de toutes les valeurs de points possibles (de 0 à 5000 inclus).
        for j in range(5001):
            # Si la probabilité d'être à cette case est 0 ou négative, alors il n'y a rien à propager, on saute.
            if dp[i][j] <= 0.0:
                continue

            # On parcourt l'ensemble des valeurs possibles dans la liste V (correspond à des déplacements/valeurs autorisées).
            for k in V:
                # Calcul du prochain 'étape de temps' potentielle où on peut aller (en partant de i et avançant de k).
                t = i + k

                # Si le prochain indice de temps t est au-delà de la limite (Y), on met à jour directement dp en fin de parcours.
                if t > Y:
                    # Ajoute la fraction de probabilité à l'état terminal (Y, j), fractionnée selon le nombre d'options X.
                    dp[Y][j] += dp[i][j] / X

                # Si l'étape de temps d'arrivée t est 'spéciale' selon le tableau E (E[t] == 1) :
                elif E[t] == 1:
                    # Dans ce cas, on applique une règle spéciale :
                    # on saute vers l'étape 't + A[t]' (avec sécurité de ne pas dépasser Y),
                    # mais on conserve le même nombre de points j.
                    dp[min(Y, t + A[t])][j] += dp[i][j] / X

                # Si l'étape d'arrivée n'est pas spéciale :
                else:
                    # On va à l'étape t, et le score des points est modifié selon A[t].
                    # On s'assure que le score des points n'est pas négatif (max avec 0 !)
                    dp[t][max(0, j + A[t])] += dp[i][j] / X

    # Une fois tous les parcours complétés, on calcule la somme pondérée des points finaux,
    # en tenant compte de la probabilité d'avoir exactement i points à la dernière étape (Y).
    s = 0
    # On parcourt toutes les valeurs possibles de points (0 à 5000) à l'étape Y.
    for i in range(5001):
        # Pour chaque nombre de points i, on ajoute i * probabilité d'arriver à Y avec i points.
        s += i * dp[Y][i]

    # Affichage du résultat final (arrondi à l'entier inférieur, car le problème attend un entier).
    print(int(s))


if __name__ == "__main__":
    import sys  # On importe le module sys pour pouvoir utiliser sys.exit() pour arrêter le script.

    while True:
        # Lecture de trois entiers séparés par des espaces : X, Y, Z.
        # - X : nombre d'options pour V
        # - Y : nombre d'étapes de temps à parcourir
        # - Z : nombre de cases "spéciales"
        X, Y, Z = map(int, input().split())
        # Si les trois valeurs sont nulles, on arrête l'exécution du programme (condition de terminaison).
        if X | Y | Z == 0:
            sys.exit()

        # Lecture des valeurs possibles V (liste de X entiers) pour les déplacements.
        V = list(map(int, input().split()))

        # Initialisation du tableau E avec des zéros : E[n] indique le type de la case n (par défaut 0, "rien de spécial").
        # Le tableau est initialisé en taille 100, par sécurité (peut-être plus que Y ou Z dans certains cas).
        E = [0] * 100
        # Initialisation du tableau A qui contient les effets spéciaux sur chaque case (valeur par défaut 0).
        A = [0] * 100

        # Traitement des Z lignes suivantes, chacune définissant une case spéciale.
        for _ in range(Z):
            # Lecture de trois entiers : n (indice de la case), e (type d'effet), a (valeur associée à l'effet).
            n, e, a = map(int, input().split())
            # Mise à jour du type d'effet spécial pour la case n.
            E[n] = e
            # Pour les effets de type 3, l'effet a est appliqué en négatif (A[n] = -a).
            if e == 3:
                A[n] = -a
            else:
                # Pour les autres types d'effets, on garde la valeur telle quelle.
                A[n] = a

        # Appel de la fonction principale solve() avec les paramètres ainsi lus et construits.
        solve(X, Y, Z, V, E, A)