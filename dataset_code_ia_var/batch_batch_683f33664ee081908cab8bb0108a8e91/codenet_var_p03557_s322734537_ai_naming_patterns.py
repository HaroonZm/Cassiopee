from bisect import bisect_left as search_left_position
from bisect import bisect_right as search_right_position

def read_integer():
    return int(input())

def read_sorted_integer_list():
    return sorted(list(map(int, input().split())))

element_count = read_integer()
list_a_sorted = read_sorted_integer_list()
list_b_sorted = read_sorted_integer_list()
list_c_sorted = read_sorted_integer_list()

combination_total = 0
for idx in range(element_count):
    count_less_a = search_left_position(list_a_sorted, list_b_sorted[idx])
    count_greater_c = element_count - search_right_position(list_c_sorted, list_b_sorted[idx])
    combination_total += count_less_a * count_greater_c

print(combination_total)