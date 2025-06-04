def solve(X, Y, Z, V, E, A):
    # Création d'une table de programmation dynamique (DP)
    # La table 'dp' est une liste de listes (une matrice)
    # dp[i][j] stockera la probabilité d'être sur la case 'i' avec la "valeur accumulée" ou "score" égal à 'j'
    # On initialise 6001 colonnes pour couvrir tous les scores potentiellement atteignables
    # On prend une marge en ligne en fonction de la taille de Y + le max lancé sur un dé (pour éviter les dépassements)
    dp = [[0.0] * 6001 for _ in range(Y + max(V) + 1)]
    # On part du point de départ : position 0, score 0, probabilité 1.0 (c'est certain)
    dp[0][0] = 1.0

    # On parcourt tous les états atteignables à chaque étape de jeu (pour chaque case jusqu'à Y-1)
    for i in range(Y):
        # Pour chaque somme accumulée possible (jusqu'à 5000)
        for j in range(5001):
            # Si la probabilité d'être dans cet état est nulle ou négative, on ignore (optimisation)
            if dp[i][j] <= 0.0:
                continue
            # Pour chaque valeur possible de déplacement (lancers de dé par ex.)
            for k in V:
                # 't' représente la nouvelle case après déplacement depuis 'i' de 'k' cases
                t = i + k
                # Si le déplacement dépasse la fin (Y), on reste à Y et on accumule la probabilité (on ne va pas plus loin)
                if t > Y:
                    # Division par X car il y a X possibilités égales (chaque valeur dans V)
                    dp[Y][j] += dp[i][j] / X
                # Si sur la case d'arrivée t il y a un événement spécial de type E[t] == 1
                elif E[t] == 1:
                    # On applique le bonus/malus associé à A[t] et on avance de A[t] cases (ou un raccourci, par exemple)
                    # min(Y, t+A[t]) garantit de ne pas dépasser la dernière case
                    dp[min(Y, t + A[t])][j] += dp[i][j] / X
                else:
                    # Sinon, on applique simplement l'effet (bonus/malus) de la case sur le score (somme accumulée)
                    # Le max(0, j + A[t]) interdit des scores négatifs
                    dp[t][max(0, j + A[t])] += dp[i][j] / X

    # À la fin, on somme l'espérance du score final sur toutes les façons d'arriver à la dernière case Y
    s = 0
    # On parcourt tous les scores possibles pour la case d'arrivée (Y)
    for i in range(5001):
        # On ignore les probas nulles ou négatives
        if dp[Y][i] <= 0.0:
            continue
        # On multiplie le score par la probabilité d'arriver à ce score, et on ajoute au total attendu
        s += i * dp[Y][i]
    # On affiche l'entier de l'espérance trouvée (chiffre après la virgule ignoré)
    print(int(s))


if __name__ == "__main__":
    # On importe le module sys pour accéder à sys.exit plus tard
    import sys

    while True:
        # On lit une ligne d'entrée standard, on la splitte en morceaux, et on convertit en entiers
        # X = nombre de valeurs possibles pour un jet (faces d'un dé par ex.)
        # Y = case de fin / objectif
        # Z = nombre de cases spéciales
        X, Y, Z = map(int, raw_input().split())
        # Si toutes les entrées valent 0, on sort du programme (cas de terminaison)
        if X | Y | Z == 0:
            sys.exit()
        # On lit les valeurs possibles pour le dé (V peut être [1, 2, 3, 4, 5, 6] pour un dé standard)
        V = map(int, raw_input().split())
        # On crée des tableaux pour stocker les types d'événement (E) et leurs valeurs associées (A)
        # Taille 100 car il n'y a jamais plus de 100 cases spéciales dans l'énoncé typique
        E = [0] * 100
        A = [0] * 100
        # On traite chaque case spéciale
        for _ in range(Z):
            # Pour chaque case définie, on lit n (numéro de case), e (type d'événement), a (valeur associée)
            n, e, a = map(int, raw_input().split())
            E[n] = e
            # Si l'événement est du type 3, alors la valeur est négative (on recule, par exemple)
            if e == 3:
                A[n] = -a
            else:
                A[n] = a
        # On lance la résolution pour ce jeu de données (partie)
        solve(X, Y, Z, V, E, A)