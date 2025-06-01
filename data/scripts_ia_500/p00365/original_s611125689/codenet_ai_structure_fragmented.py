def read_input_line():
    return input()

def split_line(line):
    return line.split()

def map_to_ints(str_list):
    return tuple(map(int, str_list))

def read_and_parse():
    line = read_input_line()
    split = split_line(line)
    ints = map_to_ints(split)
    return ints

def read_two_tuples():
    return [read_and_parse() for _ in [0,0]]

def sort_tuples(tuples_list):
    return sorted(tuples_list)

def get_first_tuple(sorted_list):
    return sorted_list[0]

def get_second_tuple(sorted_list):
    return sorted_list[1]

def get_first_element(tup):
    return tup[0]

def get_second_element(tup):
    return tup[1]

def get_third_element(tup):
    return tup[2]

def compare_second_elements(t2, t1):
    return get_second_element(t2) > get_second_element(t1)

def compare_third_elements_if_second_equal(t2, t1):
    return get_second_element(t2) == get_second_element(t1) and get_third_element(t2) > get_third_element(t1)

def compute_difference(t2, t1):
    base_diff = get_first_element(t2) - get_first_element(t1)
    increment = 1 if compare_second_elements(t2, t1) or compare_third_elements_if_second_equal(t2, t1) else 0
    return base_diff + increment

def main():
    tuples_list = read_two_tuples()
    sorted_list = sort_tuples(tuples_list)
    t1 = get_first_tuple(sorted_list)
    t2 = get_second_tuple(sorted_list)
    result = compute_difference(t2, t1)
    print(result)

main()