import sys  # Importe le module sys, qui fournit des fonctions et des variables utilisées pour interagir avec l'interpréteur Python
import re  # Importe le module re, qui permet le traitement des expressions régulières
from collections import deque, defaultdict, Counter  # Importe plusieurs structures de données utiles de la bibliothèque collections
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log  # Importe de nombreuses fonctions mathématiques, les plus utilisées
from itertools import accumulate, permutations, combinations, product  # Importe des fonctions pratiques pour travailler avec des itérateurs
from operator import itemgetter, mul  # Importe des fonctions d'opérations rapides sur les objets
from copy import deepcopy  # Importe deepcopy pour faire des copies profondes d'objets complexes
from string import ascii_lowercase, ascii_uppercase, digits  # Importe des constantes de chaîne courantes
from bisect import bisect, bisect_left  # Importe des fonctions pour la recherche binaire dans des listes triées
from fractions import gcd  # Importe la fonction gcd (plus grand commun diviseur) du module fractions (PYTHON 3.4 ; obsolète en >=3.5)
from heapq import heappush, heappop  # Importe les fonctions de file de priorité (tas)
from functools import reduce  # Importe reduce, une fonction utilitaire pour appliquer un opérateur de façon cumulative
import networkx as nx  # Importe le module networkx qui sert à travailler avec des graphes (très utilisé pour les algorithmes de graphes)

# Redéfinition de la fonction input pour qu'elle lise les entrées depuis sys.stdin et enlève les espaces devant/derrière
def input():
    return sys.stdin.readline().strip()  # Lit une ligne depuis l’entrée standard, enlève les espaces en début/fin

# Fonction utilitaire pour lire un entier depuis l'entrée standard
def INT():
    return int(input())  # Convertit l'entrée lue en entier

# Fonction utilitaire pour lire plusieurs entiers sur une même ligne, séparés par des espaces
def MAP():
    return map(int, input().split())  # Utilise input(), coupe la chaîne par les espaces, convertit chaque morceau en entier

# Fonction utilitaire qui retourne une liste d'entiers lus sur une ligne
def LIST():
    return list(map(int, input().split()))  # Crée une liste à partir de MAP()

# Fonction qui lit n lignes et zippe leurs colonnes ensemble, résultat : itérable de tuples correspondant à chaque colonne
def ZIP(n):
    return zip(*(MAP() for _ in range(n)))  # Lis n lignes avec MAP(), zippe les résultats colonne par colonne

# Définit la limite de récursion maximale (par défaut dans Python c’est 1_000)
sys.setrecursionlimit(10 ** 9)  # Met à une valeur très large pour permettre la récursion profonde (attention en vrai...)

INF = 10 ** 10  # Définit une constante représentant l’infini (fictif) pour les besoins du programme
mod = 10 ** 9 + 7  # Modulus classique dans les problèmes de programmation compétitive pour éviter les grands nombres

# Lit deux entiers H (hauteur) et W (largeur) qui déterminent la taille d'une grille
H, W = MAP()

# Crée une liste a qui contient H sous-listes. Chacune correspond à une ligne de la grille, convertie en liste de caractères.
a = [list(input()) for _ in range(H)]

# Création d'un graphe non orienté avec networkx
G = nx.Graph()  # Initialise un objet graphe vide

# Ajoute des noeuds au graphe. On numérote les noeuds de 0 à H+W+1 inclus (donc H+W+2 noeuds)
G.add_nodes_from(range(0, H + W + 2))

# Parcours de toutes les cases de la grille
for i in range(H):  #Pour chaque ligne
    for j in range(W):  #Pour chaque colonne
        if a[i][j] == "S":
            # Position de S : on la marque dans sy, sx (indices ligne et colonne)
            sy, sx = i, j
            # Ajout d'une arête du "super-source" 0 vers la ligne i+1 (nœud i+1), capacité infinie
            G.add_edge(0, i+1, capacity=INF)
            # Ajout d'une arête du super-source 0 vers la colonne H+j+1 (nœud H+j+1), capacité infinie
            G.add_edge(0, H+j+1, capacity=INF)
        elif a[i][j] == "T":
            # Position de T : indices ligne et colonne dans gy, gx
            gy, gx = i, j
            # Arête de la ligne i+1 (nœud source) vers le "super-puits", capacité infinie
            G.add_edge(i+1, H+W+1, capacity=INF)
            # Arête de la colonne H+j+1 vers le puits, capacité infinie
            G.add_edge(H+j+1, H+W+1, capacity=INF)
        elif a[i][j] == "o":
            # Pour chaque 'o', ajoute une arête entre la ligne et la colonne correspondantes
            # L’arête va de la ligne i+1 vers la colonne H+j+1 avec une capacité de 1
            G.add_edge(i+1, H+j+1, capacity=1)
            # L’arête de la colonne H+j+1 vers la ligne i+1, capacité 1 : car ce graphe non orienté
            G.add_edge(H+j+1, i+1, capacity=1)

# Vérifie un cas particulier : si S et T sont sur la même ligne ou sur la même colonne, il n’y a pas de chemin possible
if sy == gy or sx == gx:
    print(-1)  # Affiche -1 pour signaler l’impossibilité
    exit()  # Arrête le programme

# Calcule et affiche la valeur du flot maximum du super-source (noeud 0) au super-puits (noeud H+W+1)
print(nx.maximum_flow_value(G, 0, H+W+1))  # Utilise l’algorithme de flot de networkx pour déterminer la solution