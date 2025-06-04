def read_n_and_k():
    n, k = map(int, input().split())
    return n, k

def end_of_input(n):
    return n == 0

def read_first_value():
    return int(input())

def initialize_arrays(size):
    return [0] * size, [0] * size

def read_value():
    return int(input())

def update_prefix_sum(a, s, i, k):
    s[i] = s[i-1] + a[i]
    if i >= k:
        s[i] -= a[i-k]

def max_sliding_sum(s, k, n):
    ans = 0
    for i in range(k, n):
        if s[i] > ans:
            ans = s[i]
    return ans

def process_arrays(a, s, n, k):
    s[0] = a[0] = read_first_value()
    for i in range(1, n):
        a[i] = read_value()
        update_prefix_sum(a, s, i, k)

def print_answer(ans):
    print(ans)

def main_loop():
    ARRAY_SIZE = 100003
    a, s = initialize_arrays(ARRAY_SIZE)
    while True:
        n, k = read_n_and_k()
        if end_of_input(n):
            break
        process_arrays(a, s, n, k)
        ans = max_sliding_sum(s, k, n)
        print_answer(ans)

main_loop()