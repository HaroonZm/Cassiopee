def read_input():
    return input()

def split_input(input_str):
    return input_str.split()

def convert_to_int(str_list):
    return [int(x) for x in str_list]

def extract_values(int_list):
    return int_list[0], int_list[1], int_list[2], int_list[3]

def calculate_result(N, A, B, C):
    return N - (A + B) + C

def display_result(result):
    print(result)

def main():
    input_str = read_input()
    str_list = split_input(input_str)
    int_list = convert_to_int(str_list)
    N, A, B, C = extract_values(int_list)
    result = calculate_result(N, A, B, C)
    display_result(result)

main()