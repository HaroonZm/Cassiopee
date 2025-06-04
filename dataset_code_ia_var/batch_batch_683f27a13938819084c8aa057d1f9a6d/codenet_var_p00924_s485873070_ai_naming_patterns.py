import copy

input_n, input_m = [int(value) for value in input().split()]

initial_list = [int(value) for value in input().split()]
pattern_lengths = [int(value) for value in input().split()]

def compute_minimum_swaps(target_pattern_type):
    swap_count = 0
    working_list = copy.deepcopy(initial_list)
    target_pattern = []
    for pattern_idx in range(input_m):
        bit_value = int(pattern_idx % 2 == target_pattern_type)
        target_pattern.extend([bit_value] * pattern_lengths[pattern_idx])
    for idx_main in range(input_n):
        if working_list[idx_main] != target_pattern[idx_main]:
            for idx_swap in range(idx_main, input_n):
                if target_pattern[idx_main] == working_list[idx_swap]:
                    swap_count += idx_swap - idx_main
                    working_list[idx_main], working_list[idx_swap] = working_list[idx_swap], working_list[idx_main]
                    break
            else:
                return 1000
    return swap_count

minimum_swaps = min(compute_minimum_swaps(0), compute_minimum_swaps(1))
print(minimum_swaps)