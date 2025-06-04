from collections import Counter, defaultdict
import math
import random
from decimal import Decimal, ROUND_HALF_UP, ROUND_CEILING
from functools import lru_cache, reduce
from itertools import combinations_with_replacement, product, combinations

def lire_entier():
    return int(input())

def lire_liste_entiers():
    return list(map(int, input().split()))

def lire_chaine():
    return input()

def lire_liste_chaines():
    return list(map(str, input().split()))

def chronometrer(fonction_a_mesurer):
    import time
    import sys

    def fonction_emballee(*args, **kwargs):
        instant_debut = time.time()
        resultat = fonction_a_mesurer(*args, **kwargs)
        instant_fin = time.time()

        print(instant_fin - instant_debut, 'sec', file=sys.stderr)
        return resultat

    return fonction_emballee

@chronometrer
def solution_distance_minimale(position_initiale, liste_positions_cibles, liste_poids_cibles):
    liste_poids_positions_groupes = [
        [liste_poids_cibles[indice], [position_cible]] 
        for indice, position_cible in enumerate(liste_positions_cibles)
    ]

    indice_gauche = 0
    indice_droit = len(liste_poids_positions_groupes) - 1

    while indice_gauche < indice_droit:

        if liste_poids_positions_groupes[indice_gauche][0] >= liste_poids_positions_groupes[indice_droit][0]:
            liste_poids_positions_groupes[indice_gauche][0] += liste_poids_positions_groupes[indice_droit][0]
            liste_poids_positions_groupes[indice_gauche][1] += liste_poids_positions_groupes[indice_droit][1]
            indice_droit -= 1
        else:
            liste_poids_positions_groupes[indice_droit][0] += liste_poids_positions_groupes[indice_gauche][0]
            liste_poids_positions_groupes[indice_droit][1] += liste_poids_positions_groupes[indice_gauche][1]
            indice_gauche += 1

    temps_total_deplacement = 0
    position_actuelle = position_initiale
    limite_gauche = position_initiale
    limite_droite = position_initiale

    for position_objectif in liste_poids_positions_groupes[indice_gauche][1]:
        if limite_gauche < position_objectif < limite_droite:
            continue

        temps_total_deplacement += abs(position_actuelle - position_objectif)

        if position_objectif < position_actuelle:
            limite_gauche = position_objectif
        else:
            limite_droite = position_objectif

        position_actuelle = position_objectif

    return temps_total_deplacement

def point_entree_programme():

    nombre_objets, position_depart = lire_liste_entiers()
    liste_positions = []
    liste_poids = []

    for _ in range(nombre_objets):
        position, poids = lire_liste_entiers()
        liste_positions.append(position)
        liste_poids.append(poids)

    print(solution_distance_minimale(position_depart, liste_positions, liste_poids))

if __name__ == '__main__':
    point_entree_programme()