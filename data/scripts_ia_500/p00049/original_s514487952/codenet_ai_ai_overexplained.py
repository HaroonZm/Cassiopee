import sys  # Importation du module sys qui permet d'interagir avec l'interpréteur Python et d'accéder à des fonctionnalités liées aux entrées/sorties standard, aux arguments de la ligne de commande, etc.
import os  # Importation du module os qui fournit une manière d'utiliser des fonctions dépendantes du système d'exploitation pour interagir avec le système de fichiers, les processus, etc.
import math  # Importation du module math qui offre l'accès à des fonctions mathématiques telles que racine carrée, sinus, cosinus, exponentielle, etc.
import itertools  # Importation du module itertools offrant des outils pour créer des itérateurs efficaces permettant des opérations comme permutations, combinaisons, etc.

# Initialisation d'un dictionnaire nommé 'd'. Un dictionnaire en Python est une collection non ordonnée d'éléments sous forme de paires clé-valeur,
# où chaque clé est unique et permet d'accéder à sa valeur correspondante.
d = {}

# Ajout d'une entrée au dictionnaire avec la clé 'A' et la valeur 0. Cela prépare le dictionnaire à compter le nombre de fois où nous rencontrerons
# un groupe sanguin 'A'.
d['A'] = 0

# Ajout d'une entrée au dictionnaire avec la clé 'B' et la valeur 0, pour compter les occurrences du groupe sanguin 'B'.
d['B'] = 0

# Ajout d'une entrée au dictionnaire avec la clé 'AB' et la valeur 0, pour compter les occurrences du groupe sanguin 'AB'.
d['AB'] = 0

# Ajout d'une entrée au dictionnaire avec la clé 'O' et la valeur 0, pour compter les occurrences du groupe sanguin 'O'.
d['O'] = 0

# Boucle for pour parcourir chaque ligne provenant de l'entrée standard (stdin).
# sys.stdin est un objet qui représente le flux d'entrée standard, qui permet de lire des lignes de texte saisies par l'utilisateur ou
# redirigées depuis un fichier ou une autre source.
for s in sys.stdin:
    # Pour chaque ligne lue, suppression des espaces superflus au début et à la fin de la chaîne de caractères avec strip().
    # Cela permet de nettoyer la ligne pour éviter que des espaces ou des caractères invisibles ne perturbent le traitement.
    s = s.strip()

    # Découpage de la chaîne 's' en sous-chaînes utilisant la virgule ',' comme séparateur grâce à la méthode split(',').
    # split renvoie une liste de sous-chaînes. L'indice -1 permet d'accéder à la dernière sous-chaîne de cette liste.
    # Cette dernière sous-chaîne correspond vraisemblablement au groupe sanguin.
    type = s.split(',')[-1]

    # Incrémentation du compteur dans le dictionnaire 'd' à la clé correspondant au groupe sanguin identifié.
    # Cette opération ajoute 1 à la valeur actuelle, ce qui permet de compter combien de fois chaque groupe sanguin apparaît.
    d[type] += 1

# Après avoir lu et compté tous les groupes sanguins depuis l'entrée standard, on affiche un par un les totaux de chaque groupe sanguin.
# print affiche la valeur correspondante dans le dictionnaire pour la clé donnée.
print(d['A'])  # Affiche le nombre total d'occurrences du groupe sanguin 'A'
print(d['B'])  # Affiche le nombre total d'occurrences du groupe sanguin 'B'
print(d['AB']) # Affiche le nombre total d'occurrences du groupe sanguin 'AB'
print(d['O'])  # Affiche le nombre total d'occurrences du groupe sanguin 'O'