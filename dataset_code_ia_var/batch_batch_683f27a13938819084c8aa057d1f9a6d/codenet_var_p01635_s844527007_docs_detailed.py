def parse_and_evaluate_expression():
    """
    Lit les entrées standard pour n et t, ainsi qu'une expression mathématique sous forme de chaîne.
    Modifie l'expression pour être compatible avec Python (gestion des puissances et de la variable n),
    puis évalue cette expression avec les valeurs lues.
    Multiplie le résultat par t et affiche le résultat final.
    Si le résultat dépasse 10**9, affiche 'TLE' au lieu du résultat.
    """
    # Lire deux entiers n et t à partir de l'entrée standard de l'utilisateur
    n, t = map(int, raw_input().split())

    # Lire l'expression mathématique sous forme de chaîne de caractères
    s = raw_input()

    # Remplacer l'opérateur ^ par ** pour respecter la syntaxe des puissances en Python
    s = s.replace("^", "**")

    # Remplacer toutes les occurrences de la variable 'n' par la valeur lue de n (sous forme de chaîne)
    s = s.replace("n", str(n))

    # Évaluer l'expression mathématique résultante et multiplier le résultat par t
    r = eval(s) * t

    # Vérifier si le résultat excède 10^9
    if r > 10 ** 9:
        # Si oui, afficher "TLE" (Time Limit Exceeded)
        print "TLE"
    else:
        # Sinon, afficher le résultat
        print r

# Appeler la fonction principale pour exécuter le programme
parse_and_evaluate_expression()