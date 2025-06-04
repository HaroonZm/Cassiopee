# Programme pour résoudre le problème AOJ 1589 "Unhappy Class"
# Code réécrit avec des commentaires très détaillés expliquant chaque étape et chaque concept

# Lecture des trois nombres entiers N, M, L à partir de l'entrée standard.
# La fonction input() lit une ligne de texte, split() découpe la ligne en morceaux séparés par des espaces,
# et map(int, ...) convertit chaque morceau en entier.
# Les trois entiers sont affectés respectivement à N, M et L.
N, M, L = map(int, input().split())

# Création d'une liste de listes (tableau à deux dimensions), appelée tbl, qui va contenir les transitions.
# On crée une liste vide ([]) pour chaque entier i dans un intervalle de 0 à 44 (soit 45 en tout).
# Cela signifie que tbl[0] à tbl[44] sont tous initialement des listes vides.
tbl = [[] for i in range(45)]

# Cette boucle va s'exécuter M fois (une fois pour chaque transition).
for i in range(M):
    # Lecture de quatre entiers : d, a, k, t, représentant les paramètres d'une transition.
    # Encore une fois, input().split() lit une ligne et la découpe, puis map(int, ...) convertit chaque morceau en entier.
    d, a, k, t = map(int, input().split())
    # Calcul d'un indice unique pour la transition :
    # d : numéro du jour (de 0 à 4)
    # a : numéro de la classe (de 1 à N)
    # On convertit (d, a) en un seul indice pour tbl, calculé ainsi : d*N + (a-1).
    # Cela permet de stocker toutes les transitions liées à un jour et une classe donnés au même endroit.
    # On ajoute un tuple (k, t) à la liste tbl[da], où :
    #   k : combien de jours sauter après cette transition
    #   t : le "bonheur" ou score obtenu grâce à cette transition
    tbl[d*N + a - 1].append((k, t))

# Création de la table pour la programmation dynamique (DP).
# dp[x][y] représentera le score maximal possible en étant à l'étape x et en ayant effectué y actions spéciales.
# On initialise tous les éléments à 0.
# Il y a 45 lignes (pour 5*N, px. N <= 9 donc 5*9=45), et 45 colonnes.
dp = [[0 for i in range(45)] for j in range(45)]

# Boucle principale pour remplir la table DP.
# da sera l'indice représentant chaque (jour, classe) possible : il peut aller de 0 jusqu'à 5*N-1 (non inclus).
for da in range(5 * N):
    # Pour chaque nombre possible d'actions spéciales ayant déjà été utilisées (de 0 à L inclus)
    for i in range(L + 1):
        # Si on n'a pas encore utilisé toutes les actions spéciales autorisées (i < L)
        if i < L:
            # Pour chaque transition possible à partir du point (jour, classe) actuel (da)
            for k, t in tbl[da]:
                # Si l'action spéciale (correspondant à cette transition) est utilisée maintenant :
                # - On saute de k jours/classes (càd on avance de k dans l'index da)
                # - On consomme une action spéciale de plus (i+1)
                # - On ajoute le score t à notre score courant
                # - On met à jour dp[da+k][i+1] à la valeur maximale possible
                dp[da + k][i + 1] = max(dp[da + k][i + 1], dp[da][i] + t)
        # Même si aucune action spéciale n'est utilisée, on peut toujours avancer naturellement d'une classe/jour.
        # On met donc à jour dp[da+1][i] afin de propager la valeur maximale atteinte jusqu'ici.
        dp[da + 1][i] = max(dp[da + 1][i], dp[da][i])

# A la fin de toutes les transitions possibles, le résultat final est contenu dans dp[5*N][L].
# Cela correspond à être arrivé à la toute fin (après 5*N étapes) en ayant utilisé exactement L actions spéciales.
# On affiche ce résultat.
print(dp[5 * N][L])