import sys
from operator import itemgetter
from fractions import gcd
from math import ceil, floor, sqrt
from copy import deepcopy
from collections import Counter, deque
import heapq
from functools import reduce

sys.setrecursionlimit(200000)

def read_integer():
    return int(sys.stdin.readline())

def read_multiple_integers():
    return map(int, sys.stdin.readline().rstrip().split())

def read_integer_list():
    return list(map(int, sys.stdin.readline().rstrip().split()))

def read_character_list():
    return list(sys.stdin.readline().rstrip())

def debug_log(*args, sep=" ", end="\n"):
    if not __debug__:
        print("debug:", *args, file=sys.stderr, sep=sep, end=end)

def terminate_execution(*args):
    print(*args)
    sys.exit()

def main():
    total_nodes, start_node_raw_idx, target_node_raw_idx = read_multiple_integers()
    start_node_index = start_node_raw_idx - 1
    target_node_index = target_node_raw_idx - 1

    print("?", start_node_index + 1, target_node_index + 1, flush=True)
    initial_path_weight = read_integer()

    min_distance_from_start = [0] * total_nodes
    min_distance_from_start[target_node_index] = initial_path_weight

    min_distance_from_target = [0] * total_nodes
    min_distance_from_target[start_node_index] = initial_path_weight

    for current_node in range(total_nodes):
        if current_node != start_node_index and current_node != target_node_index:
            print("?", start_node_index + 1, current_node + 1, flush=True)
            min_distance_from_start[current_node] = read_integer()
            print("?", target_node_index + 1, current_node + 1, flush=True)
            min_distance_from_target[current_node] = read_integer()

    candidate_nodes_on_shortest_path = []
    for current_node in range(total_nodes):
        total_distance = min_distance_from_start[current_node] + min_distance_from_target[current_node]
        if total_distance == initial_path_weight:
            candidate_nodes_on_shortest_path.append((current_node, min_distance_from_start[current_node]))

    candidate_nodes_on_shortest_path.sort(key=itemgetter(1))

    if len(candidate_nodes_on_shortest_path) == 2:
        print("!", start_node_index + 1, target_node_index + 1, flush=True)
        sys.exit()

    reconstructed_path_indices = []
    candidate_nodes_queue = deque(candidate_nodes_on_shortest_path)
    last_visited_node = start_node_index

    candidate_nodes_queue.popleft()
    reconstructed_path_indices.append(start_node_index)

    next_node_index, next_node_weight = candidate_nodes_queue.popleft()
    reconstructed_path_indices.append(next_node_index)
    last_visited_node = next_node_index

    while True:
        next_node_index, next_node_weight = candidate_nodes_queue.popleft()
        if next_node_index == target_node_index:
            reconstructed_path_indices.append(next_node_index)
            last_visited_node = next_node_index
            break
        print("?", last_visited_node + 1, next_node_index + 1, flush=True)
        edge_weight = read_integer()
        total_cost = min_distance_from_start[last_visited_node] + edge_weight + min_distance_from_target[next_node_index]
        if total_cost == initial_path_weight:
            reconstructed_path_indices.append(next_node_index)
            last_visited_node = next_node_index
            continue
        else:
            continue

    output_path = list(map(lambda index: index + 1, reconstructed_path_indices))
    print("!", *output_path)

if __name__ == '__main__':
    main()