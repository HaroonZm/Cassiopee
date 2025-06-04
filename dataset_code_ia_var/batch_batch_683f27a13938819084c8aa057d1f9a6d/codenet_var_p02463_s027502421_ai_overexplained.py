# Demande à l'utilisateur de saisir une valeur entière via le clavier.
# La fonction input() lit l'entrée de l'utilisateur comme une chaîne de caractères.
# La fonction int() convertit ensuite cette chaîne en un entier.
a = int(input())

# Demande à l'utilisateur une ligne de nombres séparés par des espaces, puis les traite.
# input() lit la ligne de l'utilisateur sous forme de chaîne de caractères.
# split() sépare cette chaîne en une liste de sous-chaînes à chaque espace rencontré.
# map(int, ...) convertit chaque sous-chaîne en un entier, produisant un itérable.
# list(...) transforme cet itérable en une liste d'entiers.
a_li = list(map(int, input().split()))

# Comme précédemment, lit un entier depuis l'entrée standard.
b = int(input())

# Lit une ligne d'entiers séparés par des espaces et les rassemble dans une liste.
b_li = list(map(int, input().split()))

# Concatène les deux listes de nombres entiers a_li et b_li en une seule liste.
# L'opérateur + fusionne les deux listes en une seule liste contenant tous les éléments.
# set(...) convertit cette liste en un ensemble afin d'éliminer les éventuels doublons,
# car un ensemble (set) ne contient que des éléments uniques.
# sorted(...) trie ensuite tous ces éléments uniques dans l'ordre croissant et retourne une nouvelle liste.
answer = sorted(set(a_li + b_li))

# Parcourt chacun des éléments de la liste 'answer'.
# Pour chaque élément 'i' dans 'answer', la fonction print(i) affiche la valeur sur une ligne séparée.
# Cette formule [print(i) for i in answer] utilise l'expression de compréhension de liste (list comprehension),
# qui crée une liste en évaluant print(i) pour chaque élément de 'answer'.
# Cependant, le but ici n'est pas de collecter les valeurs renvoyées par print (qui est toujours None),
# mais juste d'effectuer un affichage pour chaque élément. La variable 'ans' contiendra donc une liste de None.
ans = [print(i) for i in answer]