import sys

def read_line_input():
    return sys.stdin.readline().strip()

def read_int_list():
    return list(map(int, read_line_input().split()))

def read_ints():
    return map(int, read_line_input().split())

def read_single_int():
    return int(read_line_input())

input_value = read_single_int()
output_value = pow(input_value, 3)
print(output_value)