# Demande à l'utilisateur d'entrer une valeur, qui correspondra au nombre d'entiers à traiter.
# La fonction input() attend que l'utilisateur saisisse une ligne de texte et appuie sur Entrée.
# Le résultat de input() est de type chaîne de caractères (str), donc on utilise int() pour convertir cette chaîne en un nombre entier.
n = int(input())

# Demande à l'utilisateur d'entrer une liste de nombres séparés par des espaces.
# La méthode input() renvoie, par défaut, une chaîne de caractères contenant tout ce qui a été saisi jusqu'à la touche Entrée.
# split() permet de séparer la chaîne en plusieurs sous-chaînes, en utilisant l'espace comme séparateur par défaut.
# map(int, ...) applique la conversion en entier (int()) à chaque sous-chaîne.
# list(...) convertit l'objet map, qui est un itérable, en une liste d'entiers.
a = list(map(int, input().split()))

# Pour calculer la différence entre la plus grande et la plus petite valeur de la liste,
# on utilise la fonction max() qui donne la valeur maximale de la séquence,
# et la fonction min() qui donne la valeur minimale de la même séquence.
# Ensuite, on soustrait la valeur minimale à la valeur maximale pour obtenir l'écart.
# Enfin, print() affiche le résultat sur la sortie standard (en général, l'écran).
print(max(a) - min(a))