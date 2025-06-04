#!usr/bin/env python3

# Importation des modules de la bibliothèque standard Python
from collections import defaultdict  # Permet de créer des dictionnaires avec une valeur par défaut
from collections import deque       # Permet de créer des files à double extrémité (deque) pour une manipulation efficace des files et piles
from heapq import heappush, heappop # Fournit des fonctions pour utiliser des files de priorité (tas binaire)
import sys                         # Permet d'interagir avec l'interpréteur Python (ex: stdin, recursion limit, etc.)
import math                        # Fournit de nombreuses fonctions mathématiques de base
import bisect                      # Fournit des fonctions pour la recherche et l'insertion dans des listes triées
import random                      # Permet de générer des nombres aléatoires et de faire d'autres opérations aléatoires

# Définition de fonctions utilitaires pour la lecture d'entrées, souvent utilisées en programmation compétitive
def LI():
    # Cette fonction lit une ligne sur l'entrée standard, la découpe en morceaux (split), convertit chaque morceau en entier, puis retourne la liste des entiers
    return list(map(int, sys.stdin.readline().split()))

def I():
    # Lit une ligne sur l'entrée standard, puis convertit cette chaîne en entier
    return int(sys.stdin.readline())

def LS():
    # Lit une ligne sur l'entrée standard, la découpe en morceaux (split), puis transforme chaque morceau en liste de caractères, retourne la liste de ces listes
    return list(map(list, sys.stdin.readline().split()))

def S():
    # Lit une ligne sur stdin, la convertit en liste de caractères, enlève le dernier caractère (saut de ligne) et retourne la liste résultante
    return list(sys.stdin.readline())[:-1]

def IR(n):
    # Crée une liste de taille n remplie initialement avec des valeurs None
    l = [None for i in range(n)]
    # Pour chaque indice de la liste, lit un entier de stdin et le place à cet indice
    for i in range(n):
        l[i] = I()
    return l

def LIR(n):
    # Crée une liste de taille n, chaque case contenant une liste d'entiers lue depuis stdin
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

def SR(n):
    # Crée une liste de taille n, chaque case contenant une liste de caractères lue depuis stdin
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = S()
    return l

def LSR(n):
    # Crée une liste de taille n, chaque case étant une liste obtenue par l'appel de SR()
    l = [None for i in range(n)]
    for i in range(n):
        l[i] = SR()
    return l

# Cette fonction augmente la limite de récursion maximale autorisée dans Python
# Par défaut, elle est relativement basse (par exemple 1000), ce qui peut empêcher des algorithmes récursifs profonds de fonctionner (ex: DFS profond)
sys.setrecursionlimit(1000000)

# Variable représentant un très grand nombre utilisé comme modulo pour éviter les surflows lors de calculs de grands entiers (souvent utilisé dans les problèmes algorithmiques : 1_000_000_007)
mod = 1000000007

# Partie 1 : Utilisation de structures d'ensemble (Union-Find avec et sans poids)

# ----- Partie Union-Find pondéré (pour gérer des ensembles fusionnés avec une gestion de différences de poids) -----

# Définition de la fonction pour trouver la racine d'un ensemble auquel appartient l'élément x
def root(x):
    # Si le parent de x est x lui-même, alors x est la racine, donc on retourne x
    if par[x] == x:
        return x
    # Appel récursif pour trouver la racine parente de par[x]
    r = root(par[x])
    # On ajoute à w[x] la valeur de w[par[x]] pour accumuler le poids relatif jusqu'à la racine
    w[x] += w[par[x]]
    # On compresse le chemin en rattachant le parent direct de x à la racine pour accélérer les recherches futures
    par[x] = r
    return par[x]

# Fonction permettant de vérifier si deux éléments x et y appartiennent au même ensemble (même racine)
def same(x, y):
    return root(x) == root(y)

# Fonction pour fusionner les ensembles contenant x et y en tenant compte d'une différence de poids z
def unite(x, y, z):
    # Ajustement de z en tenant compte des poids déjà stockés
    z += w[x] - w[y]
    # On retrouve la racine de x et celle de y
    x = root(x)
    y = root(y)
    # On attache l'arbre de rang inférieur à celui de rang supérieur pour limiter la hauteur de l'arbre
    if rank[x] < rank[y]:
        par[x] = y          # Le parent de x devient y
        w[x] = -z           # Le poids relatif entre x et y est stocké sous forme négative
    else:
        par[y] = x          # Le parent de y devient x
        w[y] = z            # Le poids relatif est stocké tel quel pour y
        # Si les deux arbres ont le même rang, on augmente le rang de la nouvelle racine
        if rank[x] == rank[y]:
            rank[x] += 1

# ----- Initialisation des tableaux pour Union-Find pondéré -----

# On lit deux entiers n et Q depuis stdin (n = nombre d'éléments ; Q = nombre de requêtes)
n, Q = LI()                                    # LI lit une liste d'entiers depuis stdin

# Création du tableau par représentant les parents : au début, chaque élément est son propre parent
par = [i for i in range(n)]

# Création du tableau de rangs, initialisé à zéro pour tous les éléments
rank = [0 for i in range(n)]

# Création du tableau de poids, initialisé à zéro pour chacun des n éléments
w = [0 for i in range(n)]

# Boucle principale sur les Q requêtes
for _ in range(Q):
    q = LI()   # Lecture d'une requête, qui est une liste d'entiers
    # Si le premier nombre de la requête (q[0]) est non nul, il s'agit d'une requête de type 1 (calculer une différence de poids entre deux éléments)
    if q[0]:
        x, y = q[1], q[2]    # Extraction des indices x et y depuis la requête
        # Vérifie si x et y sont dans le même ensemble
        if same(x, y):
            # Si c'est le cas, on affiche la différence de poids entre y et x
            print(w[y] - w[x])
        else:
            # Sinon, la différence n'est pas définie (on affiche "?")
            print("?")
    else:
        # Il s'agit d'une requête de fusion (type 0), donc q a trois valeurs en plus du type : x, y, z
        x, y, z = q[1:]
        # On ne fusionne que si x et y ne sont pas déjà dans le même composant connexe
        if not same(x, y):
            # Fusionne avec la différence de poids demandée
            unite(x, y, z)

# Remarque : Cette partie n'a pas de print ou d'appel à une partie principale, il s'agit uniquement de code utilitaire avec commentaires détaillés pour
# comprendre toutes les productions et manipulations d'un Union-Find pondéré.

# Les autres parties du code source original sont commentées sous forme de chaînes multilignes ;
# elles servent à illustrer des variantes ou d'autres tâches algorithmiques et ne sont pas exécutées.