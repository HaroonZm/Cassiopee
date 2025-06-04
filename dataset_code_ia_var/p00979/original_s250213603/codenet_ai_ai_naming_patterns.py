import os
import sys

def run_main():
    input_value = read_single_int()
    print(compute_result(input_value))

def compute_result(time_value):
    if time_value <= 3:
        return time_value

    sequence_counter = 1
    remaining = time_value - 1
    factor = 3

    while remaining >= 2 * factor:
        remaining -= 2 * factor
        factor *= 3
        sequence_counter += 2

    if remaining >= factor:
        remaining -= factor
        sequence_counter += 1
    else:
        factor //= 3

    while remaining > 0:
        times = remaining // factor
        remaining -= times * factor
        sequence_counter += times
        factor //= 3

    return sequence_counter

ENV_DEBUG_ENABLED = 'DEBUG' in os.environ

def read_line_input():
    return sys.stdin.readline().rstrip()

def read_single_int():
    return int(read_line_input())

def read_multiple_ints():
    return [int(element) for element in read_line_input().split()]

def debug_output(*args, sep=' ', end='\n'):
    if ENV_DEBUG_ENABLED:
        print(*args, sep=sep, end=end)

if __name__ == '__main__':
    run_main()