def get_input():
    return input()

def get_length(s):
    return len(s)

def initialize_list():
    return []

def enumerate_string(s):
    return list(enumerate(s))

def is_W(char):
    return char == "W"

def append_index_if_W(enum_list, a_list):
    for i, s in enum_list:
        if is_W(s):
            append_to_list(a_list, i)
    return a_list

def append_to_list(lst, item):
    lst.append(item)

def get_n(a_list):
    return len(a_list) - 1

def calculate_sum(a_list):
    return sum(a_list)

def calculate_combination(n):
    return (n + 1) * n // 2

def calculate_result(a_sum, comb):
    return a_sum - comb

def print_result(result):
    print(result)

def main():
    S = get_input()
    N = get_length(S)
    A = initialize_list()
    enum_S = enumerate_string(S)
    A = append_index_if_W(enum_S, A)
    n = get_n(A)
    total = calculate_sum(A)
    comb = calculate_combination(n)
    res = calculate_result(total, comb)
    print_result(res)

main()