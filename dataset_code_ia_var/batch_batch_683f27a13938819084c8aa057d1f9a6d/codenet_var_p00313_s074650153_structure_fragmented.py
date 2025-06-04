def get_input_n():
    return int(input())

def get_input_list():
    return list(map(int, input().split()))

def remove_first_element(lst):
    del lst[0]
    return lst

def read_and_process_list():
    lst = get_input_list()
    return remove_first_element(lst)

def increment_index(idx):
    return idx + 1

def is_in_list(element, lst):
    return element in lst

def not_in_list(element, lst):
    return element not in lst

def condition_i_in_c(i, c):
    return is_in_list(i, c)

def condition_not_in_a(i, a):
    return not_in_list(i, a)

def condition_in_b(i, b):
    return is_in_list(i, b)

def evaluate_conditions(i, a, b, c):
    return condition_i_in_c(i, c) and (condition_not_in_a(i, a) or condition_in_b(i, b))

def update_count(count):
    return count + 1

def print_result(result):
    print(result)

def main():
    n = get_input_n()
    a = read_and_process_list()
    b = read_and_process_list()
    c = read_and_process_list()
    count = 0
    for idx in range(n):
        i = increment_index(idx)
        if evaluate_conditions(i, a, b, c):
            count = update_count(count)
    print_result(count)

main()