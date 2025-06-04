input_number = int(input())
modulus_constant = 10**9 + 7
binary_string = bin(input_number)[2:]
binary_length = len(binary_string)
dp_table = [[0 for _ in range(2)] for _ in range(binary_length + 1)]
dp_table[0][0] = 1
dp_table[0][1] = 1

for position_index in range(binary_length):
    current_bit = int(binary_string[binary_length - position_index - 1])
    coeff_a, coeff_b, term_c = [(1, 0, 0), (1, 1, 0)][current_bit]
    coeff_d, coeff_e, term_f = [(1, 1, 1), (0, 1, 2)][current_bit]
    dp_table[position_index + 1][0] = (coeff_a * dp_table[position_index][0] + coeff_b * dp_table[position_index][1] + term_c * (3 ** position_index)) % modulus_constant
    dp_table[position_index + 1][1] = (coeff_d * dp_table[position_index][0] + coeff_e * dp_table[position_index][1] + term_f * (3 ** position_index)) % modulus_constant

print(dp_table[binary_length][0])