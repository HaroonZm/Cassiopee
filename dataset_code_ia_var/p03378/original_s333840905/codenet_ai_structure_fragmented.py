def read_input():
    return input()

def parse_input(input_line):
    return map(int, input_line.split())

def get_nmx():
    input_line = read_input()
    n, m, x = parse_input(input_line)
    return n, m, x

def read_clist():
    return input()

def parse_clist(input_line):
    return list(map(int, input_line.split()))

def get_clist():
    input_line = read_clist()
    clist = parse_clist(input_line)
    return clist

def count_lroot(clist, x):
    count = 0
    for item in clist:
        if is_less_than_x(item, x):
            count = increment(count)
    return count

def count_rroot(clist, x):
    count = 0
    for item in clist:
        if not is_less_than_x(item, x):
            count = increment(count)
    return count

def is_less_than_x(item, x):
    return item < x

def increment(value):
    return value + 1

def compute_min(lroot, rroot):
    return min(lroot, rroot)

def show_result(result):
    print(result)

def main():
    n, m, x = get_nmx()
    clist = get_clist()
    lroot = count_lroot(clist, x)
    rroot = count_rroot(clist, x)
    result = compute_min(lroot, rroot)
    show_result(result)

main()