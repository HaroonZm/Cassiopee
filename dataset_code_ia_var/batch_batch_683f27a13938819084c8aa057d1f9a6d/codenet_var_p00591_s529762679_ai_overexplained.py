# Débute une boucle infinie qui ne s'arrêtera que si une condition explicite de sortie est rencontrée.
while True:
    # Utilise la fonction input() pour lire une ligne de texte à partir de l'entrée standard (console) et l'assigne à la variable n.
    n = input()
    # Vérifie si la valeur entrée par l'utilisateur est exactement égale à 0 (zéro).
    if n == 0:
        # Si c'est le cas, sort immédiatement de la boucle while grâce à l'instruction break.
        break

    # Construit une liste L de longueur n. Utilise une compréhension de liste pour créer L :
    #   - Pour chaque valeur de i allant de 0 à n-1 (grâce à range(n)), effectue les opérations suivantes :
    #   - raw_input() lit une ligne saisie par l'utilisateur (fonctionne en Python 2).
    #   - split() divise cette ligne en différents morceaux là où se trouvent des espaces, créant une liste de chaînes.
    #   - map(int, ...) applique la fonction int à chaque chaîne de la liste résultante, transformant chaque élément en entier.
    #   - map(...) retourne un itérable (en Python 2, équivalent à une liste d'entiers).
    #   - La liste résultante contient donc n lignes, chacune étant une liste de nombres entiers.
    L = [map(int, raw_input().split()) for i in range(n)]

    # Crée un ensemble S (c'est-à-dire un ensemble d'éléments uniques).
    # Pour chaque élément i (c'est-à-dire chaque ligne) dans la liste L :
    #   - min(i) calcule la plus petite valeur de la ligne i.
    #   - Ceci est fait pour chaque ligne de L, et on ajoute chaque minimum à l'ensemble S.
    S = set([min(i) for i in L])

    # Boucle à travers chaque colonne de la matrice transposée de L :
    #   - Pour chaque index de colonne j (de 0 à n-1, grâce à range(n)), effectue les opérations suivantes :
    #   - Pour chaque ligne i dans L, prend le j-ième élément (i[j]).
    #   - Cela crée la liste t qui contient tous les éléments de la colonne j.
    for t in [[i[j] for i in L] for j in range(n)]:
        # max(t) calcule la valeur maximum de la colonne t et l'assigne à la variable maxInt.
        maxInt = max(t)
        # Vérifie si le maximum de cette colonne fait aussi partie de l'ensemble S des valeurs minimales par ligne.
        if maxInt in S:
            # Si c'est le cas, imprime cette valeur maxInt (affichage à la sortie standard).
            print maxInt
            # Sort de la boucle for, c'est-à-dire arrête de chercher d'autres colonnes.
            break
    # Si la boucle for n'a pas trouvé de solution et s'est exécutée entièrement sans trouver de maxInt dans S,
    # alors le bloc else s'exécute (c'est une particularité de la syntaxe Python for-else).
    else:
        # Affiche 0 pour indiquer qu'aucun maximum de colonne n'appartient à l'ensemble S.
        print 0