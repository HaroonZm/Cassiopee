def read_n():
    return int(input())

def read_a():
    return tuple(map(int, input().split()))

def find_max(a):
    return max(a)

def find_min(a):
    return min(a)

def abs_val(x):
    return abs(x)

def get_index(a, value):
    return a.index(value)

def compute_and_print(n, a):
    M = find_max(a)
    m = find_min(a)
    print_total_steps(n)
    if compare_abs(M, m):
        idx = get_index(a, M)
        process_indices(n, idx)
        process_chain_forward(n)
    else:
        idx = get_index(a, m)
        process_indices(n, idx)
        process_chain_backward(n)

def print_total_steps(n):
    print(2 * n - 2)

def compare_abs(M, m):
    return abs_val(M) >= abs_val(m)

def process_indices(n, idx):
    for x in indices_excluding(n, idx):
        print_step(idx, x)

def indices_excluding(n, exclude):
    return set(range(n)) - {exclude}

def print_step(from_idx, to_idx):
    print(from_idx + 1, to_idx + 1)

def process_chain_forward(n):
    for x in range(1, n):
        print(x, x + 1)

def process_chain_backward(n):
    for x in range(n - 1, 0, -1):
        print(x + 1, x)

def main():
    N = read_n()
    A = read_a()
    compute_and_print(N, A)

main()