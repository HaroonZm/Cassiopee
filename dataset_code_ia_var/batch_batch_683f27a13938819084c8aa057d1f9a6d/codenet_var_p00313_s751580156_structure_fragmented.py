def get_input():
    return input()

def to_int(x):
    return int(x)

def create_zero_list(length):
    return [0] * length

def get_indices():
    return [1, 2, 4]

def get_raw_input():
    return raw_input()

def split_input(s):
    return s.split()

def skip_first(lst):
    return lst[1:]

def map_int(lst):
    return map(int, lst)

def decrement_by_one(x):
    return x - 1

def add_value_to_list(V, idx, value):
    V[idx] += value

def process_input(n, V):
    for i in get_indices():
        raw_line = get_raw_input()
        splitted = split_input(raw_line)
        skipped = skip_first(splitted)
        int_map = map_int(skipped)
        for e in int_map:
            index = decrement_by_one(e)
            add_value_to_list(V, index, i)

def check_bit_four(e):
    return (e & 4) > 0

def is_not_five(e):
    return e != 5

def process_count(V):
    total = 0
    for e in V:
        if check_bit_four(e) and is_not_five(e):
            total += 1
    return total

def main():
    n_raw = get_input()
    n = to_int(n_raw)
    V = create_zero_list(n)
    process_input(n, V)
    result = process_count(V)
    print(result)

main()