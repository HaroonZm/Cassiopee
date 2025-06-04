# Demande à l'utilisateur de saisir une valeur depuis l'entrée standard (clavier)
# La fonction input() lit la saisie de l'utilisateur sous forme de chaîne de caractères
# int() convertit la chaîne saisie en un nombre entier (integer)
q = int(input())

# Crée un ensemble vide
# Un ensemble (set) en Python est une collection non ordonnée d'éléments uniques (pas de doublons)
S = set([])

# Boucle qui va s'exécuter q fois (de 0 jusqu'à q-1), où q est le nombre d'opérations à effectuer
for i in range(q):
    # Lire une ligne de l'entrée utilisateur, la diviser en parties distinctes par les espaces
    # map(int, ...) convertit chaque partie en un entier
    # list(...) transforme le résultat en une liste, qui sera de la forme [query, x]
    query, x = list(map(int, input().split()))
    
    # Si la requête (query) correspond à l'opération d'insertion (0), alors on ajoute l'élément x à l'ensemble S
    if query == 0:
        # Ajoute l'élément x à S. Si x est déjà présent, il n'est pas ajouté une deuxième fois (propriété des ensembles)
        S.add(x)
        # Affiche la taille actuelle de S, c'est-à-dire le nombre d'éléments uniques dans l'ensemble
        print(len(S))
    # Si la requête n'est pas 0, alors c'est une opération de recherche (find)
    else:
        # Vérifie si x est présent dans l'ensemble S
        # L'opérateur 'in' retourne True si l'élément est dans la collection, sinon False
        if x in S:
            # Si x est présent, affiche 1 pour indiquer le succès de la recherche
            print(1)
        else:
            # Si x n'est pas dans S, affiche 0 pour indiquer l'échec de la recherche
            print(0)