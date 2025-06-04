def read_first_line():
    return input()

def read_second_line():
    return input()

def split_input(line):
    return line.split()

def map_to_int_list(str_list):
    return list(map(int, str_list))

def extract_variables(int_list):
    return int_list[0], int_list[1], int_list[2], int_list[3]

def compute_l1(q, h, s):
    return min(q*4, h*2, s)

def compute_l2(q, h, s, d):
    return min(q*8, h*4, s*2, d)

def is_even(n):
    return n % 2 == 0

def half_n(n):
    return n // 2

def compute_even_result(l2, n):
    return l2 * half_n(n)

def compute_odd_result(l2, n, l1):
    return l2 * half_n(n) + l1

def main():
    first_line = read_first_line()
    second_line = read_second_line()
    str_list = split_input(first_line)
    int_list = map_to_int_list(str_list)
    q, h, s, d = extract_variables(int_list)
    n = int(second_line)
    l1 = compute_l1(q, h, s)
    l2 = compute_l2(q, h, s, d)
    if is_even(n):
        result = compute_even_result(l2, n)
    else:
        result = compute_odd_result(l2, n, l1)
    print(result)

main()