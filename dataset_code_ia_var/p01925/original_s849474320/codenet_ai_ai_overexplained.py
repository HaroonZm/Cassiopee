import math  # Ce module fournit des fonctions mathématiques, telles que sqrt, sin, cos, etc.
import string  # Ce module contient des constantes pour les chaînes (ex: ascii_letters, digits)
import itertools  # Module pour créer et manipuler les itérateurs (combinaisons, permutations...)
import fractions  # Fournit une classe Fraction pour la manipulation des fractions rationnelles
import heapq  # Implémente une file de priorité basée sur le tas (min-heap)
import collections  # Fournit des types de conteneurs spécialisés comme defaultdict, deque, etc.
import re  # Module pour les expressions régulières
import array  # Fournit un type de séquence efficace basé sur les tableaux de valeurs
import bisect  # Permet de faire des insertions/consultations efficaces dans des listes triées
import sys  # Module d'accès au système (par exemple: stdin, stdout)
import random  # Module pour générer des nombres pseudo-aléatoires
import time  # Fournit des fonctions pour la gestion du temps et du calendrier
import copy  # Donne des outils pour copier des objets
import functools  # Utilitaires pour la programmation fonctionnelle (ex: reduce, lru_cache)

# Fixe la limite maximale de récursion de la pile à 10**7 pour éviter l'erreur RecursionError lors d'appels récursifs profonds
sys.setrecursionlimit(10**7)

# La variable 'inf' (infinity) représente un nombre très grand utilisé pour initialiser des minimums, maximums, etc.
inf = 10**20

# 'eps' (epsilon) un très petit nombre flottant utilisé pour des comparaisons de flottants ultra-précises en évitant des problèmes d'arrondis
eps = 1.0 / 10**10

# Le modulo 'mod' utilisé dans beaucoup de problèmes numériques pour éviter le dépassement de capacité
mod = 10**9+7

# 'dd' est une liste de tuples représentant les 4 directions cardinales : Haut, Droite, Bas, Gauche (utilisé pour navigation sur une grille)
dd = [(-1,0), (0,1), (1,0), (0,-1)]

# 'ddn' est la liste des 8 directions (voisinage de Moore) autour d'une cellule dans une grille (Pour navigation diagonale incluse)
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

# Fonction LI : Lit une ligne de l'entrée standard, coupe la chaîne en sous-chaînes, les convertit en entiers et retourne la liste d'entiers
def LI():
    # Utilisation de la compréhension de liste pour appliquer int(x) à chaque élément dans la liste résultante de sys.stdin.readline().split()
    return [int(x) for x in sys.stdin.readline().split()]

# Fonction LI_ : Identique à LI, mais décrémente chaque valeur entière de 1 (pratique pour passer d'indice 1-based à 0-based)
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Fonction LF : Lit une ligne et retourne la liste de ses valeurs converties en float
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Fonction LS : Retourne une liste de mots sous forme de chaînes en coupant la ligne lue
def LS():
    return sys.stdin.readline().split()

# Fonction I : Retourne la prochaine ligne de l'entrée standard convertie en int unique
def I():
    return int(sys.stdin.readline())

# Fonction F : Retourne la prochaine ligne de l'entrée standard convertie en float unique
def F():
    return float(sys.stdin.readline())

# Fonction S : Retourne la chaîne d'entrée entrée par l'utilisateur (equivalent de input())
def S():
    return input()

# Fonction pf : Affiche la valeur s passée en argument et force le flush du buffer de sortie pour forcer l'affichage immédiat
def pf(s):
    return print(s, flush=True)

# Définition de la fonction principale où toute la logique du programme se produit
def main():
    # Création d'une liste pour stocker les résultats de plusieurs cas de test si présent
    rr = []

    # Définition d'une fonction interne 'f' qui va traiter une instance particulière avec n et m donnés
    def f(n, m):
        # xd est un dictionnaire (par défaut les valeurs des clés sont des entiers initialisés à 0) 
        xd = collections.defaultdict(int)
        # nd est un autre defaultdict utilisé pour un comptage spécifique 
        nd = collections.defaultdict(int)

        # On initialise nd[i] et xd[i] à 0 pour chaque i dans [1, n] (note: range(1, n+1))
        for i in range(1, n+1):
            nd[i] = 0
            xd[i] = 0

        # Boucle m fois : chaque itération lit une opération, la traite, et met à jour nd et xd en fonction du type
        for _ in range(m):
            t = LI()  # Lit la ligne spécifiant l'opération sous forme de liste d'entiers
            s = t[0]  # Le premier entier est noté 's' et correspond à une certaine quantité (score ? valeur ?)
            if t[1] == 1:
                # Si le second entier de la liste vaut 1 : seul le joueur/élément t[2] est concerné dans nd
                nd[t[2]] += s
            # On ajoute s à xd[i] pour chaque i dans t[2: ] (donc potentiellement plusieurs éléments concernés dans xd)
            for i in t[2:]:
                xd[i] += s

        # On trie les éléments de nd (par leurs valeurs croissantes puis par leur clé croissante) pour constituer la liste na
        na = sorted(nd.items(), key=lambda x: [x[1], x[0]])
        # On trie les éléments de xd (par ordre décroissant de la valeur puis clé croissante) pour constituer la liste xa
        xa = sorted(xd.items(), key=lambda x: [-x[1], x[0]])

        # Si les index correspondant à la plus petite valeur dans nd et la plus grande valeur dans xd sont différents
        if na[0][0] != xa[0][0]:
            # On retourne la différence entre la plus grande valeur de xd et la plus petite de nd + 1
            return xa[0][1] - na[0][1] + 1

        # Le cas où les deux index sont identiques
        # r : différence entre la 2ème plus grande valeur de xd et la plus petite de nd + 1
        r = xa[1][1] - na[0][1] + 1
        # t : différence entre la plus grande valeur de xd et la 2ème plus petite de nd + 1
        t = xa[0][1] - na[1][1] + 1
        # Si r < t, on met à jour r
        if r < t:
            r = t

        return r  # On retourne la valeur de r

    # Boucle principale : Traitement de tous les cas de test présents dans l'entrée
    while 1:
        n, m = LI()  # Lecture des deux entiers n et m
        if n == 0:
            # Si n vaut 0, c'est le signal que l'on doit terminer la boucle (aucun autre cas à traiter)
            break
        # On applique la fonction f(n, m) et on ajoute le résultat dans le tableau rr
        rr.append(f(n, m))

    # On joint les résultats présents dans rr en une seule chaîne séparée par des sauts de ligne
    return '\n'.join(map(str, rr))

# Démarre l'exécution du programme principal, affiche le résultat de main()
print(main())