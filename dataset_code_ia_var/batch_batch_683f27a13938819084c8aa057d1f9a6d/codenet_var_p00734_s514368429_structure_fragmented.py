def read_n_m():
    return map(int, input().split())

def read_list(size):
    return [int(input()) for _ in range(size)]

def sort_list(lst):
    lst.sort()
    return lst

def compute_sum(lst):
    return sum(lst)

def check_condition(i, j, sumt, sumh):
    return (i - j) * 2 == sumt - sumh

def print_result(i, j):
    print(i, j)

def print_not_found():
    print(-1)

def process_pair(i, j, sumt, sumh):
    if check_condition(i, j, sumt, sumh):
        print_result(i, j)
        return True
    return False

def inner_loop(i, h, sumt, sumh):
    for j in h:
        if process_pair(i, j, sumt, sumh):
            return True
    return False

def outer_loop(t, h, sumt, sumh):
    for i in t:
        if inner_loop(i, h, sumt, sumh):
            return True
    return False

def find_and_print(t, h, sumt, sumh):
    if not outer_loop(t, h, sumt, sumh):
        print_not_found()

def main_loop():
    while True:
        n, m = read_n_m()
        if n == 0:
            break
        t = read_list(n)
        h = read_list(m)
        t = sort_list(t)
        h = sort_list(h)
        sumt = compute_sum(t)
        sumh = compute_sum(h)
        find_and_print(t, h, sumt, sumh)

main_loop()