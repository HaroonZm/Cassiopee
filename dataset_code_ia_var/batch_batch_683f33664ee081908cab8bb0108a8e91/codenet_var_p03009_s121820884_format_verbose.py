import sys

# Redéfinir une version compatible de range et input pour Python 2
range_function = xrange
input_function = raw_input

MODULO = 10**9 + 7

# Lecture des trois entiers : nombre d'éléments, hauteur, distance
number_of_elements, max_height, max_distance = [int(value) for value in input_function().split()]

# Précalcul des factorielles jusqu'à une taille suffisante
MAX_FACTORIAL_SIZE = 10**6 + 10
factorials = [1]
while len(factorials) < MAX_FACTORIAL_SIZE:
    next_factorial = factorials[-1] * len(factorials) % MODULO
    factorials.append(next_factorial)

# Précalcul de la somme cumulative des factorielles modulo MODULO
cumulative_factorials = [0]
for factorial_value in factorials:
    next_cumulative = (cumulative_factorials[-1] + factorial_value) % MODULO
    cumulative_factorials.append(next_cumulative)

# Initialisation du tableau de programmation dynamique
dp_height_arrangements = [0] * (max_height + 1)
dp_height_arrangements[0] = factorials[number_of_elements]

# Calcul du nombre de façons multiples selon la spécification
number_of_multiple_ways = cumulative_factorials[number_of_elements + 1] - cumulative_factorials[1]

# Calcul de la somme glissante
current_sliding_sum = 0
for current_height in range_function(1, max_height):
    current_sliding_sum += dp_height_arrangements[current_height - 1]
    if current_height - max_distance - 1 >= 0:
        current_sliding_sum -= dp_height_arrangements[current_height - max_distance - 1]
    current_sliding_sum %= MODULO
    dp_height_arrangements[current_height] = current_sliding_sum * number_of_multiple_ways % MODULO

# Cas particulier pour la hauteur maximale
dp_height_arrangements[max_height] = sum(dp_height_arrangements[max(0, max_height - max_distance):max_height]) % MODULO

# Affichage du résultat final
print dp_height_arrangements[-1]