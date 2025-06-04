import math

def get_input():
    return int(input())

def get_list():
    return list(map(int, input().split()))

def find_minimum(numbers):
    return min(numbers)

def find_maximum(numbers):
    return max(numbers)

def sum_two_numbers(x, y):
    return x + y

def divide_by_two(val):
    return val / 2

def ceil_value(val):
    return math.ceil(val)

def subtract_two_numbers(x, y):
    return x - y

def process():
    n = get_input()
    a = get_list()
    mn = find_minimum(a)
    mx = find_maximum(a)
    s = sum_two_numbers(mn, mx)
    d = divide_by_two(s)
    c = ceil_value(d)
    result = subtract_two_numbers(c, mn)
    print(result)

process()