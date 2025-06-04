import numpy as np
from itertools import accumulate

MODULO = 10 ** 9 + 7

number_of_elements = int(input())
comparison_string = input()

possible_permutations = np.ones(number_of_elements, dtype=np.int64)

for comparison_operator in comparison_string:

    if comparison_operator == "<":
        reversed_possible_permutations = possible_permutations[::-1]
        accumulated_values = np.cumsum(reversed_possible_permutations[:-1])
        possible_permutations = accumulated_values[::-1] % MODULO

    else:
        accumulated_values = np.cumsum(possible_permutations[:-1])
        possible_permutations = accumulated_values % MODULO

number_of_valid_permutations = possible_permutations[0]

print(number_of_valid_permutations)