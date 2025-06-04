def read_integer():
    return int(input())

def read_integer_list():
    return list(map(int, input().split()))

def decrement_elements_by_indices(A):
    return [A[i] - (i + 1) for i in range(len(A))]

def sort_list(A):
    return sorted(A)

def is_odd(n):
    return n % 2 == 1

def get_median_index(n):
    return n // 2

def calculate_median(A, N):
    if is_odd(N):
        return A[get_median_index(N)]
    else:
        return (A[get_median_index(N)] + A[get_median_index(N)-1]) // 2

def sum_absolute_differences(A, b):
    return sum(abs(i - b) for i in A)

def sum_absolute_differences_alt(A, a):
    return sum(abs(i - (a - 1)) for i in A)

def process_odd_N(A, N):
    median = A[get_median_index(N)]
    return sum_absolute_differences(A, median)

def process_even_N(A, N):
    mid1 = A[get_median_index(N)-1]
    mid2 = A[get_median_index(N)]
    a = (mid1 + mid2) // 2
    s1 = sum_absolute_differences(A, a)
    s2 = sum_absolute_differences_alt(A, a)
    return min(s1, s2)

def output_result(result):
    print(result)

def main():
    N = read_integer()
    A = read_integer_list()
    A = decrement_elements_by_indices(A)
    A = sort_list(A)
    if is_odd(N):
        ans = process_odd_N(A, N)
    else:
        ans = process_even_N(A, N)
    output_result(ans)

main()