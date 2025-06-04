number_of_elements, maximum_subset_size = map(int, input().split())

modulus = 10 ** 9 + 7

maximum_combinations = min(number_of_elements - 1, maximum_subset_size)

result_sum = 0

factorials_modulus = [1]
inverse_factorials_modulus = [1]

for index in range(number_of_elements):
    current_factorial = factorials_modulus[index] * (index + 1) % modulus
    factorials_modulus.append(current_factorial)
    current_inverse_factorial = pow(factorials_modulus[index + 1], modulus - 2, modulus)
    inverse_factorials_modulus.append(current_inverse_factorial)

def combination_modulo(n, r, modulus):
    if r < 0 or r > n:
        return 0
    return factorials_modulus[n] * inverse_factorials_modulus[r] * inverse_factorials_modulus[n - r] % modulus

for subset_size in range(maximum_combinations + 1):
    combinations_n_subset = combination_modulo(number_of_elements, subset_size, modulus)
    combinations_n_minus_1_subset = combination_modulo(number_of_elements - 1, subset_size, modulus)
    result_sum += combinations_n_subset * combinations_n_minus_1_subset % modulus

print(result_sum % modulus)