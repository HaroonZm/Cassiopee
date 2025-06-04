import sys
import collections
import itertools
import re
import math
import fractions
import decimal
import random
import array
import bisect
import heapq

# decimal.getcontext().prec = 50
# sys.setrecursionlimit(10000)
# MODULO_CONSTANT = 10**9 + 7

class InputReader(object):
    def __init__(self, input_filename=None):
        self.input_file = open(input_filename) if input_filename is not None else None
        self.current_case_number = 1

    def __read_line(self):
        if self.input_file:
            return self.input_file.next().strip()
        else:
            return raw_input()

    def move_to_next_case(self):
        self.input_file.next()
        self.current_case_number += 1

    def read_single_integer(self):
        return int(self.__read_line())

    def read_single_float(self):
        return float(self.__read_line())

    def read_single_long(self):
        return long(self.__read_line())

    def read_single_decimal(self):
        return decimal.Decimal(self.__read_line())

    def read_single_string(self):
        return self.__read_line()

    def read_list_of_integers(self):
        return map(int, self.__read_line().split())

    def read_list_of_floats(self):
        return map(float, self.__read_line().split())

    def read_list_of_longs(self):
        return map(long, self.__read_line().split())

    def read_list_of_decimals(self):
        return map(decimal.Decimal, self.__read_line().split())

    def read_list_of_strings(self):
        return self.__read_line().split()


def solve(input_reader):
    input_data = input_reader.read_list_of_integers()
    number_of_segments, target_position = input_data

    segment_list = [input_reader.read_list_of_integers() for _ in xrange(number_of_segments)]

    minimal_steps = 0
    last_moved_direction = 0
    current_left_index = 0
    current_right_index = number_of_segments - 1

    while True:
        current_left_position = segment_list[current_left_index][0]
        current_right_position = segment_list[current_right_index][0]

        if current_left_position > target_position:
            return minimal_steps + (current_right_position - target_position)

        elif current_right_position < target_position:
            return minimal_steps + (target_position - current_left_position)

        else:
            left_weight = segment_list[current_left_index][1]
            right_weight = segment_list[current_right_index][1]

            if left_weight >= right_weight:
                segment_list[current_left_index][1] += right_weight
                if last_moved_direction != 1:
                    minimal_steps += current_right_position - current_left_position
                last_moved_direction = 1
                current_right_index -= 1
            else:
                segment_list[current_right_index][1] += left_weight
                if last_moved_direction != -1:
                    minimal_steps += current_right_position - current_left_position
                last_moved_direction = -1
                current_left_index += 1


if __name__ == '__main__':
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    input_reader = InputReader(input_filename)
    if input_reader.input_file:
        while True:
            print "Case #%d\n" % input_reader.current_case_number, solve(input_reader)
            try:
                input_reader.move_to_next_case()
            except StopIteration:
                break
    else:
        print solve(input_reader)