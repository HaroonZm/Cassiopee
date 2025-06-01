while True:
    # Début d'une boucle infinie qui sera interrompue explicitement avec un break lorsque la condition le demandera.
    # Cette boucle sert à traiter plusieurs cas successifs jusqu'à ce qu'une condition d'arrêt soit rencontrée.

    n = int(input())
    # On lit une entrée utilisateur, supposée représenter un entier.
    # La fonction input() récupère une chaîne de caractères depuis l'entrée standard (clavier),
    # puis int() convertit cette chaîne en un nombre entier.
    # Ce nombre 'n' symbolise ici typiquement la taille d'une structure ou le nombre de noeuds.

    if n == 0:
        # Test si la valeur de 'n' est égale à 0.
        # Cette condition sert d'arrêt pour la boucle infinie.
        break
        # Sortie immédiate de la boucle while si la condition est vraie.
    
    edges = [[] for _ in range(n)]
    # Création d'une liste de listes vide, appelée 'edges'.
    # La compréhension de liste itère sur une plage de 0 à n-1.
    # Chaque élément 'edges[i]' est initialisé à une liste vide.
    # Cette structure va représenter les arêtes (connexions) dans un graph sous forme de listes d'adjacence.

    for _ in range(n - 1):
        # Boucle qui s'exécute n-1 fois.
        # Le caractère underscore '_' est utilisé ici comme variable jetable,
        # signifiant que la variable d'itération n'est pas utilisée dans le corps de la boucle.
        # Cette boucle sert à lire les informations sur les arêtes entre les noeuds.

        a, b, t = map(int, input().split())
        # Lecture d'une ligne input, split() divise la chaîne d'entrée en sous-chaînes séparées par espaces.
        # map(int, ...) applique la fonction int à chacune de ces sous-chaînes, convertissant chaque partie en entier.
        # Les trois entiers lus sont assignés aux variables a, b, t.
        # 'a' et 'b' représentent deux noeuds connectés par une arête.
        # 't' représente probablement un poids, un temps ou une distance associé à cette arête.

        a -= 1
        b -= 1
        # On décrémente 'a' et 'b' de 1 pour passer d'un système d'indexation 1-based (commençant à 1)
        # à un système 0-based (commençant à 0) utilisé par la plupart des structures en Python.

        edges[a].append([b, t])
        edges[b].append([a, t])
        # On ajoute dans la liste d'adjacence le noeud 'b' avec son poids 't' dans la liste des voisins de 'a',
        # et réciproquement, car le graph est non orienté.
        # Cela signifie que la connexion entre a et b est bidirectionnelle.

    used = [False] * n
    # Création d'une liste booléenne de longueur n initialisée à False.
    # Cette liste servira à marquer les noeuds déjà visités dans une exploration ou parcours.
    # 'False' signifie que le noeud n'a pas encore été exploré.

    is_leaf = [False] * n
    # Création d'une autre liste booléenne de longueur n, initialisée à False,
    # destinée à indiquer pour chaque noeud s'il est une 'feuille' dans le graph (noeud avec un seul voisin).

    for i in range(1, n):
        # Parcours de tous les noeuds de l'indice 1 à n-1 (exclusion du noeud 0).
        # On ne teste pas le noeud 0 ici pour déterminer s'il est une feuille.

        if len(edges[i]) == 1:
            # On teste si le noeud i a exactement un voisin.
            # Dans une structure arborescente, cela caractérise souvent une feuille.

            is_leaf[i] = True
            # Si c'est le cas, on marque ce noeud comme étant une feuille dans la liste is_leaf.

    def check(x):
        # Définition d'une fonction récursive 'check' qui prend en entrée un noeud 'x'.
        # Cette fonction permettra de parcourir le graph et de calculer certains paramètres liés aux temps.

        used[x] = True
        # Marquage immédiat du noeud x comme visité afin d'éviter la revisite lors de l'exploration récursive.

        times = [0]
        # Initialisation d'une liste 'times' avec un élément zéro.
        # Cette liste va accumuler des durées de parcours ou pondérations lors de la récurrence.

        max_path = 0
        # Initialisation d'une variable 'max_path' à zéro.
        # Cette variable mémorise la plus grande durée ou distance trouvée dans les chemins descendants.

        for to, t in edges[x]:
            # Parcours de chaque voisin 'to' du noeud 'x'.
            # Chaque élément dans edges[x] est une paire [noeud voisin, poids temps].

            if not used[to] and not is_leaf[to]:
                # On n'explore récursivement que si le noeud voisin 'to' n'a pas encore été visité
                # ET s'il n'est pas une feuille.
                # Cette condition évite d'explorer les feuilles et garantit un parcours plus ciblé.

                time, path = check(to)
                # Appel récursif de la fonction check sur le voisin 'to'.
                # On récupère deux valeurs : 'time' (temps total retourné) et 'path' (chemin maximum).

                times.append(time + t * 2)
                # On ajoute dans la liste 'times' la durée 'time' plus le double du poids 't'.
                # Le facteur 2 correspond probablement à un aller-retour sur cette arête.

                max_path = max(max_path, path + t)
                # Mise à jour de 'max_path' en prenant la valeur maximale entre sa valeur actuelle
                # et la somme du chemin maximum descendant ('path') plus le poids 't' de cette arête.

        return sum(times), max_path
        # La fonction retourne un tuple composé de deux valeurs :
        # la somme des temps accumulés dans 'times', représentant un total potentiel,
        # et la plus longue distance trouvée dans les chemins descendantes à partir de x.

    total_time, max_path = check(0)
    # Appel initial de la fonction 'check' sur le noeud 0.
    # On récupère 'total_time', la somme globale des durées allers-retours,
    # ainsi que 'max_path', la plus longue distance sans retour.

    print(total_time - max_path)
    # Affichage du résultat calculé.
    # On soustrait la plus longue distance aux temps totaux pour obtenir un temps optimisé,
    # probablement en évitant un retour inutile sur le chemin le plus long.