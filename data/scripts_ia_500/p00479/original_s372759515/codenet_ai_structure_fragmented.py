def read_int():
    return int(input())

def read_two_ints():
    return map(int, input().split())

def compute_min_values(a, b, N):
    return min(a-1, N-a, b-1, N-b)

def compute_result(min_val):
    return min_val % 3 + 1

def process_single_case(N):
    a, b = read_two_ints()
    min_val = compute_min_values(a, b, N)
    result = compute_result(min_val)
    print(result)

def main():
    N = read_int()
    T = read_int()
    for _ in range(T):
        process_single_case(N)

main()