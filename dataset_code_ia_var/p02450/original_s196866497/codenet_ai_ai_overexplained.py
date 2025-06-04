# Importation de la fonction 'permutations' du module 'itertools'
# 'itertools' est un module standard de Python fournissant des fonctions qui créent des itérateurs pour 
# travailler efficacement avec des boucles, en particulier sur les données itérables (comme les listes ou les tuples).
from itertools import permutations

# Demander à l'utilisateur de saisir un nombre entier
# 'input()' affiche une invite (ici vide), puis lit une ligne depuis l'entrée standard (le clavier)
# Le résultat de 'input()' est une chaîne de caractères, donc on applique 'int()' pour convertir la chaîne en entier
n = int(input())

# Création d'un itérateur sur toutes les permutations possibles des nombres de 1 à n (inclus)
# 'range(1, n+1)' génère une séquence de nombres partant de 1 (inclus) jusqu'à n (inclus, car 'range' s'arrête avant n+1)
# Exemple : si n = 3, range(1, 4) génère [1, 2, 3]
# 'permutations(iterable)' produit toutes les façons de réarranger la séquence fournie
# Chaque permutation est retournée sous forme d'un tuple contenant les éléments réarrangés
b = permutations(range(1, n+1))

# Boucle sur chaque permutation générée par l'itérateur 'b'
# La variable 'ele' va contenir successivement chaque permutation (qui est un tuple d'entiers)
for ele in b:
    # Pour chaque permutation, on doit l'afficher sous forme de chaîne de caractères
    # 'map(str, ele)' applique la fonction 'str' à chaque élément du tuple 'ele',
    # convertissant chaque entier en chaîne de caractères
    # 'join' est une méthode de chaîne de caractères qui réunit les éléments fournis (ici, les chaînes issues de map)
    # en les séparant par un espace (" ")
    # Par exemple, si ele = (1, 2, 3), map(str, ele) produit ["1", "2", "3"],
    # et " ".join(...) donne "1 2 3"
    print(" ".join(map(str, ele)))