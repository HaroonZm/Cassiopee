import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class Solver:
    def __init__(self):
        pass

    def execute(self):
        diagonal_sums = [[None for col_idx in range(151)] for row_idx in range(151)]
        for row_idx in range(1, len(diagonal_sums)):
            for col_idx in range(1, len(diagonal_sums[0])):
                if row_idx >= col_idx:
                    continue
                diagonal_sums[row_idx][col_idx] = row_idx * row_idx + col_idx * col_idx
        while True:
            height, width = map(int, raw_input().split())
            if height == 0 and width == 0:
                break
            min_candidate = (float('inf'), float('inf'), float('inf'))
            for row_idx in reversed(range(1, len(diagonal_sums))):
                for col_idx in reversed(range(1, len(diagonal_sums[0]))):
                    current_value = diagonal_sums[row_idx][col_idx]
                    if current_value is not None and current_value >= height * height + width * width:
                        if current_value == height * height + width * width:
                            if height < row_idx <= min_candidate[0]:
                                min_candidate = (row_idx, col_idx, current_value)
                        elif min_candidate[2] == current_value:
                            if row_idx < min_candidate[0]:
                                min_candidate = (row_idx, col_idx, current_value)
                        elif min_candidate[2] > current_value:
                            min_candidate = (row_idx, col_idx, current_value)
            print '{0} {1}'.format(min_candidate[0], min_candidate[1])
        return None

if __name__ == '__main__':
    solver_instance = Solver()
    solver_instance.execute()