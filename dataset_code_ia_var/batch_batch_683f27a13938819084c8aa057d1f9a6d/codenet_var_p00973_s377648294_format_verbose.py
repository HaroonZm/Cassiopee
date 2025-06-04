#!/usr/bin/python3

from decimal import Decimal
from fractions import Fraction
import math
import os
import sys

###############################################################################

class Vector2D(object):
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        super().__init__()

    def __add__(self, other_vector):
        return Vector2D(self.x_coordinate + other_vector.x_coordinate,
                        self.y_coordinate + other_vector.y_coordinate)

    def __sub__(self, other_vector):
        return Vector2D(self.x_coordinate - other_vector.x_coordinate,
                        self.y_coordinate - other_vector.y_coordinate)

    def __mul__(self, scalar_value):
        return Vector2D(self.x_coordinate * scalar_value,
                        self.y_coordinate * scalar_value)

    def __rmul__(self, scalar_value):
        return self.__mul__(scalar_value)

    def __truediv__(self, scalar_value):
        return Vector2D(self.x_coordinate / scalar_value,
                        self.y_coordinate / scalar_value)

    def __iadd__(self, other_vector):
        self.x_coordinate += other_vector.x_coordinate
        self.y_coordinate += other_vector.y_coordinate
        return self

    def __isub__(self, other_vector):
        self.x_coordinate -= other_vector.x_coordinate
        self.y_coordinate -= other_vector.y_coordinate
        return self

    def __imul__(self, scalar_value):
        self.x_coordinate *= scalar_value
        self.y_coordinate *= scalar_value
        return self

    def __idiv__(self, scalar_value):
        self.x_coordinate /= scalar_value
        self.y_coordinate /= scalar_value
        return self

    def __neg__(self):
        return Vector2D(-self.x_coordinate, -self.y_coordinate)

    def __eq__(self, other_vector):
        return (self.x_coordinate == other_vector.x_coordinate and
                self.y_coordinate == other_vector.y_coordinate)

    def __ne__(self, other_vector):
        return not self.__eq__(other_vector)

    def __hash__(self):
        return hash(('Vector2D', self.x_coordinate, self.y_coordinate))

    def dot_product(self, other_vector):
        return self.x_coordinate * other_vector.x_coordinate + self.y_coordinate * other_vector.y_coordinate

    def cross_product(self, other_vector):
        return self.x_coordinate * other_vector.y_coordinate - self.y_coordinate * other_vector.x_coordinate

    def squared_length(self):
        return self.x_coordinate * self.x_coordinate + self.y_coordinate * self.y_coordinate

    def __abs__(self):
        return math.sqrt(float(self.squared_length()))

    def __str__(self):
        return '({}, {})'.format(self.x_coordinate, self.y_coordinate)

    def __repr__(self):
        return 'Vector2D({!r}, {!r})'.format(self.x_coordinate, self.y_coordinate)

###############################################################################

DEBUG_ENABLED = 'DEBUG' in os.environ

def debug_print(*args, sep=' ', end='\n'):
    if DEBUG_ENABLED:
        print(*args, sep=sep, end=end)

###############################################################################

def input_line():
    return sys.stdin.readline().rstrip()

def read_single_integer():
    return int(input_line())

def read_multiple_integers():
    return [int(value) for value in input_line().split()]

###############################################################################

def sign_of_value(numeric_value):
    if numeric_value > 0:
        return 1
    if numeric_value < 0:
        return -1
    return 0

EPSILON_ZERO = Fraction(1, 10 ** 26)

