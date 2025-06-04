def read_n_and_m():
    return map(int, input().split())

def initialize_list_a(n):
    return [i for i in range(n)]

def read_single_input():
    return int(input())

def set_a_at_index(a, idx, i):
    a[idx] = -i - 1

def mark_indices_in_a(a, m):
    for i in range(m):
        e = read_single_input()
        set_a_at_index(a, e - 1, i)
    return a

def build_b(a, n):
    return [[a[i], i + 1] for i in range(n)]

def sort_b(b):
    b.sort()
    return b

def print_b_elements(b, n):
    for i in range(n):
        print(b[i][1])

def main():
    n, m = read_n_and_m()
    a = initialize_list_a(n)
    mark_indices_in_a(a, m)
    b = build_b(a, n)
    sort_b(b)
    print_b_elements(b, n)

main()