def read_input():
    return input()

def split_input(input_str):
    return input_str.split()

def map_to_int(str_list):
    return list(map(int, str_list))

def unpack_values(int_list):
    A = int_list[0]
    B = int_list[1]
    return A, B

def calculate_value(A, B):
    return A - 2 * B

def apply_max_constraint(val):
    return max(0, val)

def print_result(result):
    print(result)

def main():
    input_str = read_input()
    str_list = split_input(input_str)
    int_list = map_to_int(str_list)
    A, B = unpack_values(int_list)
    value = calculate_value(A, B)
    final_result = apply_max_constraint(value)
    print_result(final_result)

main()