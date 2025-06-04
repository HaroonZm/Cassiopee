from collections import deque
import itertools as itertools_module
import sys
import math

# Augmenter la limite de récursion pour gérer des appels récursifs profonds
sys.setrecursionlimit(10000000)

# Lecture des paramètres d'entrée : nombre cible et coût additionnel
target_number, additional_cost = map(int, raw_input().split())

# Initialisation de la réponse avec une très grande valeur (éventuellement minimale)
minimum_total_cost = 10 ** 18

# Parcourir les différentes tailles possibles de partitionnements (1 à 64)
for number_of_factors in range(1, 65):

    # Évaluer le facteur de base pour cette taille
    base_factor = int(target_number ** (1.0 / number_of_factors))

    # Initialisation de la liste des facteurs pour cette taille
    factors_list = [base_factor] * number_of_factors

    # Index du facteur à augmenter
    position_in_factors_list = 0

    while True:

        current_product = 1

        for single_factor in factors_list:
            current_product *= single_factor

        # Si le produit atteint ou dépasse la cible, on arrête d'incrémenter
        if current_product >= target_number:
            break

        # Incrémenter le facteur courant, puis passer à la position suivante
        factors_list[position_in_factors_list] += 1
        position_in_factors_list += 1
        position_in_factors_list %= number_of_factors

    # Calculer le coût total pour cette configuration
    total_cost_for_this_partition = sum(factors_list) + additional_cost * (number_of_factors - 1)

    # Mettre à jour la valeur minimale trouvée
    minimum_total_cost = min(minimum_total_cost, total_cost_for_this_partition)

# Afficher le résultat avec le coût minimum trouvé
print minimum_total_cost