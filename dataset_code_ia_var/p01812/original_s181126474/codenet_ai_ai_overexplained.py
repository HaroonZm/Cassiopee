import math  # Module mathématique standard de Python pour les opérations mathématiques
import string  # Module pour manipuler des chaînes de caractères (alphabets, etc.)
import itertools  # Fournit des outils pour manipuler des itérateurs (produit cartésien, permutations, etc.)
import fractions  # Fournit la classe Fraction pour gérer les fractions
import heapq  # Implémente une heap basée sur une liste, utile pour les files à priorité
import collections  # Fournit des structures de données spécialisées comme defaultdict
import re  # Module d'expressions régulières
import array  # Fournit un type de séquence efficace pour des données numériques homogènes
import bisect  # Pour faire des recherches binaires et insertion dans des listes triées
import sys  # Offre l'accès à des fonctions et objets liés à l'interpréteur Python
import random  # Génère des nombres pseudo-aléatoires
import time  # Permet de mesurer le temps et de faire des pauses
import copy  # Permet la copie superficielle et profonde des objets
import functools  # Fournit des outils pour la programmation fonctionnelle

# On élève la limite de récursion pour des appels récursifs importants afin d'éviter une erreur de récursion
sys.setrecursionlimit(10**7)

# Définition d'une constante pour une valeur "infini" qui sera utilisée pour les comparaisons
inf = 10**20

# Définition d'une très petite valeur epsilon, utile pour comparer des nombres flottants avec précision
eps = 1.0 / 10**10

# Définition d'un modulo, souvent utilisé en arithmétique modulaire dans les problèmes d'algorithmique
mod = 10**9+7

# Vecteurs de direction pour les déplacements dans une grille (haut, droite, bas, gauche)
dd = [(0,-1),(1,0),(0,1),(-1,0)]

# Vecteurs de direction pour les 8 directions autour d'un point (diagonales incluses)
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

# Fonction pour lire une ligne de l'entrée standard (stdin), la diviser en entiers, et les retourner sous forme de liste
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Comme la fonction LI mais soustrait 1 à chaque entier, souvent pour passer d'un indexage 1-based à 0-based
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Lecture d'une ligne et conversion en liste de flottants
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Lecture d'une ligne et découpage en mots (strings)
def LS():
    return sys.stdin.readline().split()

# Lecture d'un entier unique de l'entrée standard
def I():
    return int(sys.stdin.readline())

# Lecture d'un nombre flottant unique depuis l'entrée standard
def F():
    return float(sys.stdin.readline())

# Récupère une ligne de l'entrée standard, équivalent à input()
def S():
    return input()

# Fonction d'affichage, avec flush explicite ; utile pour le débogage interactif
def pf(s):
    return print(s, flush=True)

# Fonction principale du programme
def main():
    # Lecture des valeurs n, m, k à partir de l'entrée standard
    n, m, k = LI()  # n : nombre de lignes, m : nombre d'éléments principaux, k : nombre de motifs (?)
    d = LI_()  # Lit une liste de m entiers, dont chacun est décrémenté de 1 (pour indexation 0)
    # Lecture d'une matrice v de taille n x m, où chaque ligne est une liste d'entiers décrémentés de 1
    v = [LI_() for _ in range(n)]
    # Création d'un dictionnaire avec valeur par défaut None pour tout nouvel élément
    dd = collections.defaultdict(lambda: None)
    for i in range(m):
        dd[d[i]] = i  # Associe chaque valeur d[i] à son index i (mapping)
    # Crée une liste de puissances de 2 pour chaque index de 0 à m-1
    ii = [2**_ for _ in range(m)]
    # Construction d'une structure vv, liste de listes :
    # Pour chacune des k lignes
    #   Pour chaque valeur c dans d (pas utilisée ici : bug ?), on effectue :
    #     Si dd[v[c][i]] n'est pas None, on met la puissance de deux correspondante ; sinon 0
    vv = [
        [
            ii[dd[v[c][i]]] if not dd[v[c][i]] is None else 0
            for c in d
        ]
        for i in range(k)
    ]
    # Nombre total d'états possible : 2^m, utile pour le bitmasking
    m2 = 2**m
    # Tableau u pour marquer quels états ont déjà été visités ; initialisé à None
    u = [None] * m2
    # L'état final, qui a tous les bits à 1 (toutes les options sélectionnées), est marqué comme atteint
    u[-1] = 1
    # La queue q contient l'état de départ : tous les bits à 1 (état final)
    q = [m2-1]
    # r compte le nombre d'étapes (niveau BFS)
    r = 0
    # Boucle principale du parcours BFS (par niveau sur les états)
    while q:
        r += 1  # On augmente le compteur de niveaux à chaque itération
        nq = []  # Liste pour stocker les états du prochain niveau
        for qd in q:  # Pour chaque état dans la file actuelle
            # On extrait la liste des indices dont le bit est à 1 dans qd
            qdi = [di for di in range(m) if qd & ii[di]]
            for vi in range(k):  # Pour chaque motif (ligne de vv)
                t = 0  # Initialisation d'un nouvel état à zéro (aucune option sélectionnée)
                vvi = vv[vi]  # Récupère le motif courant (sous forme de bitmask pour chaque composant)
                for di in qdi:  # Pour chaque index actif
                    t |= vvi[di]  # Ajoute les options du motif correspondant (opération OU binaire)
                if not u[t] is None:  # Si cet état a déjà été vu, on continue
                    continue
                if t == 0:  # Si l'état est vide (aucun bit sélectionné), on retourne r
                    return r
                u[t] = 1  # On marque l'état comme visité
                nq.append(t)  # On l'ajoute aux états du prochain niveau
        q = nq  # On passe au niveau suivant du BFS
    # Si on n'a jamais atteint l'état vide t == 0, la situation est impossible
    return -1

# Appel de la fonction principale et affichage de son résultat
print(main())