def get_input():
    return input()

def parse_int(s):
    return int(s)

def parse_int_list(s):
    return list(map(int, s.split()))

def read_n():
    s = get_input()
    return parse_int(s)

def read_a():
    s = get_input()
    return parse_int_list(s)

def is_odd(x):
    return x % 2

def process_element(n, i):
    return n - is_odd(i)

def process_all(n, a):
    new_n = n
    for i in a:
        new_n = process_element(new_n, i)
    return new_n

def display_result(result):
    print(result)

def main():
    n_val = read_n()
    a_list = read_a()
    result = process_all(n_val, a_list)
    display_result(result)

main()