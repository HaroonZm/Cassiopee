number_of_elements, sequence_length = map(int, input().split(" "))

product_of_numerator_terms = 1

for current_term in range(sequence_length, number_of_elements + sequence_length):
    product_of_numerator_terms *= current_term

for divisor in range(1, number_of_elements + 1):
    product_of_numerator_terms //= divisor

modulus = 10 ** 9 + 7

result = product_of_numerator_terms % modulus

print(result)