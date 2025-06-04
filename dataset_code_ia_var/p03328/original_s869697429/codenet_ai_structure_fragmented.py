def read_input():
    values = input().split()
    return extract_integers(values)

def extract_integers(values):
    return map_input_to_int(values)

def map_input_to_int(values):
    a = int(values[0])
    b = int(values[1])
    return (a, b)

def calculate_difference(a, b):
    return b - a

def decrement_by_one(value):
    return value - 1

def compute_sum_of_first_n(n):
    return ((n + 1) * n) // 2

def compute_result(A, a):
    return A - a

def print_result(ans):
    print(ans)

def main():
    a, b = read_input()
    x = calculate_difference(a, b)
    n = decrement_by_one(x)
    A = compute_sum_of_first_n(n)
    ans = compute_result(A, a)
    print_result(ans)

main()