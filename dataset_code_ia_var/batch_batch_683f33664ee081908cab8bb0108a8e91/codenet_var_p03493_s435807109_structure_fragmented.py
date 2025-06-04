def get_input():
    return input()

def convert_input_to_list(user_input):
    return list(user_input)

def count_ones_in_list(char_list):
    return char_list.count("1")

def print_result(count):
    print(count)

def main():
    user_input = get_input()
    char_list = convert_input_to_list(user_input)
    ones_count = count_ones_in_list(char_list)
    print_result(ones_count)

main()