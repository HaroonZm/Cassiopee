import sys

def input_line():
    return sys.stdin.readline().rstrip()

def input_int():
    return int(input_line())

def input_int_list():
    return [int(x) for x in input_line().split()]

def read_params():
    return input_int_list()

def read_aa():
    return input_int_list()

def sort_list(lst):
    lst.sort()
    return lst

def subtract_and_count(aa, x):
    c = 0
    for a in aa:
        x = subtract_x(x, a)
        if check_x_non_negative(x):
            c = increment_c(c)
    return c, x

def subtract_x(x, a):
    return x - a

def check_x_non_negative(x):
    return x >= 0

def increment_c(c):
    return c + 1

def decrement_c(c):
    return c - 1

def adjust_c(c, x):
    if x > 0:
        c = decrement_c(c)
    return c

def output_result(c):
    print(c)

def main():
    n, x = read_params()
    aa = read_aa()
    aa = sort_list(aa)
    c, x = subtract_and_count(aa, x)
    c = adjust_c(c, x)
    output_result(c)

main()