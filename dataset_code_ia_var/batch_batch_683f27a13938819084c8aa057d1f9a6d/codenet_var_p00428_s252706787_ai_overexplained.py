# Début d'une boucle infinie, ce qui signifie que le code à l'intérieur sera répété sans fin jusqu'à ce qu'une instruction de sortie (break) soit rencontrée.
while True:
    # Lecture d'une ligne de l'utilisateur via raw_input() (fonction pour Python 2, lit une chaîne de caractères).
    # La chaîne lue est ensuite découpée sur l'espace en une liste de sous-chaînes, puis chaque sous-chaîne est convertie en entier grâce à map(int, ...).
    # Les deux entiers obtenus sont affectés respectivement aux variables a et b.
    a, b = map(int, raw_input().split())
    
    # Condition "si a vaut 0 ET b vaut 0" (on teste simultanément l'égalité à zéro pour chaque variable).
    # Si c'est vrai, alors l'instruction break est exécutée, ce qui force la sortie immédiate de la boucle while la plus proche (ici, la boucle infinie).
    if a == 0 and b == 0:
        break

    # Création d'une liste vide nommée list. Cette liste servira à stocker des sommes d'entiers.
    # Note : "list" est aussi un mot-clé du langage Python (mais ici il est utilisé comme nom de variable).
    list = []

    # Boucle for qui va s'exécuter une fois pour chaque entier i de 0 (inclus) à a (exclu).
    # xrange(a) génère une séquence d'entiers de 0 à a-1 (uniquement pour Python 2, équivalent de range en Python 3).
    for i in xrange(a):
        # À chaque itération de la boucle, on demande à l'utilisateur de saisir une nouvelle ligne à l'aide de raw_input().
        # Ce sera typiquement une ligne avec b entiers séparés par des espaces.
        code = raw_input()

        # Deuxième boucle for imbriquée, sur j cette fois de 0 (inclus) à b (exclu).
        for j in xrange(b):
            # Si la longueur de la liste list est inférieure à b (donc la première fois que des éléments sont ajoutés), alors on ajoute la valeur 0.
            # Ceci assure que list a toujours exactement b éléments, donc l'indexation à list[j] sera valide pour tout j.
            if len(list) < b:
                list.append(0)
            # Ajoute à la j-ième position de la liste list l'entier correspondant à la j-ième colonne de la ligne lue.
            # code.split() découpe la chaîne 'code' sur les espaces, et int(code.split()[j]) transforme le j-ième 'mot' ainsi obtenu en entier.
            list[j] += int(code.split()[j])

    # Création d'un nouveau dictionnaire vide appelé dict (mot-clé réservé en Python, mais autorisé ici comme nom de variable).
    dict = {}
    # Remplit le dictionnaire tel que chaque clé i (pour i de 0 à b-1) aura pour valeur list[i], c'est-à-dire la somme de la colonne i.
    for i in xrange(b):
        dict[i] = list[i]

    # Trie les éléments (paires clé/valeur) du dictionnaire, selon la valeur (x[1]), par ordre décroissant (reverse=True).
    # dict.items() renvoie une liste de tuples (clé, valeur).
    # sorted(..., key=..., reverse=True) trie les éléments par clé ou valeur selon la fonction key, et de façon décroissante ici.
    dic = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    # Boucle for qui parcourt chaque élément du résultat trié dic.
    for var in dic:
        # var est un tuple (clé, valeur). On affiche la clé + 1 suivie d'un espace (la virgule à la fin de print, uniquement en Python 2, empêche de sauter une ligne).
        # On ajoute 1 car les indices sont comptés à partir de 1 dans l'affichage (et pas 0 comme les indices Python le font normalement).
        print var[0] + 1,
    # Affiche rien (print vide = nouvelle ligne). Cela termine la ligne d'affichage en cours afin que chaque jeu d'entrée donne sa propre ligne.
    print