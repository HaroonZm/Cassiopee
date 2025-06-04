def initialize_list(size):
    return [0 for _ in range(size)]

def get_query():
    return list(input().split())

def get_order(query):
    return query[0]

def get_index(query):
    return int(query[1])

def execute_print_if_one_at_index(l, idx):
    print(1 if l[idx] else 0)

def set_one_at_index(l, idx):
    l[idx] = 1

def set_zero_at_index(l, idx):
    l[idx] = 0

def flip_bit_at_index(l, idx):
    l[idx] ^= 1

def print_if_all_ones(l):
    print(1 if all_ones(l) else 0)

def all_ones(l):
    return all(l)

def print_if_any_one(l):
    print(1 if any_one(l) else 0)

def any_one(l):
    return any(l)

def print_if_none_one(l):
    print(1 if not any_one(l) else 0)

def print_sum_of_bits(l):
    print(sum_of_bits(l))

def sum_of_bits(l):
    return sum(l)

def print_decimal_value(l):
    print(list_to_decimal(l))

def list_to_decimal(l):
    return compute_decimal(l)

def compute_decimal(l):
    tmp = 0
    for i in reversed(range(len(l))):
        tmp += l[i] * two_power(i)
    return tmp

def two_power(i):
    return 2 ** i

def process_query(l, query):
    order = get_order(query)
    if order == "0":
        idx = get_index(query)
        execute_print_if_one_at_index(l, idx)
    elif order == "1":
        idx = get_index(query)
        set_one_at_index(l, idx)
    elif order == "2":
        idx = get_index(query)
        set_zero_at_index(l, idx)
    elif order == "3":
        idx = get_index(query)
        flip_bit_at_index(l, idx)
    elif order == "4":
        print_if_all_ones(l)
    elif order == "5":
        print_if_any_one(l)
    elif order == "6":
        print_if_none_one(l)
    elif order == "7":
        print_sum_of_bits(l)
    elif order == "8":
        print_decimal_value(l)

def handle_queries(l, n):
    for _ in range(n):
        query = get_query()
        process_query(l, query)

def main():
    size = 64
    l = initialize_list(size)
    n = read_number_of_queries()
    handle_queries(l, n)

def read_number_of_queries():
    return int(input())

main()