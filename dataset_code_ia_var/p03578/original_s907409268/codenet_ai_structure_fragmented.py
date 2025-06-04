def get_input_number():
    return int(input())

def get_input_list():
    return list(map(int, input().split()))

def sort_list(lst):
    return sorted(lst)

def read_and_sort_list():
    return sort_list(get_input_list())

def init_j():
    return -1

def get_next_value(lst, idx):
    return lst[idx]

def check_index_in_range(idx, length):
    return idx < length

def check_value_equals(a, b):
    return a == b

def move_to_next_idx(idx):
    return idx + 1

def print_no_and_exit():
    print('NO')
    exit()

def print_yes():
    print('YES')

def iterate_t_and_check(D, N, T):
    j = init_j()
    for i in T:
        j = move_to_next_idx(j)
        while check_index_in_range(j, N) and not check_value_equals(D[j], i):
            j = move_to_next_idx(j)
        if not check_index_in_range(j, N):
            print_no_and_exit()
    print_yes()

def main():
    N = get_input_number()
    D = read_and_sort_list()
    M = get_input_number()
    T = read_and_sort_list()
    iterate_t_and_check(D, N, T)

main()