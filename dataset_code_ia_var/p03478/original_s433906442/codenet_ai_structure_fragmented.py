def read_input():
    return input().split()

def parse_values(values):
    return tuple(map(int, values))

def int_to_str(x):
    return str(x)

def str_to_list(s):
    return list(s)

def list_map_int(lst):
    return list(map(int, lst))

def sum_digits(x):
    s = int_to_str(x)
    l = str_to_list(s)
    digits = list_map_int(l)
    return sum(digits)

def check_in_range(val, low, high):
    return low <= val <= high

def add_if_valid(total, i, a, b):
    digit_sum = sum_digits(i)
    if check_in_range(digit_sum, a, b):
        return total + i
    return total

def loop_range(start, end, a, b):
    ans = 0
    for i in range(start, end+1):
        ans = add_if_valid(ans, i, a, b)
    return ans

def print_result(result):
    print(result)

def main():
    raw_input = read_input()
    n, a, b = parse_values(raw_input)
    result = loop_range(1, n, a, b)
    print_result(result)

main()