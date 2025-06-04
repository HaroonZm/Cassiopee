import sys

def read_input():
    return sys.stdin

def split_line(line):
    return line.split()

def to_float(val):
    return float(val)

def get_pq(line):
    p, q = split_line(line)
    a = to_float(p)
    b = to_float(q)
    return a, b

def check_aaa(a, b):
    return (a < 35.5) and (b < 71.0)

def check_aa(a, b):
    return (a < 37.5) and (b < 77.0)

def check_a(a, b):
    return (a < 40.0) and (b < 83.0)

def check_b(a, b):
    return (a < 43.0) and (b < 89.0)

def check_c(a, b):
    return (a < 50.0) and (b < 105.0)

def check_d(a, b):
    return (a < 55.0) and (b < 116.0)

def check_e(a, b):
    return (a < 70.0) and (b < 148.0)

def print_grade(grade):
    print(grade)

def determine_grade(a, b):
    if check_aaa(a, b):
        print_grade('AAA')
    elif check_aa(a, b):
        print_grade('AA')
    elif check_a(a, b):
        print_grade('A')
    elif check_b(a, b):
        print_grade('B')
    elif check_c(a, b):
        print_grade('C')
    elif check_d(a, b):
        print_grade('D')
    elif check_e(a, b):
        print_grade('E')
    else:
        print_grade('NA')

def process_line(line):
    a, b = get_pq(line)
    determine_grade(a, b)

def main():
    for line in read_input():
        process_line(line)

main()