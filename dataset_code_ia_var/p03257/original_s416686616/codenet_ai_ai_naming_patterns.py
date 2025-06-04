import random
import math
import fractions

def compute_lcm(val_a, val_b):
    return (val_a // fractions.gcd(val_a, val_b)) * val_b

def check_prime(value):
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True

def generate_primes(limit_val):
    prime_list = []
    for candidate in range(2, limit_val + 1):
        if check_prime(candidate):
            prime_list.append(candidate)
    return prime_list

matrix_size = int(input())

matrix_elements = [[None for idx_col in range(matrix_size)] for idx_row in range(matrix_size)]

matrix_indices = [(row_idx, col_idx) for row_idx in range(matrix_size) for col_idx in range(matrix_size - 1, -1, -1)]

used_numbers = set()
prime_sequence = generate_primes(10 ** 4)

prime_offset = 0
while prime_sequence[prime_offset] < matrix_size + 3:
    prime_offset += 1

for tup_pos in matrix_indices:
    row_pos, col_pos = tup_pos
    if (row_pos + col_pos) % 2 == 0:
        sum_half = (row_pos + col_pos) // 2
        diff_half = matrix_size + (row_pos - col_pos) // 2
        calc_value = (sum_half + 1) * (prime_sequence[prime_offset + diff_half])
        if calc_value in used_numbers:
            print(101, calc_value)
            raise ValueError()
        matrix_elements[row_pos][col_pos] = calc_value
        used_numbers.add(calc_value)

for tup_pos in matrix_indices:
    row_pos, col_pos = tup_pos
    if (row_pos + col_pos) % 2 == 0:
        continue

    adjacent_lcm = 1
    for neighbor in [(row_pos - 1, col_pos), (row_pos + 1, col_pos), (row_pos, col_pos - 1), (row_pos, col_pos + 1)]:
        neigh_row, neigh_col = neighbor
        if 0 <= neigh_row < matrix_size and 0 <= neigh_col < matrix_size and matrix_elements[neigh_row][neigh_col] is not None:
            adjacent_lcm = compute_lcm(adjacent_lcm, matrix_elements[neigh_row][neigh_col])

    if adjacent_lcm >= 5 * 10 ** 14:
        print("ERR", adjacent_lcm)
        raise ValueError()

    candidate_result = adjacent_lcm + 1
    while candidate_result in used_numbers:
        multiplier = random.randint(1, (10 ** 15 - 1) // adjacent_lcm)
        candidate_result = multiplier * adjacent_lcm + 1

    matrix_elements[row_pos][col_pos] = candidate_result
    used_numbers.add(candidate_result)

for idx_row in range(matrix_size):
    print(" ".join(map(str, matrix_elements[idx_row])))