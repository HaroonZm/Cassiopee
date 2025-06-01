while True:
    # Boucle infinie pour traiter plusieurs cas de test jusqu'à interruption explicite.
    # Cette structure while True signifie que la boucle va continuer indéfiniment,
    # jusqu'à ce qu'un 'break' soit rencontré dans le corps de la boucle.

    # Lecture d'une ligne d'entrée, découpage en quatre parties, puis conversion de chacune en entier.
    # map applique la fonction int à chaque chaîne obtenue en divisant la ligne d'entrée sur les espaces.
    n, m, h, k = map(int, input().split())

    # Condition d'arrêt : si n est égal à 0, on sort de la boucle while.
    # Cela sert à terminer la lecture quand un cas de test spécial (n=0) est rencontré.
    if n == 0:
        break

    # Initialisation d'une liste vide 'pts' qui va contenir des entiers lus un par un.
    pts = []
    for _ in range(n):
        # Pour chaque itération, on lit un entier en entrée et on l'ajoute à la liste 'pts'.
        pts.append(int(input()))

    # Création d'une liste vide 'bars' pour stocker des sous-listes (des barres).
    bars = []
    for _ in range(m):
        # Chaque barre est définie par une ligne d'entrée contenant deux entiers.
        # Ils sont convertis en liste d'entiers avec map et list, puis ajoutés à 'bars'.
        bars.append(list(map(int, input().split())))

    # Tri de la liste 'bars' selon le deuxième élément de chaque sous-liste.
    # key=lambda x: x[1] crée une fonction anonyme qui retourne le deuxième élément x[1].
    # bars.sort modifie la liste 'bars' en place, pour la classer selon cet élément.
    bars.sort(key=lambda x: x[1])

    # Création d'une liste 'nos' contenant les indices de 0 à n-1.
    # Il s'agit d'une liste simple qui va être utilisée pour gérer les positions des points.
    nos = [i for i in range(n)]

    # Initialisation d'une liste 'barspt' vide, qui contiendra des informations sur les barres avec indices.
    barspt = []

    # Parcours chaque barre dans 'bars' pour construire 'barspt' et modifier 'nos' en fonction de permutations.
    for bar in bars:
        # b est l'indice de la première extrémité de la barre, ajusté pour correspondre à l'indexation 0-based.
        b = bar[0] - 1

        # Ajout d'une liste correspondant à cette barre dans 'barspt':
        # [nos[b], nos[b+1], 0, 0]
        # les deux premiers éléments indiquent la position actuelle des points liés par la barre,
        # les deux derniers sont des zéros temporaires qui seront remplacés plus tard.
        barspt.append([nos[b], nos[b+1], 0, 0])

        # Échange (swap) des éléments dans 'nos' aux positions b et b+1 pour simuler le "passage" de la barre.
        # Cela modifie la liste 'nos', reflétant une sorte de permutation ou échange des points.
        nos[b], nos[b+1] = nos[b+1], nos[b]

    # Réinitialisation de 'nos' à la liste des indices de 0 à n-1 pour un nouveau traitement.
    nos = [i for i in range(n)]

    # Parcours des indices des barres dans l'ordre décroissant (de m-1 à 0).
    # Cette boucle va mettre à jour les informations dans 'barspt' en fonction des points après permutation.
    for barid in range(m - 1, -1, -1):
        # Indice b0 est la position de la première extrémité de la barre 'barid', ajustée à 0-based
        b0 = bars[barid][0] - 1

        # Indice b1 est la position juste après b0, dans la barre en question.
        b1 = bars[barid][0]

        # barspt[barid][2] reçoit la valeur dans 'pts' correspondant à la position nos[b0].
        # Cela représente le point associé à la première extrémité de la barre dans son état actuel.
        barspt[barid][2] = pts[nos[b0]]

        # barspt[barid][3] reçoit la valeur dans 'pts' correspondant à la position nos[b1].
        # Cela représente le point associé à la deuxième extrémité de la barre dans son état actuel.
        barspt[barid][3] = pts[nos[b1]]

        # Échange des valeurs dans 'pts' aux indices nos[b0] et nos[b1].
        # Cela simule la permutation des valeurs de points en fonction des barres, dans l'ordre inverse.
        pts[nos[b0]], pts[nos[b1]] = pts[nos[b1]], pts[nos[b0]]

    # Initialise la variable 'atari' à -1, qui pourrait représenter un indice ou position spéciale.
    atari = -1

    # Calcul de la somme minimale initiale des premiers k éléments de 'pts'.
    # sum(pts[0:k]) calcule la somme des éléments de l'indice 0 jusqu'à k-1 inclus.
    minsc = sum(pts[0:k])

    # Initialisation de 'hosei' (correctif) à 0, utilisé pour ajuster le calcul final.
    hosei = 0

    # Boucle qui parcourt chaque barre enregistrée dans 'barspt' pour appliquer des corrections.
    for bar in barspt:
        # Premier test: Vérifie si bar[0]-1 est dans l'intervalle [atari, atari+k)
        # et bar[1]-1 est en dehors de cet intervalle.
        if atari <= bar[0] - 1 < atari + k and (bar[1] - 1 < atari or atari + k <= bar[1] - 1):
            # Calcule une différence entre les deux valeurs associées aux extrémités de la barre.
            sc = bar[2] - bar[3]

            # Met à jour 'hosei' avec la valeur sc si sc est plus petit que la valeur actuelle de 'hosei'.
            if sc < hosei:
                hosei = sc

        # Deuxième test similaire, mais avec les indices des extrémités inversés.
        if atari <= bar[1] - 1 < atari + k and (bar[0] - 1 < atari or atari + k <= bar[0] - 1):
            # Calcule la différence inverse entre les deux valeurs associées aux extrémités.
            sc = bar[3] - bar[2]

            # Mise à jour de 'hosei' si sc est plus petit que l'actuel 'hosei'.
            if sc < hosei:
                hosei = sc

    # Calcul final : impression de la somme minimale de base plus la correction la plus négative trouvée.
    # Cela donne une valeur ajustée en fonction des permutations et des corrections calculées.
    print(minsc + hosei)