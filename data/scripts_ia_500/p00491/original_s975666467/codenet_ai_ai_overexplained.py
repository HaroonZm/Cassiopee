N, K = map(int, input().split())
# N: nombre total de positions dans la séquence
# K: nombre de contraintes fournies, c'est-à-dire combien de positions ont une valeur imposée

S = [0] * N
# Initialisation d'une liste S de taille N, remplie de zéros
# Cette liste va contenir les valeurs imposées aux positions, 0 signifiant aucune valeur imposée

for _ in [0] * K:
    # Boucle répétée K fois ; le _ est une variable jetable car on n'a pas besoin de son index
    a, b = map(int, input().split())
    # Lecture de la position 'a' et de la valeur imposée 'b' pour cette position
    S[a - 1] = b
    # Stockage de la valeur b à la position a-1 dans la liste S (indices commençant à 0 en Python)

dp = [0] * 9
# dp est une liste de longueur 9 utilisée pour stocker des états dynamiques
# Ici 9 = 3 * 3, ce qui correspond probablement à une matrice 3x3 aplatie en liste
# Chaque indice correspond à un état combiné de deux positions précédentes avec 3 valeurs possibles chacune

st, nd = S[:2]
# st = valeur imposée (ou 0) à la position 0
# nd = valeur imposée (ou 0) à la position 1

if st:
    # Si la première position a une valeur imposée (différente de 0)
    if nd:
        # Si aussi la deuxième position a une valeur imposée
        dp[~-st * 3 + ~-nd] = 1
        # Allez ici étape par étape:
        # ~-st calcule (st - 1) de manière astucieuse (~ = complément à un bit)
        # Le même pour nd
        # On calcule un indice unique pour la combinaison des deux valeurs imposées st et nd
        # On met dp[indice] = 1 car seul cet état est possible dans ce cas
    else:
        # Si la deuxième position n'a pas de valeur imposée
        dp[~-st * 3 : st * 3] = [1] * 3
        # On remplit 3 éléments consécutifs de dp avec des 1, correspondant au premier valeur fixe st
        # et trois valeurs possibles pour nd (de 1 à 3)
elif nd:
    # Si seulement nd est imposé (et pas st)
    dp[~-nd::3] = [1] * 3
    # On remplit trois éléments dp à pas de 3 starting à l'indice correspondant à nd - 1
    # Cette opération couvre tous les états possibles pour st avec nd fixé
else:
    # Si ni st ni nd ne sont imposés
    dp = [1] * 9
    # Tous les états sont possibles, on initialise dp à 1 partout

for i in range(2, N):
    # Parcours des positions de la séquence à partir de la troisième (indice 2)
    cur = S[i] - 1
    # cur prend la valeur imposée à la position i, diminuée de 1 pour indexer à partir de 0
    # Si S[i] == 0 (pas de valeur imposée), cur sera -1
    tmp = [0] * 9
    # tmp sera la nouvelle liste dp calculée pour la position i

    if cur + 1:
        # Si cur != -1, donc si la position i a une valeur imposée
        for k in range(3):
            # Parcours des 3 valeurs possibles pour la position i-2 (indice k)
            tmp[k * 3 + cur] = sum(dp[k::3]) - dp[cur * 4] * (k == cur)
            # On calcule pour la combinaison (valeur en position i-2 = k,
            # valeur en position i = cur)
            # dp[k::3] récupère dp[k], dp[k+3], dp[k+6], correspondant aux états
            # où la position i-1 prend les 3 valeurs possibles
            # sum(dp[k::3]) totalise tous les états avec i-2 = k
            # dp[cur*4] correspond à dp[cur * 4], qui est un état où i-1 et i-2 sont tous les deux égaux à cur (car indices multiples de 4 donnent les états diagonaux)
            # On enlève ce cas si k == cur (i-2 == i)
            # L'idée ici est d'éviter des répétitions ou un état interdit spécifique
    else:
        # Si cur == -1 (pas de valeur imposée à la position i)
        for cur in range(3):
            # On essaie par toutes les valeurs possibles pour la position i
            for k in range(3):
                # Et pour toutes les valeurs possibles pour la position i-2
                tmp[k * 3 + cur] = sum(dp[k::3]) - dp[cur * 4] * (k == cur)
                # Même calcul qu'au-dessus, mais on remplit tous les états possibles car pas de contrainte

    dp = tmp[:]
    # Mise à jour de dp avec les nouveaux états calculés

print(sum(dp) % 10000)
# Affiche la somme mod 10000 de toutes les configurations possibles calculées dans dp
# % 10000 est utilisé pour limiter la taille du nombre affiché, probablement pour éviter des dépassements ou parce que la réponse doit être donnée modulo 10000