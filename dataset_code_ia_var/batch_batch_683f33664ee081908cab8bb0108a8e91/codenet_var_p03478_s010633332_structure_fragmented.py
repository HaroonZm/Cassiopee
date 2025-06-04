def get_input():
    return input().split()

def to_int_list(str_list):
    return list(map(int, str_list))

def parse_input():
    values = get_input()
    return to_int_list(values)

def str_number(num):
    return str(num)

def split_digits(num_str):
    return list(num_str)

def digits_to_int(digit_list):
    return list(map(int, digit_list))

def sum_digits(num):
    num_str = str_number(num)
    digits = split_digits(num_str)
    digits_int = digits_to_int(digits)
    return sum(digits_int)

def within_bounds(value, lower, upper):
    return lower <= value <= upper

def process_number(i, A, B):
    digit_sum = sum_digits(i)
    if within_bounds(digit_sum, A, B):
        return i
    return 0

def compute_total(N, A, B):
    result = 0
    for i in range(N+1):
        result += process_number(i, A, B)
    return result

def print_result(result):
    print(result)

def main():
    N, A, B = parse_input()
    ans = compute_total(N, A, B)
    print_result(ans)

main()