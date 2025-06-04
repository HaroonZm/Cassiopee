import itertools  # Importe le module 'itertools', qui contient des fonctions pour créer et manipuler des itérateurs avancés, ici utilisé pour générer des permutations

# Demander à l'utilisateur d'entrer un nombre entier.
# La fonction input() lit une ligne de l'entrée standard sous forme de chaîne de caractères.
# La fonction int() convertit cette chaîne en un entier.
n = int(input())  # Par exemple, si l'utilisateur entre '3', n prendra la valeur entière 3

# Créer une liste nommée 'L' contenant tous les entiers de 1 à n inclus.
# range(1, n + 1) génère une séquence d'entiers à partir de 1 jusqu'à (n+1) exclus, donc inclusivement 1 à n.
# La compréhension de liste [i for i in ...] parcourt chaque valeur générée et l'ajoute à la liste 'L'.
L = [i for i in range(1, n + 1)]  # Par exemple, si n vaut 3, L vaudra [1, 2, 3]

# Utiliser la fonction 'itertools.permutations()' pour générer tous les arrangements possibles (permutations)
# des éléments de la liste 'L'. Cela retourne un itérateur qui produit des tuples, chaque tuple représentant une permutation.
p = itertools.permutations(L)

# Appliquer la fonction 'sorted()' sur l'itérateur 'p'.
# La fonction sorted() convertit l'itérateur en une liste, puis trie cette liste dans l'ordre lexicographique (ordre croissant par défaut).
# Chaque permutation de L sera donc triée suivant l'ordre naturel.
L2 = sorted(p)

# Utiliser une compréhension de liste pour parcourir L2, où 'i' va de 0 à la taille de L2 moins 1 (donc tous les indices valides de L2).
# Pour chaque valeur de 'i', L2[i] correspond à une permutation (un tuple d'entiers).
# print(*L2[i]) utilise l'opérateur * pour décomposer le tuple en arguments séparés,
# ainsi print imprime chaque élément du tuple séparément, séparé par un espace, sur une ligne.
# Attention : l'utilisation de la compréhension de liste ici ne sert qu'à effectuer les impressions, la liste résultante n'est pas utilisée.
[print(*L2[i]) for i in range(len(L2))]
#  Si par exemple L2 = [(1, 2, 3), (1, 3, 2), ...], cela affichera :
# 1 2 3
# 1 3 2
# etc.