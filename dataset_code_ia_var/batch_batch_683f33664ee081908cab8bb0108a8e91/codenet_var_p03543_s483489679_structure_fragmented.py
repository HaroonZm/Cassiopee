def get_input():
    return input()

def get_first_char(s):
    return s[0]

def get_second_char(s):
    return s[1]

def get_third_char(s):
    return s[2]

def get_fourth_char(s):
    return s[3]

def all_equal(a, b, c):
    return a == b and b == c

def first_three_equal(s):
    a = get_first_char(s)
    b = get_second_char(s)
    c = get_third_char(s)
    return all_equal(a, b, c)

def last_three_equal(s):
    b = get_second_char(s)
    c = get_third_char(s)
    d = get_fourth_char(s)
    return all_equal(b, c, d)

def should_print_yes(s):
    return first_three_equal(s) or last_three_equal(s)

def print_yes():
    print('Yes')

def print_no():
    print('No')

def main():
    n = get_input()
    if should_print_yes(n):
        print_yes()
    else:
        print_no()

main()