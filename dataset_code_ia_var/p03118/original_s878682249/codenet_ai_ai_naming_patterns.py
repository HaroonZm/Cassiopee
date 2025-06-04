from copy import deepcopy

input_length = int(input())
input_sequence = input()
dp_state_matrix = [[[[0]*2 for _ in range(2)] for _ in range(2)] for _ in range(input_length)]
modulus = 10**9 + 7

for index_i in range(input_length):
    for index_j in range(2):
        for index_k in range(2):
            for index_l in range(2):
                dp_state_matrix[index_i][index_j][index_k][index_l] = [[], [], 0]

if input_sequence[0] == 'X':
    dp_state_matrix[0][0][1][0] = [[], [], 1]
else:
    dp_state_matrix[0][0][0][1] = [[], [], 1]
    dp_state_matrix[0][1][1][1] = [[1], [], modulus - 1]

factorials_list = [1, 1]
inverse_factorials_list = [1, 1]
inverse_list = [0, 1]
combinatorics_list = [1, 2]
for index_i in range(2, input_length + 5):
    factorials_list.append((factorials_list[-1] * index_i) % modulus)
    inverse_list.append((-inverse_list[modulus % index_i] * (modulus // index_i)) % modulus)
    inverse_factorials_list.append((inverse_factorials_list[-1] * inverse_list[-1]) % modulus)
    combinatorics_list.append((combinatorics_list[-1] + inverse_factorials_list[index_i]) % modulus)

def polynomial_addition(polynomial_x, polynomial_y):
    for parity_index in range(2):
        required_length = len(polynomial_y[parity_index]) - len(polynomial_x[parity_index])
        for _ in range(required_length):
            polynomial_x[parity_index].append(0)
        for element_index in range(len(polynomial_y[parity_index])):
            polynomial_x[parity_index][element_index] = (polynomial_x[parity_index][element_index] + polynomial_y[parity_index][element_index]) % modulus
    polynomial_x[2] = (polynomial_x[2] + polynomial_y[2]) % modulus

def polynomial_integrate(polynomial_p):
    polynomial_p[2] = -polynomial_p[2] % modulus
    for parity_index in range(2):
        polynomial_p[parity_index].append(0)
        for element_index in range(len(polynomial_p[parity_index]) - 2, -1, -1):
            polynomial_p[parity_index][element_index + 1] = polynomial_p[parity_index][element_index] * inverse_list[element_index + 1] % modulus
            polynomial_p[parity_index][element_index] = 0

def apply_fx0_transformation(polynomial_p):
    polynomial_integrate(polynomial_p)
    polynomial_p[0][0] = (polynomial_p[0][0] - polynomial_p[2]) % modulus

def apply_f1x_transformation(polynomial_p):
    polynomial_integrate(polynomial_p)
    for parity_index in range(2):
        for element_index in range(len(polynomial_p[parity_index])):
            polynomial_p[parity_index][element_index] = -polynomial_p[parity_index][element_index] % modulus
    polynomial_p[2] = -polynomial_p[2] % modulus
    for parity_type in range(2):
        polynomial_p[parity_type][0] = -sum(polynomial_p[parity_type]) % modulus
    polynomial_p[1][0] = (polynomial_p[1][0] - polynomial_p[2]) % modulus

for state_index in range(input_length - 1):
    if input_sequence[state_index + 1] == 'X':
        polynomial_addition(dp_state_matrix[state_index][1][1][0], dp_state_matrix[state_index][1][1][1])
        apply_fx0_transformation(dp_state_matrix[state_index][1][1][0])
        polynomial_addition(dp_state_matrix[state_index][1][1][1], dp_state_matrix[state_index][1][0][1])
        polynomial_addition(dp_state_matrix[state_index][1][1][1], dp_state_matrix[state_index][0][1][1])
        polynomial_addition(dp_state_matrix[state_index][1][1][1], dp_state_matrix[state_index][0][0][1])
        apply_f1x_transformation(dp_state_matrix[state_index][1][1][1])
        for connect_index in range(2):
            polynomial_addition(dp_state_matrix[state_index + 1][0][1][0], dp_state_matrix[state_index][1][1][connect_index])
    else:
        temp_polynomial = [[], [], 0]
        polynomial_addition(dp_state_matrix[state_index][0][1][0], dp_state_matrix[state_index][0][1][1])
        polynomial_addition(dp_state_matrix[state_index][1][1][0], dp_state_matrix[state_index][1][1][1])
        polynomial_addition(dp_state_matrix[state_index + 1][1][1][1], dp_state_matrix[state_index][0][1][0])
        apply_fx0_transformation(dp_state_matrix[state_index + 1][1][1][1])
        polynomial_addition(temp_polynomial, dp_state_matrix[state_index][0][1][0])
        polynomial_addition(temp_polynomial, dp_state_matrix[state_index][1][1][0])
        apply_f1x_transformation(temp_polynomial)
        apply_fx0_transformation(dp_state_matrix[state_index][1][1][0])
        polynomial_addition(dp_state_matrix[state_index + 1][0][0][1], dp_state_matrix[state_index][1][1][0])
        polynomial_addition(dp_state_matrix[state_index + 1][0][0][1], temp_polynomial)

def calculate_final_polynomial(polynomial_p, sign_offset, multiplier_value):
    result_list = [0] * 3
    temp_polynomial_q = deepcopy(polynomial_p)
    polynomial_integrate(temp_polynomial_q)
    result_list[0] = (sum(temp_polynomial_q[0]) - temp_polynomial_q[2]) * sign_offset % modulus
    result_list[1] = (sum(temp_polynomial_q[1]) + temp_polynomial_q[2]) * sign_offset % modulus
    for parity_index in range(2):
        for degree_index in range(len(polynomial_p[parity_index])):
            result_list[parity_index] = (result_list[parity_index] + polynomial_p[parity_index][degree_index] * factorials_list[degree_index] * multiplier_value) % modulus
            result_list[parity_index + 1] = (result_list[parity_index + 1] - polynomial_p[parity_index][degree_index] * factorials_list[degree_index] * combinatorics_list[degree_index] * multiplier_value) % modulus
    result_list[0] = (result_list[0] + polynomial_p[2] * inverse_list[2] * multiplier_value) % modulus
    result_list[2] = (result_list[2] - polynomial_p[2] * inverse_list[2] * multiplier_value) % modulus
    return result_list

polynomial_addition(dp_state_matrix[-1][0][1][1], dp_state_matrix[-1][1][1][1])
polynomial_addition(dp_state_matrix[-1][0][1][0], dp_state_matrix[-1][1][1][0])
polynomial_addition(dp_state_matrix[-1][0][0][1], dp_state_matrix[-1][1][0][1])

final_polynomial_list = [
    calculate_final_polynomial(dp_state_matrix[-1][0][1][1], 1, 0),
    calculate_final_polynomial(dp_state_matrix[-1][0][1][0], 0, 1),
    calculate_final_polynomial(dp_state_matrix[-1][0][0][1], 1, modulus - 1)
]
final_output_list = [sum(map(lambda sublist: sublist[result_index], final_polynomial_list)) % modulus for result_index in range(3)]

print(*final_output_list)