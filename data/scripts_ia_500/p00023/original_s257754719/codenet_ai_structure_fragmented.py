#!/usr/bin/env python

import sys

def read_input_line():
    return input()

def read_stdin_lines():
    return sys.stdin

def parse_floats_from_string(s):
    return list(map(float, s.split()))

def unpack_coordinates(d):
    return d[0], d[1], d[2], d[3], d[4], d[5]

def calc_distance(xa, ya, xb, yb):
    return ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5

def condition_no_overlap(distance, ra, rb):
    return distance > ra + rb

def condition_a_in_b(distance, ra, rb):
    return distance + ra < rb

def condition_b_in_a(distance, ra, rb):
    return distance + rb < ra

def print_result(value):
    print(value)

def process_line(line):
    d = parse_floats_from_string(line)
    xa, ya, ra, xb, yb, rb = unpack_coordinates(d)
    distance = calc_distance(xa, ya, xb, yb)
    if condition_no_overlap(distance, ra, rb):
        print_result(0)
    elif condition_b_in_a(distance, ra, rb):
        print_result(2)
    elif condition_a_in_b(distance, ra, rb):
        print_result(-2)
    else:
        print_result(1)

def main():
    read_input_line()
    for line in read_stdin_lines():
        process_line(line)

if __name__ == "__main__":
    main()