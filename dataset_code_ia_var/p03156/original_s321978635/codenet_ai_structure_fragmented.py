def read_n():
    return int(input())

def read_line():
    return input().split()

def to_int(x):
    return int(x)

def extract_a(line):
    return to_int(line[0])

def extract_b(line):
    return to_int(line[1])

def read_params():
    line = read_line()
    a = extract_a(line)
    b = extract_b(line)
    return a, b

def read_p(n):
    line = read_line()
    return [to_int(line[i]) for i in range(n)]

def init_counter():
    return 0

def count_first(i, a):
    return i <= a

def count_second(i, a, b):
    return a+1 <= i <= b

def count_third(i, b):
    return i >= b+1

def process_counts(p, a, b):
    c1 = init_counter()
    c2 = init_counter()
    c3 = init_counter()
    for i in p:
        if count_first(i, a):
            c1 = increment(c1)
        elif count_second(i, a, b):
            c2 = increment(c2)
        elif count_third(i, b):
            c3 = increment(c3)
    return c1, c2, c3

def increment(c):
    return c + 1

def find_minimum(c1, c2, c3):
    return min(c1, c2, c3)

def main():
    n = read_n()
    a, b = read_params()
    p = read_p(n)
    c1, c2, c3 = process_counts(p, a, b)
    result = find_minimum(c1, c2, c3)
    print(result)

main()