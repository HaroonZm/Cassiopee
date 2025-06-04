import sys  # Importe le module système, nécessaire pour accéder à des fonctions comme la gestion de l'entrée/sortie standard et pour régler la limite de récursion.
from random import *  # Importe toutes les fonctions et classes du module random, qui est utilisé pour générer des nombres ou sélectionner des éléments aléatoires.
from collections import *  # Importe toutes les classes et fonctions du module collections, qui inclut des structures de données comme deque, Counter, etc.
from heapq import *  # Importe toutes les fonctions du module heapq, qui fournit une implémentation de file de priorité (tas binaire).

# Modifie la limite maximale de récursion dans le programme,
# cela peut être utile pour des algorithmes récursifs profonds comme le DFS (Deep First Search)
sys.setrecursionlimit(10 ** 6)

# Définit une fonction lambda qui prend un argument 'x',
# convertit 'x' en entier puis retourne la valeur moins 1.
# Cela est utile, par exemple, pour convertir un index à base 1 à un index à base 0.
int1 = lambda x: int(x) - 1

# Définit une fonction lambda pour afficher chaque élément d'un objet itérable 'x' sur une nouvelle ligne.
# Cela utilise l'étoile * pour décomposer la liste/itérable et sep="\n" pour changer le séparateur par défaut (l'espace) en retour à la ligne.
p2D = lambda x: print(*x, sep="\n")

# Définit une fonction II() qui lit une ligne de l'entrée standard, 
# puis la convertit en entier et retourne ce nombre.
def II(): 
    return int(sys.stdin.readline())

# Définit une fonction MI() qui lit une ligne de l'entrée standard,
# sépare cette ligne par les espaces, convertit chaque sous-string en entier,
# puis retourne un itérable map des entiers.
def MI(): 
    return map(int, sys.stdin.readline().split())

# Définit une fonction MI1() qui lit une ligne de l'entrée standard,
# sépare cette ligne, convertit chaque sous-string grâce à la fonction int1 (qui fait -1),
# retourne un itérable map résultant en des entiers à base 0.
def MI1(): 
    return map(int1, sys.stdin.readline().split())

# Définit une fonction LI() qui lit une ligne de l'entrée standard,
# sépare cette ligne, convertit chaque sous-string en entier,
# retourne une liste des entiers.
def LI(): 
    return list(map(int, sys.stdin.readline().split()))

# Définit une fonction LI1() similaire à LI(), 
# mais convertit chaque string en entier moins un (pour index à base 0).
def LI1(): 
    return list(map(int1, sys.stdin.readline().split()))

# Définit une fonction LLI(rows_number) qui prend un argument rows_number,
# puis retourne une liste contenant rows_number listes,
# chaque sous-liste étant obtenue en appelant LI() (récupère donc rows_number lignes d'entiers).
def LLI(rows_number): 
    return [LI() for _ in range(rows_number)]

# Définit une fonction SI() qui lit une ligne de l'entrée standard,
# et retourne chaque caractère sauf le dernier (en général un retour à la ligne '\n').
def SI(): 
    return sys.stdin.readline()[:-1]

# Déclare une liste de tuples, appelée dij.
# Chaque tuple est une paire de deux entiers qui représente les directions cardinales 
# pour bouger en haut, en bas, à droite et à gauche sur une grille.
# (1,0)=bas, (-1,0)=haut, (0,1)=droite, (0,-1)=gauche
dij = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Définition de la classe UnionFind, qu'on appelle aussi Union-Find ou Disjoint Set.
# Cette structure de données gère l'appartenance d'éléments à des groupes (ensembles disjoints)
# et permet de fusionner deux ensembles et de demander rapidement si deux éléments partagent le même ensemble.
class UnionFind:
    # Le constructeur __init__ initialise une nouvelle instance de la classe UnionFind
    # en créant un tableau d'états d'une taille 'n'. Chaque case est un entier:
    # si la valeur est négative, l'indice est la racine de son ensemble, et la valeur donne la taille (-taille).
    # si la valeur est positive, elle pointe vers le parent dans l'arbre.
    def __init__(self, n):
        self.state = [-1] * n  # Crée une liste de taille n, initialisée à -1 pour chaque élément

    # Fonction pour trouver la racine d'un élément (représentant de groupe)
    # Utilise le path compression pour accélérer les recherches suivantes en mettant à jour directement les parents.
    def root(self, u):
        v = self.state[u]  # On récupère la valeur à l'index u
        if v < 0:          # Si la valeur est négative, alors 'u' est la racine de son ensemble
            return u
        self.state[u] = res = self.root(v)  # Recursion : on cherche la racine de 'v'
        return res  # On retourne l'entier représentant la racine

    # Fonction pour fusionner/deux ensembles distincts à partir de deux éléments u et v
    def merge(self, u, v):
        ru = self.root(u)  # Trouve la racine de l'ensemble de u
        rv = self.root(v)  # Trouve la racine de l'ensemble de v
        if ru == rv:       # Si ru et rv sont identiques, ils appartiennent déjà au même ensemble, on ne fait rien
            return
        du = self.state[ru]  # du est la taille négative de l'ensemble contenant ru
        dv = self.state[rv]  # dv est la taille négative de l'ensemble contenant rv
        # On veut fusionner l’ensemble le plus petit dans le plus grand (union by size)
        if du > dv:          # Si du (la taille de ru) est moins grand (moins négatif), on échange ru et rv
            ru, rv = rv, ru
        if du == dv:         # Si les tailles sont égales, on augmente la taille de l'ensemble fusionné de 1 supplémentaire
            self.state[ru] -= 1
        self.state[rv] = ru  # On rattache le représentant de rv à ru.

    # Si besoin d’accéder à la taille du groupe, on peut ajouter une méthode size non commentée comme ci-dessous.
    # def size(self, u):
    #     return self.size_table[self.root(u)]

# Lecture de deux entiers sur la même ligne depuis l'entrée standard : n et q
# n : nombre d'éléments (dans UnionFind) ; q : nombre de requêtes à traiter
n, q = MI()  # Utilisation de la fonction MI() définie au début, cela retournera deux entiers (n, q)

# Instanciation de la structure UnionFind avec n+1 éléments (de 0 à n inclus, probablement car indexation à base 1)
uf = UnionFind(n + 1)

# Boucle qui s'exécute q fois : chaque itération traite une requête
for _ in range(q):
    t, u, v = MI()  # Lit trois entiers t u v sur la même ligne (type de requête, argument 1, argument 2)
    if t:  # Si t == 1 (expression booléenne est vraie si t != 0)
        # Teste si u et v sont dans le même ensemble
        # uf.root(u) == uf.root(v) retourne True s'ils sont dans le même ensemble, False sinon
        # (uf.root(u) == uf.root(v)) * 1 convertit le booléen en entier (1 ou 0)
        print((uf.root(u) == uf.root(v)) * 1)
    else:  # Sinon, t == 0
        # Fusionne les ensembles contenant u et v
        uf.merge(u, v)