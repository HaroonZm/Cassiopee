#!/usr/bin/env python

import sys
import math
import itertools as itertools_module
from collections import deque as double_ended_queue

# Augmente la limite de récursion pour éviter un dépassement dans le calcul factoriel
sys.setrecursionlimit(10000000)

MODULO_DIVISOR = 10 ** 9 + 7

number_of_elements, combination_size = map(int, raw_input().split())

def recursive_factorial(integer_value):
    if integer_value <= 1:
        return 1
    return recursive_factorial(integer_value - 1) * integer_value

numerator = recursive_factorial(number_of_elements + combination_size - 1)
denominator = recursive_factorial(combination_size - 1) * recursive_factorial(number_of_elements)
combination_result = numerator / denominator

print (combination_result % MODULO_DIVISOR)