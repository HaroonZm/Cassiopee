def integer_log2(number):
    if number <= 0:
        return 0
    else:
        return number.bit_length() - 1

def pack_integers_into_single_value(integer_list, shift_amount):
    current_list_size = len(integer_list)
    
    while current_list_size > 1:
        packed_list = []
        for index in range(0, current_list_size - 1, 2):
            left_value = integer_list[index]
            right_value = integer_list[index + 1]
            packed_list.append(left_value | (right_value << shift_amount))
        
        if current_list_size & 1:
            packed_list.append(integer_list[-1])
        
        integer_list = packed_list
        current_list_size = (current_list_size + 1) >> 1
        shift_amount = shift_amount << 1
    
    return integer_list[0]

def unpack_single_value_packed_to_list(single_value, output_list_size, initial_shift_amount):
    temp_size = output_list_size
    size_history = []
    while temp_size > 1:
        size_history.append(temp_size)
        temp_size = (temp_size + 1) >> 1
    
    unpacked_list = [single_value]
    
    for size_at_step in size_history[::-1]:
        bitmask = (1 << initial_shift_amount) - 1
        next_unpacked = []
        for value in unpacked_list:
            next_unpacked.append(value & bitmask)
            next_unpacked.append(value >> initial_shift_amount)
        unpacked_list = next_unpacked[:size_at_step]
        initial_shift_amount = initial_shift_amount >> 1
    
    return unpacked_list

def polynomial_multiply_modulo(polynomial_f, polynomial_g, modulo):
    minimum_size = min(len(polynomial_f), len(polynomial_g))
    bit_shift_amount = ((modulo - 1) ** 2 * minimum_size).bit_length()
    result_size = len(polynomial_f) + len(polynomial_g) - 1
    combined_value = pack_integers_into_single_value(polynomial_f, bit_shift_amount) * pack_integers_into_single_value(polynomial_g, bit_shift_amount)
    unpacked_result = unpack_single_value_packed_to_list(combined_value, result_size,
        bit_shift_amount * (1 << integer_log2(result_size - 1)))
    return [int(x % modulo) for x in unpacked_result]

modulus = 998244353
precomputed_size = 10 ** 4 + 10

def modular_inverse(number):
    return pow(number, modulus - 2, modulus)

factorials = [1] * precomputed_size
inverse_factorials = [1] * precomputed_size
binomial_poly_coeff_current = 1
binomial_poly_coeffs = [1] * precomputed_size

for i in range(1, precomputed_size):
    factorials[i] = (factorials[i - 1] * i) % modulus
    inverse_factorials[i] = (inverse_factorials[i - 1] * modular_inverse(i)) % modulus
    binomial_poly_coeffs[i - 1] = inverse_factorials[i]

def polynomial_power_modulo(base_poly, exponent, max_length):
    result_poly = [1]
    current_poly = base_poly[:]
    while exponent:
        if exponent & 1:
            result_poly = polynomial_multiply_modulo(result_poly, current_poly, modulus)[:max_length]
        current_poly = polynomial_multiply_modulo(current_poly, current_poly, modulus)[:max_length]
        exponent >>= 1
    return result_poly

input_string_A = raw_input()
input_string_B = raw_input()
ones_in_A_count = 0
mismatched_ones_count = 0

for character_index in range(len(input_string_A)):
    if input_string_A[character_index] == '1':
        ones_in_A_count += 1
        if input_string_B[character_index] != '1':
            mismatched_ones_count += 1

final_result = 0
exponentiated_poly = polynomial_power_modulo(binomial_poly_coeffs, mismatched_ones_count, ones_in_A_count + 1)

for count_k in range(ones_in_A_count - mismatched_ones_count + 1):
    term_result = factorials[ones_in_A_count - mismatched_ones_count - count_k]
    term_result *= factorials[ones_in_A_count - mismatched_ones_count - count_k]
    term_result %= modulus
    
    if count_k < len(exponentiated_poly):
        term_result *= exponentiated_poly[count_k] * factorials[mismatched_ones_count]
    else:
        term_result = 0

    term_result *= factorials[ones_in_A_count - mismatched_ones_count]
    term_result *= factorials[ones_in_A_count]
    term_result *= inverse_factorials[ones_in_A_count - mismatched_ones_count - count_k]
    term_result *= inverse_factorials[ones_in_A_count - mismatched_ones_count - count_k]
    final_result += term_result

print final_result % modulus