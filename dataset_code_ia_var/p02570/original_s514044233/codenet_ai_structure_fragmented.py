import os
from sys import stdin, stdout

def read_line():
    return stdin.readline()

def split_line(line):
    return line.split()

def convert_to_ints(strs):
    return map(int, strs)

def get_input_values():
    line = read_line()
    strs = split_line(line)
    ints = convert_to_ints(strs)
    return list(ints)

def calculate_time(d, t, s):
    return d / t

def can_reach(d, t, s):
    time_needed = calculate_time(d, t, s)
    return time_needed <= s

def print_yes():
    print("Yes")

def print_no():
    print("No")

def print_result(can):
    if can:
        print_yes()
    else:
        print_no()

def process_test_case(tc):
    values = get_input_values()
    d, t, s = values
    result = can_reach(d, t, s)
    print_result(result)

def main_loop():
    tcs = 1
    tc = 1
    while tc <= tcs:
        process_test_case(tc)
        tc += 1

def main():
    main_loop()

main()