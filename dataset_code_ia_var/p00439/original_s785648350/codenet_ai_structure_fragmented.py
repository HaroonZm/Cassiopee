def read_n_k():
    return map(int, input().split())

def should_stop(n):
    return n == 0

def read_first_element():
    return int(input())

def initialize_arrays(size):
    return [0]*size, [0]*size

def read_next_element():
    return int(input())

def update_a(a, i, val):
    a[i] = val

def update_s_first(s, a):
    s[0] = a[0]

def calculate_s_for_index(s, a, i, k):
    s[i] = s[i-1] + a[i]
    if i >= k:
        s[i] -= a[i-k]

def process_sequence(n, k, a, s):
    update_a(a, 0, read_first_element())
    update_s_first(s, a)
    for i in range(1, n):
        val = read_next_element()
        update_a(a, i, val)
        calculate_s_for_index(s, a, i, k)

def find_max_sum(s, k, n):
    ans = s[k-1]
    for i in range(k, n):
        if s[i] > ans:
            ans = s[i]
    return ans

def handle_query(a, s):
    n, k = read_n_k()
    if should_stop(n):
        return False
    process_sequence(n, k, a, s)
    ans = find_max_sum(s, k, n)
    print(ans)
    return True

def main():
    SIZE = 100003
    a, s = initialize_arrays(SIZE)
    while True:
        if not handle_query(a, s):
            break

main()