import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class CombinationSumCalculator(object):

    def __init__(self):
        pass

    def find_number_of_combinations(self):

        while True:

            input_values = raw_input().split()
            number_of_elements, elements_to_choose, desired_sum = map(int, input_values)

            if (number_of_elements, elements_to_choose, desired_sum) == (0, 0, 0):
                break

            number_of_valid_combinations = 0

            for selected_elements in itertools.combinations(range(1, number_of_elements + 1), elements_to_choose):

                if sum(selected_elements) == desired_sum:
                    number_of_valid_combinations += 1

            print number_of_valid_combinations

        return None

if __name__ == '__main__':
    combination_sum_calculator = CombinationSumCalculator()
    combination_sum_calculator.find_number_of_combinations()