#!/usr/bin/env python

# Importation de la bibliothèque 'collections' pour 'deque', bien que ce ne soit pas utilisé dans ce script.
from collections import deque

# Importation du module 'itertools' sous le nom court 'it'.
import itertools as it

# Importation du module 'sys' pour manipuler des éléments systèmes comme la limite de récursion.
import sys

# Importation du module 'math', ici principalement pour accéder à des fonctions mathématiques comme 'sqrt' (racine carrée).
import math

# Modification de la limite maximale de récursion du programme.
# Par défaut en Python, cette limite est autour de 1000, mais ici 
# elle est augmentée massivement afin de pouvoir exécuter des appels récursifs très profonds
# sans provoquer d'erreur 'RecursionError'. 
sys.setrecursionlimit(10000000)

# Définition de la fonction récursive 'koch' 
# qui dessine/génère les points d'un segment du flocon de Koch à chaque niveau de récursion. 
def koch(n, sx, sy, gx, gy):
    # n : le niveau de récursion. Si n == 0, cela veut dire que nous sommes à la plus "petite unité".
    # sx, sy : coordonnées x et y du point de départ du segment courant
    # gx, gy : coordonnées x et y du point d'arrivée du segment courant
    
    # Si le niveau de récursion est 0, cela signifie qu'il n'y a plus de subdivision à faire :
    if n == 0:
        # Afficher les coordonnées du point d'arrivée de ce segment particulier.
        # 'print' est utilisé ici sans parenthèses (syntax Python 2).
        print gx, gy
        # Fin de cette exécution de la fonction : on retourne pour sortir de la fonction.
        return

    # Calcul du vecteur entre les deux points (différences x et y)
    vx = gx - sx  # Différence en x entre arrivée et départ
    vy = gy - sy  # Différence en y entre arrivée et départ

    # Calcul du point 1/3 du chemin entre le départ et l'arrivée
    x1 = sx + vx / 3.0  # Position x après avoir parcouru un tiers du segment
    y1 = sy + vy / 3.0  # Position y après avoir parcouru un tiers du segment

    # Calcul du point 2/3 du chemin entre le départ et l'arrivée.
    x3 = gx - vx / 3.0  # Position x juste avant d'arriver à la fin du segment (après avoir parcouru 2/3)
    y3 = gy - vy / 3.0  # Position y juste avant d'arriver à la fin

    # Calcul d'une rotation du vecteur (segment du centre du flocon). 
    # Ici, nous faisons tourner le vecteur d'un angle de +60 degrés par rapport à l'horizontale.
    # Cela correspond à la construction géométrique d'un pic du flocon de Koch.
    vx60 = vx / 2.0 - math.sqrt(3) * vy / 2.0  # Formule de rotation appliquée sur x
    vy60 = math.sqrt(3) * vx / 2.0 + vy / 2.0  # Formule de rotation appliquée sur y

    # Calcul du sommet du triangle équilatéral au-dessus du segment central (le "pic").
    x2 = x1 + vx60 / 3.0  # Position x du sommet du triangle
    y2 = y1 + vy60 / 3.0  # Position y du sommet du triangle

    # Appels récursifs pour subdiviser le segment initialement donné en quatre nouveaux segments plus courts.
    # Chacun de ces appels traitera une des sous-parties du segment original formant la fractale de Koch.
    koch(n - 1, sx, sy, x1, y1)      # Premier segment : de départ à 1/3 du segment
    koch(n - 1, x1, y1, x2, y2)      # Deuxième segment : de 1/3 au sommet du triangle
    koch(n - 1, x2, y2, x3, y3)      # Troisième segment : du sommet à 2/3 du segment
    koch(n - 1, x3, y3, gx, gy)      # Quatrième segment : de 2/3 à la fin du segment

# Lecture de l'entrée utilisateur pour obtenir le niveau de profondeur de la fractale à générer.
# 'input()' lis depuis l'entrée standard (clavier) ; en Python 2, il produit un objet exécuté comme une expression,
# ici il est probablement utilisé avec un entier. S'il s'agit de Python 3, il faudrait écrire 'int(input())'.
n = input()

# Afficher le point de départ, qui est l'origine (0, 0).
# 'print' utilisé ici avec deux arguments, x = 0 et y = 0.
print 0, 0

# Appel de la fonction 'koch' pour générer et afficher les points du flocon de Koch
# depuis (0.0, 0.0) jusqu'au point (100.0, 0.0), sur une ligne horizontale.
koch(n, 0.0, 0.0, 100.0, 0.0)