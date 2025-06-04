def read_input():
    return input().split()

def convert_to_ints(str_list):
    return list(map(int, str_list))

def generate_range(limit):
    return range(limit+1)

def int_to_str(n):
    return str(n)

def split_str_digits(s):
    return list(s)

def str_digits_to_int_list(str_digits):
    return list(map(int, str_digits))

def sum_digits(int_list):
    return sum(int_list)

def is_sum_in_range(s, low, high):
    return low <= s <= high

def add_to_total(total, value):
    return total + value

def main():
    input_values = read_input()
    N, A, B = convert_to_ints(input_values)
    ans = 0
    for i in generate_range(N):
        str_i = int_to_str(i)
        digits = split_str_digits(str_i)
        digit_ints = str_digits_to_int_list(digits)
        digit_sum = sum_digits(digit_ints)
        if is_sum_in_range(digit_sum, A, B):
            ans = add_to_total(ans, i)
    print(ans)

main()