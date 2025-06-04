def solve():
    # Importation du module sys, qui fournit des fonctions et des objets utiles pour interagir avec l'interpréteur Python.
    # Ici, on importe spécifiquement 'stdin', qui est un flux permettant de lire l'entrée standard (par exemple, les données saisies par l'utilisateur ou redirigées à partir d'un fichier).
    from sys import stdin
    
    # On crée un alias pour stdin (ici 'f_i') afin de faciliter les futurs appels de lecture d'entrée.
    f_i = stdin
    
    # Lecture de la première ligne depuis l'entrée standard.
    # readline() lit une ligne à la fois, qui inclut généralement un caractère de saut de ligne '\n' à la fin.
    # int() convertit la chaîne de caractères lue en un entier.
    # Ici, on lit le nombre 'n', qui représente probablement le nombre d'éléments dans un tableau ou une séquence.
    n = int(f_i.readline())
    
    # Lecture de la seconde ligne depuis l'entrée standard, qui contient probablement une séquence de nombres séparés par des espaces.
    # readline() lit la ligne entière sous forme de chaîne.
    # split() sépare la chaîne en une liste de sous-chaînes en découpant à chaque espace par défaut.
    # map(int, ...) applique la fonction int() à chaque élément de la liste obtenue, convertissant chaque sous-chaîne en entier.
    # list() transforme le résultat map en une vraie liste d'entiers.
    # Résultat : A est une liste d'entiers reconstruite à partir de l'entrée.
    A = list(map(int, f_i.readline().split()))
    
    # Lecture du nombre de requêtes à traiter.
    # À nouveau, on lit une ligne et on la convertit en entier.
    q = int(f_i.readline())
    
    # Importation du module bisect, qui contient des fonctions pour travailler efficacement avec des listes triées.
    # bisect_left renvoie la position où un élément pourrait être inséré pour maintenir la liste triée.
    # Ici, bisect_left est importé sous l'alias 'bl' pour simplifier et raccourcir son utilisation.
    from bisect import bisect_left as bl
    
    # On utilise une compréhension de générateur pour traiter chaque requête.
    # Pour chaque valeur de 'i' comprise entre 0 (inclus) et q (exclus) : range(q) engendre 'q' valeurs entières croissantes.
    # Pour chaque itération, on lit une ligne (la requête), on la convertit en entier (c'est la valeur recherchée).
    # bl(A, ...) trouve la première position d'insertion correcte de cet entier dans la liste A (qui doit être triée pour bisect_left).
    # str(...) convertit ce résultat (un entier) en chaîne de caractères pour l'affichage.
    # L'ensemble est passé à '\n'.join(...) pour concaténer chaque chaîne résultat avec un saut de ligne entre elles.
    # print(...) affiche le résultat final, chaque réponse étant sur une nouvelle ligne.
    print('\n'.join(
        str(bl(A, int(f_i.readline())))
        for i in range(q)
    ))

# Appel de la fonction 'solve', qui exécute tout le code ci-dessus.
solve()