def solve_polynomial_roots_in_range(polynomial_coefficients, lower_bound, upper_bound):
    coefficients = list(polynomial_coefficients)
    while coefficients and coefficients[-1] == 0:
        coefficients.pop()
    if len(coefficients) <= 1:
        return []
    if len(coefficients) == 2:
        constant_term, linear_coefficient = coefficients
        root = Fraction(-constant_term, linear_coefficient)
        if lower_bound <= root <= upper_bound:
            return [(root, root)]
        return []

    derivative_coefficients = []
    for coefficient_index in range(1, len(coefficients)):
        derivative_coefficients.append(coefficient_index * coefficients[coefficient_index])
    critical_segments = [(lower_bound, None)] + \
        solve_polynomial_roots_in_range(derivative_coefficients, lower_bound, upper_bound) + \
        [(None, upper_bound)]
    solutions = []

    def evaluate_polynomial_at(point):
        value = 0
        for exponent, coefficient in enumerate(coefficients):
            value += coefficient * (point ** exponent)
        return value

    for segment_index in range(len(critical_segments) - 1):
        segment_start = critical_segments[segment_index][0]
        segment_end = critical_segments[segment_index + 1][1]
        segment_start_sign = sign_of_value(evaluate_polynomial_at(segment_start))
        segment_end_sign = sign_of_value(evaluate_polynomial_at(segment_end))
        if (segment_start_sign >= 0 and segment_end_sign >= 0) or \
           (segment_start_sign < 0 and segment_end_sign < 0):
            continue
        left_point = segment_start
        right_point = segment_end
        while right_point - left_point > EPSILON_ZERO:
            mid_fraction = Fraction(left_point + right_point, 2)
            mid_decimal = Fraction(Decimal(mid_fraction.numerator) / Decimal(mid_fraction.denominator))
            if not (left_point < mid_decimal < right_point):
                mid_decimal = mid_fraction
            polynomial_value_at_mid = evaluate_polynomial_at(mid_decimal)
            if polynomial_value_at_mid >= 0:
                if segment_start_sign >= 0:
                    left_point = mid_decimal
                else:
                    right_point = mid_decimal
            else:
                if segment_start_sign >= 0:
                    right_point = mid_decimal
                else:
                    left_point = mid_decimal
        solutions.append((left_point, right_point))
    return solutions

###############################################################################

