#!/usr/bin/env python

# Importation du module 'deque' depuis la bibliothèque 'collections'.
# 'deque' signifie "double-ended queue", une structure de données permettant l'ajout et la suppression d'éléments aux deux extrémités.
from collections import deque

# Importation du module 'itertools' sous le nom abrégé 'it'.
# 'itertools' fournit des fonctions qui permettent de manipuler des itérateurs efficacement.
import itertools as it

# Importation du module 'sys', qui donne accès à certaines variables et fonctions qui interagissent fortement avec l’interpréteur Python.
import sys

# Modification de la limite de récursion maximale.
# Cela fixe la profondeur maximale de récursion que l’interpréteur autorisera (utile en cas de récursivité profonde).
sys.setrecursionlimit(1000000)

# Démarrage d'une boucle infinie qui ne sera interrompue que par une condition explicite ('break').
while True:
    # Lecture de l'entrée utilisateur sous forme de chaîne de caractères avec 'raw_input()'.
    # 'raw_input()' lit une ligne depuis l'entrée standard et la retourne sous forme de chaîne.
    S = raw_input()

    # On vérifie ici si l'utilisateur a saisi '0'.
    # Si c’est le cas, cela signifie qu’il souhaite mettre fin au programme, on quitte la boucle.
    if S == '0':
        break

    # Création initiale de la liste m
    # m est une liste qui va contenir des compteurs (ici de longueur 11 pour tous les possibles restes modulo 11)
    # On place une valeur '1' pour le premier élément car à la position de départ (différence nulle), il y a déjà 1 possibilité.
    m = [1] + [0 for i in range(10)]  # [1, 0, 0, 0, ..., 0]

    # Initialisation de la variable 'diff' à 0.
    # 'diff' servira à stocker la somme pondérée des chiffres selon la règle de l’alternance des signes, modulo 11.
    diff = 0

    # Initialisation de la variable 'ans' à 0.
    # 'ans' servira à compter le nombre total de sous-séquences dont la somme alternée de chiffres (modulo 11) tombe sur un certain critère.
    ans = 0

    # Initialisation de la variable 'even' à 1.
    # Cette variable permet d’alterner les signes (+1, -1) lors du calcul alterné sur les chiffres.
    even = 1

    # La chaîne S, lue depuis l'entrée standard, est ici renversée.
    # 'reversed()' crée un itérateur qui parcourt la séquence de caractères S de la fin vers le début.
    S = reversed(S)

    # Boucle sur chaque caractère (chiffre) de la chaîne renversée.
    for c in S:
        # Conversion du caractère 'c' (qui est une chaîne de longueur 1 représentant un chiffre) en entier.
        num = int(c)

        # Calcul de la somme alternée, en alternant le signe, puis en prenant le résultat modulo 11.
        diff = (diff + num * even) % 11

        # Si le chiffre courant n’est pas égal à zéro :
        # Cela évite de compter des séquences qui commencent par zéro, car, pour certains problèmes, des entiers avec des zéros non significatifs sont à éviter.
        if num != 0:
            # Ajout à la réponse du nombre d’occurrences précédentes du reste 'diff'.
            # m[diff] stocke le nombre de fois où la valeur 'diff' a été obtenue précédemment.
            ans += m[diff]

        # Incrémentation du compteur pour le reste 'diff' afin de prendre en compte ce nouvel état atteint.
        m[diff] += 1

        # Inversion du signe de 'even' pour alterner entre +1 et -1 à chaque itération.
        # Cela fait intervenir la règle d’alternance des signes pour la divisibilité par 11.
        even *= -1

    # Affichage du résultat final obtenu pour la chaîne d’entrée S.
    print ans