# Demande à l'utilisateur de saisir des nombres entiers séparés par des espaces.
# La fonction input() récupère la saisie sous forme de chaîne de caractères.
# split() découpe la chaîne en une liste de sous-chaînes séparées par des espaces.
# map(int, ...) convertit chacune de ces sous-chaînes en entier.
# list(...) transforme l'itérable renvoyé par map en une liste Python standard, qui sera stockée dans la variable a.
a = list(map(int, input().split()))

# Demande à l'utilisateur de saisir un nombre entier (la valeur de k).
# input() récupère la saisie sous forme de chaîne de caractères, qui est ensuite convertie en entier avec int().
k = int(input())

# Trie la liste a sur place dans l'ordre croissant.
# Cela signifie que les éléments de la liste seront arrangés du plus petit au plus grand.
a.sort()

# Calcule la valeur suivante :
#   - a[0] : le plus petit élément de la liste (puisqu'elle a été triée),
#   - a[1] : le deuxième plus petit élément de la liste,
#   - a[2] : le troisième plus petit élément de la liste.
#   - pow(2, k) : calcule 2 à la puissance k.
#   - a[2] * pow(2, k) : le troisième élément multiplié par 2 puissance k.
# Additionne a[0], a[1] et le résultat précédent, puis affiche le résultat.
print(a[0] + a[1] + a[2] * pow(2, k))