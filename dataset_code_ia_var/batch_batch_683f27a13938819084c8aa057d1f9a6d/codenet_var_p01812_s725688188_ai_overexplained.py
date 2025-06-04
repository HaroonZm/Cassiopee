import math  # Importe le module math, qui fournit des fonctions et constantes mathématiques de base
import string  # Importe le module string, qui contient des chaînes associées aux caractères ASCII, des fonctions utilitaires de chaîne, etc.
import itertools  # Importe itertools pour des fonctions utilitaires concernant les itérateurs
import fractions  # Importe le module fractions, qui permet de travailler avec des nombres rationnels
import heapq  # Importe heapq, qui offre une bibliothèque de files prioritaires (heaps)
import collections  # Importe les conteneurs spéciaux comme defaultdict, Counter, deque, etc.
import re  # Importe re, le module d'expressions régulières
import array  # Importe array, qui permet d'effectuer des opérations efficaces sur des tableaux homogènes
import bisect  # Importe bisect pour faire de la recherche et insertion binaire sur des listes triées
import sys  # Importe sys pour interagir avec l'interpréteur, accéder à stdin/stdout, etc.
import random  # Importe random pour générer des nombres aléatoires
import time  # Importe time pour accéder à des fonctions de gestion du temps
import copy  # Importe copy pour faire des copies superficielles (shallow) et profondes (deep) d'objets
import functools  # Importe functools, qui offre des outils pour la programmation fonctionnelle

sys.setrecursionlimit(10**7)  # Définit la limite maximale de récursion très haute pour éviter les erreurs des appels profonds
inf = 10**20  # Définit une variable représentant une valeur "infinie" (ici un grand nombre)
eps = 1.0 / 10**10  # Définit une très petite valeur epsilon pour les comparaisons de flottants
mod = 10**9+7  # Définit le modulo utilisé dans de nombreux problèmes d'arithmétique modulaire
dd = [(0,-1),(1,0),(0,1),(-1,0)]  # Liste de couples représentant les 4 directions cardinales : haut, droite, bas, gauche (delta x, delta y)
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]  # Liste de couples représentant les 8 directions possibles sur une grille

# Fonction pour lire une ligne de stdin, couper par espaces, convertir chaque morceau en int, et retourner la liste.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Comme LI(), mais décrémente chaque nombre de 1 (utile pour convertir des indices 1-based en 0-based)
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Idem LI, mais pour les flottants au lieu des entiers
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Lit une ligne, la découpe en mots (chaînes), et retourne la liste des chaînes.
def LS():
    return sys.stdin.readline().split()

# Lit une ligne et la convertit en int (renvoie un seul entier)
def I():
    return int(sys.stdin.readline())

# Lit une ligne, la convertit en float (renvoie un seul flottant)
def F():
    return float(sys.stdin.readline())

# Lit une ligne de l'entrée standard comme chaîne brute (utilise input)
def S():
    return input()

# Fonction pout afficher s et forcer le flush
def pf(s):
    return print(s, flush=True)

def main():
    # Lit des entiers n, m, k depuis l'entrée : 
    # n = nombre d'objets principaux
    # m = nombre d'éléments dans la liste d
    # k = nombre de transformations/relations
    n, m, k = LI()
    
    # Lit la liste d, convertie en indices 0-based (soustraction de 1)
    d = LI_()
    
    # Pour chaque objet principal (il y a n objets), on lit une ligne,
    # chaque ligne étant une liste de k entiers convertis en 0-based.
    # Ainsi, v[i][j] indique (après ajustement d'indice) la destination 
    # de l'objet i sous la transformation/colonne j.
    v = [LI_() for _ in range(n)]
    
    # On crée un defaultdict qui renvoie None pour tout élément absent.
    # dd servira à mapper chaque valeur de d (chaîne ou index) vers sa position dans d.
    dd = collections.defaultdict(lambda: None)
    
    # Pour chaque élément de la liste d de longueur m, on enregistre dans dd
    # la position d'apparition (index i).
    for i in range(m):
        dd[d[i]] = i
    
    # On veut créer une table vv de dimension m x k:
    # Pour chaque colonne c de d, on stocke la position (dans d)
    # de l'élément obtenu en appliquant la j-ième transformation sur l'élément c.
    # Si la transformation mène en dehors de d, on stocke None.
    vv = []
    for c in d:
        # Pour chaque transformation/colonne i dans v[c], 
        # on trouve l'index dans d du résultat de la transformation (via dd).
        vv.append([dd[v[c][i]] for i in range(k)])
    
    # On construit la liste vvv de dimension k x m. 
    # C'est la transposée de vv : chaque vvv[j] est une liste contenant, pour chaque 
    # élément parmi ceux de d, la cible de la j-ième transformation (ou None).
    vvv = [[vv[i][j] for i in range(m)] for j in range(k)]
    
    # On utilise un ensemble u pour mémoriser les états déjà rencontrés.
    # Un état est représenté comme un entier, dont les bits indiquent
    # la présence (1) ou l’absence (0) des éléments d dans l’état courant.
    u = set()
    
    # m2 correspond à 2 à la puissance m, soit le nombre d'états possibles
    # qu'on peut représenter (étant donné que chaque élément de d est présent/absent)
    m2 = 2 ** m
    
    # On ajoute l'état initial: tous les éléments de d présents (chaque bit à 1)
    u.add(m2 - 1)
    
    # On utilise une file FIFO (queue) pour la recherche en largeur (BFS):
    # chaque élément est un couple (état représenté par un entier, nombre d'étapes)
    q = [(m2 - 1, 1)]
    
    # ii est la liste des puissances de 2 : ii[j] est 1 << j, permettant de manipuler les bits d'états.
    ii = [2 ** _ for _ in range(m)]
    
    # Boucle principale du BFS
    while q:
        # On enlève le premier élément de la file (état courant + profondeur)
        qd, qk = q.pop(0)
        
        # qdi est la liste des indices de bits qui sont à 1 dans qd,
        # c'est-à-dire des éléments de d présents dans l’état courant.
        qdi = [di for di in range(m) if qd & ii[di]]
        
        # On essaie chaque transformation (vi de 0 à k-1)
        for vi in range(k):
            t = 0  # Nouveau masque d'état après transformation vi
            vvi = vvv[vi]  # Cette colonne de vvv indique pour chaque index son image via vi
            for di in qdi:
                # Pour chaque élément présent di, on regarde s'il a une image via la transformation.
                if not vvi[di] is None:
                    # Si oui, on active dans t le bit pointant sur l'image
                    t |= ii[vvi[di]]
            # Si cet état a déjà été vu, on ne fait rien
            if t in u:
                continue
            # Si aucun bit n'est actif, c'est-à-dire qu’on a atteint un état vide,
            # on retourne le nombre d’étapes nécessaires:
            if t == 0:
                return qk
            # On marque l'état comme déjà vu
            u.add(t)
            # On l'ajoute à la file avec une étape supplémentaire
            q.append((t, qk+1))
    # Si on termine sans avoir atteint l'état 0 (aucun élément de d restant), le but est impossible
    return -1

# Appel de la fonction principale et affichage de son résultat
print(main())