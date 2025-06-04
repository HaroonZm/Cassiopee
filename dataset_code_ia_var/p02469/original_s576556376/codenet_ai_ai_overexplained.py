import sys                               # Importe le module sys qui donne accès à certaines variables et fonctions du système d'exploitation.
import collections as cl                 # Importe le module collections, utilisé pour des structures de données optimisées, et lui donne l'alias 'cl'.
import bisect as bs                      # Importe le module bisect, utilisé pour la recherche et l'insertion dans des listes triées, et lui donne l'alias 'bs'.

sys.setrecursionlimit(100000)            # Change la limite de récursion maximale autorisée par l'interpréteur Python à 100000 pour éviter les erreurs de débordement de pile lors d'appels récursifs profonds.
Max = sys.maxsize                        # Assigne à la variable Max la plus grande valeur d'entier possible supportée par l’implémentation actuelle de Python.

def l():
    # Fonction qui lit une ligne d'entrée standard (input), sépare cette ligne selon les espaces (split),
    # convertit chaque élément de cette liste séparée en entier (int), puis construit une liste (list) contenant ces entiers.
    # Cette fonction ne prend aucun paramètre et retourne une liste d'entiers.
    return list(map(int, input().split()))

def m():
    # Fonction qui lit une ligne de l'entrée standard, la découpe selon les espaces, convertit chaque fragment en entier,
    # et les retourne sous forme d'un itérable 'map'. Utilisée si on veut simplement itérer sur ces entiers sans en créer une liste explicite.
    return map(int, input().split())

def onem():
    # Fonction qui lit une ligne de l'entrée standard et la convertit en entier.
    # Pratique pour lire un seul nombre, par exemple la taille de la liste à lire ensuite.
    return int(input())

def s(x):
    # Fonction prenant une liste x et effectuant une forme de compression dite de run-length encoding.
    # Cependant, le comportement exact ici est potentiellement inattendu, voir explications ci-dessous.
    # Crée une nouvelle liste 'a' pour stocker les résultats.
    # 'aa' est initialisé au premier élément de x.
    # 'su' commence à 1 et compte le nombre d'éléments consécutifs égaux.
    # Pour chaque élément de x (sauf le dernier), si aa == x[i+1] (ie éléments consécutifs identiques),
    # alors il ajoute [aa, su] à 'a', réinitialise 'aa' et 'su'.
    # Cela ressemble à un décompte du nombre d'occurrences consécutives,
    # mais la logique semble inversée : normalement on incrémente su dans le cas d'égalité, ici c'est l'inverse.
    # Enfin, ajoute le dernier groupe à 'a'.
    a = []
    aa = x[0]      # Stocke le premier élément de la liste x comme valeur de comparaison.
    su = 1         # Initialise le compteur de répétitions à 1 pour le premier élément déjà pris en compte.
    for i in range(len(x) - 1):    # Parcourt la liste x jusqu'à l'avant-dernier élément.
        if aa == x[i + 1]:         # Si la valeur courante est la même que la suivante :
            a.append([aa, su])     # Ajoute le couple [valeur courante, compteur actuel] à la liste 'a'.
            aa = x[i + 1]          # Met à jour la valeur de comparaison à la valeur suivante.
            su = 1                 # Réinitialise le compteur de répétitions à 1.
        else:
            su += 1                # Si les valeurs sont différentes, incrémente le compteur.
    a.append([aa, su])             # Ajoute le dernier groupe traité à la liste 'a'.
    return a                       # Retourne la liste compressée.

def jo(x):
    # Fonction transformant une liste x en chaîne de caractères où chaque élément est séparé par un espace.
    # map(str, x) convertit chaque élément en chaîne ; " ".join(...) les assemble avec des espaces.
    return " ".join(map(str, x))

def max2(x):
    # Fonction qui détermine le plus grand élément dans une liste de listes x.
    # Utilise map(max, x) : pour chaque sous-liste de x, trouve son maximum, puis retourne le maximum entre tous ces maximums.
    return max(map(max, x))

import fractions                      # Importe le module fractions, principalement utilisé dans ce script pour accéder à la fonction gcd (pgcd).
from functools import reduce          # Importe la fonction reduce du module functools, qui applique cumulativement une fonction à une séquence.

def gcd(*numbers):
    # Fonction qui calcule le PGCD (Plus Grand Commun Diviseur) de plusieurs entiers.
    # *numbers permet de passer un nombre variable d'arguments.
    # Utilise reduce et fractions.gcd pour appliquer gcd à tous les éléments.
    # Par exemple, gcd(a, b, c) effectuera gcd(gcd(a, b), c).
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    # Fonction similaire à la précédente, mais prend une séquence (liste, tuple, etc.) d’entiers en entrée.
    # Applique également fractions.gcd de façon répétée à tous les éléments de la séquence pour en extraire le PGCD commun.
    return reduce(fractions.gcd, numbers)

def lcm_base(x, y):
    # Fonction qui calcule le PPCM (Plus Petit Commun Multiple) de deux entiers x et y.
    # Formule: (x * y) // gcd(x, y)
    # Utilise fractions.gcd pour trouver le PGCD, puis calcule le PPCM comme le produit divisé par le PGCD.
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    # Fonction qui calcule le PPCM de plusieurs entiers (nombre variable d'arguments).
    # Utilise la fonction lcm_base dans reduce pour appliquer la formule du PPCM deux par deux
    # à tous les arguments passés jusqu'à trouver le PPCM de l'ensemble.
    # Initialisation à 1 pour que le produit soit neutre.
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    # Fonction qui calcule le PPCM d'une séquence d'entiers (contenue dans 'numbers').
    # Applique lcm_base deux à deux sur tous les éléments grâce à reduce, à partir de la valeur initiale 1.
    return reduce(lcm_base, numbers, 1)

n = onem()            # Lit un entier (par exemple, la taille de la liste à traiter) à partir de l'entrée standard, le stocke dans la variable n.

l = l()               # Lit une ligne d'entiers, séparés par des espaces, et les stocke dans la variable l sous forme de liste d'entiers.

print(lcm_list(l))    # Calcule le PPCM de tous les éléments de la liste l, puis affiche ce résultat à la sortie standard.