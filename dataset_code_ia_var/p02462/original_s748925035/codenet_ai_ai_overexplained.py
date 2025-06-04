import bisect  # Nous importons le module bisect, qui fournit des fonctions pour manipuler efficacement des listes triées

q = int(input())  # On lit un entier depuis l'entrée standard, ce qui représente le nombre de requêtes à traiter, et on le stocke dans q

M = {}  # On initialise un dictionnaire vide appelé M. Ce dictionnaire sera utilisé pour stocker des listes de valeurs associées à chaque clé (chaque clé étant une chaîne de caractères)
sortedList = []  # On initialise une liste vide sortedList qui contiendra toutes les clés ajoutées, maintenue dans l'ordre croissant (ordre lexicographique)

# On exécute une boucle autant de fois qu'il y a de requêtes, c'est-à-dire q fois
for value in range(q):
    # On lit une ligne depuis l'entrée standard, puis on la découpe (split) en plusieurs mots (espaces comme séparateurs)
    # La première partie de la ligne correspond à la commande (query)
    # Le reste de la ligne (inp) contient des arguments supplémentaires
    query, *inp = input().split()  # 'query' récupère le premier mot, '*inp' récupère les autres dans une liste
    key = inp[0]  # La première valeur d'arguments supplémentaires est considérée comme la clé (dans le cas des requêtes 0, 1, 2 et 3)
    
    # Si la commande (query) vaut "0", cela signifie que l'on souhaite insérer une valeur associée à une clé
    if query == "0":
        # On récupère la deuxième valeur d'arguments (inp[1]) et on la convertit en entier ; il s'agit de la valeur à ajouter
        x = int(inp[1])
        
        # On regarde si la clé n'existe pas encore dans le dictionnaire M
        if key not in M:
            # Si elle n'existe pas, on l'insère dans 'sortedList' à la position adéquate afin de garder la liste triée grâce à bisect.insort_left
            bisect.insort_left(sortedList, key)
            # On initialise la valeur associée à la clé, c'est-à-dire une liste vide qui stockera de futurs éléments
            M[key] = []
        
        # On ajoute x à la liste des valeurs associées à cette clé
        M[key].append(x)
    
    # Si la commande (query) vaut "1", cela signifie que l'on souhaite récupérer (et afficher) toutes les valeurs associées à une clé
    elif query == "1":
        # On vérifie d'abord si la clé existe bien dans le dictionnaire M
        if key in M:
            # On vérifie également que la liste des valeurs associée à cette clé n'est pas vide
            if M[key]:
                # On parcourt toutes les valeurs associées à la clé (chaque valeur dans la liste)
                for value in M[key]:
                    # On affiche chaque valeur individuellement sur une ligne séparée grâce à print
                    print(value)
    
    # Si la commande (query) vaut "2", cela signifie que l'on souhaite supprimer (vider) toutes les valeurs associées à une clé
    elif query == "2":
        # On vérifie si la clé existe avant d'essayer de la manipuler
        if key in M:
            # On vide la liste des valeurs de cette clé en l'affectant à une nouvelle liste vide
            M[key] = []
    
    # Si la commande (query) n'est ni "0", ni "1", ni "2" (tout autre type de requête), il s'agit d'une commande "dump"
    else:
        # Pour la commande "dump", on souhaite afficher toutes les valeurs de toutes les clés comprises entre L et R (bornes inclusives ou exclusives selon bisect)
        L = inp[0]  # On récupère la borne gauche (L) parmi les arguments
        R = inp[1]  # On récupère la borne droite (R) parmi les arguments
        
        # On utilise bisect.bisect_left pour trouver l'indice à gauche (la position d'insertion) de L dans la liste triée sortedList
        index_left = bisect.bisect_left(sortedList, L)
        # On utilise bisect.bisect_right pour trouver l'indice immédiatement après la dernière occurrence de R dans la liste triée sortedList
        index_right = bisect.bisect_right(sortedList, R)
        
        # On parcourt tous les indices de la liste triée des clés qui se trouvent entre les indices calculés (de index_left à index_right-1 inclus)
        for value in range(index_left, index_right):
            keyAns = sortedList[value]  # On récupère la clé à cette position dans la liste triée
            # On vérifie si la clé correspondante a des valeurs associées (liste non vide)
            if M[keyAns]:
                # On parcourt toutes les valeurs associées à keyAns
                for valueAns in M[keyAns]:
                    # On affiche la clé et la valeur, séparées par un espace, sur une seule ligne
                    print(keyAns, valueAns)