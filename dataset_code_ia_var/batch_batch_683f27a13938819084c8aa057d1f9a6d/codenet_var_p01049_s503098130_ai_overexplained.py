# Première ligne : on lit une entrée utilisateur mais on l'ignore, elle n'est pas stockée dans une variable.
# input() lit une ligne sur la console sous forme de chaîne de caractères, puis ignore cette valeur.

input()  # Lecture d'une entrée (ignorée)

# Deuxième ligne : on lit une entrée contenant deux entiers séparés par un espace.
# input().split() casse la chaîne d'entrée en une liste de sous-chaînes sur les espaces.
# map(int, ...) convertit chaque sous-chaîne en entier.
# a, d = ... affecte simultanément les deux entiers aux variables a et d.
a, d = map(int, input().split())

# Troisième bloc : construction d'une liste x de tuples d'entiers.
# int(input()) lit un entier n qui détermine le nombre de tuples à lire.
# Pour chaque itération, on lit une ligne, on la découpe et on convertit chaque morceau en entier.
# On regroupe les entiers sous forme de tuple. La liste x contiendra tous ces tuples.
x = [tuple(map(int, input().split())) for _ in range(int(input()))]

# Lecture d'un entier k, à partir d'une entrée utilisateur.
# int(input()) convertit l'entrée (une chaîne de caractères) en un entier.
k = int(input())

# La boucle qui suit parcourt la liste x dans l'ordre inverse.
# x[::-1] retourne la liste x en commençant par la fin (reverse slicing).
for i in x[::-1]:
    # Chaque élément i dans x est un tuple, on y accède comme à une séquence à l'aide d'indices.

    # Si le premier champ du tuple (i[0]) vaut 1, on exécute un bloc spécifique.
    if i[0] == 1:
        # L'entrée de type 1 a la forme (1, a, b). Si i[1] (qui représente a) est égal à k...
        if i[1] == k:
            # ...alors on remplace la valeur de k par i[2] (b).
            k = i[2]
    else:
        # Sinon, le tuple est de type 2 et a la forme (2, a, b).
        # On vérifie si k est égal à a (i[1])...
        if i[1] == k:
            # ...si oui, on remplace k par b (i[2]).
            k = i[2]
        # ...sinon, si k est égal à b (i[2])...
        elif i[2] == k:
            # ...on remplace k par a (i[1]).
            k = i[1]

# Enfin, on affiche le résultat de l'expression : a + d * (k - 1)
# Cela représente probablement une progression arithmétique : le k-ième terme avec
# a comme terme initial, d comme différence, et (k-1) comme index décalé à partir du premier terme.
print(a + d * (k - 1))