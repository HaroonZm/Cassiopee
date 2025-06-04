def get_input():
    return input()

def convert_to_str(value):
    return str(value)

def replace_commas_with_space(s):
    return s.replace(',', ' ')

def print_output(result):
    print(result)

def process():
    user_input = get_input()
    string_value = convert_to_str(user_input)
    replaced_string = replace_commas_with_space(string_value)
    print_output(replaced_string)

process()