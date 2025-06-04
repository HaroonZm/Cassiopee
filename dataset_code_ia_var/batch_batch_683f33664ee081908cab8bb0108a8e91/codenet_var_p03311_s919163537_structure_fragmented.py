def read_input():
    return int(input())

def read_array():
    return list(map(int, input().split()))

def initialize_B(N):
    return [0] * N

def compute_B_element(A, i):
    return A[i] - i

def build_B(A, N):
    B = initialize_B(N)
    for i in range(N):
        B[i] = compute_B_element(A, i)
    return B

def sort_array(arr):
    arr.sort()
    return arr

def median_index(N):
    return N // 2

def compute_b(B, N):
    idx = median_index(N)
    return B[idx] - 1

def abs_difference(a, b):
    return abs(a - b)

def compute_adjusted_value(b, i):
    return b + i + 1

def accumulate_difference(ans, diff):
    return ans + diff

def compute_total_cost(A, b, N):
    ans = 0
    for i in range(N):
        target = compute_adjusted_value(b, i)
        diff = abs_difference(A[i], target)
        ans = accumulate_difference(ans, diff)
    return ans

def print_result(ans):
    print(ans)

def main():
    N = read_input()
    A = read_array()
    B = build_B(A, N)
    B = sort_array(B)
    b = compute_b(B, N)
    ans = compute_total_cost(A, b, N)
    print_result(ans)

main()