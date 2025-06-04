# Importation de nombreux modules standards
# math : fournit des fonctions mathématiques
# string : fournit des fonctions sur les chaînes de caractères et des constantes
# itertools : offre des outils pour créer et utiliser des itérateurs efficaces
# fractions : permet de gérer les fractions avec des rationnels
# heapq : fournit des fonctions pour travailler avec des files de priorité (heaps)
# collections : contient des types de données spécialisés
# re : permet de faire des recherches par expressions régulières
# array : fournit des types de tableaux efficaces
# bisect : permet de manipuler des listes triées
# sys : fournit l'accès à certaines variables et fonctions propres à l'interpréteur Python
# random : permet de générer des nombres aléatoires
# time : fonctions de gestion du temps, pauses, temps système, etc.
# copy : pour faire des copies superficielles et profondes d'objets
# functools : offre des outils pour la programmation fonctionnelle, comme le LRU cache, les décorateurs, etc.
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

# On augmente la limite de récursion maximale à 10**7 (dix millions)
# Ceci est nécessaire pour permettre un grand nombre d'appels récursifs
sys.setrecursionlimit(10**7)

# On définit des constantes
# inf représente une valeur "infinie" pratique pour les comparaisons très grandes
inf = 10**20
# eps est une très petite valeur flottante (epsilon), utilisée souvent pour comparer des nombres flottants
eps = 1.0 / 10**10
# mod est une grande valeur utilisée pour faire du calcul modulo, notamment dans les problèmes de théorie des nombres
mod = 10**9 + 7

# Définition des listes de déplacements pour parcourir ou manipuler des grilles ou tableaux à deux dimensions
# dd contient les vecteurs pour les 4 directions cardinales : haut, droite, bas, gauche
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# ddn contient les vecteurs pour les 8 directions autour d'une cellule (y compris les diagonales)
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# Définition de fonctions utilitaires pour lire et convertir l'entrée clavier (ou standard)
def LI():
    # Lire une ligne de l'entrée standard, la scinder en morceaux et convertir chaque morceau en int
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    # Comme LI mais réduit chaque entier de 1 ; utile pour transformer des indices à base 1 en indices à base 0
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    # Idem LI mais transforme en float au lieu de int
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    # Lit une ligne et renvoie la liste des chaînes séparées par des espaces
    return sys.stdin.readline().split()

def I():
    # Lit une ligne et la convertit en un int
    return int(sys.stdin.readline())

def F():
    # Lit une ligne et la convertit en float
    return float(sys.stdin.readline())

def S():
    # Lit une ligne complète depuis l'entrée standard, via input (équivaut à sys.stdin.readline().rstrip())
    return input()

def pf(s):
    # Affiche s et vide immédiatement le buffer d'affichage (flush=True pour affichage interactif)
    return print(s, flush=True)

# Fonction principale du code
def main():
    # On définit une liste vide, qui va contenir les réponses à afficher à la fin
    rr = []

    # Boucle infinie pour traiter plusieurs jeux de données jusqu'à condition d'arrêt
    while True:
        # Lit deux entiers depuis l'entrée standard
        n, d = LI()
        # Si n vaut 0, on considère cela comme le signal de fin et on sort de cette boucle while
        if n == 0:
            break

        # On lit n lignes. Pour chaque ligne, on enlève le premier élément (sans doute une taille), on ne garde que les suivants
        a = [LI()[1:] for _ in range(n)]
        # On prépare une liste vide q (non utilisée ici), et une autre liste sa qui contiendra [somme, tableau]
        q = []
        sa = []

        # Pour chaque élément ai de a, on calcule la somme des éléments de ai, et on les stocke sous forme [somme, copie de ai] dans sa
        for ai in a:
            s = sum(ai)  # On somme tous les entiers dans ai
            sa.append([s, ai])

        # On utilise un flag pour déterminer si un tour de boucle DOIT être refait
        f = True
        while f:
            # Par défaut on va supposer qu'aucune action n'est à faire
            f = False
            # On trie sa par rapport à la somme (premier champ de chaque sous-liste)
            sa.sort()
            # On récupère la plus grande somme (dernier élément), on prend de même la liste correspondante
            ls, la = sa[-1]
            # Si la plus grande somme est nulle, on arrête puisque tout a été vidé
            if ls == 0:
                break
            # On récupère la deuxième plus grande somme (avant dernier)
            ls2 = sa[-2][0]
            # On vérifie une condition particulière :
            # Si la différence entre ls et le dernier élément de la liste associée la[-1] est plus grand que ls2 - d,
            # alors on retire ce dernier élément (la[-1]) de la liste, et on refait un tour de boucle
            if ls - la[-1] >= ls2 - d:
                sa[-1] = [ls - la[-1], la[:-1]]
                f = True
                continue
            # Sinon, on regarde chaque des autres listes de l'avant-dernier au premier
            for i in range(n-2, -1, -1):
                # On extrait somme et liste
                ts, ta = sa[i]
                # Si somme est nulle, alors la suite sera nulle aussi à cause du tri, donc on s'arrête ici
                if ts == 0:
                    break
                # Si la différence entre ts et le dernier élément de ta est supérieure à ls - d,
                # alors on fait la même opération : on enlève le dernier élément de ta et on soustrait à la somme correspondante
                if ts - ta[-1] >= ls - d:
                    sa[i] = [ts - ta[-1], ta[:-1]]
                    f = True

        # Après la terminaison du processus, si la dernière somme restante est nulle,
        # cela signifie qu'on a vidé toutes les listes correctement, sinon il reste quelque chose
        if sa[-1][0] == 0:
            # On ajoute 'Yes' aux résultats (problème résolu dans ce cas)
            rr.append('Yes')
        else:
            # Sinon, on ajoute 'No'
            rr.append('No')

    # On transforme la liste des résultats en chaîne de caractères avec un retour à la ligne entre chaque et on la retourne
    return '\n'.join(map(str, rr))

# Exécution directe de la fonction main(), on affiche son retour
print(main())