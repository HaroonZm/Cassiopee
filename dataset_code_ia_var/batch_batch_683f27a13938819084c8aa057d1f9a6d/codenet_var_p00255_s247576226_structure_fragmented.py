def read_n():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def should_break(n):
    return n == 0

def initialize_sump(p):
    return sum(p)

def initialize_sarary(sump, n):
    return sump * n

def sort_list(l):
    l.sort()
    return l

def update_sump(sump, j):
    return sump + j.pop()

def update_n(n):
    return n - 1

def calculate_sara_check(sump, n):
    return sump * n

def update_sarary(sarary, sara_check):
    return max(sarary, sara_check)

def process_case(n, p, j):
    j = sort_list(j)
    sump = initialize_sump(p)
    sarary = initialize_sarary(sump, n)
    while more_iterations(n):
        sump = update_sump(sump, j)
        n = update_n(n)
        sara_check = calculate_sara_check(sump, n)
        sarary = update_sarary(sarary, sara_check)
    print_result(sarary)

def more_iterations(n):
    return n > 1

def print_result(sarary):
    print(sarary)

def main():
    while True:
        n = read_n()
        if should_break(n):
            break
        p = read_int_list()
        j = read_int_list()
        process_case(n, p, j)

main()