import sys
import bisect
from functools import lru_cache
from collections import defaultdict

POSITIVE_INFINITY = float('inf')

standard_input_buffer = sys.stdin.buffer
read_single_line_from_input_buffer = standard_input_buffer.readline
read_all_lines_from_input_buffer = standard_input_buffer.readlines

sys.setrecursionlimit(10 ** 6)

def read_input_line():
    return sys.stdin.readline().rstrip()

def read_integer_from_input():
    return int(read_single_line_from_input_buffer())

def read_multiple_integers_from_input():
    return map(int, read_single_line_from_input_buffer().split())

number_of_repetitions_for_acl_string = read_integer_from_input()
acl_string = "ACL"
output_string = acl_string * number_of_repetitions_for_acl_string

print(output_string)