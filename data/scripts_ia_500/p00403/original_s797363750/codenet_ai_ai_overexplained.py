L = int(input())  # Lecture de la première entrée utilisateur et conversion en entier. Cette variable représente généralement la longueur ou un nombre d'éléments à traiter.

# Lecture d'une ligne d'entrée utilisateur contenant plusieurs nombres séparés par des espaces.
# La fonction input() récupère la chaîne de caractères saisie.
# La méthode split() sépare cette chaîne en une liste de sous-chaînes, séparées par des espaces.
# La fonction map(int, ...) convertit chaque sous-chaîne en entier.
# La fonction list() transforme l'itérateur retourné par map en une liste d'entiers.
C = list(map(int, input().split()))

A = []  # Initialisation d'une liste vide A qui servira à stocker certains éléments de C selon des conditions données.

# Parcours de la liste C en utilisant une boucle for. La variable i représente l'indice courant, allant de 0 à la longueur de C moins 1.
for i in range(len(C)):
    # Condition pour vérifier si l'élément courant C[i] est strictement positif.
    if C[i] > 0:
        # Si l'élément C[i] est déjà présent dans la liste A (c'est-à-dire qu'il y a au moins une occurrence).
        # La méthode count(x) retourne le nombre d'occurrences de x dans la liste.
        if A.count(C[i]):
            # Si C[i] est déjà dans A, on affiche l'indice i+1 (le décalage d'1 est probablement pour correspondre à l'indexation humaine commençant à 1).
            print(i+1)
            # La fonction exit(0) termine l'exécution du programme immédiatement avec un code de sortie 0 signifiant une fin normale.
            exit(0)
        else:
            # Si C[i] n'est pas encore dans A, on ajoute cet élément à la fin de la liste A avec append().
            A.append(C[i])
    else:
        # Si C[i] est zéro ou négatif (strictement <= 0, mais ici filtré spécifiquement pour négatif puisque 0 n'est pas géré autrement).
        # On vérifie deux conditions dans la même instruction conditionnelle:
        # 1. Si la liste A est vide (len(A)==0), ce qui signifie qu'il n'y a rien à comparer.
        # 2. Si le dernier élément de A (A[len(A)-1]) n'est pas égal à la valeur absolue de C[i] (abs(C[i])).
        # abs() retourne la valeur positive de C[i], donc on compare le dernier élément de A à cet entier positif.
        if len(A) == 0 or A[len(A) - 1] != abs(C[i]):
            # S'il n'y a pas d'éléments dans A ou si le dernier élément n'est pas celui attendu, on affiche i+1 pour indiquer l'erreur.
            print(i+1)
            # On termine immédiatement le programme.
            exit(0)
        else:
            # Si la condition ci-dessus n'est pas satisfaite, cela signifie que le dernier élément de A est bien la valeur absolue de C[i].
            # On supprime cet élément à la fin de la liste A.
            # La fonction del supprime un élément à l'indice donné, ici le dernier élément.
            del A[len(A) - 1]

# Si la boucle se termine sans avoir exécuté exit(0), cela signifie que toutes les conditions ont été respectées.
# On affiche alors 'OK' pour signaler que la validation ou le traitement a réussi sans erreur.
print('OK')