from itertools import combinations as cmb
from collections import Counter as Cntr

def generate_sum_counters(subset_list, max_group_size):
    sum_counters_by_size = []
    for group_size in range(max_group_size + 1):
        group_sums = map(sum, cmb(subset_list, group_size))
        sum_counters_by_size.append(Cntr(group_sums))
    return sum_counters_by_size

def read_input():
    input_data = list(map(int, open(0).read().split()))
    n_items, max_selection, lower_limit, upper_limit = input_data[:5]
    items_list = input_data[5:]
    return n_items, max_selection, lower_limit, upper_limit, items_list

def count_valid_selections(n_total, selection_limit, lower_bound, upper_bound, values):
    mid_point = n_total // 2
    left_counters = generate_sum_counters(values[:mid_point], selection_limit)
    right_counters = generate_sum_counters(values[mid_point:], selection_limit)
    total_valid = 0
    for left_sel_count in range(selection_limit + 1):
        left_sum_counter = left_counters[left_sel_count]
        right_sum_counter = right_counters[selection_limit - left_sel_count]
        sorted_right_sums = sorted(right_sum_counter)
        left_ptr = right_ptr = len(sorted_right_sums)
        cumulative = 0
        for left_sum, left_count in sorted(left_sum_counter.items()):
            while right_ptr and left_sum + sorted_right_sums[right_ptr - 1] > upper_bound:
                right_ptr -= 1
                cumulative -= right_sum_counter[sorted_right_sums[right_ptr]]
            while left_ptr and left_sum + sorted_right_sums[left_ptr - 1] >= lower_bound:
                left_ptr -= 1
                cumulative += right_sum_counter[sorted_right_sums[left_ptr]]
            total_valid += left_count * cumulative
    return total_valid

if __name__ == "__main__":
    n_total, selection_limit, lower_bound, upper_bound, items = read_input()
    result = count_valid_selections(n_total, selection_limit, lower_bound, upper_bound, items)
    print(result)