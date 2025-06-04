def read_input():
    return int(input())

def get_n():
    return 50

def get_initial_array_value(n):
    return n - 1

def initialize_array(n, value):
    return [value] * n

def compute_m(k, n):
    return k % n

def compute_base_add(k, n):
    return k // n

def should_increment_index(i, m):
    return i < m

def get_increment_value(n, m):
    return n - m + 1

def get_decrement_value(m):
    return -m

def update_array_element(a, i, base_add, m, n):
    if should_increment_index(i, m):
        a[i] += base_add + get_increment_value(n, m)
    else:
        a[i] += base_add + get_decrement_value(m)

def update_array(a, k, n, m):
    base_add = compute_base_add(k, n)
    for i in range(n):
        update_array_element(a, i, base_add, m, n)

def print_output(n, a):
    print(n)
    print(*a)

def main():
    k = read_input()
    n = get_n()
    initial_value = get_initial_array_value(n)
    a = initialize_array(n, initial_value)
    m = compute_m(k, n)
    update_array(a, k, n, m)
    print_output(n, a)

main()