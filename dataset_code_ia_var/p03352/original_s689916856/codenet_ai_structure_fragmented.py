import sys
import os

def get_input_function():
    return lambda: list(map(int, input().split()))

def redirect_input_if_local():
    if 'local' in os.environ:
        sys.stdin = open('./input.txt', 'r')

def initialize_array(size):
    return [0] * size

def set_one_for_index(a, idx):
    a[idx] = 1

def get_starting_value():
    return get_input_function()[0]()

def mark_power_indices(a, limit):
    for i in range(2, 1000):
        if i * i <= limit:
            mark_squares_and_powers(a, i, limit)
        else:
            break

def mark_squares_and_powers(a, i, limit):
    set_one_for_index(a, i * i)
    mark_higher_powers(a, i, limit)

def mark_higher_powers(a, i, limit):
    k = 3
    while pow_below_limit(i, k, limit):
        set_one_for_index(a, i ** k)
        k += 1

def pow_below_limit(i, k, limit):
    return i ** k <= limit

def find_and_print_max_marked(a, x):
    for i in range(x, 0, -1):
        if is_marked(a, i):
            print_value(i)
            break

def is_marked(a, i):
    return a[i] == 1

def print_value(val):
    print(val)

def main_solve():
    redirect_input_if_local()
    x = get_starting_value()
    size = 10001
    limit = 1000
    a = initialize_array(size)
    set_one_for_index(a, 1)
    mark_power_indices(a, limit)
    find_and_print_max_marked(a, x)

main_solve()