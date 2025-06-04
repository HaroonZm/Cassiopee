import sys

def set_recursion():
    sys.setrecursionlimit(10 ** 6)

def read_line():
    return sys.stdin.readline()

def split_line(line):
    return line.split()

def to_ints(strs):
    return list(map(int, strs))

def MI():
    return to_ints(split_line(read_line()))

def get_ab():
    a, b = MI()
    return a, b

def get_pqr():
    p, q, r = MI()
    return p, q, r

def compute_numerator(p, b, a, q, r):
    part1 = p * b
    part2 = a * q
    part3 = r * b
    return part1 + part2 + part3

def compute_denominator(q, r):
    return q + r

def compute_result(numerator, denominator):
    return numerator / denominator

def print_result(result):
    print(result)

def main():
    set_recursion()
    a, b = get_ab()
    p, q, r = get_pqr()
    numerator = compute_numerator(p, b, a, q, r)
    denominator = compute_denominator(q, r)
    result = compute_result(numerator, denominator)
    print_result(result)

main()