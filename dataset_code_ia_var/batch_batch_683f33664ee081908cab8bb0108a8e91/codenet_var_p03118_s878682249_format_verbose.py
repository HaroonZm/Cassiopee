from copy import deepcopy

number_of_characters = int(input())
character_sequence = input()

dynamic_programming_table = [
    [
        [
            [
                0 for x0_status in range(2)
            ] for consecutive_one_status in range(2)
        ] for one_status in range(2)
    ] for position in range(number_of_characters)
]

modulus = 10 ** 9 + 7

# Initialize each DP table cell as [[], [], 0]
for current_position in range(number_of_characters):
    for current_has_one in range(2):
        for current_consecutive_one in range(2):
            for current_has_x0 in range(2):
                dynamic_programming_table[current_position][current_has_one][current_consecutive_one][current_has_x0] = [[], [], 0]

if character_sequence[0] == 'X':
    dynamic_programming_table[0][0][1][0] = [[], [], 1]
else:
    dynamic_programming_table[0][0][0][1] = [[], [], 1]
    dynamic_programming_table[0][1][1][1] = [[1], [], modulus - 1]

factorial_list = [1, 1]
factorial_inverse_accumulate = [1, 1]
modular_inverse_list = [0, 1]
cumulative_factorial_inverse = [1, 2]

