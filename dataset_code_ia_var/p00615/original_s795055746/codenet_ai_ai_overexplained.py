# Démarre une boucle infinie, ce qui signifie qu'elle s'exécutera jusqu'à ce qu'elle soit explicitement arrêtée par un 'break'.
while 1:
    # Lit une ligne à partir de l'entrée standard (typiquement le clavier), puis sépare cette ligne en deux parties selon les espaces.
    # Utilise ensuite map pour convertir chaque partie séparée en un entier avec int().
    # Les deux entiers ainsi obtenus sont stockés, dans l'ordre, dans les variables n et m.
    n, m = map(int, raw_input().split())

    # Vérifie si les deux variables n ET m valent 0.
    # Si c'est le cas, exécute 'break' pour quitter immédiatement la boucle infinie commencée plus haut.
    if n == m == 0:
        break

    # Crée une liste contenant le seul élément 0. Ceci initialise la liste 'data' avec 0 comme premier élément.
    data = [0]

    # Vérifie si 'n' est strictement supérieur à 0, c'est-à-dire s'il y a des éléments à ajouter pour la première partie.
    if n > 0:
        # Lit une nouvelle ligne de l'entrée standard,
        # utilise split() pour séparer les valeurs et map() pour convertir chaque valeur en int,
        # puis ajoute(+=) cette liste résultante à la liste 'data' créée précédemment.
        data += map(int, raw_input().split())

    # Vérifie si 'm' est strictement supérieur à 0, c'est-à-dire s'il y a des éléments à ajouter pour la deuxième partie.
    if m > 0:
        # Lit une nouvelle ligne de l'entrée standard,
        # sépare les valeurs, les convertit en int, et concatène (+=) à la liste 'data'.
        data += map(int, raw_input().split())

    # Trie la liste 'data' dans l'ordre croissant à l'aide de la méthode sorted().
    # sorted() retourne une nouvelle liste triée sans modifier l'originale ; donc 'data' devient cette nouvelle liste triée.
    data = sorted(data)

    # Pour afficher le résultat, utilise print suivi de l'appel à max() qui déterminera le maximum.
    # L'expression à l'intérieur de max est une compréhension de générateur :
    #    - Pour chaque indice 'i' dans la plage allant de 0 jusqu'à (n + m - 1),
    #    - calcule la différence entre l'élément suivant data[i+1] et l'élément courant data[i].
    # Cela recherche le plus grand écart entre deux éléments consécutifs dans la liste triée.
    # n+m correspond au nombre total d'éléments ajoutés (hors 0) donc range(n+m) va jusqu'à l'avant-dernier.
    print max(data[i+1] - data[i] for i in range(n + m))