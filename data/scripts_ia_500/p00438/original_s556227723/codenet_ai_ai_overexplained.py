while True:
    # Boucle infinie qui va continuer à demander des entrées et traiter les données jusqu'à ce qu'une condition d'arrêt soit rencontrée.
    
    a, b = map(int, input().split())
    # On lit une ligne de l'entrée standard (typiquement ce que l'utilisateur tape).
    # input() récupère cette ligne de texte sous forme d'une chaîne de caractères.
    # La méthode split() scinde cette chaîne en une liste de sous-chaînes, séparées par des espaces.
    # map(int, ...) applique la fonction int à chaque élément de cette liste, convertissant ainsi chaque morceau en un entier.
    # On assigne ces deux entiers aux variables a et b respectivement.
    # a et b représentent probablement les dimensions d'une grille ou d'un tableau (largeur et hauteur).

    if a == b == 0:
        # Cette condition vérifie si a et b sont tous les deux égaux à zéro.
        # L'expression 'a == b == 0' est équivalente à 'a == 0 and b == 0'.
        # Si c'est vrai, cela indique la fin du traitement et on doit sortir de la boucle infinie.
        break
        # L'instruction break termine immédiatement la boucle while True,
        # donc plus aucun code dans la boucle ne sera exécuté après ce point.

    n = int(input())
    # On lit un entier n qui représente probablement le nombre d'éléments ou d'obstacles qu'on va recevoir ensuite.
    # On utilise input() pour récupérer une chaîne, puis int() pour la convertir en entier.

    lst = [[1] * (a + 1) for _ in range(b + 1)]
    # Création d'une liste à deux dimensions (une "matrice" ou "tableau").
    # lst sera une liste contenant (b + 1) sous-listes.
    # Chaque sous-liste contient (a + 1) fois l'entier 1.
    # Cela initialise toutes les cases à 1.
    # On utilise une compréhension de liste avec une variable _ (underscore) car cette variable prend des valeurs de 0 à b,
    # mais on ne s'en sert pas ; c'est juste pour répéter la création des sous-listes.

    lst[0] = [0] * (a + 1)
    # On remplace la première sous-liste (index 0) par une nouvelle liste contenant (a + 1) zéros.
    # Cela signifie que la "première ligne" (dans le contexte 2D) est remplie de zéros.
    # Ceci prépare la matrice avec une bordure spécifique de zéros en haut.

    for y in range(2, b + 1):
        # Cette boucle for parcourt les indices y de 2 jusqu'à b inclus.
        # range(2, b + 1) produit une séquence de nombres entiers: 2, 3, ..., b.
        # Ces indices correspondent probablement à des lignes dans la matrice lst (en commençant au deuxième index).

        lst[y][0] = 0
        # Pour chaque ligne y, on modifie la première colonne (index 0) de cette ligne pour y mettre 0.
        # Cela signifie qu'on crée une bordure de zéros dans la première colonne, à partir de la ligne 2.
        # Note: lst[1][0] reste à 1 car on ne modifie pas cet indice ici.

    for _ in range(n):
        # Cette boucle s'exécute n fois, où n a été défini précédemment.
        # La variable _ est utilisée comme compteur mais on ne s'en sert pas dans la boucle.
        # Cela va permettre de lire n lignes d'entrée pour récupérer des informations spécifiques.

        c = list(map(int, input().split()))
        # Pour chaque itération de la boucle, on lit une ligne d'entrée,
        # la divise en morceaux avec split, convertit chaque morceau en entier avec map,
        # et enfin transforme l'objet map en liste.
        # On obtient donc une liste d'entiers c.

        lst[c[1]][c[0]] = 0
        # On utilise les deux premiers éléments de la liste c (c[0] et c[1]) comme indices pour modifier lst.
        # lst est une matrice d'indices [ligne][colonne] (donc [y][x]).
        # On assigne la valeur 0 à cette position spécifique dans la matrice,
        # probablement pour indiquer que cette case est bloquée ou inaccessible.

    for x in range(1, a + 1):
        # Boucle sur x allant de 1 à a inclus.
        # Cela correspond à parcourir toutes les colonnes valides à partir de la colonne 1.

        for y in range(1, b + 1):
            # Pour chaque x, on boucle sur y allant de 1 à b inclus.
            # Cela correspond à parcourir toutes les lignes valides à partir de la ligne 1.
            # On traite ainsi chaque élément de la matrice en excluant la première ligne et la première colonne.

            if lst[y][x] == 0:
                # Si la case courante dans la matrice contient un 0,
                # cela signifie que cette cellule est bloquée ou inaccessible.
                # On ne modifie donc pas cette case et on passe à l'itération suivante.

                continue
                # L'instruction continue fait passer directement à l'itération suivante de la boucle for y,
                # donc tout code après continue dans ce bloc n'est pas exécuté pour cette itération.

            lst[y][x] = lst[y - 1][x] + lst[y][x - 1]
            # Si la case n'est pas bloquée, on met à jour sa valeur en faisant la somme de la valeur juste au-dessus
            # (même colonne, ligne précédente) et la valeur à gauche (même ligne, colonne précédente).
            # Cela correspond typiquement au calcul du nombre de chemins possibles pour atteindre cette cellule,
            # en additionnant le nombre de chemins venant d'en haut et de gauche.
            # On modifie directement la matrice lst qui contient donc des nombres de chemins.

    print(lst[b][a])
    # Après avoir rempli la matrice avec les calculs de chemins possibles,
    # on affiche la valeur contenue dans la case située à la ligne b et la colonne a.
    # Cette valeur représente sûrement le nombre total de chemins valides pour aller d'un point de départ à ce point final,
    # en respectant les cases bloquées (0).