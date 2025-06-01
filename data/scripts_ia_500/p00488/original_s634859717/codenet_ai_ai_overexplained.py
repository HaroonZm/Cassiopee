# Création d'une liste vide appelée 'l' pour stocker des nombres entiers
l = []

# Boucle for qui s'exécute 3 fois, avec 'i' prenant les valeurs 0, 1, et 2 successivement
for i in range(3):
    # L'instruction input() affiche une invite à l'utilisateur pour qu'il saisisse une valeur
    # int() convertit la chaîne de caractères saisie par l'utilisateur en un nombre entier
    tmp = int(input())
    # La méthode append() ajoute l'élément 'tmp' à la fin de la liste 'l'
    l.append(tmp)

# Création d'une deuxième liste vide appelée 'j' pour stocker d'autres nombres entiers
j = []

# Boucle for qui s'exécute 2 fois, avec 'i' prenant les valeurs 0 et 1 successivement
for i in range(2):
    # Comme précédemment, on demande à l'utilisateur de saisir une valeur, convertie en entier,
    # et on la stocke temporairement dans la variable 'tmp'
    tmp = int(input())
    # On ajoute ce nombre entier à la liste 'j'
    j.append(tmp)

# La fonction min() prend une liste en paramètre et retourne la plus petite valeur contenue dans cette liste
# On calcule la somme du minimum de la liste 'l' et du minimum de la liste 'j'
# Puis on soustrait 50 de cette somme et on stocke le résultat dans la variable 'a'
a = min(l) + min(j) - 50

# Enfin, on affiche la valeur de 'a' dans la console
print(a)