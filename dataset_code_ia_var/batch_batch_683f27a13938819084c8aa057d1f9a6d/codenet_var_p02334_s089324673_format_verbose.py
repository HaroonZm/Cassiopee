total_number_of_items, number_of_selections = map(int, input().split())
modulus = 10 ** 9 + 7

numerator_product = 1
denominator_product = 1

for current_index in range(total_number_of_items):
    numerator_product = (numerator_product * (total_number_of_items + number_of_selections - 1 - current_index)) % modulus
    denominator_product = (denominator_product * (current_index + 1)) % modulus

modular_inverse_of_denominator = pow(denominator_product, modulus - 2, modulus)

result = (numerator_product * modular_inverse_of_denominator) % modulus

print(result)