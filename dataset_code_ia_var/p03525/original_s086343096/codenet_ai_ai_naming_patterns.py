import sys
from itertools import groupby

input_value_count = int(input())
input_value_list = list(map(int, input().split()))

def search_minimal_difference(current_list, current_index):
    global maximal_minimum_difference
    if current_index == input_value_count:
        minimal_difference = 100
        for i_index in range(0, input_value_count):
            for j_index in range(i_index + 1, input_value_count + 1):
                absolute_difference = abs(current_list[i_index] - current_list[j_index])
                normalized_difference = min(absolute_difference, 24 - absolute_difference)
                minimal_difference = min(normalized_difference, minimal_difference)
        maximal_minimum_difference = max(maximal_minimum_difference, minimal_difference)
    else:
        search_minimal_difference(current_list + [input_value_list[current_index]], current_index + 1)
        search_minimal_difference(current_list + [24 - input_value_list[current_index]], current_index + 1)

if input_value_count >= 24:
    print(0)
elif input_value_count >= 12:
    sorted_input_values = sorted(input_value_list)
    grouped_input_values = groupby(sorted_input_values)
    for unique_value, occurrences in grouped_input_values:
        occurrence_count = len(list(occurrences))
        if unique_value == 0:
            print(0)
            sys.exit()
        elif unique_value == 12:
            if occurrence_count > 1:
                print(0)
                sys.exit()
        else:
            if occurrence_count > 2:
                print(0)
                sys.exit()
    print(1)
else:
    maximal_minimum_difference = 0
    search_minimal_difference([0], 0)
    print(maximal_minimum_difference)