def solve():
    # Importation du module 'stdin' depuis la bibliothèque 'sys' pour une lecture efficace des entrées
    from sys import stdin
    f_i = stdin  # 'f_i' fait référence à l'objet de flux d'entrée standard

    # Définition d'une fonction locale 'f' qui prend deux arguments, bm_i et bw_i
    # Cette fonction sert à évaluer une certaine différence et la transformer
    def f(bm_i, bw_i):
        # Vérifie si 'bm_i' est strictement supérieur à 'bw_i'
        if bm_i > bw_i:
            # Si c'est le cas, calcule la différence ('d') en soustrayant 'bw_i' de 'bm_i'
            d = bm_i - bw_i
        else:
            # Sinon, calcule la différence inverse, c'est-à-dire 'bw_i' moins 'bm_i'
            d = bw_i - bm_i
        # Retourne le résultat du calcul : la différence multipliée par le carré de (différence - 30)
        return d * (d - 30) ** 2

    # Boucle infinie : servir à gérer plusieurs jeux d'entrée jusqu'à rencontrer une condition d'arrêt
    while True:
        # Lecture de la ligne suivante depuis l'entrée standard et découpage en deux entiers M et W
        M, W = map(int, f_i.readline().split())
        # Si 'M' vaut 0, on sort immédiatement de la boucle (et donc de la fonction)
        if M == 0:
            break
        
        # Lecture de la ligne suivante et conversion des éléments en entiers pour la liste 'bm'
        bm = list(map(int, f_i.readline().split()))
        # Lecture d'une autre ligne, conversion en entiers pour la liste 'bw'
        bw = list(map(int, f_i.readline().split()))
        
        # Création d'une matrice 'e_gen', contenant pour chaque élément de 'bm' tous les résultats possibles
        # de 'f' avec chaque élément de 'bw'. On obtient ainsi une liste de listes.
        e_gen = [[f(m, w) for w in bw] for m in bm]
        
        # Calcul du nombre total de sous-ensembles possibles via du 'bitmasking' : 2^W, soit 1 << W
        bit_size = (1 << W) # Par exemple, si W = 4, bit_size = 16 (de 0 à 15)

        # Création de deux tableaux 'dp1' et 'dp2' avec pour chaque position la valeur initiale -1
        # Ces tableaux serviront à mémoriser la meilleure valeur (score) trouvée pour chaque bitmask
        # Chaque index du tableau représente un état différent de sélection (bitmask)
        dp1 = [-1] * bit_size
        dp2 = [-1] * bit_size

        # On initialise la valeur de l'état vide (aucun élément sélectionné) à 0 car c'est la valeur neutre
        dp1[0] = 0
        dp2[0] = 0

        # Création de la liste 'add_bit' qui contient la valeur d'un bit unique à chaque position
        # add_bit[i] == 2^i, qui permettra d'activer/désactiver chaque joueur 'w'
        add_bit = [1 << i for i in range(W)]
        
        # Boucle principale sur les joueurs masculin (indices de 'M')
        for i in range(M):
            # On parcourt tous les états possibles (sous-ensembles) déjà calculés précédemment dans 'dp1'
            for s1, e1 in enumerate(dp1):
                # Si cet état (bitmask/sous-ensemble) n'a pas été atteint (valeur -1), on passe au suivant
                if e1 == -1:
                    continue
                # Pour chaque possibilité d'attribution d'un joueur masculin à un joueur féminin
                for b, e in zip(add_bit, e_gen[i]):
                    # Si le joueur féminin correspondant à ce bit est déjà pris dans ce sous-ensemble, on saute
                    if s1 & b:
                        continue
                    # Sinon, on construit le nouveau sous-ensemble en ajoutant ce joueur féminin
                    s2 = s1 | b
                    # On calcule le score associé à cette nouvelle allocation
                    e2 = e1 + e
                    # Si ce nouveau score est supérieur à l'ancien pour le même sous-ensemble...
                    if e2 > dp2[s2]:
                        # ...on le met à jour avec cette meilleure valeur
                        dp2[s2] = e2
            # Mise à jour des valeurs de 'dp1' pour le prochain tour grâce à la copie de 'dp2'
            # Ceci garantit que chaque masculin est attribué une seule fois à une féminine
            dp1 = dp2[:]
        
        # À la fin, on récupère la plus grande valeur obtenue dans le tableau des états finaux
        # Cela correspond au meilleur score que l'on peut avoir en associant les joueurs
        print(max(dp2))

# Appel de la fonction 'solve' pour démarrer le traitement
solve()