#!/usr/bin/env python

# Importation des fonctionnalités du futur pour assurer une compatibilité maximale avec les prochaines versions de Python.
from __future__ import (division, absolute_import, print_function, unicode_literals)

# Importation de la variable 'stdin' du module 'sys' permettant la lecture de l'entrée standard.
from sys import stdin

# Création d'une liste vide 'L' qui sera utilisée pour stocker des tuples d'entiers.
L = []

# Début d'une boucle infinie qui sera explicitement interrompue avec 'break'.
while True:
    # Lecture d'une ligne à partir de l'entrée standard. La fonction 'readline' lit une ligne à la fois.
    line = stdin.readline()
    # Vérification si la ligne commence par '0,0'. Si c'est le cas, on sort de la boucle avec 'break'.
    if line.startswith('0,0'):
        break
    # On coupe la ligne selon la virgule, ce qui donne une liste de chaînes de caractères.
    # Ensuite, à l'aide d'une compréhension de générateur, on convertit chaque élément en entier.
    # Enfin, on transforme le résultat en tuple et on l'ajoute à la liste 'L'.
    L.append(tuple(int(s) for s in line.split(',')))

# Tri de la liste L en place. Le tri se fait selon la valeur 'point' du tuple (id, point).
# La clé de tri est une fonction anonyme (lambda) qui prend comme paramètre un tuple (id, point).
# Le tri se fait dans l'ordre décroissant (du plus grand 'point' au plus petit) grâce à reverse=True.
L.sort(key=lambda x: x[1], reverse=True)

# Pour chaque ligne restante dans l'entrée standard (stdin),
for line in stdin:
    # Conversion de la ligne lue en entier, qui représente un identifiant 'n'.
    n = int(line)
    # Initialisation de la variable 'order' à 0, qui servira à maintenir le classement des points.
    order = 0
    # Initialisation de 'p' (points de référence) à 0, utilisé pour détecter les changements de score.
    p = 0
    # Parcours de chaque tuple (id, point) dans la liste triée 'L'.
    for id, point in L:
        # Si 'point' n'est pas égal à 'p', on a détecté un nouveau score, donc on met à jour 'p' et on incrémente 'order'.
        if p != point:
            p = point
            order += 1
        # Si l'identifiant actuel 'id' correspond à l'identifiant recherché 'n', on quitte la boucle.
        if n == id:
            break
    # Affichage de la variable 'order' qui indique le rang de l'identifiant 'n' en termes de scores.
    print(order)