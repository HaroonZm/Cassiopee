# Demande à l'utilisateur de saisir un entier via l'entrée standard (clavier)
# La fonction input() lit une ligne de texte sous forme de chaîne de caractères
# La fonction int() convertit cette chaîne en entier
N = int(input())

# Importe la fonction accumulate du module itertools
# itertools est une bibliothèque standard pour manipuler des itérateurs efficaces
from itertools import accumulate

# Demande à l'utilisateur de saisir une ligne de nombres séparés par des espaces
# input() retourne une chaîne, split() coupe la chaîne par défaut sur les espaces et retourne une liste de chaînes
# map(int, ...) applique la fonction int à chaque élément de la liste, c'est-à-dire convertit chaque chaîne en entier
# list(...) convertit l'itérateur en liste d'entiers
A = list(map(int, input().split()))
# Répète le même processus pour B : saisie, découpage, conversion en entier, puis en liste
B = list(map(int, input().split()))

# La méthode reverse() modifie sur place la liste, ici on inverse l'ordre des éléments de la liste B
B.reverse()

# Utilise la fonction accumulate pour calculer la somme cumulée des éléments de la liste A
# accumulate([1, 2, 3]) donne [1, 3, 6] car 1, puis 1+2=3, puis 1+2+3=6
# On convertit l'objet accumulate (qui est un itérateur) en liste pour un accès indexé direct
A = list(accumulate(A))
# Fait de même pour la liste B : somme cumulée après inversion
B = list(accumulate(B))
# Inverse à nouveau B pour retrouver l'ordre original mais avec valeurs cumulées depuis la fin
B.reverse()

# zip(A, B) combine les deux listes A et B élément par élément : [(A[0], B[0]), (A[1], B[1]), ...]
# Pour chaque couple (a, b), on calcule leur somme a+b
# L'expression a+b for a,b in zip(A,B) crée un générateur où chaque élément est la somme des éléments correspondants de A et B
# On utilise la fonction max() pour trouver la valeur maximale parmi toutes ces sommes
m = max(a + b for a, b in zip(A, B))

# Affiche la valeur de m sur la sortie standard
print(m)