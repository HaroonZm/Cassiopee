import math  # Module pour les fonctions mathématiques de base
import string  # Module pour les chaînes de caractères et les opérations associées
import itertools  # Module permettant d'utiliser des outils pour créer et utiliser des itérateurs efficaces
import fractions  # Module pour gérer les fractions rationnelles
import heapq  # Module fournissant une implémentation du tas binaire (heap)
import collections  # Module regroupant différentes structures de données avancées, comme deque, Counter, etc.
import re  # Module permettant l’utilisation des expressions régulières
import array  # Module permettant la gestion de structures de type tableau (arrays)
import bisect  # Module pour la gestion efficace de listes triées (insertion, recherche, etc.)
import sys  # Module qui fournit l’accès à certaines variables et fonctions interagissant avec l’interpréteur Python
import random  # Module permettant de générer des nombres pseudo-aléatoires
import time  # Module pour accéder au temps système (dates, temporisateurs, etc.)
import copy  # Module permettant de copier (shallow ou deep) des objets Python
import functools  # Module qui fournit des outils pour la programmation fonctionnelle

# Change la limite de récursion maximale autorisée par Python pour éviter le dépassement de pile lors de récursions profondes
sys.setrecursionlimit(10**7)  # Fixe la profondeur maximale de récursion à 10 millions

inf = 10**20  # Définit une valeur très grande à utiliser comme infinité dans les algorithmes
eps = 1.0 / 10**10  # Définit une très petite valeur, souvent utilisée pour comparer des nombres flottants en évitant les problèmes d’arrondi
mod = 998244353  # Nombre premier souvent utilisé comme modulo lors de calculs pour éviter les débordements d’entiers

# Définit les directions de déplacement possibles sur une grille en 2D (haut, droite, bas, gauche)
dd = [ (0,-1), (1,0), (0,1), (-1,0) ]
# Définit les directions de déplacement sur une grille en 2D mais en incluant les diagonales : 8 directions possibles
ddn = [ (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,-1), (-1,0), (-1,1) ]

# Fonction utilitaire qui lit une ligne de l'entrée standard, la découpe en mots, convertit chaque élément en entier, et retourne une liste d’entiers
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Fonction similaire à LI mais décrémente chaque entier lu de 1, utile souvent pour passer d'indices humains (1-based) à indices de Python (0-based)
def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

# Fonction qui lit une ligne de l'entrée standard, découpe en mots, convertit chaque élément en flottant, et retourne une liste de floats
def LF():
    return [float(x) for x in sys.stdin.readline().split()]

# Fonction qui lit une ligne de l'entrée standard, découpe en mots, et retourne une liste de chaînes de caractères
def LS():
    return sys.stdin.readline().split()

# Fonction qui lit une ligne depuis l'entrée standard, la convertit en entier, et retourne sa valeur
def I():
    return int(sys.stdin.readline())

# Fonction qui lit une ligne depuis l'entrée standard, la convertit en float, et retourne sa valeur
def F():
    return float(sys.stdin.readline())

# Fonction qui lit une entrée avec la fonction input (équivalent, mais plus explicite), retourne une chaîne
def S():
    return input()

# Fonction qui affiche une chaîne (ou autre objet), et force immédiatement l’affichage, utile pour communiquer avec des juges ou des systèmes externes qui attendent la sortie en temps réel
def pf(s):
    return print(s, flush=True)

# Fonction principale contenant l'ensemble de la logique du programme
def main():
    # Création de la liste qui stockera les résultats à la fin de tous les calculs
    rr = []
    
    M = 20000  # Définition de la limite supérieure pour le calcul des sommes de carrés
    s = set()  # Création d’un ensemble pour stocker toutes les valeurs possibles de la somme de deux carrés > 1
    
    # Boucle imbriquée pour générer tous les entiers t > 1 de la forme i^2 + j^2 où i et j varient de 0 à racine carrée entière de M incluse
    for i in range(int(M**0.5)+1):
        for j in range(int(M**0.5)+1):
            t = i**2 + j**2  # Calcul de la somme de deux carrés
            if t > 1:  # Seulement si t est strictement supérieur à 1
                s.add(t)  # Ajoute t à l'ensemble s pour éviter les doublons

    n = I()  # Lit le nombre de cas de test depuis l'entrée standard
    ni = 0  # Initialise un compteur à 0 pour parcourir tous les cas de test
    
    # Boucle principale exécutée une fois pour chaque cas de test
    while ni < n:
        ni += 1  # Incrémente le compteur à chaque itération

        a, b = LI()  # Lit deux entiers pour ce cas de test depuis l'entrée standard
        t = a**2 + b**2  # Calcule la somme des carrés des deux entiers

        r = 'P'  # Définit la valeur par défaut du résultat pour ce cas de test ('P')
        
        # Parcourt chaque valeur c possible parmi les sommes de deux carrés calculées précédemment
        for c in s:
            # Vérifie que t est divisible par c (donc t/c est entier), et que l'autre facteur t/c est aussi une somme de deux carrés > 1
            if t % c == 0 and t // c in s:
                r = 'C'  # Si c'est vrai, change la réponse en 'C'
                break  # Arrête la boucle dès que la condition est remplie

        rr.append(r)  # Ajoute le résultat 'P' ou 'C' à la liste des réponses

    # Construit une chaîne compacte à partir de la liste des réponses, séparée par des sauts de ligne, et la retourne
    return '\n'.join(map(str, rr))

# Exécute la fonction principale et affiche son résultat à l’écran
print(main())