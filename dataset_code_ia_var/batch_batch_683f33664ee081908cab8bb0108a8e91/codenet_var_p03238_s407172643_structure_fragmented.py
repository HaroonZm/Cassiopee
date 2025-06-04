from sys import stdin

def get_input():
    return stdin.readline()

def parse_int(value):
    return int(value)

def read_int():
    return parse_int(get_input())

def condition_n_lt_2(n):
    return n < 2

def print_hello_world():
    print('Hello World')

def get_A():
    return read_int()

def get_B():
    return read_int()

def add(a, b):
    return a + b

def print_result(result):
    print(result)

def process_case_n_lt_2():
    print_hello_world()

def process_case_n_ge_2():
    a = get_A()
    b = get_B()
    result = add(a, b)
    print_result(result)

def process_n(n):
    if condition_n_lt_2(n):
        process_case_n_lt_2()
    else:
        process_case_n_ge_2()

def main():
    n = read_int()
    process_n(n)

main()