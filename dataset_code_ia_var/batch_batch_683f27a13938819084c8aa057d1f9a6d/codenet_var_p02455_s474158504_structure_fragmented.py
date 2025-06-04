def read_number():
    return int(input())

def read_input_line():
    return input()

def parse_order_value(line):
    return map(int, line.split())

def process_add(S, value):
    S.add(value)
    return get_set_size(S)

def process_query(S, value):
    return check_membership(S, value)

def get_set_size(S):
    return len(S)

def check_membership(S, value):
    return 1 if value in S else 0

def print_result(result):
    print(result)

def process_iteration(S):
    line = read_input_line()
    order, value = parse_order_value(line)
    if is_add_order(order):
        result = process_add(S, value)
        print_result(result)
    else:
        result = process_query(S, value)
        print_result(result)

def is_add_order(order):
    return order == 0

def main():
    S = create_set()
    n = read_number()
    for _ in range(n):
        process_iteration(S)

def create_set():
    return set()

main()