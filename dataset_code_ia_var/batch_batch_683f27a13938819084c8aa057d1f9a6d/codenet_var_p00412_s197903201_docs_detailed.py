import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop
import copy

# Constantes globales
BIG_NUM = 2000000000  # Utilisé comme une très grande valeur pour initier des comparaisons
MOD = 1000000007      # Modulo couramment utilisé dans les problèmes algorithmiques
EPS = 0.000000001     # Petite valeur epsilon pour les comparaisons flottantes

def process_lane_operations(num_lane, num_info, input_lines):
    """
    Gère une série d'opérations d'ajout et de retrait de valeurs dans plusieurs files (queues) de véhicules.

    Args:
        num_lane (int): Le nombre de files de véhicules.
        num_info (int): Le nombre de commandes à traiter.
        input_lines (List[str]): Liste de chaînes contenant les instructions sous la forme "commande valeur".

    Returns:
        List[int]: Une liste des éléments retirés des files (en réponse à la commande 0).
    """
    # Initialisation d'une liste de files (deque) correspondant à chaque voie
    Q = [deque() for _ in range(num_lane)]
    output = []

    # Boucle à travers chaque commande d'entrée
    for line in input_lines:
        command, value = map(int, line.split())
        if command == 0:
            # Commande 0 : retirer l'élément en tête de la file désignée et l'afficher
            value -= 1  # Conversion vers un index commençant à 0
            removed = Q[value].popleft()
            print("%d" % removed)
            output.append(removed)
        else:
            # Commande 1 : ajouter la voiture à la file la plus courte (minimale)
            min_car = BIG_NUM  # Nombre minimum de voitures (initialisé à une très grande valeur)
            min_lane = BIG_NUM # Indice de la file minimale
            # Rechercher la file avec le moins de véhicules
            for i in range(num_lane):
                if len(Q[i]) < min_car:
                    min_car = len(Q[i])
                    min_lane = i
            # Ajouter la valeur à la file identifiée
            Q[min_lane].append(value)
    return output

def main():
    """
    Fonction principale pour lire l'entrée standard et exécuter le traitement des commandes.
    """
    # Lecture des deux premiers entiers pour le nombre de files et de commandes
    num_lane, num_info = map(int, input().split())
    input_lines = []
    # Lecture des lignes de commandes suivantes
    for _ in range(num_info):
        input_lines.append(input())
    # Exécution des opérations de files de véhicules
    process_lane_operations(num_lane, num_info, input_lines)

if __name__ == "__main__":
    main()