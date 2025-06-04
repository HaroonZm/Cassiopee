# Importation de la bibliothèque itertools, qui contient des outils pour travailler avec des itérateurs
from itertools import *

# Demande à l'utilisateur de saisir une valeur (par défaut, input retourne une chaîne de caractères)
n = int(input())  # Convertit la saisie de l'utilisateur en un entier avec int()

# La fonction range(1, n+1) génère une séquence d'entiers de 1 à n inclus (n+1 n'est pas compris)
# permutations(range(1, n+1)) génère tous les arrangements possibles (permutations) des nombres de 1 à n
for i in permutations(range(1, n+1)):
    # map(str, i) convertit chacun des entiers de la permutation en chaînes de caractères
    # " ".join(...) combine ces chaînes en une seule, séparée par des espaces
    print(" ".join(map(str, i)))  # Affiche chaque permutation à l'écran, à une ligne par permutation