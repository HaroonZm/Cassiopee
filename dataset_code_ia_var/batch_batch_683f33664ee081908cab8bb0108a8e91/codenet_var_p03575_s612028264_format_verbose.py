import sys

# Augmenter la limite de récursivité pour les grands graphes
sys.setrecursionlimit(10**6)

# Raccourci pour lecture rapide de l'entrée
input = sys.stdin.readline

# Importations de modules standards fréquemment utilisés
from math import floor, sqrt, factorial, hypot, log
from heapq import heappop, heappush, heappushpop
from collections import Counter, defaultdict, deque
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right
from copy import deepcopy
from fractions import gcd
from random import randint

# Fonction de plafond pour la division entière 
def division_entiere_haut(numerateur, denominateur):
    return (numerateur + denominateur - 1) // denominateur

INFINI = float('inf')
MODULO_PRIME = 10**9 + 7

def afficher_liste_de_listes(*listes):
    for liste in listes:
        print(*liste, sep='\n')

def lire_entier_reduit_un(n):
    return int(n) - 1

def lire_deux_entiers():
    return map(int, input().split())

def lire_deux_flottants():
    return map(float, input().split())

def lire_paire_indices_reduits_un():
    return map(lire_entier_reduit_un, input().split())

def lire_ligne_entiers():
    return list(lire_deux_entiers())

def lire_ligne_indices_reduits_un():
    return [int(x) - 1 for x in input().split()]

def lire_ligne_flottants():
    return list(lire_deux_flottants())

def lire_n_entiers(n):
    return [lire_entier() for _ in range(n)]

def lire_n_lignes_entiers(n):
    return [lire_ligne_entiers() for _ in range(n)]

def lire_n_lignes_indices_reduits_un(n):
    return [lire_ligne_indices_reduits_un() for _ in range(n)]

def lire_liste_lignes_entiers():
    return [list(map(int, ligne.split())) for ligne in input()]

def lire_entier():
    return int(input())

def lire_flottant():
    return float(input())

def lire_chaine_sans_saut():
    return input().replace('\n', '')

def main():
    nombre_noeuds, nombre_aretes = lire_deux_entiers()

    adjacence_matrice = [[False] * nombre_noeuds for _ in range(nombre_noeuds)]

    liste_aretes_zero_indexees = lire_n_lignes_indices_reduits_un(nombre_aretes)

    for noeud_u, noeud_v in liste_aretes_zero_indexees:
        adjacence_matrice[noeud_u][noeud_v] = True
        adjacence_matrice[noeud_v][noeud_u] = True

    def arrete_est_ponte():
        pile_noeuds_a_visiter = [0]
        ensemble_noeuds_visites = set()

        while pile_noeuds_a_visiter:
            noeud_actuel = pile_noeuds_a_visiter.pop()
            if noeud_actuel in ensemble_noeuds_visites:
                continue
            ensemble_noeuds_visites.add(noeud_actuel)
            for noeud_voisin in range(nombre_noeuds):
                if adjacence_matrice[noeud_actuel][noeud_voisin]:
                    if noeud_voisin in ensemble_noeuds_visites:
                        continue
                    pile_noeuds_a_visiter.append(noeud_voisin)
        return len(ensemble_noeuds_visites) < nombre_noeuds

    nombre_de_pontes = 0

    for noeud_u, noeud_v in liste_aretes_zero_indexees:
        adjacence_matrice[noeud_u][noeud_v] = False
        adjacence_matrice[noeud_v][noeud_u] = False

        if arrete_est_ponte():
            nombre_de_pontes += 1

        adjacence_matrice[noeud_u][noeud_v] = True
        adjacence_matrice[noeud_v][noeud_u] = True

    print(nombre_de_pontes)

if __name__ == '__main__':
    main()