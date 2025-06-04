# Demande à l'utilisateur d'entrer une valeur, puis convertit l'entrée en entier, et l'affecte à la variable 'a'
a = int(input())  # 'input()' reçoit une chaîne depuis la console ; 'int()' transforme la chaîne en un entier

# Répète la même opération qu'au dessus pour la variable 'b'
b = int(input())

# Encore une fois, demande une saisie à l'utilisateur pour la variable 'c'
c = int(input())

# Calcule une nouvelle valeur 'd'
# Multiplie la variable 'c' par 2, puis soustrait la somme de 'a' et 'b' du résultat
d = 2 * c - (a + b)
# Cela donne à 'd' la valeur 'deux fois c moins a moins b'

# Crée une liste nommée 'm' contenant trois listes internes (une liste de listes, soit une "matrice" 3x3)
# Chaque sous-liste représente une ligne de la matrice
# Les calculs à l'intérieur utilisent les variables précédentes ('a', 'b', 'c', 'd') et des opérations arithmétiques
m = [
    [a, b, c + d],           # Première ligne : premier élément est 'a', deuxième est 'b', troisième est 'c' augmenté de 'd'
    [b + d + d, c, a - d],   # Deuxième ligne : 'b' augmenté de deux fois 'd', puis 'c', puis 'a' diminué de 'd'
    [c - d, a + d, b + d]    # Troisième ligne : 'c' diminué de 'd', 'a' augmenté de 'd', et 'b' augmenté de 'd'
]

# Utilise une boucle 'for' pour parcourir la liste 'm'
# À chaque itération, la variable 'x' reçoit une des sous-listes de 'm'
for x in m:
    # 'print()' affiche des objets (ici l'opérateur * décompresse la liste 'x' en arguments séparés)
    # Ainsi, les éléments de chaque sous-liste sont affichés séparés par des espaces, sur une ligne
    print(*x)  # Le symbole * permet de passer les éléments individuellement à la fonction 'print'