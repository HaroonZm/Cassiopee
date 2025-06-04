# Commence une boucle 'while' infinie. La boucle continuera à s'exécuter encore et encore jusqu'à l'apparition d'un 'break'
while 1:
    # Demande à l'utilisateur d'entrer une valeur au clavier. La fonction 'input()' lit la saisie de l'utilisateur sous forme de chaîne de caractères (string)
    n = input()
    # Si la valeur entrée par l'utilisateur est exactement égale à zéro (0), alors sortir de la boucle grâce à 'break'
    if n == 0:
        break
    # Demande maintenant à l'utilisateur une nouvelle ligne de nombres séparés par des espaces à l'aide de 'raw_input()'
    # Ceci est typique de Python 2 ; en Python 3, il faudrait remplacer 'raw_input()' par 'input()'
    # 'raw_input().split()' divise la chaîne de caractères entrée par l'utilisateur en une liste de sous-chaînes selon les espaces
    # 'map(int, ...)' convertit chaque sous-chaîne (qui représente un nombre) en un entier (type int)
    t = map(int, raw_input().split())
    # 'max(t)' permet de trouver la plus grande valeur présente dans la séquence 't'
    # Si le maximum des nombres de la liste 't' est strictement inférieur à 2, alors imprime "NA" (Not Available)
    # Sinon, l'autre partie du 'if' est exécutée :
    # [i for i in t if i > 0] est une compréhension de liste qui va créer une nouvelle liste contenant seulement les éléments de 't' strictement positifs (>0)
    # len([i for i in t if i > 0]) donne le nombre total d'éléments de cette nouvelle liste, c'est-à-dire le nombre d'éléments strictement positifs dans 't'
    # On ajoute 1 à ce nombre trouvé, puis on affiche ce résultat sur la sortie standard (l'écran) grâce à 'print'
    print "NA" if max(t) < 2 else 1 + len([i for i in t if i > 0])