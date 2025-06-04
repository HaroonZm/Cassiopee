import sys
input_stream = sys.stdin

sys.setrecursionlimit(10 ** 7)

def input_int_iter(): return map(int, input_stream.readline().split())
def input_int0_iter(): return map(lambda x: int(x) - 1, input_stream.readline().split())
def input_float_iter(): return map(float, input_stream.readline().split())
def input_str_iter(): return input_stream.readline().split()
def input_str(): return input_stream.readline().rstrip()
def input_char_list(): return list(input_str())
def input_int(): return int(input_stream.readline())
def input_float(): return float(input_stream.readline())

from collections import defaultdict

input_string = input_str()
char_count_dict = defaultdict(int)
for char in input_string:
    char_count_dict[char] += 1

is_valid = True
for _, count in char_count_dict.items():
    if count != 2:
        is_valid = False
        break

print("Yes" if is_valid else "No")