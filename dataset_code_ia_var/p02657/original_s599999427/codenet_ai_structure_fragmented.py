def get_input():
    return input()

def split_input(user_input):
    return user_input.split()

def convert_to_int_list(str_list):
    return list(map(int, str_list))

def get_first_element(int_list):
    return int_list[0]

def get_second_element(int_list):
    return int_list[1]

def multiply_values(val1, val2):
    return val1 * val2

def display_result(result):
    print(result)

def main():
    user_input = get_input()
    split_values = split_input(user_input)
    int_values = convert_to_int_list(split_values)
    first = get_first_element(int_values)
    second = get_second_element(int_values)
    product = multiply_values(first, second)
    display_result(product)

main()