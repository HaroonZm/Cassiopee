import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

sys.setrecursionlimit(10**7)

INFINITE_DISTANCE = 10**20
FLOAT_EPSILON = 1.0 / 10**10
MODULO_VALUE = 10**9 + 7

DIRECTIONS_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTIONS_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_line_of_integers():
    return [int(token) for token in sys.stdin.readline().split()]

def read_line_of_integers_zero_based():
    return [int(token) - 1 for token in sys.stdin.readline().split()]

def read_line_of_floats():
    return [float(token) for token in sys.stdin.readline().split()]

def read_line_of_strings():
    return sys.stdin.readline().split()

def read_integer():
    return int(sys.stdin.readline())

def read_float():
    return float(sys.stdin.readline())

def read_string():
    return input()

def print_flush(text):
    print(text, flush=True)

def are_line_segments_crossing_directed(endpoint_a1, endpoint_a2, endpoint_b1, endpoint_b2):
    x1, y1, _ = endpoint_a1
    x2, y2, _ = endpoint_a2
    x3, y3, _ = endpoint_b1
    x4, y4, _ = endpoint_b2

    direction_vector_across_to_b1 = (x1 - x2) * (y3 - y1) + (y1 - y2) * (x1 - x3)
    direction_vector_across_to_b2 = (x1 - x2) * (y4 - y1) + (y1 - y2) * (x1 - x4)
    return direction_vector_across_to_b1 * direction_vector_across_to_b2 < 0

def are_segments_crossing(endpoint_a1, endpoint_a2, endpoint_b1, endpoint_b2):
    return (are_line_segments_crossing_directed(endpoint_a1, endpoint_a2, endpoint_b1, endpoint_b2) and
            are_line_segments_crossing_directed(endpoint_b1, endpoint_b2, endpoint_a1, endpoint_a2))

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def point_to_segment_distance(segment_point1, segment_point2, external_point):
    x1, y1, _ = segment_point1
    x2, y2, _ = segment_point2
    x3, y3, _ = external_point

    segment_vector_x = x2 - x1
    segment_vector_y = y2 - y1
    point_vector_x = x3 - x1
    point_vector_y = y3 - y1

    projection_ratio = ((segment_vector_x * point_vector_x) + (segment_vector_y * point_vector_y)) / \
                       (segment_vector_x ** 2 + segment_vector_y ** 2)

    if projection_ratio <= 0:
        return euclidean_distance(x1, y1, x3, y3)
    if projection_ratio >= 1:
        return euclidean_distance(x2, y2, x3, y3)
    projected_x = x1 + projection_ratio * segment_vector_x
    projected_y = y1 + projection_ratio * segment_vector_y
    return euclidean_distance(projected_x, projected_y, x3, y3)

def main():
    result_distances = []

    def process_graph_and_compute_shortest_distance(number_of_polygons, start_polygon_index, end_polygon_index):
        polygon_sides = []
        for polygon_index in range(number_of_polygons):
            center_x, center_y, angle_degrees, radius = read_line_of_integers()
            angle_radians = angle_degrees / 360 * math.pi * 2 + math.pi / 2
            vertices = []
            for vertex_index in range(5):
                current_angle = angle_radians + math.pi * 2 / 5 * vertex_index
                vertex_x = math.cos(current_angle) * radius + center_x
                vertex_y = math.sin(current_angle) * radius + center_y
                vertices.append((vertex_x, vertex_y, polygon_index))
            for edge_index in range(5):
                polygon_sides.append((vertices[edge_index], vertices[edge_index - 2]))

        segment_distance_matrix = [[INFINITE_DISTANCE] * number_of_polygons for _ in range(number_of_polygons)]

        total_sides = number_of_polygons * 5
        for first_side_index in range(total_sides):
            side_a_start, side_a_end = polygon_sides[first_side_index]
            polygon_index_a = side_a_start[2]
            for second_side_index in range(first_side_index + 1, total_sides):
                side_b_start, side_b_end = polygon_sides[second_side_index]
                polygon_index_b = side_b_start[2]
                if polygon_index_a == polygon_index_b or segment_distance_matrix[polygon_index_a][polygon_index_b] == 0:
                    continue
                if are_segments_crossing(side_a_start, side_a_end, side_b_start, side_b_end):
                    segment_distance_matrix[polygon_index_a][polygon_index_b] = 0
                    continue
                distances = []
                distances.append(point_to_segment_distance(side_a_start, side_a_end, side_b_start))
                distances.append(point_to_segment_distance(side_a_start, side_a_end, side_b_end))
                distances.append(point_to_segment_distance(side_b_start, side_b_end, side_a_start))
                distances.append(point_to_segment_distance(side_b_start, side_b_end, side_a_end))
                minimum_distance = min(distances)
                if segment_distance_matrix[polygon_index_a][polygon_index_b] > minimum_distance:
                    segment_distance_matrix[polygon_index_a][polygon_index_b] = minimum_distance

        polygon_graph = collections.defaultdict(list)
        for source_polygon in range(number_of_polygons):
            for target_polygon in range(source_polygon + 1, number_of_polygons):
                connection_distance = segment_distance_matrix[source_polygon][target_polygon]
                polygon_graph[source_polygon].append((target_polygon, connection_distance))
                polygon_graph[target_polygon].append((source_polygon, connection_distance))

        def dijkstra_shortest_paths(source_polygon_index):
            shortest_distances = collections.defaultdict(lambda: INFINITE_DISTANCE)
            shortest_distances[source_polygon_index] = 0
            priority_queue = []
            heapq.heappush(priority_queue, (0, source_polygon_index))
            visited_polygons = collections.defaultdict(bool)
            while priority_queue:
                current_distance, current_polygon = heapq.heappop(priority_queue)
                if visited_polygons[current_polygon]:
                    continue
                visited_polygons[current_polygon] = True
                for neighbor_polygon, edge_distance in polygon_graph[current_polygon]:
                    if visited_polygons[neighbor_polygon]:
                        continue
                    total_distance = current_distance + edge_distance
                    if shortest_distances[neighbor_polygon] > total_distance:
                        shortest_distances[neighbor_polygon] = total_distance
                        heapq.heappush(priority_queue, (total_distance, neighbor_polygon))
            return shortest_distances

        shortest_paths_from_start = dijkstra_shortest_paths(start_polygon_index - 1)
        return shortest_paths_from_start[end_polygon_index - 1]

    while True:
        number_of_polygons, start_polygon_index, end_polygon_index = read_line_of_integers()
        if number_of_polygons == 0:
            break
        shortest_distance = process_graph_and_compute_shortest_distance(number_of_polygons, start_polygon_index, end_polygon_index)
        result_distances.append(shortest_distance)

    return '\n'.join(str(distance) for distance in result_distances)

print(main())