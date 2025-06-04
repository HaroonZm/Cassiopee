# Initialisation d'une liste vide qui va contenir les données des six entrées
a = []

# Boucle for qui s'exécutera 6 fois, avec le caractère de variable '_'
# On utilise '_' par convention pour indiquer que la valeur de l'itérateur n'est pas importante
for _ in range(6):
    # La fonction input() attend que l'utilisateur saisisse une ligne de texte.
    # split() découpe cette ligne en une liste de chaînes de caractères, en séparant selon les espaces (par défaut).
    # map(int, ...) convertit chaque chaîne de caractères obtenue en entier.
    # list(...) transforme l'objet map (qui est un itérable) en une liste d'entiers.
    # sorted(...) trie cette liste d'entiers par ordre croissant et retourne une nouvelle liste triée.
    # append(...) ajoute cette liste triée à la fin de la liste 'a'.
    a.append(sorted(list(map(int, input().split()))))

# Première opération de tri de la liste 'a' :
# sort(key = lambda x: x[1]) trie la liste 'a' selon le deuxième élément (indice 1) de chaque sous-liste.
# Le mot-clé 'key' permet de spécifier une fonction qui sera appelée sur chaque élément pour obtenir la valeur de tri.
# lambda x: x[1] est une fonction anonyme qui retourne le deuxième élément de la liste 'x'.
a.sort(key = lambda x: x[1])

# Deuxième opération de tri :
# sort(key = lambda x: x[0]) trie la liste 'a' selon le premier élément (indice 0) de chaque sous-liste.
# Ainsi, si deux sous-listes avaient le même premier élément, elles restent dans l'ordre défini précédemment par le tri sur le second élément.
a.sort(key = lambda x: x[0])

# La fonction print(...) affiche un texte à l'écran.
# L'opérateur conditionnel ternaire "A if condition else B" retourne A si condition est vraie, sinon retourne B.
# Ici, on vérifie plusieurs conditions logiques à l'aide de l'opérateur 'and' (qui nécessite que toutes les conditions soient vraies).
# Les conditions comparent les triplets de la liste 'a' pour vérifier des égalités :
# a[0] == a[1] vérifie que les deux premiers éléments de 'a' sont identiques (c'est-à-dire que les deux triplets sont égaux).
# a[2] == a[3] vérifie que les troisièmes et quatrièmes triplets sont identiques.
# a[4] == a[5] pareil pour les cinquièmes et sixièmes triplets.
# a[0][0] == a[2][0] vérifie que le premier élément du premier triplet est égal au premier élément du troisième triplet.
# a[0][1] == a[4][0] vérifie que le deuxième élément du premier triplet est égal au premier élément du cinquième triplet.
# a[2][1] == a[4][1] vérifie que le deuxième élément du troisième triplet est égal au deuxième élément du cinquième triplet.
# Si toutes les conditions sont vraies, on affiche 'yes', sinon on affiche 'no'.
print(
    "yes"
    if a[0] == a[1]
    and a[2] == a[3]
    and a[4] == a[5]
    and a[0][0] == a[2][0]
    and a[0][1] == a[4][0]
    and a[2][1] == a[4][1]
    else "no"
)