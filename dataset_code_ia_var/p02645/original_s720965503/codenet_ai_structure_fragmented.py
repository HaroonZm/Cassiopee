import sys

def set_recursion_limit():
    sys.setrecursionlimit(10 ** 7)

def get_infinity():
    return float('inf')

def get_modulus():
    return 10 ** 9 + 7

def read_input():
    return input()

def extract_first_three_characters(s):
    return s[:3]

def print_result(result):
    print(result)

def resolve():
    s = read_input()
    first_three = extract_first_three_characters(s)
    print_result(first_three)

def main():
    set_recursion_limit()
    f_inf = get_infinity()
    mod = get_modulus()
    resolve()

if __name__ == '__main__':
    main()