import sys  # Importe le module sys, qui fournit des fonctions et des objets liés à l'environnement d'exécution du script Python

# Redéfinit 'input' pour utiliser sys.stdin.readline, une méthode qui lit une ligne de l'entrée standard
# Cela diffère de la fonction intégrée input() car readline() ne supprime pas le caractère de nouvelle ligne (\n)
input = sys.stdin.readline

# Appelle la fonction input(), qui lit une ligne entière saisie par l'utilisateur (ou fournie en entrée standard)
# Utilise la méthode split() pour diviser la chaîne lue en éléments individuels sur la base des espaces
# map(int, ...) convertit chaque élément de la liste obtenue en un entier (int)
# Les valeurs sont affectées respectivement aux variables a, b, c et d
a, b, c, d = map(int, input().split())

# Initialise la variable t à la valeur opposée de l'infini positif
# float("inf") représente l'infini positif en virgule flottante, donc -float("inf") représente l'infini négatif
# Cela signifie que t est initialisé à une valeur extrêmement basse, inférieure à toutes les autres valeurs réelles
t = -float("inf")

# Vérifie deux conditions avec un opérateur logique 'or' (OU)
# Première condition : vérifie si la valeur 0 (zéro) est incluse dans l'intervalle [a, b] (b + 1 car range est exclusif à droite)
# Deuxième condition : vérifie si la valeur 0 est présente dans l'intervalle [c, d]
# Cela se fait en utilisant l'opérateur 'in' qui teste l'appartenance de 0 à l'intervalle construit par range()
if 0 in range(a, b + 1) or (0 in range(c, d + 1)):
    # Si au moins une des deux conditions est vraie, affecte la valeur 0 à t
    # Cela signifie que le nombre 0 est inclus dans au moins un des deux intervalles spécifiés
    t = 0

# Calcule les produits possibles des extrémités des deux intervalles :
# a * c, b * d, a * d, b * c
# Ces produits correspondent à chaque combinaison possible des bornes des deux intervalles
# Ensuite, la fonction max() retourne la valeur maximale parmi ces quatre produits et la valeur t
# Si t a été mis à 0 (c'est-à-dire si 0 était dans un des intervalles), le zéro sera aussi inclus dans la comparaison
# max() garantit que la valeur la plus grande possible est affichée
print(max(a * c, b * d, a * d, b * c, t))