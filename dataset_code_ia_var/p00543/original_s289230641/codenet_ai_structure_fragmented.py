def read_two_ints():
    return map(int, input().split())

def read_single_int():
    return int(input())

def initialize_array(size):
    return [0] * size

def fill_array(arr, size):
    for idx in range(size):
        arr[idx] = read_single_int()

def should_continue_outer(i):
    return i == 1

def swap_needed(a, b, mod_val):
    return (a % mod_val) > (b % mod_val)

def swap(arr, idx):
    temp = arr[idx]
    arr[idx] = arr[idx + 1]
    arr[idx + 1] = temp

def process_bubble_pass(arr, n, mod_val):
    for j in range(n - 1):
        if swap_needed(arr[j], arr[j+1], mod_val):
            swap(arr, j)

def perform_sorting(arr, n, m):
    for i in range(1, m+1):
        if should_continue_outer(i):
            continue
        else:
            process_bubble_pass(arr, n, i)

def print_element(val):
    print(val)

def print_array(arr, n):
    for idx in range(n):
        print_element(arr[idx])

def main():
    N, M = read_two_ints()
    A = initialize_array(N)
    fill_array(A, N)
    perform_sorting(A, N, M)
    print_array(A, N)

main()