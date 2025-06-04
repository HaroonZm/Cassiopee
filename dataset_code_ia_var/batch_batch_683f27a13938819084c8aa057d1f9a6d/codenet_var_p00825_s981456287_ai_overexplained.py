# Boucle principale du programme qui continuera de s'exécuter indéfiniment jusqu'à ce qu'une condition d'arrêt soit rencontrée.
while 1:
    # Lecture d'une ligne au clavier grâce à input(), puis conversion de cette entrée en entier avec int().
    # Cette valeur entière, N, représente probablement le nombre d'éléments à traiter pour ce "test case".
    N = int(input())
    # Vérification si N est égal à 0 : cela sert ici de condition de sortie, donc arrêt de la boucle principale si vrai.
    if N == 0:
        break
    # Construction d'une liste de N éléments : on va lire N lignes via input(), 
    # splitter chaque ligne en des morceaux (morceaux séparés par des espaces), 
    # puis convertir chacun de ces morceaux en entier via map(int, ...),
    # puis transformer l'objet map obtenu en une liste, et ranger le tout dans la liste P.
    # Donc P est une liste de N sous-listes d'entiers.
    P = [list(map(int, input().split())) for i in range(N)]
    # On fixe la valeur de M à 366. Cela représente le nombre de jours dans une année bissextile (+1 pour manipulations de jours, probablement).
    M = 366
    # Création d'une liste nommée E composée de M listes vides. 
    # Chaque sous-liste va contenir les événements ou objets associés à un certain indice de jour.
    E = [[] for i in range(M)]
    # Initialisation d'une table de programmation dynamique (DP), nommée dp.
    # Il s'agit d'une liste de M+1 sous-listes, chacune contenant M+1 zéros. 
    # Cette table va servir à mémoriser des résultats optimaux intermédiaires sur des intervalles de jours.
    dp = [[0]*(M+1) for i in range(M+1)]
    # Parcours des éléments de la liste P, tout en conservant l'indice de boucle t (qui commence à 0 et va jusqu'à N-1).
    # Chaque élément de P s'attend à contenir trois entiers (i, j, w).
    for t, (i, j, w) in enumerate(P):
        # On ajoute à la sous-liste de E correspondant au jour i-1, un tuple composé de
        # t (l'indice de l'élément, pour servir plus tard à la gestion d'ordre),
        # j (un jour cible),
        # et w (une valeur ou poids associé à cet événement).
        E[i-1].append((t, j, w))
    # Première grande boucle sur les jours i, de 0 à M-1, donc sur tous les jours possibles.
    for i in range(M):
        # Pour bien comprendre, récupérons la sous-liste des événements commençant le jour i.
        Ei = E[i]
        # Première sous-boucle : on parcourt tous les jours j de i à M-1 inclus,
        # donc tous les jours postérieurs ou égaux à i. 
        for j in range(i, M):
            # A chaque couple (i+1, j+1), on met à jour la valeur de dp en prenant le maximum entre
            # 1) l'état courant dp[i+1][j+1]
            # 2) dp[i+1][j] (c'est-à-dire sans étendre "j")
            # 3) dp[i][j+1] (c'est-à-dire sans étendre "i")
            # Cela permet de propager les informations d'optimalité sur la grille DP.
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
        # Deuxième sous-boucle, cette fois en partant de M-1 jusqu'à i+1 (non inclus), donc parcours à l'envers.
        for j in range(M-1, i, -1):
            # On récupère la valeur courante dp[i+1][j+1] dans une variable v.
            v = dp[i+1][j+1]
            # Pour chaque événement (_, k, w) commençant au jour i (donc dans Ei),
            # On cherche à mettre à jour la DP entre la position courante (i+1 ici) et la cible k+1 ou j+1.
            for _, k, w in Ei:
                # Si l'indice cible k est strictement inférieur à j,
                if k < j:
                    # On pousse la nouvelle valeur v + w dans dp sur l'intervalle [k+1][j+1], avec un maximum.
                    dp[k+1][j+1] = max(dp[k+1][j+1], v + w)
                else:
                    # Sinon, on pousse dans l'autre sens, sur [j+1][k+1].
                    dp[j+1][k+1] = max(dp[j+1][k+1], v + w)
        # Traitement du cas où les deux bornes sont égales (i.e. diagonale principale),
        # Ici, v prend la valeur dp[i+1][i+1], qui représente l'état optimal courant sur l'intervalle (i, i).
        v = dp[i+1][i+1]
        # Pour chaque événement (t1, k1, w1) de la liste Ei, c'est-à-dire ceux démarrant aujourd'hui :
        for t1, k1, w1 in Ei:
            # Mise à jour pour la sélection de cet événement seul : ajout de son poids w1.
            dp[i+1][k1+1] = max(dp[i+1][k1+1], v + w1)
            # On examine toutes les paires d'événements distincts de Ei.
            for t2, k2, w2 in Ei:
                # On s'arrête lorsque t1 <= t2 : on évite les redondances ou maintient l'ordre croissant des indices t1, t2.
                if t1 <= t2:
                    break
                # Si l'indice de fin de t1 est inférieur à celui de t2, 
                if k1 < k2:
                    # On met à jour dp pour inclure la combinaison des deux événements, sur l'intervalle [k1+1][k2+1]
                    dp[k1+1][k2+1] = max(dp[k1+1][k2+1], v + w1 + w2)
                else:
                    # Sinon, on met à jour symétriquement [k2+1][k1+1]
                    dp[k2+1][k1+1] = max(dp[k2+1][k1+1], v + w1 + w2)
    # Enfin, une fois la table dp complètement évaluée, 
    # on recherche le maximum absolu de toutes les valeurs de dp (en prenant le maximum de chaque sous-liste dpi, puis le maximum global).
    print(max(max(dpi) for dpi in dp))