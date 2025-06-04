import sys
sys.setrecursionlimit(10**7)
from pprint import pprint as pretty_print
from pprint import pformat as pretty_format
import math
import bisect

class GCDSolver:

    def __init__(self, num_count, max_gcd):
        self.num_count = num_count
        self.max_gcd = max_gcd
        self.gcd_case_counts = [0] * (max_gcd + 1)
        self.modulo_const = 10 ** 9 + 7

    def compute_gcd_cases(self, divisor):
        multiples_count = self.max_gcd // divisor
        divisor_cases = pow(multiples_count, self.num_count, self.modulo_const)
        multiple = divisor * 2
        while multiple <= self.max_gcd:
            divisor_cases -= self.gcd_case_counts[multiple]
            multiple += divisor
        self.gcd_case_counts[divisor] = divisor_cases % self.modulo_const

    def solve(self):
        for current_divisor in range(self.max_gcd, 0, -1):
            self.compute_gcd_cases(current_divisor)
        result = 0
        for gcd_value, case_count in enumerate(self.gcd_case_counts):
            result += gcd_value * case_count
        return result % self.modulo_const

if __name__ == '__main__':
    input_num_count, input_max_gcd = map(int, input().split())
    output_result = GCDSolver(input_num_count, input_max_gcd).solve()