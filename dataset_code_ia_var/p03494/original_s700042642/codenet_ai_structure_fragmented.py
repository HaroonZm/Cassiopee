def get_input():
    return input()

def parse_int(value):
    return int(value)

def parse_int_list(value):
    return list(map(int, value.split()))

def read_N():
    return parse_int(get_input())

def read_A():
    return parse_int_list(get_input())

def is_even(n):
    return n % 2 == 0

def all_even(lst):
    return all([is_even(i) for i in lst])

def halve(n):
    return n / 2

def halve_list(lst):
    return [halve(i) for i in lst]

def should_continue(lst):
    return all_even(lst)

def increment(n):
    return n + 1

def process(A):
    cnt = 0
    while True:
        if should_continue(A):
            A = halve_list(A)
            cnt = increment(cnt)
        else:
            break
    return cnt

def show_result(result):
    print(result)

def main():
    N = read_N()
    A = read_A()
    cnt = process(A)
    show_result(cnt)

main()