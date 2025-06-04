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

# Augmenter la limite de récursion pour des appels récursifs profonds
sys.setrecursionlimit(10 ** 7)

# Définition de constantes utilisées dans le programme
INFINITY = 10 ** 20
EPSILON = 1.0 / (10 ** 10)
MODULO = 10 ** 9 + 7

# Directions cardinales pour mouvement sur une grille
FOUR_DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Directions diagonales et cardinales pour mouvement sur une grille
EIGHT_DIRECTIONS = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1)
]

# Fonctions d'entrée sorties
def lire_ligne_entiers():
    return [int(element) for element in sys.stdin.readline().split()]

def lire_ligne_entiers_decalage_moins_un():
    return [int(element) - 1 for element in sys.stdin.readline().split()]

def lire_ligne_flottants():
    return [float(element) for element in sys.stdin.readline().split()]

def lire_ligne_chaine_caracteres():
    return sys.stdin.readline().split()

def lire_entier():
    return int(sys.stdin.readline())

def lire_flottant():
    return float(sys.stdin.readline())

def lire_chaine():
    return input()

def print_flush(texte):
    return print(texte, flush=True)

def main():
    liste_resultats_pour_tous_cas = []

    while True:
        nombre_elements = lire_entier()
        if nombre_elements == 0:
            break

        liste_cercle_infos = [lire_ligne_entiers() for _ in range(nombre_elements)]
        liste_ensembles_intersections = [set() for _ in range(nombre_elements)]
        dictionnaire_groupe_par_couleur = collections.defaultdict(list)

        for index_cercle_actuel in range(nombre_elements):
            couleur_cercle = liste_cercle_infos[index_cercle_actuel][3]
            dictionnaire_groupe_par_couleur[couleur_cercle].append(index_cercle_actuel)
            for index_cercle_precedent in range(index_cercle_actuel):
                distance_cercles_au_carre = (
                    (liste_cercle_infos[index_cercle_actuel][0] - liste_cercle_infos[index_cercle_precedent][0]) ** 2 +
                    (liste_cercle_infos[index_cercle_actuel][1] - liste_cercle_infos[index_cercle_precedent][1]) ** 2
                )
                somme_rayons_au_carre = (
                    (liste_cercle_infos[index_cercle_actuel][2] + liste_cercle_infos[index_cercle_precedent][2]) ** 2
                )
                if distance_cercles_au_carre < somme_rayons_au_carre:
                    liste_ensembles_intersections[index_cercle_actuel].add(index_cercle_precedent)

        toutes_possibilites_groupes = None

        for liste_indices_meme_couleur in dictionnaire_groupe_par_couleur.values():
            nombre_paires = len(liste_indices_meme_couleur) // 2
            ensembles_groupes_possibles = set(
                map(
                    lambda permutation_choix: tuple(
                        sorted(
                            [
                                tuple(sorted([permutation_choix[2 * i], permutation_choix[2 * i + 1]]))
                                for i in range(nombre_paires)
                            ]
                        )
                    ),
                    itertools.permutations(liste_indices_meme_couleur)
                )
            )
            liste_ensembles_groupes_possibles = list(ensembles_groupes_possibles)
            if toutes_possibilites_groupes is None:
                toutes_possibilites_groupes = liste_ensembles_groupes_possibles
            else:
                toutes_possibilites_groupes = list(
                    map(
                        lambda combinaison:
                            list(combinaison[0]) + list(combinaison[1]),
                        itertools.product(toutes_possibilites_groupes, liste_ensembles_groupes_possibles)
                    )
                )

        nombre_maximum_elements_non_intersectants = 0

        for liste_paires in toutes_possibilites_groupes:
            existe_amelioration = True
            ensemble_restants = set(range(nombre_elements))
            ensemble_paires_actives = set(liste_paires)
            compteur_retrait = 0

            while existe_amelioration:
                existe_amelioration = False
                for paire in list(ensemble_paires_actives):
                    premiere, seconde = paire
                    if (
                        len(ensemble_restants & liste_ensembles_intersections[premiere]) == 0 and
                        len(ensemble_restants & liste_ensembles_intersections[seconde]) == 0
                    ):
                        ensemble_restants.remove(premiere)
                        ensemble_restants.remove(seconde)
                        ensemble_paires_actives.remove(paire)
                        existe_amelioration = True
                        compteur_retrait += 2

            if nombre_maximum_elements_non_intersectants < compteur_retrait:
                nombre_maximum_elements_non_intersectants = compteur_retrait

        liste_resultats_pour_tous_cas.append(nombre_maximum_elements_non_intersectants)

    return '\n'.join(map(str, liste_resultats_pour_tous_cas))

print(main())