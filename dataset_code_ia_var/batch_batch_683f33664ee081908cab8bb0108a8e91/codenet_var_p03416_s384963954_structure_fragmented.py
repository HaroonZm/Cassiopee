def get_input():
    return input()

def split_input(s):
    return s.split()

def parse_ints(lst):
    return map(int, lst)

def unpack_pair(it):
    a, b = it
    return a, b

def to_range(a, b):
    return range(a, b + 1)

def to_str(v):
    return str(v)

def reverse_str(s):
    return s[::-1]

def is_palindrome(s):
    return s == reverse_str(s)

def check(v):
    s = to_str(v)
    return is_palindrome(s)

def gen_values(a, b):
    rng = to_range(a, b)
    return (check(v) for v in rng)

def sum_values(gen):
    return sum(gen)

def print_result(res):
    print(res)

def main():
    inp = get_input()
    splitted = split_input(inp)
    ints = parse_ints(splitted)
    a, b = unpack_pair(list(ints))
    values = gen_values(a, b)
    result = sum_values(values)
    print_result(result)

main()