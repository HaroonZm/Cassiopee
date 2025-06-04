def read_n():
    return int(input())

def init_c():
    return 0

def init_list(n):
    return [0] * n

def read_pair():
    return tuple(map(int, input().split()))

def set_pair_at_index(d, t, idx):
    di, ti = read_pair()
    d[idx] = di
    t[idx] = ti

def check_equal_triplet(d, t, i):
    if d[i] == t[i] and d[i-1] == t[i-1] and d[i-2] == t[i-2]:
        return True
    return False

def process_input(n, d, t):
    set_pair_at_index(d, t, 0)
    set_pair_at_index(d, t, 1)
    return

def iterate_triples_and_count(n, d, t):
    c = 0
    for i in range(2, n):
        set_pair_at_index(d, t, i)
        if check_equal_triplet(d, t, i):
            c = increment_c(c)
    return c

def increment_c(c):
    return c + 1

def print_yes():
    print('Yes')

def print_no():
    print('No')

def decide_print(c):
    if c != 0:
        print_yes()
    else:
        print_no()

def main():
    n = read_n()
    c = init_c()
    d = init_list(n)
    t = init_list(n)
    process_input(n, d, t)
    c = iterate_triples_and_count(n, d, t)
    decide_print(c)

main()