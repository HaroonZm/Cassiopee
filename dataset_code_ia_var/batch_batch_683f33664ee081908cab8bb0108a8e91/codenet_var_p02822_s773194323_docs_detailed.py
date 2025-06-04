from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from operator import mul

# Augmenter la limite de récursion maximale, utile pour les grands arbres
sys.setrecursionlimit(2147483647)
# Utilisé pour l'infini
INF = 10 ** 20
# Constante pour le modulo
mod = 1000000007

def LI():
    """
    Lit une ligne de l'entrée standard et retourne une liste d'entiers.
    """
    return list(map(int, sys.stdin.readline().split()))

def I():
    """
    Lit une ligne de l'entrée standard et retourne un entier.
    """
    return int(sys.stdin.readline())

def LS():
    """
    Lit une ligne de l'entrée standard (bufferisée) et retourne une liste de chaînes (mots séparés).
    """
    return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()

def S():
    """
    Lit une ligne de l'entrée standard (bufferisée) et retourne une chaîne décodée en UTF-8.
    """
    return sys.stdin.buffer.readline().rstrip().decode('utf-8')

def IR(n):
    """
    Lit n entiers (un entier par ligne).
    Args:
        n (int): Nombre de lignes à lire.
    Returns:
        list[int]: Liste d'entiers lus.
    """
    return [I() for i in range(n)]

def LIR(n):
    """
    Lit n listes d'entiers (une liste par ligne).
    Args:
        n (int): Nombre de listes à lire.
    Returns:
        list[list[int]]: Liste de listes d'entiers.
    """
    return [LI() for i in range(n)]

def SR(n):
    """
    Lit n chaînes de caractères (une par ligne).
    Args:
        n (int): Nombre de lignes à lire.
    Returns:
        list[str]: Liste de chaînes lues.
    """
    return [S() for i in range(n)]

def LSR(n):
    """
    Lit n listes de mots (une liste par ligne, mots séparés par des espaces).
    Args:
        n (int): Nombre de lignes à lire.
    Returns:
        list[list[str]]: Liste de listes de mots.
    """
    return [LS() for i in range(n)]

def SRL(n):
    """
    Lit n chaînes, et les convertit en listes de caractères.
    Args:
        n (int): Nombre de lignes à lire.
    Returns:
        list[list[str]]: Liste de listes de caractères.
    """
    return [list(S()) for i in range(n)]

def MSRL(n):
    """
    Lit n chaînes et convertit chaque caractère en un entier.
    Args:
        n (int): Nombre de lignes à lire.
    Returns:
        list[list[int]]: Liste de listes d'entiers.
    """
    return [[int(j) for j in list(S())] for i in range(n)]

# Lecture du nombre de sommets
n = I()
# Initialisation de la structure du graphe G comme une liste d'adjacence vide
G = [[] for _ in range(n)]
# Lecture des arêtes du graphe et construction de la liste d'adjacence
for _ in range(n - 1):
    a, b = LI()
    G[a - 1].append(b - 1)  # On convertit à un indice basé sur 0
    G[b - 1].append(a - 1)  # Même chose pour l'autre extrémité

# Initialisation des tableaux pour les parents et les tailles de sous-arbres
par = [-1] * n   # par[u]: parent de u dans l'arbre
cnt = [0] * n    # cnt[u]: nombre de sommets dans le sous-arbre enraciné à u

def f(u):
    """
    Calcule la taille du sous-arbre enraciné à u en utilisant un DFS récursif.
    Args:
        u (int): Le sommet courant.
    Returns:
        int: La taille du sous-arbre enraciné à u.
    Side effect:
        Remplit les tableaux par (parent) et cnt (taille du sous-arbre) pour tous les sommets.
    """
    ret = 1  # Compte le sommet courant
    for v in G[u]:
        if v == par[u]:  # Ne pas revenir vers le parent
            continue
        par[v] = u
        ret += f(v)  # Ajoute la taille du sous-arbre du fils v
    cnt[u] = ret  # Enregistre la taille du sous-arbre enraciné à u
    return ret

# Détermine le parent de chaque sommet et la taille des sous-arbres pour tous les sommets, à partir de la racine 0
f(0)

# Précalcule les puissances de 2 modulo 'mod' jusqu'à n inclus
pow2 = [1] * (n + 1)
for i in range(1, n + 1):
    pow2[i] = pow2[i - 1] * 2 % mod

# Parcours BFS ou DFS itératif pour calculer la réponse finale
q = deque([0])  # Commence à la racine
ans = 0         # Accumulateur de la réponse finale

while q:
    u = q.pop()
    # Initialiser ret au nombre de sous-ensembles non-vides sur les n-1 autres sommets
    ret = pow2[n - 1] - 1

    for v in G[u]:
        if v == par[u]:  # Ne pas retourner vers le parent
            continue
        # On exclut les sous-ensembles contenus dans le sous-arbre de v
        ret -= pow2[cnt[v]] - 1
        q.append(v)  # Ajoute v à la queue pour visite ultérieure

    # On exclut les sous-ensembles contenus dans la composante extérieure au sous-arbre de u
    ret -= pow2[n - cnt[u]] - 1

    # Accumule le résultat en prenant soin du modulo
    ans = (ans + ret) % mod

# On corrige la réponse en la divisant par le nombre total de sous-ensembles (hors vide)
# Cela correspond à une multiplication par l'inverse modulaire de pow2[n] (nombre total de sous-ensembles)
# La formule pow(pow2[n], mod - 2, mod) donne l'inverse modulaire de pow2[n] modulo mod
print(ans * pow(pow2[n], mod - 2, mod) % mod)