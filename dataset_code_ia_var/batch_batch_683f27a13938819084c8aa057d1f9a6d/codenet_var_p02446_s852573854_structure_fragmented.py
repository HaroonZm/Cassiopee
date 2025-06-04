def get_input():
    return input()

def parse_int(value):
    return int(value)

def split_input(input_str):
    return input_str.split()

def map_to_ints(str_list):
    return list(map(int, str_list))

def make_set(int_list):
    return set(int_list)

def sort_set(int_set):
    return sorted(int_set)

def unpack_and_print(sorted_list):
    print(*sorted_list)

def main():
    n_str = get_input()
    n = parse_int(n_str)
    values_str = get_input()
    values_split = split_input(values_str)
    values_int = map_to_ints(values_split)
    values_set = make_set(values_int)
    values_sorted = sort_set(values_set)
    unpack_and_print(values_sorted)

main()