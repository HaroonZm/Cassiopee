def compute_extended_gcd(value_a, value_b):
    if value_b == 0:
        result_x = 1
        result_y = 0
        return value_a, result_x, result_y
    gcd, prev_x, prev_y = compute_extended_gcd(value_b, value_a % value_b)
    result_x = prev_y
    result_y = prev_x - (value_a // value_b) * prev_y
    return gcd, result_x, result_y

def solve_chinese_remainder(remainders_list, moduli_list):
    current_remainder = 0
    current_modulus = 1
    for index in range(len(remainders_list)):
        gcd, coef_p, coef_q = compute_extended_gcd(current_modulus, moduli_list[index])
        if (remainders_list[index] - current_remainder) % gcd != 0:
            return 0, -1
        temp_solution = ((remainders_list[index] - current_remainder) // gcd) * coef_p % (moduli_list[index] // gcd)
        current_remainder += current_modulus * temp_solution
        current_modulus *= moduli_list[index] // gcd
    return current_remainder, current_modulus

input_n, input_m, input_d = [int(input_value) for input_value in input().split()]
moduli_array = [int(input_value) for input_value in input().split()]
remainders_matrix = [[int(input_value) for input_value in input().split()] for _ in range(input_d)]
for row_index in range(input_d):
    restricted_moduli = []
    restricted_remainders = []
    for column_index in range(input_m):
        if remainders_matrix[row_index][column_index] > -1:
            restricted_moduli.append(moduli_array[column_index])
            restricted_remainders.append(remainders_matrix[row_index][column_index])
    solution_remainder, solution_modulus = solve_chinese_remainder(restricted_remainders, restricted_moduli)
    if solution_modulus < 0:
        print(-1)
        quit()
    solution_multiplier = (input_n - solution_remainder) // solution_modulus
    if solution_multiplier < 0:
        print(-1)
        quit()
    input_n = solution_modulus * solution_multiplier + solution_remainder
print(input_n)