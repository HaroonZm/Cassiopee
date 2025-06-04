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

sys.setrecursionlimit(10 ** 7)

infinity_value = 10 ** 20
modulo_value = 10 ** 9 + 7

def read_integers_from_input():
    return [int(element) for element in sys.stdin.readline().split()]

def read_floats_from_input():
    return [float(element) for element in sys.stdin.readline().split()]

def read_strings_from_input():
    return sys.stdin.readline().split()

def read_single_integer():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_single_string():
    return input()

def main():
    number_of_vertices, number_of_edges = read_integers_from_input()
    
    adjacency_list = collections.defaultdict(set)
    
    for _ in range(number_of_edges):
        vertex_u, vertex_v = read_integers_from_input()
        adjacency_list[vertex_u - 1].add(vertex_v - 1)
        adjacency_list[vertex_v - 1].add(vertex_u - 1)
    
    vertex_colors = [0] * number_of_vertices

    number_of_queries = read_single_integer()
    queries = sorted([[query_index] + read_integers_from_input() for query_index in range(number_of_queries)], reverse=True)
    
    farthest_visited_depth = [-1] * number_of_vertices

    for _, start_vertex, max_depth, color_value in queries:
        start_vertex -= 1
        
        if farthest_visited_depth[start_vertex] >= max_depth:
            continue
        
        if vertex_colors[start_vertex] == 0:
            vertex_colors[start_vertex] = color_value
        
        vertices_to_explore_current_level = [start_vertex]
        
        for current_depth in range(max_depth - 1, -1, -1):
            vertices_to_explore_next_level = []
            for current_vertex in vertices_to_explore_current_level:
                for neighbor_vertex in adjacency_list[current_vertex]:
                    if farthest_visited_depth[neighbor_vertex] >= current_depth:
                        continue
                    farthest_visited_depth[neighbor_vertex] = current_depth
                    vertices_to_explore_next_level.append(neighbor_vertex)
                    if vertex_colors[neighbor_vertex] == 0:
                        vertex_colors[neighbor_vertex] = color_value
            vertices_to_explore_current_level = vertices_to_explore_next_level

    return '\n'.join(map(str, vertex_colors))

print(main())