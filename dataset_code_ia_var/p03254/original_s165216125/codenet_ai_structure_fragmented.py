def read_input():
    return input().split()

def parse_ints(strs):
    return list(map(int, strs))

def get_n_and_x():
    vals = read_input()
    return parse_ints(vals)

def get_A():
    vals = read_input()
    return parse_ints(vals)

def sort_list(lst):
    return sorted(lst)

def get_prefix_sum(lst, end_index):
    return sum(lst[:end_index + 1])

def check_sum_exceeds(prefix_sum, x):
    return prefix_sum > x

def check_sum_equals(prefix_sum, x):
    return prefix_sum == x

def print_and_exit(val):
    print(val)
    exit()

def process(n, x, A):
    for i in range(n):
        prefix_sum = get_prefix_sum(A, i)
        if check_sum_exceeds(prefix_sum, x):
            print_and_exit(i)
        if check_sum_equals(prefix_sum, x):
            print_and_exit(i + 1)
    print(i)

def main():
    n_and_x = get_n_and_x()
    n = n_and_x[0]
    x = n_and_x[1]
    A = get_A()
    A = sort_list(A)
    process(n, x, A)

main()