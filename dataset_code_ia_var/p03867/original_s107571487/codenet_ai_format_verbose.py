import sys

def read_input_line():
    return sys.stdin.readline().rstrip()

sys.setrecursionlimit(max(1000, 10 ** 9))

def write_output_line(output_string):
    sys.stdout.write(output_string + "\n")

# Lire les valeurs de n et k depuis l'entrée
total_number, exponent_limit = map(int, read_input_line().split())

MODULO_CONSTANT = 10 ** 9 + 7

def list_all_divisors(number_to_divide):
    divisors_set = set()
    maximum_check = int(number_to_divide ** 0.5) + 2
    for candidate_divisor in range(1, maximum_check):
        if number_to_divide % candidate_divisor == 0:
            divisors_set.add(candidate_divisor)
            divisors_set.add(number_to_divide // candidate_divisor)
    sorted_divisors_list = sorted(divisors_set)
    return sorted_divisors_list

divisors_of_n = list_all_divisors(total_number)
total_divisor_count = len(divisors_of_n)

sequence_count_by_divisor = [None] * total_divisor_count

for index_current_divisor in range(total_divisor_count):
    current_divisor = divisors_of_n[index_current_divisor]
    sequence_count = pow(exponent_limit, (current_divisor + 1) // 2, MODULO_CONSTANT)
    for index_smaller_divisor in range(index_current_divisor):
        smaller_divisor = divisors_of_n[index_smaller_divisor]
        if current_divisor % smaller_divisor == 0:
            sequence_count -= sequence_count_by_divisor[index_smaller_divisor]
            sequence_count %= MODULO_CONSTANT
    sequence_count_by_divisor[index_current_divisor] = sequence_count % MODULO_CONSTANT

final_result_sum = 0
modular_inverse_of_2 = pow(2, MODULO_CONSTANT - 2, MODULO_CONSTANT)

for index_divisor, current_divisor in enumerate(divisors_of_n):
    current_sequence_count = sequence_count_by_divisor[index_divisor]
    if current_divisor % 2 == 0:
        final_result_sum += current_divisor * current_sequence_count * modular_inverse_of_2
    else:
        final_result_sum += current_divisor * current_sequence_count
    final_result_sum %= MODULO_CONSTANT

print(final_result_sum % MODULO_CONSTANT)