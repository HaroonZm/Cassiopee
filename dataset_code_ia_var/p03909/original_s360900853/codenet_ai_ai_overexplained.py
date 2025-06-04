# Début de la section "header" : Cette région contient les importations de modules et les définitions de fonctions utilitaires fréquemment utilisées dans divers problèmes Python.

# Importation du module 'sys', qui fournit l'accès à certaines variables et fonctions propres à l'interpréteur Python, notamment pour la lecture de l'entrée standard.
import sys

# Importation du module 'math', qui inclut des fonctions mathématiques usuelles comme sqrt, sin, cos, etc.
import math

# Importation des fonctions bisect_left, bisect_right, insort_left, insort_right du module 'bisect', utiles pour travailler avec des listes triées (insertion, recherche de positions d'insertion, etc.).
from bisect import bisect_left, bisect_right, insort_left, insort_right

# Importation de classes et fonctions de 'collections' :
# - defaultdict pour des dictionnaires avec valeur par défaut,
# - deque pour des files/déques performantes,
# - Counter pour compter les objets hashables.
from collections import defaultdict, deque, Counter

# Importation de deepcopy du module 'copy', pour effectuer des copies profondes d'objets imbriqués.
from copy import deepcopy

# Importation de la fonction gcd (plus grand commun diviseur) du module 'fractions'. (À noter : depuis Python 3.5, math.gcd est recommandé).
from fractions import gcd

# Importation de lru_cache (cache avec taille limitée pour les fonctions) et reduce (appliquer une fonction cumulativement) depuis functools.
from functools import lru_cache, reduce

# Importation des fonctions pour le tas/min-heap (heappop, heappush) depuis heapq.
from heapq import heappop, heappush

# Importation de fonctions utiles du module itertools :
# - accumulate : somme cumulée,
# - groupby : regroupement après tri,
# - product : produit cartésien,
# - permutations : toutes les permutations possibles,
# - combinations : toutes les combinaisons possibles,
# - combinations_with_replacement : combinaisons autorisant la répétition.
from itertools import accumulate, groupby, product, permutations, combinations, combinations_with_replacement

# Importation de fonctions mathématiques spécifiques du module math.
# - ceil : entier le plus proche supérieur,
# - floor : entier le plus proche inférieur,
# - factorial : factorielle,
# - log : logarithme en base e,
# - sqrt : racine carrée,
# - sin, cos : sinus et cosinus.
from math import ceil, floor, factorial, log, sqrt, sin, cos

# Importation de la fonction itemgetter du module operator, pour récupérer des éléments par indice dans des éléments indexables.
from operator import itemgetter

# Importation de constantes string pour les lettres minuscules et majuscules de l'alphabet anglais, ainsi que les chiffres décimaux.
from string import ascii_lowercase, ascii_uppercase, digits

# Augmentation de la limite de récursion dans Python à 1 000 000, ce qui peut s'avérer nécessaire lors de l'utilisation de la récursivité profonde.
sys.setrecursionlimit(10 ** 6)

# Définition d'une constante représentant "l'infini" réel (utilisé pour initialiser des minima ou des maxima).
INF = float('inf')

# Définition du modulo fréquemment utilisé dans les problèmes d'arithmétique modulaire (souvent rencontré lors de compétitions).
MOD = 10 ** 9 + 7

# Définition de fonctions utilitaires pour la lecture de l'entrée, typiquement depuis sys.stdin (fréquent pour du code de compétition).

# Fonction 'rs' : lit une ligne de l'entrée standard (sys.stdin), supprime le saut de ligne à droite puis retourne la chaîne résultante.
def rs():
    return sys.stdin.readline().rstrip()

# Fonction 'ri' : lit une ligne, supprime le saut de ligne, puis convertit la chaîne en entier.
def ri():
    return int(rs())

# Fonction 'rf' : lit une ligne, supprime le saut de ligne, puis convertit la chaîne en nombre flottant.
def rf():
    return float(rs())

# Fonction 'rs_' : lit une ligne, supprime le saut de ligne, puis sépare la chaîne par les espaces ; retourne une liste de chaînes.
def rs_():
    return [_ for _ in rs().split()]

# Fonction 'ri_' : lit une ligne, supprime le saut de ligne, sépare la chaîne par espaces, puis convertit chaque élément en entier ; retourne une liste d'entiers.
def ri_():
    return [int(_) for _ in rs().split()]

# Fonction 'rf_' : lit une ligne, supprime le saut de ligne, sépare la chaîne par espaces, puis convertit chaque élément en float ; retourne une liste de flottants.
def rf_():
    return [float(_) for _ in rs().split()]

# Fonction 'divisors' : retourne tous les diviseurs d'un entier n.
# - On parcourt i de 1 à racine de n (inclue). 
#   Si i est un diviseur (n % i == 0), on ajoute i à la liste.
#   Si le quotient n // i est différent de i, on l'ajoute également (pour éviter de doubler la racine si n est carré parfait).
# - Si 'sortedresult' est True, on trie la liste des diviseurs avant de la retourner.
def divisors(n, sortedresult=True):
    div = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:  # Si i est diviseur de n
            div.append(i)  # On ajoute i à la liste
            if i != n // i:  # Pour éviter les doublons quand n est un carré parfait
                div.append(n // i)  # On ajoute n // i aussi.
    if sortedresult:
        div.sort()  # On trie la liste si besoin.
    return div  # On retourne la liste des diviseurs

# Fin de la section "header".

# Lecture de deux entiers sur une seule ligne, qui représentent la hauteur (H) et la largeur (W) d'une grille.
H, W = ri_()
# À ce stade, H contient le nombre de lignes de la grille, W le nombre de colonnes.

# Lecture du contenu de la grille S :
# Pour chaque ligne de la grille (il y en a H), on lit une ligne de l'entrée, qu'on découpe par espaces.
# Cela donne une liste de listes : S[i][j] est l'élément de la i-ème ligne et la j-ème colonne.
S = [rs_() for _ in range(H)]

# Parcours de toutes les cases de la grille par deux boucles imbriquées.
for i in range(H):  # Pour chaque ligne, indice i variant de 0 à H-1
    for j in range(W):  # Pour chaque colonne, indice j variant de 0 à W-1
        # Si le contenu de la case S[i][j] est égal à la chaîne de caractères 'snuke'
        if S[i][j] == 'snuke':
            # On veut afficher la position en format demandé :
            # La lettre correspondant à la colonne (A pour 0, B pour 1, etc.) 
            # suivi du numéro de la ligne (on ajoute 1 car les lignes sont numérotées à partir de 1)
            # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[j] renvoie le j-ème caractère du string.
            print('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[j] + str(i + 1))
            # On n'arrête pas explicitement la recherche (par exemple via break), mais selon l'énoncé on suppose qu'il n'y a qu'une occurrence.