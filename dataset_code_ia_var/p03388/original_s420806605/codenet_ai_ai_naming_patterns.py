import sys
_input_stream = sys.stdin

sys.setrecursionlimit(10 ** 5)

def read_ints(): return map(int, _input_stream.readline().split())
def read_ints0(): return map(lambda x: int(x) - 1, _input_stream.readline().split())
def read_floats(): return map(float, _input_stream.readline().split())
def read_strings(): return _input_stream.readline().split()
def read_str(): return _input_stream.readline().rstrip()
def read_chars(): return list(read_str())
def read_int(): return int(_input_stream.readline())
def read_float(): return float(_input_stream.readline())

from math import sqrt

def compute_steps(x_value: int, y_value: int) -> int:
    if x_value == y_value:
        return 2 * x_value - 2
    elif abs(x_value - y_value) == 1:
        return 2 * min(x_value, y_value) - 2
    else:
        candidate = int(sqrt(x_value * y_value))
        if x_value * y_value == candidate * candidate:
            candidate -= 1
        if x_value * y_value > candidate * (candidate + 1):
            return 2 * candidate - 1
        else:
            return 2 * candidate - 2

query_count = read_int()
query_list = [tuple(read_ints()) for _ in range(query_count)]

for query_x, query_y in query_list:
    print(compute_steps(query_x, query_y))