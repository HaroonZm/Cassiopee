import math  # Importation du module math qui contient des fonctions mathématiques
import string  # Importation du module string pour les opérations sur les chaînes de caractères
import itertools  # Importation du module itertools pour les outils d’itération efficaces
import fractions  # Importation du module fractions pour manipuler des fractions (nombres rationnels)
import heapq  # Importation du module heapq pour la manipulation de files de priorité (heaps)
import collections  # Importation du module collections pour les structures de données de haut niveau
import re  # Importation du module re pour les expressions régulières
import array  # Importation du module array pour manipuler des tableaux typés
import bisect  # Importation du module bisect pour le tri et la recherche dans des listes triées
import sys  # Importation du module sys pour accéder à certaines variables système et fonctions
import random  # Importation du module random pour la génération de nombres aléatoires
import time  # Importation du module time pour le temps et les mesures de performance
import copy  # Importation du module copy pour la copie superficielle et profonde d’objets
import functools  # Importation du module functools pour les fonctions utilitaires de programmation fonctionnelle

# Modification de la limite maximale de récursion, car certaines fonctions récursives
# peuvent dépasser la limite par défaut pour des entrées importantes.
sys.setrecursionlimit(10**7)  # Définit la limite de récursion à 10 millions

inf = 10**20  # Définit une valeur pour représenter de l’infini (utilisée comme valeur très grande)
eps = 1.0 / 10**13  # Définit une valeur de précision très petite (epsilon)
mod = 10**9+7  # Définit un modulo utilisé souvent dans les problèmes de programmation compétitive

# Définit une liste de 4 directions (haut, droite, bas, gauche) pour la navigation sur une grille
dd = [(-1,0), (0,1), (1,0), (0,-1)]  

# Définit une liste de 8 directions autour d’un point (haut, haut-droit, droite, bas-droit, bas, bas-gauche, gauche, haut-gauche)
ddn = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]  

# Fonction LI : lit une ligne de l’entrée standard, la scinde par espace et convertit chaque morceau en entier.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Fonction LI_ : fait la même chose que LI mais soustrait 1 à chaque entier (utile pour des indices zéro-based)
def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

# Fonction LF : lit une ligne de l’entrée standard et convertit chaque élément en float
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Fonction LS : lit une ligne de l’entrée standard, la scinde, retourne une liste de sous-chaînes
def LS():
    return sys.stdin.readline().split()

# Fonction I : lit une ligne de l’entrée standard et la convertit en entier
def I():
    return int(sys.stdin.readline())

# Fonction F : lit une ligne de l’entrée standard et la convertit en float
def F():
    return float(sys.stdin.readline())

# Fonction S : lit une ligne de l’entrée standard via input() (attention à la différence avec sys.stdin.readline()) 
def S():
    return input()

# Fonction pf : affiche l'argument passé et applique flush=True pour forcer l'affichage (utile dans les concours en ligne pour output immédiat)
def pf(s):
    return print(s, flush=True)

# Fonction principale du programme
def main():
    rr = []  # Initialise une liste vide pour stocker les résultats de chaque cas

    # Définition d’une fonction interne f prenant en paramètre n (nombre d’éléments à lire/traiter)
    def f(n):
        # Lis n lignes d’entrées, chaque ligne convertie en liste d’entiers, stockées dans une liste a
        a = [LI() for _ in range(n)]
        # Calcule le maximum de la fonction x[0]*2+x[1] sur tous les éléments de a
        t = max(map(lambda x: x[0]*2 + x[1], a))
        # Calcule la somme totale de tous les éléments de toutes les listes de a
        u = sum(map(sum, a))
        # Trouve le max de x[0] (premier entier) et -x[1] (opposé du deuxième entier), 
        # ce qui permet d'identifier l'élément ayant la plus grande valeur du premier entier,
        # et 'triche' avec -x[1] pour les égalités
        mx = max(map(lambda x: [x[0], -x[1]], a))
        # Trouve l'indice dans 'a' de la première occurrence du couple [mx[0], -mx[1]]
        mxi = a.index([mx[0], -mx[1]])
        # Calcule la somme de tous les premiers entiers de chaque liste dans a, puis enlève mx[0]
        k = sum(map(lambda x: x[0], a)) - mx[0]
        # Vérifie si la somme k des premiers entiers restants est inférieur à mx[0]
        if k < mx[0]:
            mx0 = mx[0]  # On conserve la valeur du plus grand premier entier
            # Initialise un tableau pour la programmation dynamique, taille de mx0 + 1, tout à 0
            dp = [0] * (mx0 + 1)
            dp[k] = 1  # On marque la position k comme atteignable
            # Parcourt chaque élément par son indice de 0 à n-1
            for ai in range(n):
                if ai == mxi:
                    continue  # Ignore l’élément maximal déjà considéré
                c = a[ai][1]  # Prend le deuxième entier c de la (ai)-ième liste
                # Parcourt les positions du tableau dynamique à l’envers pour éviter les doubles comptages
                for i in range(mx0 - c, -1, -1):
                    dp[i + c] |= dp[i]  # Marque la position i+c si i était atteignable
            mt = 0  # Initialisation de mt pour stocker la valeur maximale atteignable
            # Recherche depuis la fin (valeur la plus haute) jusqu’à 0 celle qui a été marquée atteignable
            for i in range(mx0, -1, -1):
                if dp[i]:
                    mt = i
                    break
            u += (mx0 - mt)  # Met à jour u, ajoutant la différence pour atteindre la valeur maximale
        # Renvoie le maximum entre t et u pour ce test
        return max(t, u)

    while 1:  # Boucle infinie pour lire de multiples cas de test
        n = I()  # Lit le nombre d’éléments à traiter pour ce cas
        if n == 0:
            break  # Brise la boucle si n==0, la condition d’arrêt
        rr.append(f(n))  # Ajoute le résultat de f(n) à la liste des résultats
        # print('rr', rr[-1])  # (Commenté) Affichait le dernier résultat, utile pour le debug

    # Transforme la liste des résultats en chaînes, séparées par des sauts de ligne, et retourne
    return '\n'.join(map(str, rr))

# Appelle la fonction principale main(), affiche son résultat (retourne un string global)
print(main())