def compute_min_max_sqrt_distances_between_area_halving_chords(
    number_of_vertices,
    polygon_vertices_list
):
    if DEBUG_ENABLED:
        debug_print('polygon({!r}, fill=False)'.format([
            (vertex.x_coordinate, vertex.y_coordinate) for vertex in polygon_vertices_list
        ]))

    twice_polygon_area = 0
    for vertex_index in range(1, number_of_vertices - 1):
        relative_vector_a = polygon_vertices_list[vertex_index] - polygon_vertices_list[0]
        relative_vector_b = polygon_vertices_list[vertex_index + 1] - polygon_vertices_list[vertex_index]
        twice_polygon_area += relative_vector_a.cross_product(relative_vector_b)

    accumulated_area = 0
    b_side_index = -1
    for vertex_index in range(1, number_of_vertices - 1):
        relative_vector_a = polygon_vertices_list[vertex_index] - polygon_vertices_list[0]
        relative_vector_b = polygon_vertices_list[vertex_index + 1] - polygon_vertices_list[vertex_index]
        area_contributed_by_edge = relative_vector_a.cross_product(relative_vector_b) * 2
        if accumulated_area + area_contributed_by_edge <= twice_polygon_area:
            accumulated_area += area_contributed_by_edge
            continue
        remaining_area_to_bisect = twice_polygon_area - accumulated_area
        area_fraction_on_current_edge = Fraction(
            twice_polygon_area - accumulated_area, area_contributed_by_edge
        )
        assert 0 <= area_fraction_on_current_edge < 1

        b_side_index = vertex_index
        area_fraction_b = area_fraction_on_current_edge
        b_point_on_edge = polygon_vertices_list[vertex_index] + area_fraction_on_current_edge * (
            polygon_vertices_list[vertex_index + 1] - polygon_vertices_list[vertex_index]
        )
        debug_print('bi =', b_side_index, 'bk =', area_fraction_b, 'bv =', b_point_on_edge)
        break

    assert b_side_index != -1

    a_side_index = 0
    area_fraction_a = 0

    squared_distance_maximum = (b_point_on_edge - polygon_vertices_list[0]).squared_length()
    squared_distance_minimum = squared_distance_maximum

    while b_side_index != 0:
        assert 0 <= area_fraction_a < 1
        assert 0 <= area_fraction_b < 1

        debug_print('***\nai =', a_side_index, 'ak =', area_fraction_a,
                    'bi =', b_side_index, 'bk =', area_fraction_b)
        debug_print('minl =', squared_distance_minimum, 'maxl =', squared_distance_maximum)

        vertex_a_start = polygon_vertices_list[a_side_index]
        vertex_a_end = polygon_vertices_list[(a_side_index + 1) % number_of_vertices]
        vertex_b_start = polygon_vertices_list[b_side_index]
        vertex_b_end = polygon_vertices_list[(b_side_index + 1) % number_of_vertices]

        point_a = vertex_a_start + area_fraction_a * (vertex_a_end - vertex_a_start)
        point_b = vertex_b_start + area_fraction_b * (vertex_b_end - vertex_b_start)

        debug_print('a0 =', vertex_a_start, 'a1 =', vertex_a_end, 'a2 =', point_a)
        debug_print('b0 =', vertex_b_start, 'b1 =', vertex_b_end, 'b2 =', point_b)

        next_area_fraction_a = 1
        cross_b_end = (point_b - vertex_a_end).cross_product(vertex_b_end - vertex_b_start)
        if cross_b_end != 0:
            next_area_fraction_b = Fraction(
                (vertex_b_start - point_a).cross_product(point_b - vertex_a_end),
                cross_b_end
            )
        else:
            next_area_fraction_b = 2  # Interpret as infinity
        assert area_fraction_b < next_area_fraction_b
        if next_area_fraction_b > 1:
            next_area_fraction_a = Fraction(
                (point_b - vertex_a_start).cross_product(vertex_b_end - point_a),
                (vertex_a_end - vertex_a_start).cross_product(vertex_b_end - point_a)
            )
            next_area_fraction_b = 1

        assert area_fraction_a < next_area_fraction_a <= 1
        assert area_fraction_b < next_area_fraction_b <= 1

        point_a_new = vertex_a_start + next_area_fraction_a * (vertex_a_end - vertex_a_start)
        point_b_new = vertex_b_start + next_area_fraction_b * (vertex_b_end - vertex_b_start)
        debug_print('a3 =', point_a_new, 'b3 =', point_b_new)

        vector_from_a3_to_b3 = point_b_new - point_a_new
        squared_length_ab = vector_from_a3_to_b3.squared_length()
        debug_print('l =', squared_length_ab)
        squared_distance_maximum = max(squared_distance_maximum, squared_length_ab)
        squared_distance_minimum = min(squared_distance_minimum, squared_length_ab)

        diff_a3_a2 = point_a_new - point_a
        diff_b3_b2 = point_b_new - point_b
        diff_b2_a2 = point_b - point_a

        area_A0 = diff_a3_a2.cross_product(diff_b2_a2)
        area_B0 = diff_b2_a2.cross_product(diff_b3_b2)
        denominator_area_A0 = area_A0.denominator if isinstance(area_A0, Fraction) else 1
        denominator_area_B0 = area_B0.denominator if isinstance(area_B0, Fraction) else 1
        gcd_denominator = denominator_area_A0 * denominator_area_B0 // math.gcd(denominator_area_A0, denominator_area_B0)
        area_A0 *= gcd_denominator
        area_B0 *= gcd_denominator
        area_A0 = int(area_A0)
        area_B0 = int(area_B0)
        gcd_A0_B0 = math.gcd(area_A0, area_B0)
        area_A0 //= gcd_A0_B0
        area_B0 //= gcd_A0_B0
        debug_print('y = ({}) * x / (({}) - ({}) * x)'.format(area_A0, area_B0, area_B0 - area_A0))

        if area_A0 == area_B0:
            quadratic_coeff_x2 = (diff_a3_a2 - diff_b3_b2).squared_length()
            quadratic_coeff_x1 = -2 * diff_b2_a2.dot_product(diff_a3_a2 - diff_b3_b2)
            quadratic_constant = diff_b2_a2.squared_length()
            debug_print('L = ({}) * x^2 + ({}) * x + ({})'
                        .format(quadratic_coeff_x2, quadratic_coeff_x1, quadratic_constant))
            root_x = Fraction(-quadratic_coeff_x1, 2 * quadratic_coeff_x2)
            debug_print('x =', root_x)
            if 0 <= root_x <= 1:
                value_at_root = root_x * (quadratic_coeff_x1 + root_x * quadratic_coeff_x2) + quadratic_constant
                debug_print('l =', value_at_root)
                squared_distance_minimum = min(squared_distance_minimum, value_at_root)
        else:
            quadratic_coeff_x2 = diff_a3_a2.squared_length()
            quadratic_coeff_x1 = 2 * (-diff_b2_a2.dot_product(diff_a3_a2) +
                                      Fraction(area_A0, area_B0 - area_A0) * diff_a3_a2.dot_product(diff_b3_b2))
            quadratic_coeff_y2 = diff_b3_b2.squared_length()
            quadratic_coeff_y1 = 2 * (diff_b2_a2.dot_product(diff_b3_b2) -
                                      Fraction(area_B0, area_B0 - area_A0) * diff_a3_a2.dot_product(diff_b3_b2))
            quadratic_constant_term = diff_b2_a2.squared_length()
            def evaluate_quadratic_expression(x_value, y_value):
                return (x_value * (quadratic_coeff_x1 + x_value * quadratic_coeff_x2) +
                        y_value * (quadratic_coeff_y1 + y_value * quadratic_coeff_y2) + quadratic_constant_term)
            parameter_A = Fraction(area_A0, area_B0 - area_A0)
            parameter_B = Fraction(area_B0, area_B0 - area_A0)
            quartic_poly_coeffs = [
                -2 * parameter_A * parameter_A * parameter_B * parameter_B * quadratic_coeff_y2,
                -parameter_A * parameter_B * (2 * parameter_A * quadratic_coeff_y2 - quadratic_coeff_y1),
                0,
                2 * parameter_B * quadratic_coeff_x2 + quadratic_coeff_x1,
                2 * quadratic_coeff_x2
            ]
            debug_print('poly =', quartic_poly_coeffs)
            root_intervals = solve_polynomial_roots_in_range(quartic_poly_coeffs, -parameter_B, 1 - parameter_B)
            debug_print('sols =', root_intervals)
            for interval_start, interval_end in root_intervals:
                solution_x0 = interval_start + parameter_B
                solution_x1 = interval_end + parameter_B
                solution_y0 = Fraction(-parameter_A * parameter_B, solution_x0 - parameter_B) - parameter_A
                solution_y1 = Fraction(-parameter_A * parameter_B, solution_x1 - parameter_B) - parameter_A
                result_0 = evaluate_quadratic_expression(solution_x0, solution_y0)
                result_1 = evaluate_quadratic_expression(solution_x1, solution_y1)
                debug_print('l0 =', result_0, 'l1 =', result_1)
                squared_distance_minimum = min(squared_distance_minimum, result_0, result_1)

        area_fraction_a = next_area_fraction_a
        area_fraction_b = next_area_fraction_b
        if area_fraction_a == 1:
            a_side_index = (a_side_index + 1) % number_of_vertices
            area_fraction_a = 0
        if area_fraction_b == 1:
            b_side_index = (b_side_index + 1) % number_of_vertices
            area_fraction_b = 0

    debug_print('minl', squared_distance_minimum)
    debug_print('maxl', squared_distance_maximum)
    if isinstance(squared_distance_minimum, Fraction):
        minimum_distance = Decimal(squared_distance_minimum.numerator) / Decimal(squared_distance_minimum.denominator)
    else:
        minimum_distance = Decimal(squared_distance_minimum)
    if isinstance(squared_distance_maximum, Fraction):
        maximum_distance = Decimal(squared_distance_maximum.numerator) / Decimal(squared_distance_maximum.denominator)
    else:
        maximum_distance = Decimal(squared_distance_maximum)
    return minimum_distance.sqrt(), maximum_distance.sqrt()

###############################################################################

def main():
    polygon_vertex_count = read_single_integer()
    polygon_vertex_list = [
        Vector2D(*read_multiple_integers())
        for _ in range(polygon_vertex_count)
    ]
    min_distance, max_distance = compute_min_max_sqrt_distances_between_area_halving_chords(
        polygon_vertex_count, polygon_vertex_list
    )
    print(min_distance)
    print(max_distance)

if __name__ == '__main__':
    main()