for index in range(2, number_of_characters + 5):
    factorial_list.append((factorial_list[-1] * index) % modulus)
    modular_inverse_list.append((-modular_inverse_list[modulus % index] * (modulus // index)) % modulus)
    factorial_inverse_accumulate.append((factorial_inverse_accumulate[-1] * modular_inverse_list[-1]) % modulus)
    cumulative_factorial_inverse.append((cumulative_factorial_inverse[-1] + factorial_inverse_accumulate[index]) % modulus)

def add_polynomials(target_polynomial_group, source_polynomial_group):
    for group_index in range(2):
        # Extend list if shorter
        for _ in range(len(source_polynomial_group[group_index]) - len(target_polynomial_group[group_index])):
            target_polynomial_group[group_index].append(0)
        for polynomial_index in range(len(source_polynomial_group[group_index])):
            target_polynomial_group[group_index][polynomial_index] = (
                target_polynomial_group[group_index][polynomial_index]
                + source_polynomial_group[group_index][polynomial_index]
            ) % modulus
    target_polynomial_group[2] = (target_polynomial_group[2] + source_polynomial_group[2]) % modulus

def integrate_polynomial(polynomial_group):
    polynomial_group[2] = (-polynomial_group[2]) % modulus
    for group_index in range(2):
        # Extend with one more polynomial degree
        polynomial_group[group_index].append(0)
        for degree_index in range(len(polynomial_group[group_index]) - 2, -1, -1):
            polynomial_group[group_index][degree_index + 1] = (
                polynomial_group[group_index][degree_index] * modular_inverse_list[degree_index + 1]
            ) % modulus
            polynomial_group[group_index][degree_index] = 0

def apply_fx0_transformation(polynomial_group):
    integrate_polynomial(polynomial_group)
    polynomial_group[0][0] = (polynomial_group[0][0] - polynomial_group[2]) % modulus

def apply_f1x_transformation(polynomial_group):
    integrate_polynomial(polynomial_group)
    for group_index in range(2):
        for coefficient_index in range(len(polynomial_group[group_index])):
            polynomial_group[group_index][coefficient_index] = -polynomial_group[group_index][coefficient_index] % modulus
    polynomial_group[2] = -polynomial_group[2] % modulus
    for group_index in range(2):
        polynomial_group[group_index][0] = -sum(polynomial_group[group_index]) % modulus
    polynomial_group[1][0] = (polynomial_group[1][0] - polynomial_group[2]) % modulus

for character_index in range(number_of_characters - 1):
    if character_sequence[character_index + 1] == 'X':
        add_polynomials(
            dynamic_programming_table[character_index][1][1][0],
            dynamic_programming_table[character_index][1][1][1]
        )
        apply_fx0_transformation(dynamic_programming_table[character_index][1][1][0])
        add_polynomials(
            dynamic_programming_table[character_index][1][1][1],
            dynamic_programming_table[character_index][1][0][1]
        )
        add_polynomials(
            dynamic_programming_table[character_index][1][1][1],
            dynamic_programming_table[character_index][0][1][1]
        )
        add_polynomials(
            dynamic_programming_table[character_index][1][1][1],
            dynamic_programming_table[character_index][0][0][1]
        )
        apply_f1x_transformation(dynamic_programming_table[character_index][1][1][1])
        for has_x0_flag in range(2):
            add_polynomials(
                dynamic_programming_table[character_index + 1][0][1][0],
                dynamic_programming_table[character_index][1][1][has_x0_flag]
            )
    else:
        temp_polynomial = [[], [], 0]
        add_polynomials(
            dynamic_programming_table[character_index][0][1][0],
            dynamic_programming_table[character_index][0][1][1]
        )
        add_polynomials(
            dynamic_programming_table[character_index][1][1][0],
            dynamic_programming_table[character_index][1][1][1]
        )
        add_polynomials(
            dynamic_programming_table[character_index + 1][1][1][1],
            dynamic_programming_table[character_index][0][1][0]
        )
        apply_fx0_transformation(dynamic_programming_table[character_index + 1][1][1][1])
        add_polynomials(temp_polynomial, dynamic_programming_table[character_index][0][1][0])
        add_polynomials(temp_polynomial, dynamic_programming_table[character_index][1][1][0])
        apply_f1x_transformation(temp_polynomial)
        apply_fx0_transformation(dynamic_programming_table[character_index][1][1][0])
        add_polynomials(
            dynamic_programming_table[character_index + 1][0][0][1],
            dynamic_programming_table[character_index][1][1][0]
        )
        add_polynomials(
            dynamic_programming_table[character_index + 1][0][0][1],
            temp_polynomial
        )

def evaluate_final_polynomial(polynomial_group, o_value, e_value):
    result_coefficients = [0] * 3
    duplicated_polynomial_group = deepcopy(polynomial_group)
    integrate_polynomial(duplicated_polynomial_group)
    result_coefficients[0] = (sum(duplicated_polynomial_group[0]) - duplicated_polynomial_group[2]) * o_value % modulus
    result_coefficients[1] = (sum(duplicated_polynomial_group[1]) + duplicated_polynomial_group[2]) * o_value % modulus
    for group_index in range(2):
        for coefficient_index in range(len(polynomial_group[group_index])):
            result_coefficients[group_index] = (
                result_coefficients[group_index]
                + polynomial_group[group_index][coefficient_index] * factorial_list[coefficient_index] * e_value
            ) % modulus
            result_coefficients[group_index + 1] = (
                result_coefficients[group_index + 1]
                - polynomial_group[group_index][coefficient_index] * factorial_list[coefficient_index] * cumulative_factorial_inverse[coefficient_index] * e_value
            ) % modulus
    result_coefficients[0] = (
        result_coefficients[0]
        + polynomial_group[2] * modular_inverse_list[2] * e_value
    ) % modulus
    result_coefficients[2] = (
        result_coefficients[2]
        - polynomial_group[2] * modular_inverse_list[2] * e_value
    ) % modulus
    return result_coefficients

add_polynomials(
    dynamic_programming_table[-1][0][1][1],
    dynamic_programming_table[-1][1][1][1]
)
add_polynomials(
    dynamic_programming_table[-1][0][1][0],
    dynamic_programming_table[-1][1][1][0]
)
add_polynomials(
    dynamic_programming_table[-1][0][0][1],
    dynamic_programming_table[-1][1][0][1]
)
result_polynomial_list = [
    evaluate_final_polynomial(dynamic_programming_table[-1][0][1][1], 1, 0),
    evaluate_final_polynomial(dynamic_programming_table[-1][0][1][0], 0, 1),
    evaluate_final_polynomial(dynamic_programming_table[-1][0][0][1], 1, modulus - 1)
]

final_result_coefficients = [
    sum(map(lambda result: result[coefficient_index], result_polynomial_list)) % modulus
    for coefficient_index in range(3)
]

print(*final_result_coefficients)