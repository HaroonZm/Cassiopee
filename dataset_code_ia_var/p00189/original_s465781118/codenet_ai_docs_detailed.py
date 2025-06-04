"""
Résolution du problème AOJ 0189 (le village optimal pour vivre avec une matrice de distances), 
en utilisant l'algorithme de Warshall-Floyd pour déterminer les plus courts chemins entre toutes les paires de villes.
"""

import sys
from sys import stdin

# Utilise la méthode readline optimisée pour la saisie rapide
input = stdin.readline

def warshallFloyd(V, dp):
    """
    Applique l'algorithme de Warshall-Floyd sur la matrice d'adjacence dp.

    Args:
        V (int): Nombre de sommets (villes) dans le graphe.
        dp (list of list of float/int): Matrice des distances, où dp[i][j] représente la distance de la ville i vers la ville j.
            Modifiée sur place pour contenir les plus courtes distances après l'exécution.
    """
    for k in range(V):
        # Pour chaque sommet intermédiaire k
        for i in range(V):
            # Pour chaque sommet de départ i
            for j in range(V):
                # Pour chaque sommet d'arrivée j
                # Si passer par k est un meilleur chemin de i à j, on met à jour
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]


def main(args):
    """
    Point d'entrée principal pour la résolution du problème.
    Lit les entrées représentant les routes entre les villages, calcule toutes les plus courtes distances
    puis détermine le village optimal où la somme des distances vers les autres villages est minimale.

    Args:
        args (list): Arguments passés depuis la ligne de commande (non utilisés ici).

    Entrée:
        Plusieurs jeux de tests, jusqu'à ce qu'une entrée composée d'un seul zéro soit lue.
            n                -- nombre de routes (0 pour terminer)
            a b c (répété n) -- chaque ligne décrit une route entre la ville a et b avec un coût c

    Sortie:
        Pour chaque jeu de test: deux entiers séparés par un espace,
            la ville optimale et la somme minimale des distances vers toutes les autres villes.
    """
    while True:
        n_max = 10  # Nombre maximal possible de villages (de 0 à 9 inclus)
        n = int(input())  # Nombre de routes dans ce jeu de test
        if n == 0:  # Condition d'arrêt
            break

        # Initialisation de la matrice des distances
        # inf pour toute paire, 0 pour la diagonale (distance d'un village à lui-même)
        dp = [[float('inf')] * n_max for _ in range(n_max)]
        for i in range(n_max):
            dp[i][i] = 0

        max_town = 0  # Pour garder trace du village avec le plus grand numéro rencontré

        # Lecture des routes et construction de la matrice d'adjacence
        for _ in range(n):
            a, b, c = map(int, input().split())
            dp[a][b] = c  # Route directe de a à b, coût c
            dp[b][a] = c  # Route directe de b à a (routes bidirectionnelles)
            max_town = max(max_town, a, b)  # Mise à jour du numéro maximal de village

        # Calcul de toutes les plus courtes distances entre paires
        warshallFloyd(max_town + 1, dp)

        # Recherche du village avec la somme minimale des distances aux autres villages
        min_dist = float('inf')
        town_live = -1
        for i in range(max_town + 1):
            # Calcule la somme des distances de ce village vers tous les autres villages actifs
            sum_dist = sum(dp[i][:max_town + 1])
            if sum_dist < min_dist:
                min_dist = sum_dist
                town_live = i

        # Affiche le résultat pour ce jeu de test
        print(f'{town_live} {min_dist}')

if __name__ == '__main__':
    main(sys.argv[1:])