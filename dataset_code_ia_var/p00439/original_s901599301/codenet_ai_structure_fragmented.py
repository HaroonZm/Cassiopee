def read_input():
    values = input().split()
    return int(values[0]), int(values[1])

def should_terminate(n):
    return n == 0

def read_array(n):
    return [int(input()) for _ in range(n)]

def compute_prefix_sum(A):
    s = [0] * (len(A) + 1)
    for i in range(len(A)):
        s[i + 1] = s[i] + A[i]
    return s

def max_k_subarray_sum(n, k, s):
    ans = -1
    for l in range(n):
        r = l + k
        if r > n:
            break
        ans = max(ans, s[r] - s[l])
    return ans

def process_case():
    n, k = read_input()
    if should_terminate(n):
        return False
    A = read_array(n)
    s = compute_prefix_sum(A)
    result = max_k_subarray_sum(n, k, s)
    output_result(result)
    return True

def output_result(result):
    print(result)

def solve():
    while True:
        if not process_case():
            return

if __name__ == '__main__':
    solve()