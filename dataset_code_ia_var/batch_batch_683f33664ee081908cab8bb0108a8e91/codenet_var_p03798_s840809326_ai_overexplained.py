import sys  # Importe le module sys, qui contient des fonctions relatives au système, notamment l'accès aux flux d'entrée/sortie standard.
from collections import *  # Importe tout du module collections, qui propose des structures de données supplémentaires, telles deque et Counter.
import heapq  # Importe le module heapq, qui permet de manipuler les files de priorité (tas binaires).
import math  # Importe le module math, qui propose des fonctions mathématiques standard comme sqrt, pow, etc.
import bisect  # Importe le module bisect, qui permet d'insérer des éléments de façon ordonnée dans des listes triées.
from itertools import permutations, accumulate, combinations, product
# Importe des fonctions du module itertools :
# - permutations : génère toutes les permutations possibles
# - accumulate : calcule les sommes cumulées
# - combinations : génère toutes les combinaisons possibles sans répétition
# - product : fait le produit cartésien

from fractions import gcd  # Importe la fonction gcd depuis fractions (obsolète en Python 3.5+, préférer math.gcd)

def input():
    # Redéfinit la fonction input pour lire une ligne depuis l'entrée standard (stdin)
    # sys.stdin.readline() lit jusqu'au retour à la ligne inclus, donc on enlève le dernier caractère (saut de ligne)
    return sys.stdin.readline()[:-1]

def ruiseki(lst):
    # Ajoute un zéro au début pour calculer facilement les sommes partielles (cumulative sum)
    # Utilise accumulate pour générer la liste des préfixes : [0, sum(lst[0]), sum(lst[0:1]), ...]
    return [0] + list(accumulate(lst))

mod = pow(10, 9) + 7  # Calcule 10^9 et ajoute 7, valeur souvent utilisée comme modulo dans les problèmes compétitifs.

al = [chr(ord('a') + i) for i in range(26)]
# Crée une liste composée des 26 lettres minuscules de l'alphabet en utilisant :
# - ord('a') pour obtenir le code ASCII de 'a'
# - chr(...) pour reconvertir un code ASCII en caractère
# - i de 0 à 25 (26 lettres)

n = int(input())  # Lit une ligne, la convertit en entier, affecte à n (nombre d'animaux ou d'éléments)
s = input()  # Lit la ligne suivante, affecte à s (chaîne décrivant les observations)

lst = [[0, 0], [0, 1], [1, 0], [1, 1]]
# Initialise une liste de listes, chacune représentant une possibilité initiale :
# - Chaque sous-liste représente deux états initiaux (animal 0 et animal 1), 0 et 1 pouvant signifier respectivement 'S' (Sheep) et 'W' (Wolf)
# - Ainsi les 4 combinaisons de départs possibles sont couvertes

# On va maintenant construire séquentiellement, pour chaque hypothèse de départ,
# la liste des états (0 ou 1) pour les n animaux en fonction des observations

# Parcourt les indices de 0 à n-2 (car i+1 doit aller jusqu'à n-1)
for i in range(n - 1):
    for j in range(4):  # Parcourt les 4 configurations initiales
        # lst[j] est la j-ième configuration, on va y ajouter un nouvel état selon les règles du problème
        if lst[j][-1] == 0 and s[1 + i] == "o":
            # Si l'animal précédent (le dernier ajouté) est un mouton (0) et l'observation est "o"
            # alors "o" signifie : le prochain est du même type que celui d'avant l'actuel
            lst[j].append(lst[j][-2])
        elif lst[j][-1] == 0 and s[1 + i] == "x":
            # Si mouton et observation "x": le prochain est de type différent du précédent
            lst[j].append(1 - lst[j][-2])
        elif lst[j][-1] == 1 and s[1 + i] == "o":
            # Si l'animal précédent est un loup (1) et observation "o": même logique,
            # mais "o" veut dire différent car c'est un loup
            lst[j].append(1 - lst[j][-2])
        else:
            # Si loup et observation "x": même type que celui avant l'actuel
            lst[j].append(lst[j][-2])

# On traite la boucle pour refermer le cycle sur les deux premiers états
for j in range(4):  # Pour chaque configuration possible de départ
    if lst[j][-1] == 0 and s[0] == "o":
        # Si l'animal à la fin de la boucle (dernier) est un mouton,
        # et l'observation du tout premier est "o" : même type que celui d'avant
        lst[j].append(lst[j][-2])
    elif lst[j][-1] == 0 and s[0] == "x":
        # Mouton et observation "x": différent du précédent
        lst[j].append(1 - lst[j][-2])
    elif lst[j][-1] == 1 and s[0] == "o":
        # Loup et observation "o": différent du précédent
        lst[j].append(1 - lst[j][-2])
    else:
        # Loup et observation "x": même que précédent
        lst[j].append(lst[j][-2])
# À ce stade, chaque lst[j] est une liste de longueur n+2,
# qui décrit une hypothèse complète d'agencement des animaux

# On recherche la solution valide, c'est-à-dire où la boucle est fermée correctement :
for i in range(4):  # Pour chaque configuration testée
    if lst[i][-2:] == lst[i][:2]:
        # On vérifie si les deux derniers états correspondent exactement aux deux premiers
        # Ce qui veut dire que le cycle est cohérent (lignes fermées)
        tmp = []  # On prépare la liste de caractères à produire en résultat
        for j in range(n):  # Pour chaque animal dans l'hypothèse
            if lst[i][j] == 0:
                tmp.append("S")  # Si 0, c'est un mouton ("Sheep")
            else:
                tmp.append("W")  # Si 1, c'est un loup ("Wolf")
        print("".join(tmp))  # Concatène et affiche la solution trouvée
        quit()  # Termine immédiatement le programme si solution trouvée

# Si aucune hypothèse n'est valide (pas de solution possible), on affiche -1
print(-1)