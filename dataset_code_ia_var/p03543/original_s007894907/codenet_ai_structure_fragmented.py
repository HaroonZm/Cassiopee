def get_input():
    return input()

def convert_to_list(s):
    return list(s)

def get_first_element(lst):
    return lst[0]

def get_second_element(lst):
    return lst[1]

def get_third_element(lst):
    return lst[2]

def get_fourth_element(lst):
    return lst[3]

def check_first_three_equal(a, b, c):
    return a == b and b == c

def check_last_three_equal(b, c, d):
    return b == c and c == d

def evaluate_condition(a):
    first = get_first_element(a)
    second = get_second_element(a)
    third = get_third_element(a)
    fourth = get_fourth_element(a)
    cond1 = check_first_three_equal(first, second, third)
    cond2 = check_last_three_equal(second, third, fourth)
    return cond1 or cond2

def print_result(result):
    if result:
        print('Yes')
    else:
        print('No')

def main():
    s = get_input()
    a = convert_to_list(s)
    result = evaluate_condition(a)
    print_result(result)

main()