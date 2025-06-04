def input_single_int():
    return int(input())

def input_int_list():
    return list(map(int, input().split()))

# Exemple 1 :
# n_value = input_single_int()
# a_list = input_int_list()
# print(a_list.index(min(a_list)) + 1)

# Exemple 2 :
# n_value = input_single_int()
# a_set = set(input_int_list())
# print(len(a_set))

def binary_search_bound(sorted_list, target_value, is_right_bound):
    left_idx = 0
    right_idx = len(sorted_list) - 1
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if sorted_list[mid_idx] == target_value:
            return mid_idx if is_right_bound else mid_idx
        elif sorted_list[mid_idx] > target_value:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx + 1
    return right_idx if is_right_bound else left_idx

query_n, query_q = input_int_list()
element_list = input_int_list()
element_list.sort()
left_query_list, right_query_list = [], []

for _ in range(query_q):
    query_left, query_right = input_int_list()
    left_query_list.append(query_left)
    right_query_list.append(query_right)

for left_bound, right_bound in zip(left_query_list, right_query_list):
    left_idx = binary_search_bound(element_list, left_bound, False)
    right_idx = binary_search_bound(element_list, right_bound, True)
    print(right_idx - left_idx + 1)