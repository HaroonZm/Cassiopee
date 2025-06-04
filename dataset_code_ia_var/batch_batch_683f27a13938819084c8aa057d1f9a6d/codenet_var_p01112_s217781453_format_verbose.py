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
import copy
import functools
import time
import random
import resource

# Augmentation de la limite de récursion pour autoriser des appels récursifs profonds
sys.setrecursionlimit(10**7)

INFINITY = 10**20
EPSILON = 1.0 / 10**10
MODULUS_1 = 10**9 + 7
MODULUS_2 = 998244353

# Directions cardinales (haut, droite, bas, gauche)
GRID_DIRECTIONS_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# Directions sur une grille 8-voisins
GRID_DIRECTIONS_8 = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def read_int_list():
    return list(map(int, sys.stdin.readline().split()))

def read_list_of_int_lists():
    return [list(map(int, line.split())) for line in sys.stdin.readlines()]

def read_int_list_decremented():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def read_float_list():
    return [float(x) for x in sys.stdin.readline().split()]

def read_string_list():
    return sys.stdin.readline().split()

def read_single_int():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_single_string():
    return input()

def print_flush(message):
    return print(message, flush=True)

def print_stderr(message):
    return print(str(message), file=sys.stderr)

def join_array_as_string(array, separator):
    return separator.join(map(str, array))

def join_2d_array_as_string(array_2d, row_separator, column_separator):
    return row_separator.join(column_separator.join(map(str, row)) for row in array_2d)

def main():
    results_per_case = []

    def solve_single_test_case():
        number_of_vertices = read_single_int()
        if number_of_vertices == 0:
            return

        number_of_edges = read_single_int()
        edge_list = [read_int_list_decremented() for _ in range(number_of_edges)]

        half_vertex_count = number_of_vertices // 2
        adjacency_matrix = [[0] * number_of_vertices for _ in range(number_of_vertices)]
        edge_assignment_counts = [[0] * 2 for _ in range(number_of_vertices)]  # [assigned as left, assigned as right] for each vertex

        for vertex_a, vertex_b in edge_list:
            adjacency_matrix[vertex_a][vertex_b] = 1
            adjacency_matrix[vertex_b][vertex_a] = 1
            edge_assignment_counts[vertex_a][0] += 1  # vertex_a assigned as left
            edge_assignment_counts[vertex_b][1] += 1  # vertex_b assigned as right

        # Si un sommet a déjà trop d'assignations à gauche ou à droite, le cas n'est pas valide
        for vertex_index in range(number_of_vertices):
            if edge_assignment_counts[vertex_index][0] > half_vertex_count or edge_assignment_counts[vertex_index][1] > half_vertex_count:
                results_per_case.append(0)
                return True

        # Liste des couples de sommets non connectés
        unconnected_vertex_pairs = []
        for vertex_x in range(number_of_vertices):
            for vertex_y in range(vertex_x + 1, number_of_vertices):
                if adjacency_matrix[vertex_x][vertex_y] == 0:
                    unconnected_vertex_pairs.append((vertex_x, vertex_y))
        number_of_unconnected_pairs = len(unconnected_vertex_pairs)

        def count_valid_assignments(current_edge_assignment_counts, current_pair_index):
            if current_pair_index == number_of_unconnected_pairs:
                return 1

            total_ways = 0
            vertex_x, vertex_y = unconnected_vertex_pairs[current_pair_index]

            # Essayer d'assigner (x,y) comme (gauche, droite)
            if current_edge_assignment_counts[vertex_x][0] < half_vertex_count and current_edge_assignment_counts[vertex_y][1] < half_vertex_count:
                current_edge_assignment_counts[vertex_x][0] += 1
                current_edge_assignment_counts[vertex_y][1] += 1
                total_ways += count_valid_assignments(current_edge_assignment_counts, current_pair_index + 1)
                current_edge_assignment_counts[vertex_x][0] -= 1
                current_edge_assignment_counts[vertex_y][1] -= 1

            # Essayer d'assigner (x,y) comme (droite, gauche)
            if current_edge_assignment_counts[vertex_x][1] < half_vertex_count and current_edge_assignment_counts[vertex_y][0] < half_vertex_count:
                current_edge_assignment_counts[vertex_x][1] += 1
                current_edge_assignment_counts[vertex_y][0] += 1
                total_ways += count_valid_assignments(current_edge_assignment_counts, current_pair_index + 1)
                current_edge_assignment_counts[vertex_x][1] -= 1
                current_edge_assignment_counts[vertex_y][0] -= 1

            return total_ways

        results_per_case.append(count_valid_assignments(edge_assignment_counts, 0))
        return True

    while solve_single_test_case():
        pass

    return join_array_as_string(results_per_case, "\n")

print(main())