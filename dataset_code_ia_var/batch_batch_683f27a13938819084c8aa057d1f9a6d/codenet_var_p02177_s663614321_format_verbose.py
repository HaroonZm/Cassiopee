import sys
import math
from bisect import bisect_right as bisect_right
from bisect import bisect_left as bisect_left
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop, heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations

MODULO = 10 ** 9 + 7
INFINITY = float('inf')

def read_integer():
    return int(sys.stdin.readline())

def read_list_of_integers():
    return list(map(int, sys.stdin.readline().split()))

number_of_vertices, number_of_edges = read_list_of_integers()

adjacency_list = [[] for _ in range(number_of_vertices)]

for _ in range(number_of_edges):
    start_vertex, end_vertex = read_list_of_integers()
    adjacency_list[start_vertex - 1].append(end_vertex - 1)

def depth_first_search(current_vertex, visited_vertices_list, adjacency_list, visitable):
    visited_vertices_list.append(current_vertex)
    visitable[current_vertex] = False

    for next_vertex in adjacency_list[current_vertex]:
        if visitable[next_vertex]:
            depth_first_search(next_vertex, visited_vertices_list, adjacency_list, visitable)

    return visited_vertices_list

all_reachable_vertices_sorted = []

for source_vertex in range(number_of_vertices):
    is_vertex_visitable = [True] * number_of_vertices
    reachable_vertices = depth_first_search(source_vertex, [], adjacency_list, is_vertex_visitable)
    reachable_vertices.sort()
    all_reachable_vertices_sorted.append(reachable_vertices)

mutually_reachable_vertices = [[] for _ in range(number_of_vertices)]

for source_vertex in range(number_of_vertices):
    for reachable_vertex in all_reachable_vertices_sorted[source_vertex]:
        if source_vertex in all_reachable_vertices_sorted[reachable_vertex]:
            mutually_reachable_vertices[source_vertex].append(reachable_vertex + 1)

for vertex_index in range(number_of_vertices):
    print(*mutually_reachable_vertices[vertex_index])