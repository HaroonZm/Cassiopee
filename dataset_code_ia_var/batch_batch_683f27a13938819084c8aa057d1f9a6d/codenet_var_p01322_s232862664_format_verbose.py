from collections import deque
import itertools as itertools
import sys
import math
import re

sys.setrecursionlimit(10000000)

while True:
    number_of_patterns, number_of_strings = map(int, raw_input().split())

    if number_of_patterns + number_of_strings == 0:
        break

    pattern_score_list = []

    for pattern_index in range(number_of_patterns):
        raw_pattern, score_string = raw_input().split()
        regex_pattern = raw_pattern.replace("*", ".")
        score_value = int(score_string)
        pattern_score_list.append((regex_pattern, score_value))

    total_score = 0

    for string_index in range(number_of_strings):
        input_string = raw_input()

        for regex_pattern, score_value in pattern_score_list:
            if re.search(regex_pattern, input_string):
                total_score += score_value

    print total_score