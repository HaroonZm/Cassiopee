import math  # Importe le module mathématiques standards pour différentes opérations mathématiques de base
import string  # Fournit des utilitaires pour le traitement de chaînes de caractères
import itertools  # Fournit des fonctions pour créer des itérateurs efficaces
import fractions  # Pour le calcul exact avec des fractions, mais non utilisé directement ici
import heapq  # Fournit des fonctions pour manipuler des listes comme des files de priorité (heaps)
import collections  # Contient des conteneurs spécialisés comme defaultdict et deque
import re  # Module pour expressions régulières, non utilisé ici dans ce code
import array  # Permet de manipuler des tableaux efficaces de valeurs numériques, non utilisé ici
import bisect  # Fournit des fonctions pour la recherche et l’insertion ordonnée dans des listes
import sys  # Accès à des fonctions et objets systèmes, comme stdin ou setrecursionlimit
import random  # Fournit des fonctions de génération de nombres pseudo-aléatoires
import time  # Fonctions pour mesurer/interagir avec le temps, non utilisé explicitement ici
import copy  # Pour des opérations de copie sur des objets complexes (shallow & deep copy)
import functools  # Fournit des outils pour la programmation fonctionnelle (ex: lru_cache)

# Augmente la limite de récursivité de l’interpréteur Python afin de permettre une récursivité profonde
sys.setrecursionlimit(10**7)

# Définition d’une variable 'inf' à une très grande valeur numérique pour représenter « l’infini » en pratique
inf = 10**20

# Définition d’une petite valeur epsilon pour gérer les imprécisions dues aux calculs flottants
eps = 1.0 / 10**13

# Un nombre utilisé pour les calculs modulo (très courant dans les problèmes d’arithmétique modulaire)
mod = 10**9 + 7

# Définit une liste de déplacements (delta) pour explorer les cases voisines en 4 directions (haut, droite, bas, gauche)
dd = [(-1,0), (0,1), (1,0), (0,-1)]

# Définit une liste de déplacements (delta) pour explorer les 8 cases adjacentes (nord, nord-est, est, sud-est, sud, sud-ouest, ouest, nord-ouest)
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

# Fonction qui lit une ligne de l’entrée standard, la divise en éléments, et les convertit en entiers
def LI():
    # sys.stdin.readline() lit une ligne depuis l’entrée standard, .split() la découpe en tokens, chaque x est converti avec int
    return [int(x) for x in sys.stdin.readline().split()]

# Comme LI(), mais décrémente chaque valeur de 1, utile pour convertir d’un index basé sur 1 à un index basé sur 0
def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

# Similaire à LI(), mais convertit chaque entrée en nombre flottant
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Lit une ligne de l’entrée standard et la découpe en mots/chaînes (sans conversion)
def LS():
    return sys.stdin.readline().split()

# Lit une seule ligne de l’entrée standard et la convertit en entier
def I():
    return int(sys.stdin.readline())

# Lit une seule ligne de l’entrée standard et la convertit en nombre flottant
def F():
    return float(sys.stdin.readline())

# Lit une ligne de l’entrée standard via input() et retourne la chaîne saisie
def S():
    return input()

# Fonction qui affiche un résultat et force le vidage du buffer d’affichage (flush), utile pour l’affichage interactif
def pf(s):
    return print(s, flush=True)

# Définition d’une classe Union-Find (aussi appelée ‘DSU’ Disjoint Set Union)
class UnionFind:
    # Constructeur de la classe, initialise la structure pour 'size' éléments
    def __init__(self, size):
        # self.table stocke pour chaque élément son parent ou la taille de son ensemble s’il est le représentant
        # On initialise à -1 (valeur négative) signifiant que chaque élément est représentant de son propre ensemble et que l’ensemble a une taille de 1
        self.table = [-1 for _ in range(size)]

    # Fonction pour trouver le représentant (racine) de l'ensemble auquel x appartient, avec compression de chemin
    def find(self, x):
        # Si self.table[x] < 0, alors x est la racine de son ensemble
        if self.table[x] < 0:
            return x  # x est la racine
        else:
            # Appel récursif pour trouver la racine, suivi de la mémorisation (compression de chemin)
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    # Fusionne deux ensembles contenant les éléments x et y respectivement
    def union(self, x, y):
        # Recherche des représentants des ensembles de x et y
        s1 = self.find(x)
        s2 = self.find(y)
        # Si les représentants sont distincts, on procède à la fusion
        if s1 != s2:
            # La racine ayant le plus grand ensemble (c'est-à-dire celle avec le nombre le plus négatif) devient la nouvelle racine
            if self.table[s1] <= self.table[s2]:
                # Additionne les tailles et déplace s2 sous s1
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                # Additionne les tailles et déplace s1 sous s2
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True  # Fusion a été effectuée
        return False  # x et y étaient déjà dans le même ensemble

    # Fonction qui retourne tous les représentants d'ensembles et leur taille respective
    def subsetall(self):
        a = []  # Liste des (racines, taille d’ensemble)
        for i in range(len(self.table)):
            # Si la valeur est négative, c’est un représentant (racine)
            if self.table[i] < 0:
                a.append((i, -self.table[i]))  # Ajoute un tuple (racine, taille positive)
        return a

