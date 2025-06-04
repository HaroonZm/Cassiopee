def get_input():
    return input()

def split_input(s):
    return s.split()

def convert_to_int_list(str_list):
    return list(map(int, str_list))

def extract_first(values):
    return values[0]

def extract_second(values):
    return values[1]

def multiply(a, b):
    return a * b

def print_result(result):
    print(result)

def main():
    raw_input = get_input()
    split_values = split_input(raw_input)
    int_values = convert_to_int_list(split_values)
    a = extract_first(int_values)
    b = extract_second(int_values)
    product = multiply(a, b)
    print_result(product)

main()