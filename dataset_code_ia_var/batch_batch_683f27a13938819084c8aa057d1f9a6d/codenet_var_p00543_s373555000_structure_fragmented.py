def get_input():
    return input()

def parse_n_and_m(line):
    n, m = map(int, line.split())
    return n, m

def read_single_value():
    return int(get_input())

def build_initial_list(n):
    lst = []
    for _ in range(n):
        lst.append(read_single_value())
    return lst

def modulo(val, mod):
    return val % mod

def swap_elements(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def should_swap(a, b, mod_val):
    return modulo(a, mod_val) > modulo(b, mod_val)

def bubble_sort_pass(arr, n, mod_val):
    for j in range(n - 1):
        if should_swap(arr[j], arr[j+1], mod_val):
            swap_elements(arr, j, j+1)

def perform_all_passes(arr, n, m):
    for i in range(m):
        mod_val = i + 1
        bubble_sort_pass(arr, n, mod_val)

def print_element(val):
    print(val)

def print_all_elements(arr):
    for val in arr:
        print_element(val)

def main():
    first_line = get_input()
    n, m = parse_n_and_m(first_line)
    arr = build_initial_list(n)
    perform_all_passes(arr, n, m)
    print_all_elements(arr)

main()