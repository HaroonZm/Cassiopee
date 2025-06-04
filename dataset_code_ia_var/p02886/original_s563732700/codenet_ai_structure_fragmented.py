def get_input():
    return input()

def parse_int(s):
    return int(s)

def parse_int_list(s):
    return list(map(int, s.split()))

def get_n():
    return parse_int(get_input())

def get_d():
    return parse_int_list(get_input())

def calculate_product(a, b):
    return a * b

def add_to_total(total, value):
    return total + value

def process_pair(i, j, d):
    return calculate_product(d[i], d[j])

def loop_inner(i, N, d, current_res):
    j = i + 1
    while j < N:
        current_res = add_to_total(current_res, process_pair(i, j, d))
        j += 1
    return current_res

def compute_result(N, d):
    res = 0
    i = 0
    while i < N:
        res = loop_inner(i, N, d, res)
        i += 1
    return res

def print_result(res):
    print(res)

def main():
    N = get_n()
    d = get_d()
    res = compute_result(N, d)
    print_result(res)

main()