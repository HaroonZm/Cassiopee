#!/usr/bin/env python

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

def solve(L):
    """
    Compte le nombre de composantes connexes de 1 dans une grille 12x12,
    en reliant les cases adjacentes verticalement et horizontalement.
    
    Args:
        L (list of list of int): Grille 12x12, chaque case vaut 0 (vide) ou 1 (pleine).
        
    Returns:
        int: Nombre de composantes connexes trouvées dans la grille.
    """

    n = 0            # Compteur pour les labels uniques de composantes
    sets = set()     # Ensemble pour stocker les labels uniques (composantes)
    # Parcours ligne par ligne et colonne par colonne
    for y in range(12):
        for x in range(12):
            # Ignore les cases vides
            if not L[y][x]:
                continue
            # Si la case au-dessus fait partie d'une composante, propage ce label
            elif y and L[y-1][x]:
                L[y][x] = L[y-1][x]
            # Sinon, si la case à gauche fait partie d'une composante, propage ce label
            elif x and L[y][x-1]:
                L[y][x] = L[y][x-1]
            # Sinon, nouvelle composante : incrémente le label et ajoute au set
            else:
                n += 1
                sets.add(n)
                L[y][x] = n
        # Fusionne les composantes si deux cases adjacentes (à droite) portent des labels différents
        for x in range(10, -1, -1):  # Parcourt la ligne de droite à gauche
            if L[y][x] and L[y][x+1] and L[y][x] != L[y][x+1]:
                sets.discard(L[y][x])        # Supprime l'ancien label du set
                L[y][x] = L[y][x+1]         # Remplace l'ancien label par le nouveau

    return len(sets)   # Le nombre de composantes différentes

# Lecture des grilles depuis l'entrée standard jusqu'à épuisement
s = '\n'   # Initialise la variable de lecture
sep = '\n'
while s:
    L = []
    # Lit 12 lignes pour former une grille 12x12
    for i in range(12):
        L.append([int(s) for s in stdin.readline().rstrip()])
    print(solve(L))  # Affiche le nombre de composantes connexes de cette grille
    s = stdin.readline()  # Prépare la lecture de la prochaine grille (s'arrête à EOF)