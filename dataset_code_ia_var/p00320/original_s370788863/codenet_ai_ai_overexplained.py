# Création d'une liste vide nommée 'lst' qui contiendra 6 ensembles
# Pour chaque itération de la boucle for (de 0 à 5 inclus, soit 6 itérations), on fait :
#   - On utilise input() pour permettre à l'utilisateur d'entrer une ligne de texte qui représente des entiers séparés par des espaces.
#   - La méthode .split() sépare la chaîne d'entrée en sous-chaînes pour chaque espace trouvé.
#   - map(int, ...) convertit chaque sous-chaîne obtenue après le split en entier.
#   - set(...) prend l'itérable résultant et crée un ensemble contenant ces entiers (un ensemble ne contient pas de doublons, l'ordre n'est pas garanti).
# La compréhension de liste encapsule tout ce processus pour exécuter le tout 6 fois et stocker chaque ensemble dans la liste 'lst'.
lst = [set(map(int, input().split())) for _ in range(6)]

# Initialisation d'une liste vide nommée 'rec' qui permettra de stocker des tuples indiquant le nombre d'occurrences et l'ensemble associé.
rec = []

# Début d'une boucle while qui s'exécute tant que la liste 'lst' n'est pas vide
while lst:
    # On prend le premier ensemble de la liste 'lst' et le stocke dans la variable 'x'
    x = lst[0]
    # Utilisation de la méthode .count() pour compter combien de fois l'ensemble 'x' apparaît dans la liste 'lst'
    count = lst.count(x)
    # On vérifie si le nombre d'occurrences de 'x' dans 'lst' est impair (le reste de la division euclidienne par 2 est 1)
    if count % 2 == 1:
        # Si le nombre d'occurrences est impair, on affiche "no"
        print("no")
        # On quitte immédiatement la boucle while avec 'break'
        break
    # On ajoute le tuple (count, x) à la liste 'rec'
    rec.append((count, x))
    # Pour chaque occurrence de 'x' (autant de fois que sa valeur de 'count'), on supprime 'x' de 'lst'
    for _ in range(count):
        # lst.index(x) retourne l'indice de la première occurrence de 'x' dans 'lst' (l'ensemble)
        # lst.pop(...) supprime puis renvoie l'élément à l'indice spécifié, ce qui modifie 'lst' en place
        lst.pop(lst.index(x))
# Le bloc 'else' associé à la boucle while s'exécute uniquement si le while se termine sans 'break'
else:
    # Si le nombre de tuples dans la liste 'rec' vaut exactement 1
    if len(rec) == 1:
        # On considère le seul tuple stocké dans 'rec', il est à l'indice 0
        # L'ensemble correspondant est stocké à l'indice 1 du tuple (count, x)
        # On teste si la taille de cet ensemble est égale à 1 (c'est-à-dire ensemble à un seul élément)
        if len(rec[0][1]) == 1:
            # Si cet ensemble a exactement un seul élément, on affiche "yes"
            print("yes")
        else:
            # Sinon (l'ensemble contient plus d'un élément), on affiche "no"
            print("no")
    # Sinon, si la liste 'rec' contient exactement 2 tuples
    elif len(rec) == 2:
        # On trie la liste 'rec', ce qui peut permettre de garantir un ordre spécifique permettant la suite des tests
        rec.sort()
        # On teste si l'intersection entre les deux ensembles de rec (rec[0][1] & rec[1][1]) est exactement le premier ensemble (rec[0][1])
        if rec[0][1] & rec[1][1] == rec[0][1]:
            # Si oui, alors on affiche "yes"
            print("yes")
        else:
            # Sinon, on affiche "no"
            print("no")
    # Sinon, si la liste 'rec' contient exactement 3 tuples
    elif len(rec) == 3:
        # On vérifie que chaque ensemble dans les 3 tuples de rec a exactement 2 éléments (len(rec[0][1]) == 2, etc.)
        # Ensuite, on vérifie si l'intersection entre rec[2][1] (troisième ensemble) et l'union des deux premiers ensembles est égal au troisième ensemble
        # - rec[0][1] | rec[1][1] : union des deux premiers ensembles
        # - rec[2][1] & (...)     : intersection entre le troisième ensemble et l'union des deux premiers
        # - == rec[2][1]          : on regarde si l'intersection est exactement le troisième ensemble
        if len(rec[0][1]) == len(rec[1][1]) == len(rec[2][1]) == 2 and (rec[2][1] & (rec[0][1] | rec[1][1]) == rec[2][1]):
            # Si les deux conditions sont vraies, on affiche "yes"
            print("yes")
        else:
            # Sinon, on affiche "no"
            print("no")