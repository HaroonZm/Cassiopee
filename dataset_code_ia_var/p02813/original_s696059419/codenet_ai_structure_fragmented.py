import math

def read_int():
    return int(input())

def read_int_list():
    return [int(x) for x in input().split()]

def compute_factorial(val):
    return math.factorial(val)

def count_lower_elements(lst, index, N):
    count = 0
    for j in range(index+1, N):
        if lst[index] > lst[j]:
            count += 1
    return count

def increment_for_index(lst, index, N):
    count = count_lower_elements(lst, index, N)
    fac = compute_factorial(N-1-index)
    return count * fac

def compute_score(lst, N):
    total = 0
    for i in range(N-1):
        inc = increment_for_index(lst, i, N)
        total += inc
    return total

def print_result(diff):
    print(diff)

def main():
    N = read_int()
    p = read_int_list()
    q = read_int_list()
    P = compute_score(p, N)
    Q = compute_score(q, N)
    diff = abs(P-Q)
    print_result(diff)

main()