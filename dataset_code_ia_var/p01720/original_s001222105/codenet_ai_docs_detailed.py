import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

# Augmente la limite de récursion pour éviter l'échec sur de grandes profondeurs d'appel récursif.
sys.setrecursionlimit(10 ** 7)

# Constantes utiles
inf = 10 ** 20                 # Valeur représentant l'infini
eps = 1.0 / 10 ** 10           # Petite valeur epsilon pour comparer les flottants
mod = 10 ** 9 + 7              # Modulo typique pour les problèmes de congruence
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Déplacements dans 4 directions
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)] # 8 directions

def LI():
    """
    Lit une ligne depuis l'entrée standard et la convertit en liste d'entiers.
    """
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    """
    Lit une ligne depuis l'entrée standard et retourne une liste d'entiers,
    chacun décrémenté de 1 (pratique pour les indices 0-based).
    """
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    """
    Lit une ligne depuis l'entrée standard et la convertit en liste de flottants.
    """
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    """
    Lit une ligne depuis l'entrée standard et la convertit en liste de chaînes (mots).
    """
    return sys.stdin.readline().split()

def I():
    """
    Lit un entier depuis l'entrée standard.
    """
    return int(sys.stdin.readline())

def F():
    """
    Lit un flottant depuis l'entrée standard.
    """
    return float(sys.stdin.readline())

def S():
    """
    Lit une chaîne (ligne) depuis l'entrée standard.
    """
    return input()

def pf(s):
    """
    Affiche une chaîne avec l'affichage forcé immédiat.
    """
    return print(s, flush=True)

def main():
    """
    Fonction principale du programme. Lit un graphe non orienté, applique la plus courte 
    distance depuis deux sommets de référence 's' et 't', et compte le nombre de chemins 
    particuliers entre ces deux sommets ne passant pas par le plus court chemin direct.
    Retourne ce nombre.
    
    Entrée :
        n m s t            # n : nombre de noeuds, m : nombre d'arêtes
        m lignes : x y     # Les arêtes du graphe (non-orienté)
    
    Retour :
        int : Le nombre de paires (u, v) de sommets telles que le plus court chemin de s à u 
              plus le plus court chemin de v à t soit égal à la longueur du plus court chemin
              de s à t, et que u et v ne soient pas sur le plus court chemin direct entre s et t.
    """
    # Lecture des paramètres du graphe et du nombre d'arêtes
    n, m, s, t = LI()
    # Lecture des arêtes du graphe
    xy = [LI() for _ in range(m)]
    # Initialisation de la liste d'adjacence du graphe
    e = collections.defaultdict(list)
    for x, y in xy:
        # Comme le graphe est non-orienté, on ajoute les deux sens
        e[x].append((y, 1))
        e[y].append((x, 1))

    def search(start):
        """
        Effectue une recherche de plus court chemin depuis 'start' 
        en utilisant Dijkstra (ici équivalent à BFS car poids constant).
        
        Args:
            start (int): sommet de départ
        
        Returns:
            dict: dictionnaire associant à chaque sommet sa distance minimale depuis start
        """
        d = collections.defaultdict(lambda: inf)  # Distance à chaque sommet initialisée à infini
        d[start] = 0                              # Distance au sommet initial est 0
        q = []
        heapq.heappush(q, (0, start))             # File de priorité pour explorer le graphe
        v = collections.defaultdict(bool)         # Marqueur de sommets déjà visités

        while len(q):
            k, u = heapq.heappop(q)               # Récupère le sommet le plus proche
            if v[u]:                              # Ignore s'il a déjà été visité
                continue
            v[u] = True

            for uv, ud in e[u]:
                if v[uv]:                         # Ignore les voisins déjà visités
                    continue
                vd = k + ud                       # Calcule la nouvelle distance potentielle
                if d[uv] > vd:
                    d[uv] = vd
                    heapq.heappush(q, (vd, uv))

        return d

    # Calcule les plus courtes distances de s et de t vers tous les autres sommets
    d1 = search(s)
    d2 = search(t)
    tt = d1[t]  # La longueur du plus court chemin entre s et t

    # Cas particuliers : le plus court chemin est direct (longueur 1 ou 2) 
    if tt == 1:
        return 0
    if tt == 2:
        return 1

    # Comptage des nombres de sommets à chaque distance de s et t
    v1 = collections.defaultdict(int)
    v2 = collections.defaultdict(int)
    for k, v in d1.items():
        v1[v] += 1
    for k, v in d2.items():
        v2[v] += 1

    # Compte le nombre de paires (u,v) telles que leur distance respective à s et t
    # additionnée fait exactement tt-2 (donc ils sont "à mi-chemin" sans être sur 
    # le plus court chemin direct).
    r = 0
    for i in range(tt - 1):
        r += v1[i] * v2[tt - i - 2]

    return r

# Appelle la fonction principale et affiche le résultat
print(main())