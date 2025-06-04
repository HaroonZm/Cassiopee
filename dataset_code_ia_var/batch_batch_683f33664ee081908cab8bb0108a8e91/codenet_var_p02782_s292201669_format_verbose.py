MODULO_PRIME = 10 ** 9 + 7

row_start, column_start, row_end, column_end = map(int, input().split())

maximum_combination_index = (2 * 10 ** 6) + 2

from math import factorial

class PrecomputedFactorials:
    """
    Class to efficiently compute combinations and permutations modulo a prime.
    Factorials are precomputed and stored in a list for fast access.
    """
    def __init__(self, max_index=10**5, modulo=10**9 + 7):
        self.modulo = modulo
        self.max_index = max_index
        self.factorial_list = [1] * (self.max_index + 1)
        for current_index in range(1, self.max_index + 1):
            self.factorial_list[current_index] = (
                self.factorial_list[current_index - 1] * current_index
            ) % self.modulo

    def combination(self, n_value, k_value):
        """
        Calculate n choose k modulo specified modulus.
        """
        if n_value < 0 or k_value < 0 or n_value < k_value:
            return 0
        if n_value == 0 or k_value == 0:
            return 1
        numerator = self.factorial_list[n_value]
        denominator_k = self.factorial_list[k_value]
        denominator_n_minus_k = self.factorial_list[n_value - k_value]
        return (
            numerator
            * self.modular_inverse(denominator_k)
            * self.modular_inverse(denominator_n_minus_k)
        ) % self.modulo

    def permutation(self, n_value, k_value):
        """
        Calculate n permute k modulo specified modulus.
        """
        if n_value < 0 or k_value < 0 or n_value < k_value:
            return 0
        if n_value == 0 or k_value == 0:
            return 1
        numerator = self.factorial_list[n_value]
        denominator = self.factorial_list[n_value - k_value]
        return (numerator * self.modular_inverse(denominator)) % self.modulo

    def modular_inverse(self, number):
        """
        Compute the modular inverse using fast exponentiation.
        Fermat's little theorem: a^(-1) ≡ a^(p-2) mod p  
        """
        return self.fast_exponentiation(number, self.modulo - 2)

    def fast_exponentiation(self, base, exponent):
        """
        Compute (base ^ exponent) modulo given modulus using binary exponentiation.
        """
        if exponent == 0:
            return 1
        elif exponent % 2 == 0:
            half_power = self.fast_exponentiation(base, exponent // 2)
            return (half_power * half_power) % self.modulo
        else:
            previous_power = self.fast_exponentiation(base, exponent - 1)
            return (base * previous_power) % self.modulo

factorial_helper = PrecomputedFactorials(maximum_combination_index, MODULO_PRIME)

def rectangle_paths_combinations(sum_x, sum_y):
    """
    Count the number of ways to move from (0,0) to (sum_x, sum_y) moving only right and down.
    """
    return factorial_helper.combination(sum_x + sum_y, sum_y)

def rectangle_paths_combinations_offset(one_past_x, one_past_y):
    """
    Helper to count paths to cell (one_past_x, one_past_y) inclusive of edges.
    Used for inclusion-exclusion.
    """
    return rectangle_paths_combinations(one_past_x + 1, one_past_y + 1)

# Calculation using the inclusion-exclusion principle for the rectangle sum
total_paths_in_rectangle = (
    rectangle_paths_combinations_offset(row_end, column_end)
    - rectangle_paths_combinations_offset(row_end, column_start - 1)
    - rectangle_paths_combinations_offset(row_start - 1, column_end)
    + rectangle_paths_combinations_offset(row_start - 1, column_start - 1)
) % MODULO_PRIME

print(total_paths_in_rectangle)