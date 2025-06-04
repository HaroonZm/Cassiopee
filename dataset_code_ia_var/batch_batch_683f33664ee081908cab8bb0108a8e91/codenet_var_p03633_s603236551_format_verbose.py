import sys

sys.setrecursionlimit(2147483647)

POSITIVE_INFINITY = float("inf")
MODULO_CONSTANT = 10 ** 9 + 7

def compute_least_common_multiple_of_inputs():
    number_of_inputs = int(input())
    least_common_multiple = 1

    from math import gcd

    for _ in range(number_of_inputs):
        current_input_number = int(input())
        least_common_multiple = (
            least_common_multiple * current_input_number //
            gcd(least_common_multiple, current_input_number)
        )

    print(least_common_multiple)

compute_least_common_multiple_of_inputs()