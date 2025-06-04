#!/usr/bin/env python3

import sys
import math
import copy

# Les constantes très grandes, souvent utilisées comme bornes ou "infini".
HUGE = 2147483647            # Plus grande valeur sur 32 bits signée
HUGEL = 9223372036854775807  # Plus grande valeur sur 64 bits signée

# Chaîne contenant les lettres minuscules de l'alphabet anglais.
ABC = "abcdefghijklmnopqrstuvwxyz"

def main():
    """
    Fonction principale du programme.
    
    Ce programme lit un entier n et une liste de n entiers donnés en entrée.
    Pour chaque élément a de la liste, il incrémente un compteur pour les valeurs a, a+1 et a+2.
    À la fin, il affiche la valeur maximale trouvée dans le tableau de compteurs.
    L'objectif général est de savoir quel nombre, parmi tous les entiers possibles, peut être obtenu le plus souvent en ajoutant 0, 1 ou 2 à chaque élément de la liste.
    """
    # Lecture du nombre d'éléments à lire dans la liste
    n = int(input())

    # Lecture de la liste d'entiers, séparés par des espaces, provenant de l'entrée standard
    ai = list(map(int, input().split()))

    # Vérification que la liste ai contient effectivement n éléments
    assert len(ai) == n

    # Initialisation d'un tableau de compteurs avec 100002 zéros (pour index de 0 à 100001 inclus)
    cnt = [0 for i in range(100002)]

    # Parcours de chaque élément de la liste ai
    for a in ai:
        # Pour chaque nombre a, on incrémente le compteur pour a, a+1 et a+2
        for b in [a, a + 1, a + 2]:
            cnt[b] += 1

    # Affichage de la valeur maximale trouvée dans le tableau cnt
    print(max(cnt))

if __name__ == "__main__":
    main()