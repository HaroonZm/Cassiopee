# Boucle infinie, qui sera arrêtée manuellement avec 'break' à l'intérieur de la boucle
while 1:
    # On lit une ligne d'entrée utilisateur (par exemple '3 5'), puis on la découpe en morceaux
    # Ensuite, on convertit chaque morceau en entier à l'aide de 'map' et 'int'
    # On affecte respectivement les deux entiers lus aux variables 'n' et 'm'
    n, m = map(int, raw_input().split())
    
    # Vérification de la condition d'arrêt : si à la fois n == 0 et m == 0,
    # on quitte la boucle à l'aide de 'break'
    if n == m == 0:
        break

    # Création d'une liste de sous-listes 'p'. Cette liste comprend m éléments.
    # Chaque sous-liste est de la forme [0, m-i], où i varie de 1 à m (inclus)
    # Cela signifie, par exemple pour m=5 :
    # i=1 : [0,4], i=2 : [0,3], ..., i=5 : [0,0]
    # La première case (0) servira à stocker une somme dont on parlera plus loin
    # Utilisation de 'xrange' pour générer la séquence d'entiers de 1 à m
    p = [[0, m - i] for i in xrange(1, m + 1)]
    
    # On utilise une boucle pour parcourir les n lignes suivantes (chaque ligne représente des marques/notes)
    for i in xrange(n):
        # On lit la prochaine ligne d'entrée contenant m entiers séparés par des espaces (ex: '1 0 1 2 0')
        # La fonction 'split' divise la chaîne d'entrée en une liste de chaînes, chaque élément correspondant à une colonne
        mark = raw_input().split()
        # Pour chaque colonne de 0 à m-1, on convertit la chaîne en entier avec 'int'
        # et on l'ajoute à la première case de la sous-liste correspondante dans 'p'
        # Ainsi, p[i][0] accumule la somme des entrées à la colonne i sur toutes les lignes
        for i in xrange(m):
            p[i][0] += int(mark[i])

    # On trie la liste 'p' en ordre décroissant (reverse=True)
    # Le tri s'effectue en premier sur p[i][0] car c'est le premier élément
    # S'il y a égalité, alors p[i][1] sert de critère, i.e. l'indice m-i original
    p.sort(reverse=True)

    # Création d'une nouvelle liste 's' qui va stocker les résultats finaux transformés en chaînes de caractères
    # Pour chaque index i de 0 à m-1, on calcule m - p[i][1]
    # Ceci retrouve l'indice de colonne original (puisque p[i][1] == m - colonne)
    # On convertit chaque nombre entier en chaîne avec 'str' pour pouvoir ensuite les assembler
    s = [str(m - p[i][1]) for i in range(m)]
    
    # On rassemble les éléments de la liste 's' en une seule chaîne, séparés par des espaces
    # Finalement, on affiche cette chaîne avec 'print'
    print " ".join(s)