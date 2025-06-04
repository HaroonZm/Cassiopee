import math

def read_input():
    raw_data = input()
    return raw_data

def split_input(raw_data):
    return raw_data.split()

def convert_to_int(str_list):
    return list(map(int, str_list))

def unpack_values(int_list):
    x = int_list[0]
    y = int_list[1]
    return x, y

def compute_gcd(a, b):
    return math.gcd(a, b)

def sum_values(a, b):
    return a + b

def subtract_gcd(value, gcd_value):
    return value - gcd_value

def add_one(value):
    return value + 1

def main():
    raw_data = read_input()
    split_data = split_input(raw_data)
    int_values = convert_to_int(split_data)
    x, y = unpack_values(int_values)
    values_sum = sum_values(x, y)
    gcd_value = compute_gcd(x, y)
    subtracted = subtract_gcd(values_sum, gcd_value)
    result = add_one(subtracted)
    print(result)

main()