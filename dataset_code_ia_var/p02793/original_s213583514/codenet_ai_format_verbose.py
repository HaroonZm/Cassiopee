import sys
from collections import deque
from heapq import heapify, heappop, heappush
from itertools import combinations, permutations
from bisect import bisect, bisect_left

def compute_gcd(first_number, second_number):
    maximum_value = max(first_number, second_number)
    minimum_value = min(first_number, second_number)
    product_of_numbers = maximum_value * minimum_value

    while maximum_value % minimum_value > 0:
        maximum_value, minimum_value = minimum_value, maximum_value % minimum_value

    return minimum_value

def solve_problem():
    input_function = sys.stdin.readline
    modulus = 7 + 10 ** 9

    total_number_count = int(input_function())
    integer_array = [int(single_value) for single_value in input_function().split()]

    if total_number_count == 1:
        print(1)
    else:
        least_common_multiple = integer_array[0]

        for current_index in range(1, total_number_count):
            current_gcd = compute_gcd(least_common_multiple, integer_array[current_index])
            least_common_multiple = least_common_multiple * integer_array[current_index] // current_gcd

        least_common_multiple %= modulus

        sum_of_results = 0

        for current_index, current_integer in enumerate(integer_array):
            modular_inverse = pow(current_integer, modulus - 2, modulus)
            sum_of_results += least_common_multiple * modular_inverse
            sum_of_results %= modulus

        print(sum_of_results)

    return 0

if __name__ == "__main__":
    solve_problem()