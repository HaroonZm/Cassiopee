"""
Ce code traite une chaîne de caractères composée des lettres 'R', 'G', 'B' et effectue des opérations de comptage et de calcul combinatoire pour obtenir un résultat modulo 998244353. Le script est structuré pour une entrée compétitive, typiquement pour un problème d'attribution ou de permutation sous contrainte de couleurs.
"""

import math
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit

# Lecture rapide de l'entrée standard
ipt = stdin.readline

# Définition d'une grande limite de récursion pour éviter les erreurs de récursion profonde
setrecursionlimit(10**7)

# Modulo pour éviter les débordements d'entiers, standard dans les compétitions AtCoder
mod = 998244353

# Directions de déplacement potentielles sur une grille (haut, bas, gauche, droite)
dir = [(-1,0), (1,0), (0,-1), (0,1)]

# Alphabet minuscule anglais
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    """
    Fonction principale du script.
    Lit les entrées, puis effectue un traitement sur une chaîne de couleurs ('R', 'G', 'B').
    Calcule le nombre de permutations ou arrangements distincts selon des règles spécifiques,
    avec gestion de combinaisons et de modularité.
    Affiche le résultat final.

    Entrée attendue :
    - n (int) : longueur de la chaîne
    - s (str) : chaîne composée des lettres 'R', 'G', 'B'

    Aucun retour.
    """

    # Lecture du nombre d'éléments à traiter
    n = int(ipt())
    # Lecture de la chaîne de couleurs (depuis l'entrée standard)
    s = input()

    # Dictionnaire pour mapper chaque caractère de couleur à son index
    d = {"R": 0, "G": 1, "B": 2}
    
    # Initialisation du résultat (nombre d'arrangements possibles)
    nm = 1

    # Compteurs de chaque couleur rencontrée (nc[0] pour 'R', nc[1] pour 'G', nc[2] pour 'B')
    nc = [0, 0, 0]

    # Statut intermédiaire pour chaque couleur, utilisé pour les calculs combinatoires
    stt = [0, 0, 0]

    # Ressources intermédiaires pour chaque couleur, participent au calcul de nm
    res = [0, 0, 0]

    # Parcours de chaque caractère de la chaîne s
    for si in s:
        # Récupère l’indice correspondant à la couleur courante
        i = d[si]
        # Incrémente le compteur de la couleur courante
        nc[i] += 1
        
        # Si le compteur courant est supérieur à ceux des autres couleurs, on incrémente le statut courant
        if nc[i] > nc[i-1] and nc[i] > nc[i-2]:
            stt[i] += 1
        # Si le compteur courant est inférieur ou égal aux deux autres, on réduit le nombre de résultats possibles
        elif nc[i] <= nc[i-1] and nc[i] <= nc[i-2]:
            nm *= res[i]
            res[i] -= 1
        # Sinon, mise à jour des ressources et statuts pour les autres couleurs
        else:
            if stt[i-1] == 0:
                # On renforce la ressource de la couleur précédente et on diminue le statut d'encore avant
                res[i-1] += 1
                nm *= stt[i-2]
                stt[i-2] -= 1
            else:
                # On renforce la ressource de la couleur d'avant précédent et on diminue l'autre statut
                res[i-2] += 1
                nm *= stt[i-1]
                stt[i-1] -= 1
        
        # Application du modulo après chaque mise à jour pour rester dans la limite
        nm %= mod

    # Boucle pour multiplier le résultat final par toutes les valeurs de 1 à n (factorielle)
    for i in range(1, n+1):
        nm *= i
        nm %= mod
    
    # Affichage du résultat final modulo 998244353
    print(nm)

    return None

if __name__ == '__main__':
    main()