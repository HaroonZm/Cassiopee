# Demande à l'utilisateur de saisir un nombre entier, qui sera stocké dans la variable n.
# Ceci représente la taille de la séquence d'éléments à traiter.
n = int(input())

# Crée une liste 'a' qui contiendra 'n' entiers.
# Pour chaque indice de 0 à n-1, on demande à l'utilisateur de saisir une valeur entière.
# Chacune de ces valeurs est saisie via input(), convertie en entier puis insérée dans la liste.
a = [int(input()) for _ in range(n)]

# On initialise une matrice bidimensionnelle dp de taille n x n (une liste de listes).
# Cette matrice 'dp' servira à stocker des sous-solutions du problème pour la programmation dynamique.
# Chaque case dp[i][j] représente le meilleur score possible (pour une certaine définition selon le problème)
# en partant de l'intervalle allant de l'indice i à l'indice j (en considérant le cycle, donc %n).
dp = [
    [ 
        # Si i et j sont les mêmes, cela signifie que l'intervalle ne comporte qu'un seul élément.
        # Dans ce cas, la meilleure option est simplement la valeur de a[i].
        a[i] if i == j else
        # Si j est immédiatement après i en tenant compte du cycle circulaire (donc (i+1)%n == j)
        # alors l'intervalle est constitué de deux éléments (i et j).
        # Le maximum entre a[i] et a[(i+1)%n] est pris comme valeur optimale pour cet intervalle minimal à deux éléments.
        max(a[i], a[(i+1)%n]) if (i+1)%n == j else
        # Pour tous les autres cas (où l'intervalle est plus grand que deux), on initialise à 0,
        # car on n'a pas encore calculé la valeur optimale pour ces intervalles.
        0
        for j in range(n)
    ]
    for i in range(n)
]

# La boucle externe va parcourir des intervalles de longueurs croissantes, seulement les intervalles de taille impaire.
# Si n est pair, on commence à 3, sinon on commence à 2. Cela gère correctement la parité dans cette construction dynamique.
# On augmente i de 2 à chaque itération, car les sous-intervalles possibles augmentent de manière cyclique.
for i in range(3 if n % 2 == 0 else 2, n, 2):

    # Pour chaque possible position de départ l de l'intervalle sur le cycle,
    # on doit calculer la valeur optimale dp[l][r] pour l'intervalle allant de l à r.
    for l in range(n):
        # Le bord droit de l'intervalle courant, r, est calculé en tenant compte du cycle par (l+i)%n,
        # garantissant que les indices restent dans l'intervalle [0, n-1].
        r = (l + i) % n

        # On prépare une liste temporaire 'pat' pour stocker les valeurs potentielles.
        # Celle-ci contiendra deux options correspondant à deux manières de choisir un élément à chaque extrémité de l'intervalle.
        pat = []

        # On simule les deux manières possibles de retirer (prendre) un élément d'un des bords de l'intervalle :
        # - Soit on prend l'élément à gauche (l), soit à droite (r).
        # Pour chaque cas, on prépare les indices correspondants :
        # (x, nextl, nextr)
        # x : l'indice choisi (soit l soit r)
        # nextl : nouvel indice de gauche après retrait
        # nextr : nouvel indice de droite après retrait
        for x, nextl, nextr in [ (l, (l+1)%n, r), (r, l, (r+n-1)%n) ]:

            # On vérifie si l'élément suivant à gauche (nextl) a une valeur plus grande que celui à droite (nextr)
            if a[nextl] > a[nextr]:
                # Si c'est le cas, on retire aussi l'élément à gauche pour le tour suivant,
                # donc on avance nextl de 1 en prenant en compte le cycle circulaire.
                nextl = (nextl + 1) % n
            else:
                # Sinon, on retire à droite pour le tour suivant,
                # donc on recule nextr de 1 en tenant compte du cycle.
                nextr = (nextr + n - 1) % n

            # On ajoute dans 'pat' la somme de la valeur prise actuellement (a[x])
            # et de la meilleure solution déjà calculée sur l'intervalle réduit [nextl][nextr].
            pat.append(a[x] + dp[nextl][nextr])

        # Parmi les deux options testées ci-dessus (prendre à gauche ou à droite),
        # on garde la meilleure, c'est-à-dire la plus grande valeur de 'pat'.
        # Ceci constitue la solution optimale pour l'intervalle [l][r] pour cette taille d'intervalle.
        dp[l][r] = max(pat)

# Après avoir terminé de remplir la table 'dp' pour tous les intervalles et toutes les positions de départ,
# on cherche à extraire la solution optimale finale.
# On énumère tous les indices initiaux possibles 'i', et pour chacun on regarde la valeur dp[(i+1)%n][i].
# Ceci correspond à la meilleure solution lorsqu'on commence juste après 'i', jusqu'à 'i' en cyclant.
# On prend finalement la plus grande valeur de toutes ces positions de départ.
print(max(dp[(i+1)%n][i] for i in range(n)))