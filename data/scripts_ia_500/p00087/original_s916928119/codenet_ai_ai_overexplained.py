# Boucle infinie permettant de traiter plusieurs lignes d'entrée jusqu'à la fin du fichier ou de l'entrée standard
while True :
    try :
        # Récupère une ligne de texte depuis l'entrée standard (comme le clavier ou un fichier)
        # input() lit une ligne complète sous forme de chaîne de caractères
        # split() divise cette chaîne en une liste de sous-chaînes en utilisant l'espace comme délimiteur par défaut
        # list() convertit l'objet iterable retourné par split() en une liste concrète de chaînes
        lst = list(input().split())
    except EOFError :
        # Lorsqu'on atteint la fin de l'entrée (EOF), input() lève une exception EOFError
        # Ici on interrompt la boucle while pour arrêter le programme proprement
        break
    
    # Initialisation d'une pile vide, qui sera utilisée pour évaluer une expression en notation polonaise inversée (postfixe)
    stack = []
    
    # Parcours de chaque élément (opérande ou opérateur) dans la liste d'entrée
    for i in lst :
        # Vérification si l'élément est l'opérateur '+'
        if i == '+' :
            # Lorsque l'on rencontre un opérateur, on retire (pop) les deux derniers éléments de la pile
            # Ces éléments correspondent aux opérandes de l'opération
            b = stack.pop(-1)  # On récupère le dernier élément ajouté à la pile
            a = stack.pop(-1)  # On récupère l'élément avant-dernier
            # On calcule la somme des deux opérandes a et b
            resultat = a + b
            # On ajoute le résultat de l'opération à la pile pour une utilisation éventuelle dans les opérations suivantes
            stack.append(resultat)
        # Vérification de l'opérateur '-'
        elif i == '-' :
            # Idem, récupération des deux opérandes
            b = stack.pop(-1)
            a = stack.pop(-1)
            # Calcul de la différence en respectant l'ordre : a moins b
            resultat = a - b
            # Ajout du résultat à la pile
            stack.append(resultat)
        # Vérification de l'opérateur '*'
        elif i == '*' :
            b = stack.pop(-1)
            a = stack.pop(-1)
            # Calcul du produit des deux opérandes
            resultat = a * b
            stack.append(resultat)
        # Vérification de l'opérateur '/'
        elif i == '/' :
            b = stack.pop(-1)
            a = stack.pop(-1)
            # Calcul de la division de a par b
            # Attention : division flottante en Python 3 (le résultat peut être un nombre à virgule)
            resultat = a / b
            stack.append(resultat)
        else :
            # Si l'élément n'est pas un opérateur, on suppose que c'est un nombre entier sous forme de chaîne de caractères
            # On convertit cette chaîne en un entier grâce à int()
            nombre = int(i)
            # On ajoute ce nombre à la pile, car il sera utilisé dans les opérations suivantes
            stack.append(nombre)
    # Une fois toute la ligne traitée, la pile doit contenir exactement un élément : le résultat final de l'expression
    # On récupère ce résultat à l'indice 0 de la liste stack
    # On affiche ce résultat sous forme décimale avec exactement huit chiffres après la virgule grâce à la méthode format()
    print('{:.8f}'.format(stack[0]))