def solve(X, Y, Z, V, E, A):
    # Crée une table dynamique dp où dp[i][j] représente la probabilité d’être à la case i
    # avec un score j. Y+11 est choisi pour allouer suffisamment d’espace pour les cases futures.
    # 6001 est arbitrairement large pour couvrir tous les scores possibles (étant donné le problème original).
    dp = [[0.0] * 6001 for _ in range(Y + 11)]

    # On commence au niveau 0 avec un score de 0, donc la probabilité ici vaut 1.0 (100% de chances)
    dp[0][0] = 1.0

    # Boucle sur chaque position possible jusqu'à Y-1 (inclus)
    for i in range(Y):
        # Boucle sur chaque score possible jusqu'à 5000 (inclus)
        for j in range(5001):
            # Si la probabilité de se trouver à [i][j] est nulle ou négative, il est inutile d’envisager cet état.
            if dp[i][j] <= 0.0:
                continue
            # Pour chaque valeur k dans la liste des valeurs de déplacement V (par exemple : résultats de dés)
            for k in V:
                # t représente la nouvelle position après avoir avancé de k cases.
                t = i + k
                # Si on dépasse la dernière case (t > Y), alors on considère avoir atteint la fin
                if t > Y:
                    # On contribue à la probabilité d’arriver exactement à Y avec le score actuel (j)
                    # On divise par X pour tenir compte de la probabilité sur tous les X choix possibles
                    dp[Y][j] += dp[i][j]/X
                # Sinon, si la case t possède un effet (par ex. effet spécial signalé par E[t] == 1)
                elif E[t] == 1:
                    # On applique l'effet A[t] à la position t pour calculer la destination réelle (t+A[t])
                    # On n’autorise pas de dépasser Y, donc on prend le minimum de Y et t+A[t]
                    # La probabilité de cet évènement s’ajoute à la case correspondante avec le même score (j)
                    dp[min(Y, t+A[t])][j] += dp[i][j]/X
                else:
                    # Si la case n’a pas d’effet spécial, on avance normalement à la position t
                    # On met à jour le score : score actuel (j) + effet d’éventuel bonus/malus sur la case A[t]
                    # On ne veut pas de score négatif, donc on prend max(0, j+A[t])
                    dp[t][max(0, j+A[t])] += dp[i][j]/X

    # On va maintenant calculer la somme espérée du score final sur toutes les issues possibles arrivant à la case finale Y
    s = 0
    # On parcourt tous les scores possibles jusqu'à 5000
    for i in range(5001):
        # On saute toutes les probabilités nulles ou négatives
        if dp[Y][i] <= 0.0:
            continue
        # On ajoute à s la contribution espérée : score i * probabilité d’obtenir ce score à l’arrivée
        s += i * dp[Y][i]
    # On affiche le résultat en nombre entier, ce qui veut dire qu’on arrondit en bas.
    print(int(s))

if __name__ == "__main__":
    import sys  # On importe le module sys pour utiliser sys.exit() afin de quitter proprement la boucle

    while True:
        # On lit la première ligne d'entrée : X (nombre de faces du dé), Y (nombre de cases), Z (nombre de cases spéciales)
        X, Y, Z = map(int, input().split())
        # Si la somme au niveau du bit-à-bit du triplet est nulle (donc tous à 0), le programme s’arrête
        if X | Y | Z == 0:
            sys.exit()
        # On lit une ligne correspondant à la liste des faces (V), par exemple la liste des déplacements possibles
        V = list(map(int, input().split()))
        # On initialise le tableau des effets spéciaux : E[n] vérifie sur la n-ième case la présence d’un effet spécial
        E = [0] * 100
        # On initialise le tableau des bonus/malus : A[n] indique le score à ajouter (bonus/malus) en arrivant sur la n-ième case
        A = [0] * 100
        # Pour chaque case spéciale (il y en a Z), on lit ses paramètres
        for _ in range(Z):
            n, e, a = map(int, input().split())
            # n est le numéro de la case spéciale (index), e code le type d'effet, a est la valeur de l'effet
            E[n] = e  # On marque l’effet spécial du type e dans E[n]
            # Si c’est un effet de type 3, alors a sera considéré comme un malus (score négatif), donc on inverse a
            if e == 3:
                A[n] = -a
            else:
                # Sinon a est positif (ou 0)
                A[n] = a
        # On appelle la fonction principale solve avec tous les paramètres réunis pour calculer le résultat pour ce jeu
        solve(X, Y, Z, V, E, A)