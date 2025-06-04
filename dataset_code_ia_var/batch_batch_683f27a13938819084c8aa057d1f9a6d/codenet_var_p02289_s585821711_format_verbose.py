import sys
import os
import math
import heapq

sys.setrecursionlimit(10000000)

def read_single_integer():
    return int(sys.stdin.buffer.readline().rstrip())

def read_integer_list():
    return list(map(int, sys.stdin.buffer.readline().split()))

def read_float_list():
    return list(map(float, sys.stdin.buffer.readline().split()))

def read_n_integers(number_of_lines):
    return [int(sys.stdin.buffer.readline().rstrip()) for _ in range(number_of_lines)]

def read_single_line_as_string():
    return sys.stdin.buffer.readline().decode().rstrip()

def read_string_list():
    return list(map(str, sys.stdin.buffer.readline().decode().split()))

def read_n_strings(number_of_lines):
    return [sys.stdin.buffer.readline().decode().rstrip() for _ in range(number_of_lines)]

def compute_least_common_multiple(value_1, value_2):
    return (value_1 * value_2) // math.gcd(value_1, value_2)

MODULO_CONSTANT = 10 ** 9 + 7
INFINITY = float('inf')

def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    max_heap_container = []
    heapq.heapify(max_heap_container)

    while True:
        input_command = read_string_list()
        if input_command[0] == 'end':
            break
        elif input_command[0] == 'insert':
            value_to_insert = int(input_command[1])
            heapq.heappush(max_heap_container, -value_to_insert)
        elif input_command[0] == 'extract':
            maximum_value = -heapq.heappop(max_heap_container)
            print(maximum_value)

if __name__ == '__main__':
    main()