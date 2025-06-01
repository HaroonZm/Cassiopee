#!/usr/bin/env python

# Importation de la classe deque depuis le module collections.
# Une deque est une file à double extrémité, permettant d'ajouter ou de retirer des éléments des deux côtés avec efficacité.
from collections import deque

# Importation du module itertools avec un alias 'it'.
# itertools propose des fonctions pour créer des itérateurs complexes.
import itertools as it

# Importation du module sys qui offre des variables et fonctions liées à l'interpréteur Python.
import sys

# Importation du module math qui fournit des fonctions mathématiques.
import math

# Modification de la limite maximale de récursivité à 10 millions.
# La récursivité correspond à une fonction qui s'appelle elle-même.
# Par défaut, Python limite la profondeur de récursivité pour éviter un débordement de pile.
# Ici, on augmente cette limite pour gérer des cas très profonds sans erreur.
sys.setrecursionlimit(10000000)

# Lecture d'une entrée utilisateur, correspondant au nombre de cas de test T.
# input() lit une chaîne de caractères depuis l'entrée standard.
# Comme on traite un nombre, on considère qu'il sera converti plus tard en entier si besoin.
T = input()

# Boucle sur chaque cas de test, de 0 à T-1.
# 'loop' est une variable compteur pour indiquer le numéro d'itération.
for loop in range(T):
    # Lecture de l'entier N depuis l'entrée standard.
    # N représente une valeur propre au problème, souvent une taille ou un nombre d'éléments.
    N = input()
    
    # Lecture d'une chaîne de caractères S en entrée.
    # raw_input() lit une chaîne de caractères depuis l'entrée standard (ancienne syntaxe Python 2).
    # On suppose ici que le script est en Python 2.
    S = raw_input()
    
    # Création de la chaîne S1 en concaténant la lettre 'N', 
    # puis les premiers 2*N caractères de S, puis à nouveau 'N'.
    # Cette opération permet de construire une chaîne encadrée par 'N' servant de sentinelle.
    S1 = 'N' + S[:N * 2] + 'N'
    
    # Création de la chaîne S2, similaire à S1 mais avec la tranche de S commençant à 2*N caractères.
    S2 = 'N' + S[N * 2:] + 'N'
    
    # Initialisation des variables sx1 et sx2 à une valeur très grande (100000).
    # Ces variables serviront à retenir un indice minimum trouvé dans des boucles.
    sx1 = sx2 = 100000
    
    # Initialisation des variables gx1 et gx2 à -1.
    # Ces variables serviront à retenir un indice maximum trouvé.
    gx1 = gx2 = -1
    
    # Initialisation de la variable ans à zéro.
    # Cette variable cumulera des compteurs pour la solution finale.
    ans = 0
    
    # Boucle sur les indices de 0 jusqu'à N inclus.
    # L'indice i sert à parcourir les positions pertinentes dans S1 et S2.
    for i in range(N + 1):
        # Condition qui vérifie si le caractère à la position i*2 dans S1 est 'Y'
        # ou si le caractère suivant i*2+1 est aussi 'Y'.
        # 'Y' est probablement une valeur significative dans le problème.
        if S1[i * 2] == 'Y' or S1[i * 2 + 1] == 'Y':
            # Incrémentation du compteur ans car une condition favorable est rencontrée.
            ans += 1
            
            # Mise à jour de sx1 avec la plus petite valeur entre sx1 actuel et i.
            # Cela permet de retenir le plus petit indice avec 'Y' dans S1.
            sx1 = min(sx1, i)
            
            # Mise à jour de gx1 avec la valeur i.
            # Comme on parcourt i dans l'ordre croissant, gx1 retiendra la dernière position atteinte.
            gx1 = i
        
        # Logique identique appliquée à la chaîne S2.
        if S2[i * 2] == 'Y' or S2[i * 2 + 1] == 'Y':
            ans += 1
            sx2 = min(sx2, i)
            gx2 = i
    
    # Après avoir traité toutes les positions, comparaison des indices minima entre sx1 et sx2.
    if sx1 > sx2:
        # Si sx1 est plus grand que sx2, on ajoute 1 à ans.
        ans += 1
    
    # Comparaison des indices maxima entre gx1 et gx2.
    if gx1 < gx2:
        # Si gx1 est plus petit que gx2, on ajoute 1 à ans.
        ans += 1
    
    # Affichage du résultat final pour ce cas de test.
    # On affiche la somme de N et ans.
    print N + ans