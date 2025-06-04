def get_input():
    return input()

def split_input(s):
    return s.split()

def map_to_int(lst):
    return map(int, lst)

def unpack_values(mapped):
    return list(mapped)

def assign_values(vals):
    a = vals[0]
    b = vals[1]
    c = vals[2]
    return a, b, c

def is_in_range(a, b, c):
    return a <= c <= b

def yes_or_no(condition):
    return 'Yes' if condition else 'No'

def output_result(result):
    print(result)

def main():
    s = get_input()
    splitted = split_input(s)
    mapped = map_to_int(splitted)
    vals = unpack_values(mapped)
    a, b, c = assign_values(vals)
    condition = is_in_range(a, b, c)
    result = yes_or_no(condition)
    output_result(result)

main()