def read_input():
    line = get_input_line()
    return line

def get_input_line():
    return input()

def split_line(line):
    return line.split()

def map_to_ints(str_list):
    return list(map(convert_to_int, str_list))

def convert_to_int(s):
    return int(s)

def unpack_values(values):
    return values[0], values[1]

def multiply(a, b):
    return a * b

def print_result(result):
    print(result)

def main():
    line = read_input()
    split_values = split_line(line)
    int_values = map_to_ints(split_values)
    a, b = unpack_values(int_values)
    result = multiply(a, b)
    print_result(result)

main()