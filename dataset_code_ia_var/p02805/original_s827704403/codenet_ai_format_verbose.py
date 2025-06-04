from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd, sqrt
from operator import mul
from functools import reduce
from pprint import pprint

sys.setrecursionlimit(2147483647)

INFINITE_DISTANCE = 10 ** 20
MODULO_CONSTANT = 1000000007

def read_integer_list():
    return list(map(int, sys.stdin.buffer.readline().split()))


def read_integer():
    return int(sys.stdin.buffer.readline())


def read_string_list():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()


def read_string():
    return sys.stdin.buffer.readline().rstrip().decode('utf-8')


def read_integers_repeatedly(number_of_lines):
    return [read_integer() for _ in range(number_of_lines)]


def read_integer_lists(number_of_lines):
    return [read_integer_list() for _ in range(number_of_lines)]


def read_strings_repeatedly(number_of_lines):
    return [read_string() for _ in range(number_of_lines)]


def read_string_lists(number_of_lines):
    return [read_string_list() for _ in range(number_of_lines)]


def read_strings_as_lists(number_of_lines):
    return [list(read_string()) for _ in range(number_of_lines)]


def read_multiple_strings_as_lists_of_ints(number_of_lines):
    return [[int(character) for character in list(read_string())] for _ in range(number_of_lines)]


def compute_minimum_enclosing_circle_radius_by_three_points(index_point1, index_point2, index_point3):
    x1, y1 = list_of_points[index_point1]
    x2, y2 = list_of_points[index_point2]
    x3, y3 = list_of_points[index_point3]

    squared_length_side_a = (x2 - x3) ** 2 + (y2 - y3) ** 2
    squared_length_side_b = (x1 - x3) ** 2 + (y1 - y3) ** 2
    squared_length_side_c = (x2 - x1) ** 2 + (y2 - y1) ** 2

    triangle_area = ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2

    if triangle_area == 0:
        return INFINITE_DISTANCE

    numerator_x = (
        squared_length_side_a * (squared_length_side_b + squared_length_side_c - squared_length_side_a) * x1 +
        squared_length_side_b * (squared_length_side_c + squared_length_side_a - squared_length_side_b) * x2 +
        squared_length_side_c * (squared_length_side_a + squared_length_side_b - squared_length_side_c) * x3
    )

    numerator_y = (
        squared_length_side_a * (squared_length_side_b + squared_length_side_c - squared_length_side_a) * y1 +
        squared_length_side_b * (squared_length_side_c + squared_length_side_a - squared_length_side_b) * y2 +
        squared_length_side_c * (squared_length_side_a + squared_length_side_b - squared_length_side_c) * y3
    )

    denominator = 16 * triangle_area * triangle_area

    circle_center_x = numerator_x / denominator
    circle_center_y = numerator_y / denominator

    radius = sqrt((x1 - circle_center_x) ** 2 + (y1 - circle_center_y) ** 2)

    for index_point in range(number_of_points):
        if index_point in (index_point1, index_point2, index_point3):
            continue
        other_point_x, other_point_y = list_of_points[index_point]
        if (other_point_x - circle_center_x) ** 2 + (other_point_y - circle_center_y) ** 2 > radius ** 2:
            return INFINITE_DISTANCE
    return radius


def get_circle_parameters_by_diameter_endpoints(x1, y1, x2, y2):
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    radius = sqrt((center_x - x1) ** 2 + (center_y - y1) ** 2)
    return center_x, center_y, radius


def calculate_euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


number_of_points = read_integer()

list_of_points = []

for _ in range(number_of_points):
    point_x, point_y = read_integer_list()
    list_of_points.append((point_x, point_y))


minimum_enclosing_circle_radius = INFINITE_DISTANCE

for index_point1, index_point2, index_point3 in combinations(range(number_of_points), 3):
    current_radius = compute_minimum_enclosing_circle_radius_by_three_points(index_point1, index_point2, index_point3)
    minimum_enclosing_circle_radius = min(minimum_enclosing_circle_radius, current_radius)

for index_point1, index_point2 in combinations(range(number_of_points), 2):

    point1_x, point1_y = list_of_points[index_point1]
    point2_x, point2_y = list_of_points[index_point2]

    midpoint_x = (point1_x + point2_x) / 2
    midpoint_y = (point1_y + point2_y) / 2

    squared_radius = (midpoint_x - point1_x) ** 2 + (midpoint_y - point1_y) ** 2

    for index_other_point in range(number_of_points):
        if index_other_point == index_point1 or index_other_point == index_point2:
            continue
        other_x, other_y = list_of_points[index_other_point]
        if (other_x - midpoint_x) ** 2 + (other_y - midpoint_y) ** 2 > squared_radius:
            break
    else:
        minimum_enclosing_circle_radius = min(minimum_enclosing_circle_radius, sqrt(squared_radius))

print(minimum_enclosing_circle_radius)