import sys
import bisect

def process_input():
    num_elements, target_count, lower_bound, upper_bound = map(int, sys.stdin.readline().split())
    element_values = tuple(map(int, sys.stdin.readline().split()))
    return num_elements, target_count, lower_bound, upper_bound, element_values

def generate_subset_sums(array, subset_size):
    subset_sums_by_count = [[] for _ in range(subset_size + 1)]
    for mask in range(1 << subset_size):
        bit_count = bin(mask).count('1')
        subset_sum = sum(array[index] for index in range(subset_size) if (mask >> index) & 1)
        subset_sums_by_count[bit_count].append(subset_sum)
    for count in range(subset_size + 1):
        subset_sums_by_count[count].sort()
    return subset_sums_by_count

def count_valid_combinations(total_count, target_selections, lower_limit, upper_limit, values):
    first_half_size = total_count // 2
    second_half_size = total_count - first_half_size
    first_half_values = values[:first_half_size]
    second_half_values = values[first_half_size:]

    first_half_sums_by_count = generate_subset_sums(first_half_values, first_half_size)
    total_valid_subsets = 0

    for mask in range(1 << second_half_size):
        second_half_selected_count = bin(mask).count('1')
        second_half_sum = sum(second_half_values[index] for index in range(second_half_size) if (mask >> index) & 1)
        for used_in_first_half in range(max(0, target_selections - second_half_selected_count), min(target_selections, first_half_size) + 1):
            if used_in_first_half + second_half_selected_count == target_selections:
                required_sum_lower = lower_limit - second_half_sum
                required_sum_upper = upper_limit - second_half_sum
                left = bisect.bisect_left(first_half_sums_by_count[used_in_first_half], required_sum_lower)
                right = bisect.bisect_right(first_half_sums_by_count[used_in_first_half], required_sum_upper)
                total_valid_subsets += (right - left)
    return total_valid_subsets

def main():
    total_count, target_selections, lower_limit, upper_limit, values = process_input()
    result = count_valid_combinations(total_count, target_selections, lower_limit, upper_limit, values)
    print(result)

if __name__ == '__main__':
    main()