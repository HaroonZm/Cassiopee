from itertools import *        # Permet d'utiliser des fonctions utiles pour manipuler des itérateurs
from bisect import *           # Fonctions pour la gestion de tableaux triés
from math import *             # Accès aux fonctions mathématiques de base
from collections import *      # Fournit des structures de données optimisées (defaultdict, deque, etc.)
from heapq import *            # Fonctions pour travailler avec des files à priorité (tas)
from random import *           # Fonctions pour la génération aléatoire
import sys                     # Accès à des paramètres et fonctions liés au système (stdin, limites, etc.)

# On augmente la limite de récursion pour éviter les problèmes sur des appels récursifs profonds
sys.setrecursionlimit(10 ** 6)

# Lambda/utilitaires pour convertion et affichage rapide
int1 = lambda x: int(x) - 1   # Convertit en entier et décrémente de 1 (pour index 0-based)
p2D = lambda x: print(*x, sep="\n") # Affiche une liste 2D, une ligne par sous-liste

def II():
    """
    Lecture d'un entier depuis l'entrée standard.
    :return: Entier lu sur la ligne courante.
    """
    return int(sys.stdin.readline())

def MI():
    """
    Lit une ligne de plusieurs entiers depuis l'entrée standard.
    :return: Générateur d'entiers (non listé).
    """
    return map(int, sys.stdin.readline().split())

def MI1():
    """
    Lit une ligne de plusieurs entiers, les convertit en indices 0-based.
    :return: Générateur d'entiers (index 0-based).
    """
    return map(int1, sys.stdin.readline().split())

def MF():
    """
    Lit une ligne de plusieurs flottants depuis l'entrée standard.
    :return: Générateur de floats (non listé).
    """
    return map(float, sys.stdin.readline().split())

def LI():
    """
    Lit une ligne de plusieurs entiers sous forme de liste.
    :return: Liste d'entiers.
    """
    return list(map(int, sys.stdin.readline().split()))

def LI1():
    """
    Lit une ligne de plusieurs entiers sous forme de liste (index 0-based).
    :return: Liste d'entiers (index 0-based).
    """
    return list(map(int1, sys.stdin.readline().split()))

def LF():
    """
    Lit une ligne de plusieurs flottants sous forme de liste.
    :return: Liste de floats.
    """
    return list(map(float, sys.stdin.readline().split()))

def LLI(rows_number):
    """
    Lit plusieurs lignes composées de listes d'entiers.
    :param rows_number: Nombre de lignes à lire.
    :return: Liste de listes d'entiers.
    """
    return [LI() for _ in range(rows_number)]

# Déplacements directionnels standards (droite, bas, gauche, haut)
dij = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def main():
    """
    Fonction principale contenant la résolution du problème.
    Lit les paramètres, construit le graphe puis effectue une recherche de plus court chemin
    entre deux sommets en utilisant Dijkstra (file à priorité).
    """
    # Lecture des paramètres principaux : x, y, z, n, m, s, t
    x, y, z, n, m, s, t = MI()
    # Ajustement des indices de départ et d'arrivée en index 0-based pour compatibilité
    s, t = s - 1, t - 1 + n
    
    # itoab contiendra les couples (a, b) pour chaque point
    itoab = []
    # to1[a] : liste des indices ayant le même a -> pour "joindre" par le premier point
    to1 = defaultdict(list)
    # to2[b] : liste des indices ayant le même b -> pour "joindre" par le second point
    to2 = defaultdict(list)
    
    # Gestion des n premiers sommets : lecture des couples (a, b)
    for i in range(n):
        a, b = MI1()         # Lecture avec indices 0-based
        itoab.append([a, b])
        to1[a].append(i)     # Ajoute le sommet à son groupe a
        to2[b].append(i)     # Ajoute le sommet à son groupe b
    
    # Gestion des m seconds sommets : lecture des couples (b, a), a modifié par x
    for i in range(n, n + m):
        b, a = MI1()
        a += x               # Décalage de l'indice a pour ce groupe
        itoab.append([a, b])
        to1[a].append(i)
        to2[b].append(i)
    
    # Tableau pour les distances (-1 = sommet non visité)
    dist = [-1] * (n + m)
    hp = []     # File à priorité min (tas) pour Dijkstra/BFS pondéré
    heappush(hp, [0, s]) # Distance initiale 0 du sommet de départ
    
    # Algorithme de plus court chemin type Dijkstra (poids uniforme entre les "liens")
    while hp:
        d, i = heappop(hp)
        if dist[i] != -1:
            continue            # Si sommet déjà visité on ignore
        dist[i] = d             # Marque la distance au sommet
        
        a, b = itoab[i]         # Récupère les identifiants de ce sommet

        # Pour chaque sommet joignable par a
        for j in to1[a]:
            if j == t:
                print(d + 1)    # Arrivé au but
                exit()
            if j == i or dist[j] != -1:
                continue
            heappush(hp, [d + 1, j])    # Ajoute au tas, +1 distance
        
        # Pour chaque sommet joignable par b
        for j in to2[b]:
            if j == t:
                print(d + 1)    # Arrivé au but
                exit()
            if j == i or dist[j] != -1:
                continue
            heappush(hp, [d + 1, j])
    # Si aucune solution trouvée
    print(-1)

# Lancement du programme principal
main()