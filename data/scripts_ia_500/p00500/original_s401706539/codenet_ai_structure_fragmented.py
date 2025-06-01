def initialize_lists(size):
    return [0]*size, [0]*size, [0]*size

def has_value(value):
    return value != 0

def get_element(lst, index):
    return lst[index]

def set_elements_to_zero(lst, index1, index2):
    lst[index1] = 0
    lst[index2] = 0

def check_list(lst, n):
    for i in iterate_indices(n-1):
        if not has_value(get_element(lst, i)):
            continue
        t = get_element(lst, i)
        check_inner_loop(lst, i, n, t)

def iterate_indices(limit):
    for idx in range(limit):
        yield idx

def check_inner_loop(lst, i, n, t):
    for j in iterate_inner_indices(i+1, n):
        if t == get_element(lst, j):
            set_elements_to_zero(lst, i, j)

def iterate_inner_indices(start, end):
    for idx in range(start, end):
        yield idx

def read_n():
    return int(input())

def read_line():
    return map(int, input().split())

def assign_values(a, b, c, index, values):
    a[index], b[index], c[index] = values

def print_sum_elements(a, b, c, index):
    print(a[index] + b[index] + c[index])

def main():
    size = 200
    a, b, c = initialize_lists(size)
    n = read_n()
    for i in iterate_indices(n):
        values = read_line()
        assign_values(a, b, c, i, values)
    check_list(a, n)
    check_list(b, n)
    check_list(c, n)
    for i in iterate_indices(n):
        print_sum_elements(a, b, c, i)

if __name__ == '__main__':
    main()