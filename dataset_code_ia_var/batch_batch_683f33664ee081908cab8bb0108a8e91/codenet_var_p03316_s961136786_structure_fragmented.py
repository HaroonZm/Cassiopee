def get_input():
    return input()

def convert_input_to_int(s):
    return int(s)

def int_to_str(n):
    return str(n)

def str_to_list(s):
    return list(s)

def char_list_to_int_list(char_list):
    return list(map(int, char_list))

def sum_of_list(lst):
    return sum(lst)

def is_divisible(n, divisor):
    return n % divisor == 0

def print_yes():
    print("Yes")

def print_no():
    print("No")

def decide_and_print(n, divisor):
    if is_divisible(n, divisor):
        print_yes()
    else:
        print_no()

def main():
    s = get_input()
    n = convert_input_to_int(s)
    a = int_to_str(n)
    char_list = str_to_list(a)
    int_list = char_list_to_int_list(char_list)
    b = sum_of_list(int_list)
    decide_and_print(n, b)

main()