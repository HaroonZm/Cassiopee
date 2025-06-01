#!/usr/bin/python3

import os
import sys

def main():
    H = read_height()
    W = read_width()
    A = read_matrix(H)
    result = compute_best_value(H, W, A)
    print_result(result)

def read_height():
    values = read_ints()
    return values[0]

def read_width():
    values = read_ints()
    if len(values) > 1:
        return values[1]
    # Fallback if height and width are not read together
    return read_int()

def read_matrix(H):
    rows = []
    for _ in range(H):
        row = read_ints()
        rows.append(row)
    return rows

def compute_best_value(H, W, A):
    best_initial = initialize_best_value()
    best = best_initial
    for ay in generate_range(H):
        for ax in generate_range(W):
            s = calculate_sum_for_point(H, W, A, ay, ax)
            best = update_best_value(best, s)
    return best

def initialize_best_value():
    return 2 ** 63

def generate_range(limit):
    return range(limit)

def calculate_sum_for_point(H, W, A, ay, ax):
    s = 0
    for y in generate_range(H):
        for x in generate_range(W):
            cell_value = get_cell_value(A, y, x)
            distance = calculate_distance(y, x, ay, ax)
            contribution = multiply_values(cell_value, distance)
            s = add_values(s, contribution)
    return s

def get_cell_value(matrix, y, x):
    return matrix[y][x]

def calculate_distance(y, x, ay, ax):
    distance_y = calculate_abs_diff(y, ay)
    distance_x = calculate_abs_diff(x, ax)
    minimum_distance = minimum_of_two(distance_y, distance_x)
    return minimum_distance

def calculate_abs_diff(a, b):
    diff = subtract_values(a, b)
    abs_diff = absolute_value(diff)
    return abs_diff

def subtract_values(a, b):
    return a - b

def absolute_value(v):
    if v < 0:
        return -v
    return v

def minimum_of_two(a, b):
    if a < b:
        return a
    return b

def multiply_values(a, b):
    return a * b

def add_values(a, b):
    return a + b

def update_best_value(current_best, candidate):
    if candidate < current_best:
        return candidate
    return current_best

def print_result(value):
    print(value)

###############################################################################

DEBUG = 'DEBUG' in os.environ

def inp():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(inp())

def read_ints():
    return [int(e) for e in inp().split()]

def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()