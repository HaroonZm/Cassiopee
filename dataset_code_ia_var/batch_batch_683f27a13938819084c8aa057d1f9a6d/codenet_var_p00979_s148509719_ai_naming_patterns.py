import sys

# Constantes
CONST_INF = 10 ** 18
CONST_MOD = 10 ** 9 + 7
SYS_RECURSION_LIMIT = 1000000

# Configuration du système
sys.setrecursionlimit(SYS_RECURSION_LIMIT)

# Entrée de l'utilisateur
input_value = int(input())

# Initialisation de la réponse
minimum_result = input_value

# Boucle principale avec des noms explicites
for pattern_index in range(1, 50):
    base_sum = 2 * sum(3 ** exponent_index for exponent_index in range(pattern_index)) - 1
    if base_sum > input_value:
        break
    temp_number = 2 * pattern_index - 1
    remainder = input_value - base_sum
    for digit_index in range(pattern_index):
        temp_number += remainder % 3
        remainder //= 3
    temp_number += remainder
    minimum_result = min(minimum_result, temp_number)

print(minimum_result)