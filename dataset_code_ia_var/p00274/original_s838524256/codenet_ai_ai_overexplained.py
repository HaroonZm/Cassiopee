# Commence une boucle infinie car la condition de la boucle est "while 1", et 1 est toujours vrai en Python.
while 1:
    # Demande à l'utilisateur de saisir une valeur et l'assigne à la variable 'n'.
    # La fonction 'input()' lit une ligne de texte que l'utilisateur saisit.
    n = input()
    # Vérifie si la valeur saisie 'n' est égale à zéro.
    # En Python, '==' est l'opérateur de comparaison d'égalité.
    if n == 0:
        # Si la condition est vraie, utiliser 'break' pour sortir de la boucle 'while'.
        break
    # Appelle la fonction 'raw_input()' qui lit une chaîne de caractères depuis l'entrée standard (fonctionne en Python 2).
    # Cette chaîne contient des nombres séparés par des espaces. 
    # La méthode 'split()' sépare la chaîne en une liste de sous-chaînes, découpant partout où il y a des espaces.
    # La fonction 'map(int, ...)' convertit chaque élément de la liste en un entier.
    # Le résultat de 'map' est un objet itérable contenant les entiers, assigné à la variable 't'.
    t = map(int, raw_input().split())
    # Utilise la fonction 'max(t)' pour trouver la plus grande valeur dans 't'.
    # Vérifie si la valeur maximale dans 't' est strictement inférieure à 2.
    if max(t) < 2:
        # Si tous les éléments sont inférieurs à 2, affiche la chaîne de caractères "NA".
        print "NA"
        # Utilise 'continue' pour passer immédiatement à la prochaine itération de la boucle, sans exécuter le reste du bloc.
        continue
    # Construit une liste en compréhension : [i for i in t if i>0].
    # Parcourt chaque élément 'i' de 't' et inclut 'i' dans la nouvelle liste seulement si 'i' est strictement supérieur à 0.
    # Calcule ensuite la longueur de cette liste grâce à la fonction 'len()', ce qui donne le nombre d'éléments positifs dans 't'.
    # Ajoute 1 à ce résultat.
    # Utilise 'print' pour afficher cette valeur.
    print 1 + len([i for i in t if i > 0])