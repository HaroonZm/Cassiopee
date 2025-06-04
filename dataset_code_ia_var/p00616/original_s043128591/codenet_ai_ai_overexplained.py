#!/usr/bin/env python

# Importer le module 'deque' de la bibliothèque 'collections'
# 'deque' signifie 'double-ended queue' : une file d'attente où l'on peut ajouter/retirer des éléments à gauche ou à droite
from collections import deque

# Importer le module 'itertools' en lui donnant le nom 'it' pour un accès plus bref
# 'itertools' contient des fonctions permettant de créer et manipuler des itérateurs
import itertools as it

# Importer le module 'sys' qui fournit des fonctions et variables utilisées pour manipuler divers éléments du runtime Python
import sys

# Importer le module 'math' qui fournit des fonctions mathématiques de base
import math

# Modifier la limite maximale de profondeur de la pile d'appels récursifs
# Par défaut, cette limite est généralement autour de 1000, mais ici on la fixe à 10 000 000 (très grand)
# Ceci permet d'éviter les erreurs de récursion maximale atteinte si une fonction récursive profonde est employée
sys.setrecursionlimit(10000000)

# Commencer une boucle qui continuera indéfiniment jusqu'à rencontrer une condition d'arrêt
while True:
    # Lire une ligne sur l'entrée standard avec raw_input(), la découper en utilisant l'espace comme séparateur
    # Puis convertir chacun des morceaux en un entier grâce à map(int, ...)
    # On assigne ces deux entiers aux variables 'n' et 'h'
    n, h = map(int, raw_input().split())
    
    # Tester la valeur de 'n' pour déterminer si la boucle doit se terminer
    # Si 'n' vaut 0, alors on quitte la boucle avec 'break'
    if n == 0:
        break
    
    # Créer un nouveau dictionnaire vide 'm'
    # Ce dictionnaire servira à mémoriser certains triplets entiers spécifiques que l'on rencontrera plus tard
    m = {}
    
    # Pour chacune des 'h' instructions qui suivent, on effectue les opérations suivantes
    for loop in range(h):
        # Lire une ligne d'entrée contenant trois valeurs séparées par des espaces grâce à raw_input()
        # Les assigner respectivement à S (une chaîne de caractères), p1 (un entier), p2 (un entier, également)
        S, p1, p2 = raw_input().split()
        
        # Convertir les deux derniers arguments de 'p1' et 'p2' en entiers, car raw_input() lit tout sous forme de chaînes de caractères
        p1 = int(p1)
        p2 = int(p2)
        
        # Commencer une boucle allant de 1 à n inclus (c'est-à-dire de 1 à n, compris)
        for i in range(1, n + 1):
            # Trois types de plans peuvent être donnés : 'xy', 'xz', ou 'yz'
            # Chacun correspondra à "bloquer" ou "colorier" (selon l'interprétation du problème d'origine) un ensemble de points dans un cube tridimensionnel de taille n x n x n
            
            # Si S = 'xy', alors on bloque le plan d'équation x = p1, y = p2 quel que soit z (donc pour tous les i de 1 à n sur z)
            if S == 'xy':
                # On crée une clef dans le dictionnaire à partir du triplet (p1, p2, i) et on lui donne la valeur 1
                # La clef représente la position (x, y, z) qui est ici (p1, p2, i)
                # La valeur 1 joue juste le rôle de présence, sa vraie valeur importe peu
                m[(p1, p2, i)] = 1
            
            # Si S = 'xz', alors on bloque le plan x = p1, z = p2 pour tous les y
            if S == 'xz':
                # La clef est de la forme (p1, i, p2), donc y varie de 1 à n
                m[(p1, i, p2)] = 1
            
            # Si S = 'yz', alors on bloque le plan y = p1, z = p2 pour tous les x
            if S == 'yz':
                # La clef est (i, p1, p2), donc x varie de 1 à n
                m[(i, p1, p2)] = 1
    
    # Afficher le résultat :
    # - n ** 3 correspond au nombre total de points dans un cube de dimension n (le cube a n positions sur chaque axe, donc n * n * n)
    # - len(m) correspond au nombre total de triplets "bloqués", c'est-à-dire ceux qui apparaissent au moins une fois comme clef dans le dictionnaire m
    # En soustrayant len(m) à n ** 3, on obtient le nombre de triplets qui n'ont été "bloqués" par aucun plan, autrement dit les points "libres"
    print n ** 3 - len(m)