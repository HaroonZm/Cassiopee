# Solution en Python pour le problème "ルパン四世"
# Approche détaillée:
# - Il s'agit d'un problème d'optimisation de chemin où l'ordre de visite des entrepôts (蔵) doit minimiser le temps total de déplacement.
# - Les entrepôts sont alignés sur une même ligne (nord-sud), donc les déplacements entre entrepôts sont en une dimension.
# - Le temps de déplacement dépend de la charge que Daisuke porte, qui augmente à chaque entrepôt visité (car il récolte les 千両箱).
# - La vitesse de déplacement est : vitesse = 2000 / (70 + poids_en_kg)
# - Le poids augmente de 20 kg par 千両箱, et chaque entrepôt a un certain nombre de 千両箱.
# - La méthode consistera à chercher la permutation d'entrepôts qui:
#   1) commence par l'entrepôt le plus proche (premier entrepôt visité)
#   2) minimise le temps total de déplacement en tenant compte du poids accumulé.
# 
# Stratégie algorithmique:
# - Comme n ≤ 15, il est possible d'utiliser une programmation dynamique avec bitmask (Held-Karp) pour un TSP modifié.
# - Ici, l'état est défini par:
#   - l'ensemble des entrepôts visités (bitmask)
#   - le dernier entrepôt visité
#   - la charge totale transportée (recalculable à partir des entrepôts visités)
# - Mais comme recomposer la charge à chaque fois serait lourd, on peut pré-calculer pour chaque sous-ensemble la charge totale.
# - On fait DP[state][last] = temps minimum pour avoir visité 'state' et être au dernier entrepôt 'last'
# - Transitions sur l'entrepôt suivant 'nxt' non visité:
#   temps += distance(last, nxt) / vitesse(charge)
#   charge est la somme des 千両箱 dans 'state' (avant d'ajouter 'nxt') * 20 kg

import sys
import math
from functools import lru_cache

sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline

    n = int(input())
    warehouses = []
    # Lire les informations: numéro, distance (m), nombre de 千両箱
    for _ in range(n):
        s, d, v = map(int, input().split())
        warehouses.append( (s, d, v) )

    # Trier selon la distance d pour obtenir l'ordre de départ possible
    # On doit commencer par le premier entrepôt. Selon l'énoncé / exemples, on commence au premier entrepôt visité (donné).
    # Ce que signifie "ルパンの運転で最初の蔵へ行き、その後順に" → l'ordre est à déterminer, mais on doit choisir un ordre
    # qui minimise le temps en partant du premier entrepôt visité.
    # Le problème est que le premier entrepôt n'est pas forcément celui le plus proche.
    # Le problème indique "ルパンは、最初の蔵を破ってから最後の蔵に辿りつくまでの..."
    # Donc on doit commencer par un entrepôt choisi par la permutation: la première visite est fixée par l'ordre.
    # Cela signifie que l'on doit considérer que le premier entrepôt est le premier de l'ordre choisi: on choisit la permutation qui minimise le temps,
    # sans contrainte de point de départ autre que le premier entrepôt visité.
    #
    # Donc, on minimise parmi toutes les permutations (ordre de visite), les permutations commencant par n'importe quel entrepôt,
    # mais le problème demande la séquence commençant par le premier entrepôt + suite.
    #
    # En fait, dans l'exemple, on utilise la séquence complète, ordre quelconque.
    # Donc dans notre DP, on teste toutes permutations, et on choisit la meilleure.
    #
    # Pour représentation, on indexe les entrepôts de 0 à n-1.

    # Pré-calcul des distances absolues (car alignés sur un axe)
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = abs(warehouses[i][1] - warehouses[j][1])

    # Pré-calcul du poids accumulé pour chaque sous-ensemble de entrepôts
    # poids (en kg) = nombre total de 千両箱 * 20
    weight_for_state = [0]*(1<<n)
    for state in range(1<<n):
        total_boxes = 0
        for i in range(n):
            if (state>>i) & 1:
                total_boxes += warehouses[i][2]
        weight_for_state[state] = total_boxes * 20

    # Vitesse en fonction du poids (w en kg)
    # vitesse = 2000 / (70 + w)
    def velocity(w):
        return 2000 / (70 + w)

    # On utilise un DP avec mémorisation pour le TSP modifié
    # dp(state, last): temps min pour avoir visité 'state' et être à 'last'
    from math import inf

    @lru_cache(None)
    def dp(state, last):
        # Si 'state' ne comprend que 'last', c-à-d un seul entrepôt visité,
        # alors temps = 0 car pas encore de déplacement
        if state == (1 << last):
            return 0.0

        res = inf
        # on cherche quel entrepôt a précédé 'last'
        prev_state = state & ~(1 << last)
        w = weight_for_state[prev_state]  # poids avant de récupérer l'entrepôt 'last'

        # Essayer tous les candidats 'k' avant 'last'
        for k in range(n):
            if (prev_state >> k) & 1:
                # distance entre k et last
                d = dist[k][last]
                v = velocity(w)
                time_move = d / v
                candidate = dp(prev_state, k) + time_move
                if candidate < res:
                    res = candidate
        return res

    # Recherche du résultat minimal parmi toutes permutations, c-à-d choisir la meilleure dernière étape en ayant visité tous
    full = (1 << n) - 1

    best_time = inf
    best_last = -1
    for last in range(n):
        # on considère toutes séquences finissant dans last entrepôt et couvrant full
        t = dp(full, last)
        if t < best_time:
            best_time = t
            best_last = last

    # Reconstruction du chemin:
    path = []

    def reconstruct(state, last):
        path.append(last)
        if state == (1 << last):
            # début
            return
        prev_state = state & ~(1 << last)
        w = weight_for_state[prev_state]
        # retrouver k précédent qui minimise dp
        for k in range(n):
            if (prev_state >> k) & 1:
                d = dist[k][last]
                v = velocity(w)
                if abs(dp(state, last) - (dp(prev_state, k) + d/v)) < 1e-9:
                    reconstruct(prev_state, k)
                    break

    reconstruct(full, best_last)
    path.reverse()

    # Afficher les numéros des entrepôts dans l'ordre choisi
    # warehouses[i][0] correspond au numéro s_i
    print(' '.join(str(warehouses[i][0]) for i in path))

if __name__ == '__main__':
    main()