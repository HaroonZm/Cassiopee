total_elements, elements_to_choose = map(int, input().split())

modulo_base = 10 ** 9 + 7

if elements_to_choose < total_elements:
    print(0)

else:
    permutation_numerator = 1
    permutation_denominator = 1

    for current_index in range(total_elements):
        permutation_numerator = (
            permutation_numerator * (elements_to_choose - current_index)
        ) % modulo_base

        permutation_denominator = (
            permutation_denominator * (current_index + 1)
        ) % modulo_base

    modular_inverse_denominator = pow(
        permutation_denominator, modulo_base - 2, modulo_base
    )

    result = (permutation_numerator * modular_inverse_denominator) % modulo_base

    print(result)