def get_input():
    return input()

def to_str(n):
    return str(n)

def to_char_list(s):
    return list(s)

def char_to_int_list(lst):
    return list(map(int, lst))

def sum_list(lst):
    return sum(lst)

def digit_sum(n):
    s = to_str(n)
    char_lst = to_char_list(s)
    int_lst = char_to_int_list(char_lst)
    total = sum_list(int_lst)
    return total

def is_divisible_by_9(num):
    return digit_sum(num) % 9 == 0

def print_result(is_div_9):
    if is_div_9:
        print("Yes")
    else:
        print("No")

def main():
    num = get_input()
    result = is_divisible_by_9(num)
    print_result(result)

main()