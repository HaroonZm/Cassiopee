#!/usr/bin/env python

from collections import deque as queue
import itertools as itertools_module
import sys as sys_module
import math as math_module
import re as regex_module

sys_module.setrecursionlimit(10000000)

def main():
    while True:
        input_values = raw_input().split()
        row_count, col_count = map(int, input_values)
        if row_count + col_count == 0:
            break
        pattern_score_list = []
        for row_index in range(row_count):
            pattern_str, score_str = raw_input().split()
            standardized_pattern = pattern_str.replace("*", ".")
            pattern_score_list.append((standardized_pattern, int(score_str)))
        total_score = 0
        for col_index in range(col_count):
            target_string = raw_input()
            for pattern, score in pattern_score_list:
                if regex_module.search(pattern, target_string):
                    total_score += score
        print total_score

main()