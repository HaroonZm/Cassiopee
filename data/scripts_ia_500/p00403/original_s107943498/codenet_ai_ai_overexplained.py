# Demander à l'utilisateur de saisir un nombre entier et le stocker dans la variable 'n'
# 'input()' lit une chaîne de caractères depuis l'entrée standard (le clavier)
# 'int()' convertit cette chaîne en un entier
n = int(input())

# Demander à l'utilisateur de saisir une ligne contenant plusieurs entiers séparés par des espaces
# 'input().split()' divise la chaîne d'entrée en une liste de sous-chaînes en utilisant l'espace comme séparateur
# La compréhension de liste parcourt chaque sous-chaîne 's' et la convertit en entier avec 'int(s)'
# Le résultat est une liste d'entiers stockée dans la variable 'a'
a = [int(s) for s in input().split()]

# Initialiser une liste vide appelée 'memory' qui servira à stocker temporairement des entiers
# Cette liste fonctionnera comme une pile (structure de données LIFO - Last In First Out)
memory = []

# Initialiser une variable 'flag' avec la valeur False
# Cette variable sert à indiquer si une condition spécifique a été rencontrée pendant le traitement
flag = False

# Démarrer une boucle qui va itérer de 0 à n-1 (c'est-à-dire pour chaque index valide de la liste 'a')
for i in range(n):
    # Vérifier si l'élément courant 'a[i]' est strictement supérieur à zéro
    if a[i] > 0:
        # Si oui, vérifier si cet élément est déjà présent dans la liste 'memory'
        # L'opérateur 'in' teste l'appartenance d'un élément à une liste
        if a[i] in memory:
            # Si l'élément est déjà dans 'memory', afficher la position 1-based (index + 1)
            print(i+1)
            # Modifier la variable 'flag' pour indiquer qu'une condition d'arrêt a été rencontrée
            flag = True
            # Sortir de la boucle immédiatement car la condition est satisfaite
            break
        else:
            # Si l'élément n'était pas dans 'memory', l'ajouter à la fin de la liste
            # 'append()' insère un élément à la fin d'une liste
            memory.append(a[i])
    else:
        # Si l'élément courant 'a[i]' est inférieur ou égal à zéro (ici, exactement inférieur à zéro)
        # Calculer la valeur absolue de cet élément avec 'abs()' pour obtenir sa valeur positive équivalente
        # Vérifier si la liste 'memory' n'est pas vide avec 'len(memory) > 0'
        # Puis vérifier si le dernier élément de 'memory' (avec memory[-1]) est égal à la valeur absolue de 'a[i]'
        if len(memory) > 0 and memory[-1] == abs(a[i]):
            # Si ces conditions sont vraies, supprimer le dernier élément de 'memory'
            # 'pop()' enlève et retourne le dernier élément d'une liste (ici, on ne garde pas la valeur retournée)
            memory.pop()
        else:
            # Si la condition précédente n'était pas vraie, afficher la position 1-based (index + 1)
            print(i+1)
            # Modifier 'flag' pour indiquer que la condition d'arrêt a été rencontrée
            flag = True
            # Sortir immédiatement de la boucle pour arrêter le traitement
            break

# Après la boucle, vérifier si 'flag' est toujours False (c'est-à-dire qu'aucune condition d'arrêt n'a eu lieu)
if flag == False:
    # Si c'est le cas, afficher la chaîne de caractères "OK"
    # Cela signifie que toutes les conditions ont été respectées durant le traitement complet
    print("OK")