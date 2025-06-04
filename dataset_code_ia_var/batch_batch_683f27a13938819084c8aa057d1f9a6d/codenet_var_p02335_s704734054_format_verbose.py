from collections import defaultdict

class BinomialCoefficientPreprocessor:

    def __init__(self, maximum_n_value, field_prime_modulus):

        '''
        Preprocess to compute binomial coefficients (nCr) efficiently in the
        finite field Z/(field_prime_modulus)Z, for all 0 <= r <= n <= maximum_n_value.

        Args:
            maximum_n_value (int): Upper limit for n in combinations nCr.
            field_prime_modulus (int): Prime modulus for field Z/pZ (should be a prime).
        '''

        self.prime_modulus = field_prime_modulus

        self.factorial_modulo = {i: None for i in range(maximum_n_value + 1)}        # Stores i! mod prime_modulus for 0 <= i <= maximum_n_value
        self.modular_inverse = {i: None for i in range(1, maximum_n_value + 1)}      # Stores modular multiplicative inverse of i mod prime_modulus for 1 <= i <= maximum_n_value
        self.factorial_inverse_modulo = {i: None for i in range(maximum_n_value + 1)} # Stores (i!)^(-1) mod prime_modulus for 0 <= i <= maximum_n_value

        # Initialize base cases
        self.factorial_modulo[0] = 1
        self.factorial_modulo[1] = 1
        self.factorial_inverse_modulo[0] = 1
        self.factorial_inverse_modulo[1] = 1
        self.modular_inverse[1] = 1

        # Precompute all factorials, inverses, and factorial inverses up to maximum_n_value
        for current_value in range(2, maximum_n_value + 1):

            # Compute current_value! mod prime_modulus
            self.factorial_modulo[current_value] = (current_value * self.factorial_modulo[current_value - 1]) % self.prime_modulus

            quotient, remainder = divmod(self.prime_modulus, current_value)

            # Compute modular inverse of current_value using the formula:
            # inv[i] = - (prime_modulus // i) * inv[prime_modulus % i] mod prime_modulus
            self.modular_inverse[current_value] = (- (quotient % self.prime_modulus) * self.modular_inverse[remainder]) % self.prime_modulus

            # Compute the modular inverse of current_value! using its decomposition
            self.factorial_inverse_modulo[current_value] = (self.modular_inverse[current_value] * self.factorial_inverse_modulo[current_value - 1]) % self.prime_modulus

    def compute_permutation_modulo(self, n_value, r_value):
        '''
        Returns nPr modulo prime_modulus.
        '''
        if n_value < r_value or n_value < 0 or r_value < 0:
            return 0
        return (self.factorial_modulo[n_value] * self.factorial_inverse_modulo[n_value - r_value]) % self.prime_modulus

    def compute_binomial_coefficient_modulo(self, n_value, r_value):
        '''
        Returns nCr modulo prime_modulus.
        '''
        if n_value < r_value or n_value < 0 or r_value < 0:
            return 0
        return (self.factorial_modulo[n_value] *
                self.factorial_inverse_modulo[r_value] *
                self.factorial_inverse_modulo[n_value - r_value]) % self.prime_modulus

    def compute_multichoose_modulo(self, number_of_classes, object_count):
        '''
        Returns the number of multisets: (number_of_classes H object_count) = C(number_of_classes + object_count - 1, object_count) mod prime_modulus.
        '''
        if number_of_classes == 0 and object_count > 0:
            return 0
        if number_of_classes >= 0 and object_count == 0:
            return 1
        return self.compute_binomial_coefficient_modulo(number_of_classes + object_count - 1, object_count)

# Example usage:
number_to_choose, total_objects = map(int, input().split())
prime_modulus_for_field = 10 ** 9 + 7

binomial_coefficient_helper = BinomialCoefficientPreprocessor(total_objects, prime_modulus_for_field)

resulting_binomial_coefficient_modulo = binomial_coefficient_helper.compute_binomial_coefficient_modulo(total_objects, number_to_choose)

print(resulting_binomial_coefficient_modulo)