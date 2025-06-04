def get_input():
    return input()

def to_int(s):
    return int(s)

def split_digits(x):
    return list(str(x))

def digit_strs_to_ints(digit_strs):
    return list(map(int, digit_strs))

def sum_digits(digit_ints):
    return sum(digit_ints)

def f(X):
    digit_strs = split_digits(X)
    digit_ints = digit_strs_to_ints(digit_strs)
    return sum_digits(digit_ints)

def is_divisible(N, s):
    return N % s == 0

def print_yes():
    print('Yes')

def print_no():
    print('No')

def main():
    inp = get_input()
    N = to_int(inp)
    s = f(N)
    if is_divisible(N, s):
        print_yes()
    else:
        print_no()

main()