import math
from functools import reduce

def compute_greatest_common_divisor_of_list(integer_list):

    return reduce(math.gcd, integer_list)

number_of_elements = int(input())

integer_list = [int(element) for element in input().split()]

greatest_common_divisor_of_input_list = compute_greatest_common_divisor_of_list(integer_list)

print(greatest_common_divisor_of_input_list)