# Importation du module 'sys' qui fournit des fonctions et des objets pour interagir avec l'interpréteur Python
import sys
# Importation du module 'os' qui permet des interactions avec le système d'exploitation, ici il n’est pas utilisé
import os
# Importation du module 'math' qui fournit des fonctions mathématiques, ici il n’est pas utilisé
import math
# Importation du module 'itertools' qui fournit des outils pour créer des itérateurs, ici il n’est pas utilisé
import itertools

# Création d'un dictionnaire vide nommé 'd' qui va servir à compter les occurrences de chaque groupe sanguin
d = {}

# Ajout d’une nouvelle entrée au dictionnaire pour le groupe sanguin 'A' et initialisation du compteur à 0
d['A'] = 0
# Ajout d’une nouvelle entrée au dictionnaire pour le groupe sanguin 'B' et initialisation du compteur à 0
d['B'] = 0
# Ajout d’une nouvelle entrée au dictionnaire pour le groupe sanguin 'AB' et initialisation du compteur à 0
d['AB'] = 0
# Ajout d’une nouvelle entrée au dictionnaire pour le groupe sanguin 'O' et initialisation du compteur à 0
d['O'] = 0

# Début d'une boucle for qui parcourt chaque ligne disponible dans l'entrée standard (par exemple, l'entrée clavier ou un fichier redirigé)
for s in sys.stdin:
    # Suppression des caractères de début et de fin de ligne inutiles comme les espaces ou les sauts de ligne avec la méthode strip()
    s = s.strip()
    # Division de la chaîne de caractères en une liste en utilisant la virgule comme séparateur grâce à split(',')
    # Puis on prend le dernier élément de la liste [-1], ce qui devrait correspondre au groupe sanguin
    type = s.split(',')[-1]
    # On incrémente le compteur correspondant au groupe sanguin extrait dans le dictionnaire 'd'
    d[type] += 1

# Affichage du nombre d'occurrences du groupe sanguin 'A' en consultant la valeur correspondante dans le dictionnaire 'd'
print(d['A'])
# Affichage du nombre d'occurrences du groupe sanguin 'B'
print(d['B'])
# Affichage du nombre d'occurrences du groupe sanguin 'AB'
print(d['AB'])
# Affichage du nombre d'occurrences du groupe sanguin 'O'
print(d['O'])