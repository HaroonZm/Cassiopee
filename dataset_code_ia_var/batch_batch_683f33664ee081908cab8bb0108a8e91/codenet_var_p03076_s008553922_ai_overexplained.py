# Importation de la fonction 'ceil' depuis le module 'math'.
# 'ceil' (pour "ceiling") permet d'arrondir un nombre à l'entier supérieur le plus proche.
from math import ceil

# Création d'une liste nommée 'a' qui contiendra 5 entiers.
# Pour cela, on utilise une compréhension de liste, un mécanisme qui permet de créer une nouvelle liste à partir d'une expression.
# 'int(input())' : à chaque itération, on appelle 'input()' pour demander à l'utilisateur d'entrer une valeur au clavier (de type chaîne de caractères).
# Ensuite, 'int()' convertit cette chaîne de caractères en entier.
# 'for _ in range(5)' : ceci signifie que cette opération est répétée 5 fois.
# La variable '_' est utilisée quand on n'a pas besoin de la valeur de boucle elle-même.
a = [int(input()) for _ in range(5)]

# Création d'une deuxième liste 'b' à partir de la liste 'a'.
# Chaque élément 'i' de 'a' est utilisé ici.
# 'i / 10' : on divise l'entier 'i' par 10, ce qui donne un nombre flottant.
# 'ceil(i / 10)' : on applique la fonction 'ceil' pour arrondir 'i / 10' à l'entier supérieur le plus proche.
# 'ceil(i / 10) * 10' : on multiplie le résultat par 10 pour obtenir le multiple de 10 immédiatement supérieur (sauf si 'i' est déjà un multiple de 10).
# Ceci sert donc à arrondir chaque valeur de 'a' au multiple de 10 supérieur (ou égal).
# Par exemple, pour i=23, ceil(23/10)=3 donc 3*10=30.
b = [ceil(i / 10) * 10 for i in a]

# Création d'une troisième liste 'c' basée sur les listes précédentes.
# Cette liste va contenir 5 éléments, un pour chaque index 'i' de 0 à 4.
# Pour chaque 'i', on procède comme suit :

# - '[a[i]]' : on commence par créer une liste contenant l'élément de 'a' à l'index 'i'.
# - '[b[j] for j in range(5) if i != j]' : c'est une compréhension de liste qui collecte les éléments 'b[j]' pour chaque index 'j' allant de 0 à 4, à l'exception de 'i' (on exclut 'i' pour éviter la redondance).
# - '[a[i]] + [b[j] for j in range(5) if i != j]' : on combine la liste contenant l'élément 'a[i]' et la liste formée par les autres éléments 'b[j]' où j différent de i, utilisant l'opérateur '+', qui concatène les listes en Python.

# - 'sum([...])' : on fait ensuite la somme de tous les éléments de la liste obtenue à l'étape précédente.
# Cela revient donc, pour chaque index 'i', à ajouter :
#      - l'élément correspondant de 'a' (non arrondi) pour l'index 'i'
#      - les éléments arrondis au multiple de 10 pour tous les autres indexes

# On répète la chose pour les 5 valeurs possibles de 'i', ce qui donne une liste de 5 sommes possibles.
c = [sum([a[i]] + [b[j] for j in range(5) if i != j]) for i in range(5)]

# 'min(c)' : on trouve la valeur minimale parmi les 5 éléments de la liste 'c'.
# Cette valeur est ensuite affichée à l'écran avec 'print'.
print(min(c))