import math

def int_input():
    return int(input())

def get_dimensions():
    return int_input(), int_input()

def get_number_of_items():
    return int_input()

def find_max_len(H, W):
    return max(H, W)

def compute_division(N, max_len):
    return N / max_len

def calculate_ceiling(value):
    return math.ceil(value)

def print_result(result):
    print(result)

def main():
    H, W = get_dimensions()
    N = get_number_of_items()
    max_len = find_max_len(H, W)
    division_result = compute_division(N, max_len)
    ceiling_result = calculate_ceiling(division_result)
    print_result(ceiling_result)

main()