# Prendre deux entiers N et M en entrée sur une seule ligne séparés par un espace.
# La fonction input() lit une ligne depuis l'entrée standard (le clavier dans ce cas).
# La fonction split() sépare la ligne en une liste de chaînes de caractères en utilisant l'espace comme séparateur.
# map(int, ...) applique la fonction int à chaque élément de la liste pour les convertir en entiers.
# Enfin, l'affectation multiple N, M = ... permet d'assigner ces deux entiers à N et M respectivement.
N, M = map(int, input().split())

# Calcule une expression mathématique et affiche le résultat avec print().
# Explication détaillée de chaque composant :
#
# (1900 * M)         : Calcule le produit de 1900 par M. Cela représente généralement un coût ou un temps de base répété M fois.
# (N - M)            : Soustrait le nombre M de N, ce qui donne le nombre d'éléments restants après en avoir retiré M.
# 100 * (N - M)      : Multiplie 100 par le résultat précédent. Peut représenter un coût supplémentaire par élément restant.
# 1900 * M + 100 * (N - M): Additionne les deux résultats précédents, représentant le coût total ou temps de base.
# 2 ** M             : Élève 2 à la puissance M. C'est l'opérateur d'exponentiation en Python.
#                     Cela revient à multiplier le résultat précédent par 2, M fois (donc double à chaque fois).
# (1900*M + 100*(N-M)) * 2**M : Multiplie le coût total par 2 puissance M. Cela peut simuler un nombre total de cas, de tentatives ou autre.
# print(...)          : Affiche le résultat final à l’écran.
print((1900 * M + 100 * (N - M)) * 2 ** M)