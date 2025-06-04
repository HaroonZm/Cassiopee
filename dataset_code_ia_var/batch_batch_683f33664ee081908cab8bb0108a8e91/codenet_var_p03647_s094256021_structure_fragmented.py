def get_input():
    return input()

def parse_two_ints(s):
    return list(map(int, s.split()))

def init_bool_list(size):
    return [False] * size

def copy_list(lst):
    return lst[:]

def set_true(lst, idx):
    lst[idx] = True

def handle_first_if(p, k):
    set_true(p, k)

def handle_second_if(q, k):
    set_true(q, k)

def handle_elif(q, j):
    set_true(q, j)

def process_input(m, p, q, n):
    for _ in range(m):
        j, k = parse_two_ints(get_input())
        if j == 1:
            handle_first_if(p, k)
        if j == n:
            handle_second_if(q, k)
        elif k == n:
            handle_elif(q, j)

def both_true(p, q, i):
    return p[i] and q[i]

def check_possible(n, p, q):
    for i in range(n):
        if both_true(p, q, i):
            print_possible()
            return True
    return False

def print_possible():
    print("POSSIBLE")

def print_impossible():
    print("IMPOSSIBLE")

def main():
    n, m = parse_two_ints(get_input())
    p = init_bool_list(n)
    q = copy_list(p)
    process_input(m, p, q, n)
    if not check_possible(n, p, q):
        print_impossible()

main()