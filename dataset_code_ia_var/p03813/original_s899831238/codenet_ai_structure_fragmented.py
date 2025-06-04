def get_user_input():
    return input()

def convert_to_int(value):
    return int(value)

def compare_with_1200(number):
    return 1200 > number

def get_string():
    return "AARBCC"

def get_start_index(condition):
    return int(condition)

def get_step():
    return 2

def get_substring(s, start, step):
    return s[start::step]

def print_result(result):
    print(result)

def main():
    user_input = get_user_input()
    number = convert_to_int(user_input)
    condition = compare_with_1200(number)
    s = get_string()
    start_index = get_start_index(condition)
    step = get_step()
    substring = get_substring(s, start_index, step)
    print_result(substring)

main()