import sys

# Augmente la limite de récursion pour éviter les erreurs lors de calculs lourds
sys.setrecursionlimit(10**7)

class CombinationCalculatorUsingFermatLittleTheorem:
    def __init__(self, maximum_n_value, modulus):
        self.maximum_n_value = maximum_n_value
        self.modulus = modulus

        self.factorials_modulo = [1]
        self.inverse_factorials_modulo = [1]
        current_factorial = 1

        # Pré-calcul des factorielles modulo 'modulus' et de leurs inverses grâce au petit théorème de Fermat
        for current_integer in range(1, self.maximum_n_value + 1):
            current_factorial = (current_factorial * current_integer) % self.modulus
            self.factorials_modulo.append(current_factorial)
            inverse_factorial = pow(current_factorial, self.modulus - 2, self.modulus)
            self.inverse_factorials_modulo.append(inverse_factorial)

    def compute_binomial_coefficient(self, total_elements, elements_chosen):
        if total_elements < elements_chosen:
            return 0
        return (
            self.factorials_modulo[total_elements]
            * self.inverse_factorials_modulo[elements_chosen]
            * self.inverse_factorials_modulo[total_elements - elements_chosen]
        ) % self.modulus

maximum_combination_size = 1000
prime_modulus = 10**9 + 7

combination_calculator = CombinationCalculatorUsingFermatLittleTheorem(
    maximum_combination_size,
    prime_modulus
)

input_line = input()
number_of_elements_to_choose, total_number_of_elements = map(int, input_line.split())

binomial_coefficient_result = combination_calculator.compute_binomial_coefficient(
    total_number_of_elements,
    number_of_elements_to_choose
)

print(binomial_coefficient_result)