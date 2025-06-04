def get_input():
    return input().split()

def parse_int_list(str_list):
    return [int(i) for i in str_list]

def get_n_and_m():
    return parse_int_list(get_input())

def get_int():
    return int(input())

def init_table(n):
    return [True] * n

def read_numbers(m):
    nums = []
    for _ in range(m):
        nums.append(get_int())
    return nums

def process_lis(lis, table):
    for i in reverse_list(lis):
        process_element(i, table)

def reverse_list(lst):
    return lst[::-1]

def print_if_true(index, table):
    if table[index]:
        print(index+1)

def process_element(i, table):
    index = i-1
    if table[index]:
        print(i)
    table[index] = False

def print_remaining_true(table):
    for i in range_table(table):
        print_if_true(i, table)

def range_table(table):
    return range(len(table))

def main():
    n, m = get_n_and_m()
    table = init_table(n)
    lis = read_numbers(m)
    process_lis(lis, table)
    print_remaining_true(table)

main()