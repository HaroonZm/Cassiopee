import copy
import numpy as np
import random

def get_input():
    return input().split()

def parse_ints(lst):
    return list(map(int, lst))

def get_nm_x():
    return parse_ints(get_input())

def get_array():
    return parse_ints(get_input())

def create_range_right(x, n):
    return range(x, n)

def create_range_left(x):
    return range(x)

def in_a(i, a):
    return i in a

def increment_counter_if_in_a(counter, i, a):
    if in_a(i, a):
        return counter + 1
    return counter

def calculate_cost_r(x, n, a):
    cost = 0
    for i in create_range_right(x, n):
        cost = increment_counter_if_in_a(cost, i, a)
    return cost

def calculate_cost_l(x, a):
    cost = 0
    for i in create_range_left(x):
        cost = increment_counter_if_in_a(cost, i, a)
    return cost

def print_minimum_cost(cost_l, cost_r):
    print(min(cost_l, cost_r))

def main():
    n, m, x = get_nm_x()
    a = get_array()
    cost_r = calculate_cost_r(x, n, a)
    cost_l = calculate_cost_l(x, a)
    print_minimum_cost(cost_l, cost_r)

main()