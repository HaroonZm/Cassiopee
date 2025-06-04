from bisect import bisect_left, bisect_right
from itertools import accumulate

def find_minimum_valid_index():
    number_of_elements, target_sum_limit = map(int, input().split())
    list_of_elements = list(map(int, input().split()))

    list_of_elements.sort()

    index_of_first_gte_target = bisect_left(list_of_elements, target_sum_limit)
    elements_below_target = list_of_elements[:index_of_first_gte_target]
    count_below_target = len(elements_below_target)

    possible_sums_prefix = [1 << (target_sum_limit - 1)]
    current_bitset_prefix = 1 << (target_sum_limit - 1)
    for element in elements_below_target:
        current_bitset_prefix |= current_bitset_prefix >> element
        possible_sums_prefix.append(current_bitset_prefix)

    possible_sums_suffix = [1 << (target_sum_limit - 1)]
    current_bitset_suffix = 1 << (target_sum_limit - 1)
    for element in reversed(elements_below_target):
        current_bitset_suffix |= current_bitset_suffix >> element
        possible_sums_suffix.append(current_bitset_suffix)
    possible_sums_suffix.reverse()

    def satisfies_subset_sum_condition(index_to_ignore):
        element_to_ignore = elements_below_target[index_to_ignore]

        suffix_possible = [0] * target_sum_limit
        suffix_bitset = possible_sums_suffix[index_to_ignore + 1]
        for sum_value in range(target_sum_limit):
            if suffix_bitset & (1 << (target_sum_limit - 1 - sum_value)):
                suffix_possible[sum_value] = 1
        accumulated_suffix = list(accumulate([0] + suffix_possible))

        prefix_bitset = possible_sums_prefix[index_to_ignore]
        for sum_value in range(target_sum_limit):
            if prefix_bitset & (1 << (target_sum_limit - 1 - sum_value)):
                left_index = max(0, target_sum_limit - sum_value - element_to_ignore)
                right_index = target_sum_limit - sum_value
                if accumulated_suffix[right_index] - accumulated_suffix[left_index] > 0:
                    return True
        return False

    lower_bound = -1
    upper_bound = count_below_target

    while abs(upper_bound - lower_bound) > 1:
        midpoint = (lower_bound + upper_bound) // 2
        if satisfies_subset_sum_condition(midpoint):
            upper_bound = midpoint
        else:
            lower_bound = midpoint

    print(upper_bound)

find_minimum_valid_index()