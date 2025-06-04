import sys  # Importe le module sys, qui fournit un accès à certaines variables et fonctions interactives du système, notamment les flux d'entrée/sortie
import bisect  # Importe le module bisect, utilisé pour l'insertion d'éléments dans des listes triées (non utilisé dans ce code)
import math  # Importe le module math, qui fournit des fonctions mathématiques courantes (non utilisé dans ce code)

# Lis une ligne à partir de l'entrée standard (par exemple, l'utilisateur ou un fichier d'entrée)
# 'sys.stdin.readline()' renvoie une chaîne de caractères représentant une ligne saisie
# La méthode 'split()' sépare cette chaîne en une liste de chaînes, découpée selon les espaces par défaut
# 'map(int, ...)' applique la fonction int à chaque élément de la liste, convertissant ainsi les chaînes en entiers
# On affecte ensuite les deux entiers résultants aux variables 'A' et 'B', respectivement
A, B = map(int, sys.stdin.readline().split())

# Effectue une division entière de A par B à l’aide de l’opérateur '//' (qui renvoie le quotient sans la partie décimale)
res = A // B

# Vérifie deux conditions :
# 1. 'res < 0' : Cela signifie que le résultat de la division entière est négatif
# 2. 'A % B != 0' : L’opérateur '%' calcule le reste de la division de A par B ; si ce reste n'est pas égal à zéro, cela signifie que A n'est pas exactement divisible par B
if res < 0 and A % B != 0:
    # Si les deux conditions ci-dessus sont vraies, il faut ajuster le résultat de la division entière
    # En effet, en Python, la division entière arrondit vers le bas (floor), donc pour les nombres négatifs
    # et quand il y a un reste non nul, il faut incrémenter le résultat de 1 pour correspondre à l’arrondi standard attendu dans certains problèmes
    print(res + 1)  # Affiche le résultat corrigé à l'écran (ou dans le flux de sortie standard)
    exit()  # Termine immédiatement l’exécution du programme

# Si la condition précédente n’est pas remplie, cela signifie soit que la division donne un nombre positif,
# soit que A est divisible par B sans reste, donc il suffit d'afficher 'res' tel quel
print(res)  # Affiche le résultat standard de la division entière