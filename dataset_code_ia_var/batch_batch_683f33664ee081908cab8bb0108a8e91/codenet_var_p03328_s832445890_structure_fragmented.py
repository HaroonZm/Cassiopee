def read_input():
    return input()

def parse_input(s):
    return s.split()

def convert_to_ints(strs):
    return list(map(int, strs))

def assign_values(ints):
    return ints[0], ints[1]

def compute_difference(a, b):
    return b - a

def initialize_counter():
    return 0

def get_range_end(c):
    return c - 1

def compute_increment(i):
    return i + 1

def update_counter(cnt, increment):
    return cnt + increment

def iterate_and_sum(c):
    cnt = initialize_counter()
    for i in range(get_range_end(c)):
        increment = compute_increment(i)
        cnt = update_counter(cnt, increment)
    return cnt

def subtract_a(cnt, a):
    return cnt - a

def main():
    s = read_input()
    strs = parse_input(s)
    ints = convert_to_ints(strs)
    a, b = assign_values(ints)
    c = compute_difference(a, b)
    cnt = iterate_and_sum(c)
    result = subtract_a(cnt, a)
    print(result)

main()