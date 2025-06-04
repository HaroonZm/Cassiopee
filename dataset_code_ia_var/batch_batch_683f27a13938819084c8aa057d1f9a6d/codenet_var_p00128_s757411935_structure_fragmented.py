import sys

def read_lines():
    return sys.stdin.readlines()

def should_print_newline(flag):
    return flag

def print_newline():
    print

def preprocess_line(s):
    return s.strip().zfill(5)

def compute_range_val(i):
    return 5 * i

def char_for_first_pattern(n, i, j):
    num = int(n[j]) - compute_range_val(i)
    if num in range(5):
        return "*"
    else:
        return " "

def print_first_pattern(n):
    for i in range_first_pattern():
        print("".join([char_for_first_pattern(n, i, j) for j in range_digits()]))

def range_first_pattern():
    return xrange(2)

def range_digits():
    return xrange(5)

def print_separator():
    print("="*5)

def char_for_second_pattern(n, i, j):
    if (int(n[j])%5) == i:
        return " "
    else:
        return "*"

def print_second_pattern(n):
    for i in range_second_pattern():
        print("".join([char_for_second_pattern(n, i, j) for j in range_digits()]))

def range_second_pattern():
    return xrange(5)

def process_line(s, print_flag):
    n = preprocess_line(s)
    if should_print_newline(print_flag):
        print_newline()
    print_first_pattern(n)
    print_separator()
    print_second_pattern(n)

def main():
    c = False
    lines = read_lines()
    for s in lines:
        process_line(s, c)
        c = True

main()