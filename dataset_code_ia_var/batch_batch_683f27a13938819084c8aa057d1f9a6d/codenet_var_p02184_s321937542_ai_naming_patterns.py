from itertools import permutations as permute_digits, combinations as choose_halves

MODULO_BASE = 10**9 + 7

target_sum = int(input())
digit_indices = list(map(int, input()))

if len(digit_indices) == 1 and target_sum == 0:
    print(0)
    exit()

digit_position_values = [0] * 10
current_power_of_ten = 1
for digit in reversed(digit_indices):
    digit_position_values[digit] += current_power_of_ten
    current_power_of_ten = (current_power_of_ten * 10) % MODULO_BASE

for first_half_index_set in choose_halves(range(10), 5):
    first_half_indices = list(first_half_index_set)
    second_half_indices = list(set(range(10)) - set(first_half_indices))
    first_half_values = [digit_position_values[idx] for idx in first_half_indices]
    second_half_values = [digit_position_values[idx] for idx in second_half_indices]

    if digit_indices[0] in first_half_indices:
        first_half_permutations = [
            perm for perm in permute_digits(first_half_indices)
            if perm[digit_indices[0]] != 0
        ]
    else:
        first_half_permutations = list(permute_digits(first_half_indices))

    sum_to_perm_map = {}
    for perm in reversed(first_half_permutations):
        index_map = {idx: pos for pos, idx in enumerate(first_half_indices)}
        sum_value = sum(first_half_values[index_map[idx]] * idx for idx in first_half_indices)
        sum_to_perm_map[sum_value % MODULO_BASE] = perm

    for perm_second_half in permute_digits(second_half_indices):
        second_half_sum = sum(val * idx for val, idx in zip(second_half_values, perm_second_half))
        required_first_half_sum = (target_sum - second_half_sum) % MODULO_BASE
        if required_first_half_sum in sum_to_perm_map:
            full_perm = sum_to_perm_map[required_first_half_sum] + perm_second_half
            position_dict = {}
            for idx, digit in zip(first_half_indices + second_half_indices, full_perm):
                position_dict[idx] = digit
            if position_dict[digit_indices[0]] != 0:
                output_digits = [str(position_dict[idx]) for idx in digit_indices]
                print("".join(output_digits))
                exit()
print(-1)