# Fonction principale (point d’entrée du code)
def main():
    # Fixe la graine du générateur de nombres aléatoires à une valeur constante pour des résultats reproductibles
    random.seed(42)
    rr = []  # Liste pour stocker l’ensemble des réponses à afficher à la fin

    # Fonction locale prenant en entrée le nombre de noeuds n et le nombre d’opérations m
    def f(n, m):
        # Lecture des m opérations (chaque opération est une liste de chaînes de caractères)
        qa = [LS() for _ in range(m)]
        # Initialisation d’un dictionnaire de dictionnaires (avec valeur par défaut 0) pour stocker les poids/différences
        d = collections.defaultdict(lambda: collections.defaultdict(int))
        # Pour chaque nœud i (de 0 à n inclus), on l’initialise avec une valeur pseudo-aléatoire (pour l’exemple)
        for i in range(n+1):
            d[i][i] = random.randrange(1, 100)
        r = []  # Liste pour stocker les résultats de cette instance
        uf = UnionFind(n+1)  # Initialisation de la structure UnionFind, pour (n+1) éléments

        # Parcours de chaque opération lue
        for q in qa:
            # Si la première chaîne de l’opération est un point d’exclamation, c’est une opération de fusion avec contrainte de différence pondérée
            if q[0] == '!':
                # Récupération et conversion en int des paramètres de l’opération : a, b, w
                a, b, w = map(int, q[1:])
                fa = uf.find(a)  # Récupère la racine d'a après compression de chemin
                fb = uf.find(b)  # Récupère la racine de b après compression de chemin
                if fa == fb:
                    continue  # Ils sont déjà dans le même ensemble, aucune opération n’est nécessaire
                uf.union(a, b)  # Fusionne les ensembles de a et b
                # Après la fusion, les ensembles représentant a et b peuvent avoir changé, on doit donc mettre à jour les poids relatifs
                if fa == uf.find(a):
                    # Si fa reste le représentant de l’ensemble unifié : on ajuste d[fa] avec les informations de d[fb]
                    sa = w + (d[fa][a] - d[fb][b])
                    for k in d[fb].keys():
                        # Met à jour pour chaque nœud k de l’ensemble fb sa différence par rapport à la nouvelle racine fa
                        d[fa][k] = d[fb][k] + sa
                else:
                    # Si fb est devenu le représentant : on ajuste d[fb] depuis d[fa]
                    sa = (d[fa][a] - d[fb][b]) + w
                    for k in d[fa].keys():
                        # Met à jour pour chaque nœud k de fa sa différence par rapport à la nouvelle racine fb
                        d[fb][k] = d[fa][k] - sa
            else:
                # Pour tout autre type d’opération (ici c’est la requête '?', question sur la différence entre deux nœuds)
                a, b = map(int, q[1:])
                fa = uf.find(a)  # Trouve la racine de a
                # Si a et b n’appartiennent pas au même ensemble, la réponse est 'UNKNOWN'
                if fa != uf.find(b):
                    r.append('UNKNOWN')
                else:
                    # Sinon, calcule la différence de valeur/distance entre b et a dans le même ensemble
                    r.append(d[fa][b] - d[fa][a])
        return r  # Retourne la liste de toutes les réponses aux requêtes '?'

    # Boucle infinie pour traiter plusieurs ensembles d’entrées jusqu’à rencontre du couple 0 0
    while 1:
        # Lecture de deux entiers n et m pour chaque instance
        n, m = LI()
        if n == 0 and m == 0:
            break  # Quand n et m valent 0, on quitte la boucle (fin de toutes les instances)
        # Appelle la fonction f(n, m) et étend la liste globale rr avec les réponses de cette instance
        rr.extend(f(n, m))

    # Joint toutes les réponses avec un retour à la ligne, prêt à afficher
    return '\n'.join(map(str, rr))

# Appel du point d’entrée principal du script et affichage du résultat
print(main())