def read_input():
    return input()

def to_int(x):
    return int(x)

def INT():
    return to_int(read_input())

def split_string(s):
    return s.split()

def map_to_int(lst):
    return map(int, lst)

def MI():
    return map_to_int(split_string(read_input()))

def list_conversion(mapped):
    return list(mapped)

def LI():
    return list_conversion(map_to_int(split_string(read_input())))

def generate_range(n):
    return range(n)

def read_strings(n):
    return [read_input() for _ in generate_range(n)]

def import_counter():
    from collections import Counter
    return Counter

def count_elements(lst):
    counter = import_counter()
    return counter(lst)

def get_value_from_counter(counter, key):
    return counter[key]

def format_result(label, count):
    return f"{label} x {count}"

def print_result(s):
    print(s)

def process():
    N = INT()
    S = read_strings(N)
    S_counter = count_elements(S)
    labels = ['AC', 'WA', 'TLE', 'RE']
    for label in labels:
        count = get_value_from_counter(S_counter, label)
        result = format_result(label, count)
        print_result(result)

process()