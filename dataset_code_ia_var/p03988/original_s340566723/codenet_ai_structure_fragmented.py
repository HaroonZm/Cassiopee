import numpy as np

def get_max(da):
    return max(da)

def get_min(da):
    return min(da)

def is_len_two(n):
    return n == 2

def is_special_case(da):
    return da == [1, 1]

def is_max_less_than_two(mx):
    return mx < 2

def is_n_less_equal_max(n, mx):
    return n <= mx

def initialize_array(mx):
    return np.zeros(mx + 1, dtype=int)

def count_occurrences(arr, da, n):
    for i in range(n):
        increment_array(arr, da[i])
    return arr

def increment_array(arr, ind):
    arr[ind] += 1

def is_max_odd(mx):
    return mx % 2 == 1

def get_half_ceil(mx):
    return (mx + 1) // 2

def get_half(mx):
    return mx // 2

def check_min_counts_odd(arr, mi):
    return arr[mi] <= 2

def check_min_equals_half_ceiled(mx, mi):
    return get_half_ceil(mx) == mi

def check_min_counts_even(arr, mi):
    return arr[mi] <= 1

def check_min_equals_half(mx, mi):
    return get_half(mx) == mi

def check_inner_counts(arr, mi, mx):
    for i in range(mi, mx):
        if not has_at_least_two(arr, i + 1):
            return False
    return True

def has_at_least_two(arr, idx):
    return arr[idx] >= 2

def checker(n, da):
    mx = get_max(da)
    mi = get_min(da)
    if is_len_two(n):
        return is_special_case(da)
    if is_max_less_than_two(mx) or is_n_less_equal_max(n, mx):
        return False
    arr = initialize_array(mx)
    arr = count_occurrences(arr, da, n)
    if is_max_odd(mx):
        if not (check_min_counts_odd(arr, mi) and check_min_equals_half_ceiled(mx, mi)):
            return False
    else:
        if not (check_min_counts_even(arr, mi) and check_min_equals_half(mx, mi)):
            return False
    if not check_inner_counts(arr, mi, mx):
        return False
    return True

def get_input():
    return input()

def parse_int(s):
    return int(s)

def parse_int_list(s):
    return list(map(int, s.split()))

def print_possible():
    print('Possible')

def print_impossible():
    print('Impossible')

def main():
    n = parse_int(get_input())
    da = parse_int_list(get_input())
    if checker(n, da):
        print_possible()
    else:
        print_impossible()
    return

if __name__ == "__main__":
    main()