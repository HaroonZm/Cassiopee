# Début d'une boucle infinie : le programme restera dans cette boucle jusqu'à ce qu'une instruction de sortie soit rencontrée
while True:
    # Demande à l'utilisateur d'entrer une valeur au clavier avec la fonction input()
    # La valeur entrée est récupérée sous forme de chaîne de caractères
    # La fonction int() convertit cette chaîne en un nombre entier
    n = int(input())
    # Vérifie si la valeur entrée (n) est égale à 0 ; l'opérateur == signifie une comparaison d'égalité
    if n == 0:
        # Interrompt la boucle while et sort complètement de l'instruction while True
        break
    # Initialise un dictionnaire vide, qui sera utilisé pour stocker des données avec des clés uniques
    d = {}
    # Initialise une liste vide, qui permettra de garder en mémoire l'ordre d'apparition des différentes clés rencontrées
    e = []
    # Lance une boucle for qui va s'exécuter n fois ; range(n) génère une séquence d'entiers de 0 jusqu'à n-1
    for i in range(n):
        # Demande à l'utilisateur de saisir une ligne de valeurs séparées par des espaces
        # La méthode split(' ') découpe la chaîne saisie à chaque espace simple et retourne une liste de morceaux de la chaîne
        # La fonction map(int, ...) applique la fonction int à chaque morceau, convertissant chaque élément en entier
        # Enfin, list(...) transforme le résultat du map en une liste d'entiers
        tmp = list(map(int, input().split(' ')))
        # Vérifie si la première valeur de la liste tmp (tmp[0]) existe déjà comme clé dans le dictionnaire d
        if tmp[0] in d:
            # Si oui, on ajoute à la valeur associée à cette clé, le résultat produit par la multiplication des deux autres éléments tmp[1] et tmp[2]
            d[tmp[0]] += tmp[1] * tmp[2]
        else:
            # Si la clé n'existe pas encore dans le dictionnaire, on crée une nouvelle entrée dans d.
            # La valeur associée à cette nouvelle clé est obtenue en multipliant tmp[1] par tmp[2]
            d[tmp[0]] = tmp[1] * tmp[2]
            # On ajoute aussi la nouvelle clé à la liste e pour mémoriser l'ordre d'apparition des clés
            e.append(tmp[0])
    # Après la boucle for, on vérifie si la plus grande valeur présente dans le dictionnaire d est strictement inférieure à 1000000
    # La fonction max(d.values()) retourne la plus grande des valeurs présentes dans le dictionnaire d
    if max(d.values()) < 1000000:
        # Si aucune des valeurs n'atteint ou dépasse 1 000 000, on affiche 'NA'
        print('NA')
    else:
        # Sinon, cela signifie qu'au moins une des valeurs atteint ou dépasse le seuil de 1 000 000
        # On parcourt alors chaque clé enregistrée dans la liste e (c'est-à-dire chaque clé dans l'ordre d'apparition)
        for k in e:
            # Pour chaque clé k, on vérifie si la valeur associée d[k] atteint ou dépasse 1 000 000 (>=)
            if d[k] >= 1000000:
                # Si tel est le cas, on affiche la clé correspondante (qui est un entier)
                print(k)