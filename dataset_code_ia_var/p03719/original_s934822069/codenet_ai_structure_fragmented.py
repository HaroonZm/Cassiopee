def read_input():
    return input()

def split_input(s):
    return s.split()

def map_to_int(lst):
    return list(map(int, lst))

def get_values():
    raw = read_input()
    splitted = split_input(raw)
    ints = map_to_int(splitted)
    return ints

def assign_values(ints):
    a = ints[0]
    b = ints[1]
    c = ints[2]
    return a, b, c

def is_in_range(a, b, c):
    return a <= c <= b

def select_output(result):
    if result:
        return 'Yes'
    else:
        return 'No'

def display(msg):
    print(msg)

def main():
    ints = get_values()
    a, b, c = assign_values(ints)
    result = is_in_range(a, b, c)
    msg = select_output(result)
    display(msg)

main()