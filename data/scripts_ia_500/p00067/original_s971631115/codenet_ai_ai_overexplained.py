#!/usr/bin/env python

# Importation des fonctionnalités futures pour assurer la compatibilité et le comportement moderne
from __future__ import (
    division,          # Le symbole / fait une division flottante même entre entiers (au lieu de division entière)
    absolute_import,   # Les imports sont absolus par défaut, évite les confusions entre modules locaux et standards
    print_function,    # La fonction print devient une vraie fonction avec des parenthèses, compatible Python 3
    unicode_literals   # Les chaines de caractères sont unicode par défaut au lieu de bytes
)
# Importation uniquement de la fonction stdin de la bibliothèque sys, qui permet de lire les entrées standard
from sys import stdin

# Définition d'une fonction appelée solve qui prend en entrée une liste L représentant une grille 12x12
def solve(L):
    # Initialisation d'un compteur n qui servira à numéroter les ensembles/connectivités détectées
    n = 0
    # Création d'un ensemble vide 'sets' pour stocker les identifiants uniques des groupes détectés
    sets = set()
    # Parcours des lignes y allant de 0 à 11 inclus (12 lignes)
    for y in range(12):
        # Pour chaque ligne, parcours des colonnes x allant de 0 à 11 inclus (12 colonnes)
        for x in range(12):
            # Vérification si la valeur du pixel/cellule à la position y,x est nulle (0) (considéré comme vide)
            if not L[y][x]:
                # Si la cellule est vide, on passe à la suivante sans rien faire (continue)
                continue
            # Si la cellule n’est pas vide, on vérifie si on peut la relier à un ensemble adjacent au-dessus
            elif y and L[y-1][x]:
                # 'y' vérifie que l’on n’est pas sur la première ligne pour éviter un index invalide y-1
                # Si la cellule directement au-dessus (y-1, x) est occupée (non nulle),
                # on affecte à la cellule actuelle le même identifiant/groupement que celle du dessus
                L[y][x] = L[y-1][x]
            # Sinon, on vérifie si on peut relier cette cellule à un ensemble adjacent à gauche
            elif x and L[y][x-1]:
                # 'x' vérifie que ce n’est pas la première colonne pour éviter un index invalide x-1
                # Si la cellule à gauche (y, x-1) est occupée (non nulle),
                # on affecte à la cellule actuelle le même identifiant/groupement que celle de gauche
                L[y][x] = L[y][x-1]
            else:
                # Si aucune cellule adjacente au-dessus ou à gauche n’est occupée,
                # cela signifie que cette cellule commence un nouveau groupe distinct
                n += 1  # On incrémente le compteur n pour créer un nouvel identifiant unique
                sets.add(n)  # On ajoute ce nouvel identifiant à l’ensemble des groupes détectés
                L[y][x] = n  # On assigne ce nouvel identifiant à la cellule actuelle
        # Après avoir parcouru la ligne de gauche à droite, on effectue un parcours en sens inverse sur la même ligne
        # On part de la colonne 10 vers 0 inclus (colonne précédente) pour vérifier les connexions avec la droite
        for x in range(10, -1, -1):
            # Si la cellule actuelle L[y][x] est occupée, ainsi que la cellule à droite L[y][x+1]
            # Et que leurs identifiants sont différents (appartiennent à deux groupes distincts)
            if L[y][x] and L[y][x+1] and L[y][x] != L[y][x+1]:
                # Cela signifie qu'il faut fusionner ces deux groupes en un seul
                # On retire l’identifiant de la cellule actuelle de l’ensemble des groupes
                sets.discard(L[y][x])
                # On réaffecte à la cellule actuelle l’identifiant du groupe de la cellule à droite pour fusionner
                L[y][x] = L[y][x+1]
    # A la fin du traitement, on retourne la taille de l’ensemble des groupes, c’est-à-dire le nombre de groupes distincts
    return len(sets)

# Initialisation de la variable s avec un saut de ligne, qui servira à savoir si la lecture continue
s = '\n'
# Initialisation de la variable sep inutilisée ici mais probablement prévue pour séparer les sorties ou entrées
sep = '\n'

# Boucle qui s’exécute tant que la variable s n’est pas vide (c’est-à-dire que l’on n’a pas atteint la fin de l'entrée standard)
while s:
    # Initialisation d’une liste vide L qui va stocker les 12 lignes de la grille actuelle
    L = []
    # Lecture de 12 lignes consécutives à partir de l’entrée standard
    for i in range(12):
        # Lecture d’une ligne sur l’entrée standard avec suppression des espaces de fin (rstrip)
        line = stdin.readline().rstrip()
        # Transformation de cette ligne de caractères en une liste d’entiers en découpant chaque caractère
        L.append([int(s) for s in line])
    # Appel de la fonction solve avec la grille L et affichage du résultat (nombre de groupes distincts)
    print(solve(L))
    # Lecture d'une nouvelle ligne en entrée standard pour déterminer si la boucle doit continuer
    s = stdin.readline()