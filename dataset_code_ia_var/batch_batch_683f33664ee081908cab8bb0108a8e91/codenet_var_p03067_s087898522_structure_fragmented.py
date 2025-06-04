def read_input():
    return input().split()

def convert_to_ints(str_list):
    return [int(x) for x in str_list]

def assign_values(int_list):
    return int_list[0], int_list[1], int_list[2]

def make_list(a, b, c):
    return [a, b, c]

def sort_list(lst):
    return sorted(lst)

def get_middle_value(sorted_lst):
    return sorted_lst[1]

def compare_values(val1, val2):
    return val1 == val2

def print_yes():
    print("Yes")

def print_no():
    print("No")

def main():
    str_values = read_input()
    int_values = convert_to_ints(str_values)
    A, B, C = assign_values(int_values)
    values_list = make_list(A, B, C)
    sorted_values = sort_list(values_list)
    middle_value = get_middle_value(sorted_values)
    is_equal = compare_values(middle_value, C)
    if is_equal:
        print_yes()
    else:
        print_no()

main()