def get_input():
    return input()

def convert_to_list(s):
    return list(s)

def convert_str_list_to_int_list(lst):
    return list(map(int, lst))

def sum_digits(lst):
    total = 0
    for x in lst:
        total += x
    return total

def is_divisible_by_9(n):
    return (n % 9) == 0

def print_yes():
    print('Yes')

def print_no():
    print('No')

def main():
    inp = get_input()
    lst = convert_to_list(inp)
    int_lst = convert_str_list_to_int_list(lst)
    total = sum_digits(int_lst)
    if is_divisible_by_9(total):
        print_yes()
    else:
        print_no()

main()