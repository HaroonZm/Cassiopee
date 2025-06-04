import sys
import numpy as np

# Lecture de la ligne d'entrée depuis stdin
read_line_from_stdin = sys.stdin.readline

# Récupération de la taille de la permutation et du nombre d'opérations
number_of_elements, number_of_iterations = map(int, read_line_from_stdin().split())

# Lecture des deux permutations de taille number_of_elements
permutation_P, permutation_Q = [
    np.array(read_line_from_stdin().split(), dtype=np.int32) for _ in range(2)
]

# Conversion pour travailler en base 0
permutation_P = permutation_P - 1
permutation_Q = permutation_Q - 1

def compute_inverse_permutation(permutation_array):
    """
    Calcule l'inverse d'une permutation.
    """
    inverse_permutation = np.empty_like(permutation_array)
    inverse_permutation[permutation_array] = np.arange(len(inverse_permutation))
    return inverse_permutation

def multiply_permutation_by_inverse(first_permutation, second_permutation):
    """
    Effectue la multiplication d'une permutation par l'inverse d'une autre (premier * inverse(deuxième)).
    """
    result_permutation = np.empty_like(first_permutation)
    result_permutation[second_permutation] = first_permutation
    return result_permutation

def multiply_permutations(left_permutation, right_permutation):
    """
    Multiplie deux permutations : left . right^{-1}
    """
    return multiply_permutation_by_inverse(left_permutation, compute_inverse_permutation(right_permutation))

def compute_permutation_power(permutation, exponent):
    """
    Calcule la puissance d'une permutation.
    """
    if exponent == 0:
        return np.arange(len(permutation))
    half_power = compute_permutation_power(permutation, exponent // 2)
    squared_power = multiply_permutations(half_power, half_power)
    if exponent % 2:
        return multiply_permutations(permutation, squared_power)
    else:
        return squared_power

# Générer la séquence périodique de permutations
periodic_permutation_sequence = [permutation_P, permutation_Q]
for index in range(4):
    next_permutation = multiply_permutation_by_inverse(
        periodic_permutation_sequence[-1],
        periodic_permutation_sequence[-2]
    )
    periodic_permutation_sequence.append(next_permutation)

quotient_of_iterations, remainder_of_iterations = divmod(number_of_iterations - 1, 6)

# Conjugaison spécifique sur les permutations
qpq_p = multiply_permutations(
    multiply_permutation_by_inverse(
        multiply_permutation_by_inverse(permutation_Q, permutation_P),
        permutation_Q
    ),
    permutation_P
)

left_conjugation_power = compute_permutation_power(qpq_p, quotient_of_iterations)
inverse_left_conjugation_power = compute_inverse_permutation(left_conjugation_power)
core_result_permutation = multiply_permutations(
    multiply_permutations(left_conjugation_power, periodic_permutation_sequence[remainder_of_iterations]),
    inverse_left_conjugation_power
) + 1

# Afficher le résultat en base 1
print(' '.join(core_result_permutation.astype(str)))