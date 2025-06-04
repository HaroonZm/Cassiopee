import sys

def get_input():
    return sys.stdin.readline

def get_read():
    return sys.stdin.read

def read_n(get_input_func):
    return int(get_input_func())

def parse_numbers(read_func):
    data = read_func()
    return data.split()

def to_int_list(str_list):
    return list(map(int, str_list))

def enumerate_list(lst):
    return enumerate(lst)

def build_tuple_list(enum):
    return [(value, index) for index, value in enum]

def sort_tuples(tuples):
    return sorted(tuples)

def compute_difference_index(sorted_list, n):
    differences = []
    for i in range(n):
        val = (sorted_list[i][1] - i) % 2
        differences.append(val)
    return differences

def sum_differences(diff_list):
    total = 0
    for val in diff_list:
        total += val
    return total

def compute_answer(total):
    return (total + 1) // 2

def print_answer(ans):
    print(ans)

def main():
    input_func = get_input()
    read_func = get_read()
    n = read_n(input_func)
    str_nums = parse_numbers(read_func)
    int_list = to_int_list(str_nums)
    enum = enumerate_list(int_list)
    tuple_list = build_tuple_list(enum)
    sorted_tuples = sort_tuples(tuple_list)
    differences = compute_difference_index(sorted_tuples, n)
    total = sum_differences(differences)
    ans = compute_answer(total)
    print_answer(ans)

main()