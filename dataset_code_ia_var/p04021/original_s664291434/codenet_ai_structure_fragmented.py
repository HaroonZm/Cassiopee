def get_input_n():
    return int(input())

def get_single_input():
    return int(input())

def build_input_list(n):
    return [get_single_input() for _ in range(n)]

def sort_list(lst):
    return sorted(lst)

def is_odd_index(idx):
    return idx % 2 == 1

def filter_by_odd_indices(lst):
    return [value for idx, value in enumerate(lst) if is_odd_index(idx)]

def to_set(lst):
    return set(lst)

def compute_difference_len(set1, set2):
    return len(set1.difference(set2))

def main():
    n = get_input_n()
    input_list = build_input_list(n)
    sorted_list = sort_list(input_list)
    odd_index_values = filter_by_odd_indices(input_list)
    odd_index_sorted_values = filter_by_odd_indices(sorted_list)
    set_odd_indices = to_set(odd_index_values)
    set_odd_indices_sorted = to_set(odd_index_sorted_values)
    diff_len = compute_difference_len(set_odd_indices, set_odd_indices_sorted)
    print(diff_len)

main()