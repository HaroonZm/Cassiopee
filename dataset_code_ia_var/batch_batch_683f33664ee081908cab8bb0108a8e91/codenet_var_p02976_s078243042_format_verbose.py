from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def read_int_list():
    return [int(value) for value in sys.stdin.readline().split()]

def read_single_int():
    return int(sys.stdin.readline())

def read_str_list():
    return [list(item) for item in sys.stdin.readline().split()]

def read_char_list():
    return list(sys.stdin.readline())[:-1]

def read_int_rows(number_of_rows):
    return [read_single_int() for _ in range(number_of_rows)]

def read_list_of_int_lists(number_of_rows):
    return [read_int_list() for _ in range(number_of_rows)]

def read_char_rows(number_of_rows):
    return [read_char_list() for _ in range(number_of_rows)]

def read_list_of_str_lists(number_of_rows):
    return [read_str_list() for _ in range(number_of_rows)]

sys.setrecursionlimit(1000000)
MODULO = 1000000007

# Problem A
def solve_problem_A():
    number_of_elements = read_single_int()
    integer_list = read_int_list()

    if sum(integer_list) == 0:
        print("Yes")
        return

    if number_of_elements % 3 != 0:
        print("No")
        return

    frequency_counter = defaultdict(lambda: 0)
    for element in integer_list:
        frequency_counter[element] += 1

    if len(list(frequency_counter.items())) == 2:
        if frequency_counter[0] == number_of_elements // 3:
            print("Yes")
            return
        else:
            print("No")
            return

    xor_accumulator = 0
    for unique_value, count in frequency_counter.items():
        xor_accumulator ^= unique_value
        if count != number_of_elements // 3:
            print("No")
            return

    if xor_accumulator == 0:
        print("Yes")
        return

    print("No")
    return

# Problem B
def solve_problem_B():

    def depth_first_search(current_node, visited_nodes):
        for adjacent_node in adjacency_list[current_node]:
            if visited_nodes[adjacent_node]:
                visited_nodes[adjacent_node] = 0
                depth_first_search(adjacent_node, visited_nodes)
                if flip_flag[adjacent_node]:
                    edge_key = (min(current_node, adjacent_node), max(current_node, adjacent_node))
                    edge_orientation[edge_key] ^= 1
                    flip_flag[current_node] ^= 1
                    flip_flag[adjacent_node] ^= 1

    number_of_nodes, number_of_edges = read_int_list()
    edge_orientation = defaultdict(int)
    flip_flag = [0] * (number_of_nodes + 1)
    adjacency_list = [[] for _ in range(number_of_nodes + 1)]

    for _ in range(number_of_edges):
        node_u, node_v = read_int_list()
        edge_key = (min(node_u, node_v), max(node_u, node_v))
        edge_orientation[edge_key] = 1
        adjacency_list[node_u].append(node_v)
        adjacency_list[node_v].append(node_u)
        flip_flag[min(node_u, node_v)] ^= 1

    if number_of_edges % 2 == 1:
        print(-1)
        return

    visited_nodes = [1] * (number_of_nodes + 1)
    visited_nodes[1] = 0
    depth_first_search(1, visited_nodes)

    for edge_tuple, orientation in edge_orientation.items():
        if orientation:
            print(*edge_tuple)
        else:
            print(*edge_tuple[::-1])
    return

# Problem C
def solve_problem_C():
    given_integer = read_single_int()
    power_of_two_list = [(1 << bit_index) for bit_index in range(100)]
    if given_integer in power_of_two_list:
        print("No")
        quit()
    if given_integer + 1 in power_of_two_list:
        print("Yes")
        for edge_label in range(1, 2 * given_integer):
            print(edge_label, edge_label + 1)
        quit()
    edge_list = []
    for edge_label in range(1, 3):
        edge_list.append((edge_label, edge_label + 1))
    edge_list.append((3, given_integer + 1))
    for edge_label in range(1, 3):
        edge_list.append((edge_label + given_integer, edge_label + given_integer + 1))
    upper_node = 1
    lower_node = 1
    for edge_label in range(2, given_integer // 2 + given_integer % 2):
        edge_list.append((upper_node, 2 * edge_label))
        edge_list.append((lower_node, 2 * edge_label + 1))
        edge_list.append((2 * edge_label, 2 * edge_label + given_integer + 1))
        edge_list.append((2 * edge_label + 1, 2 * edge_label + given_integer))
        upper_node = 2 * edge_label + given_integer + 1
        lower_node = 2 * edge_label + given_integer

    if given_integer % 2:
        print("Yes")
        for node_u, node_v in edge_list:
            print(node_u, node_v)
    else:
        edge_list.append((given_integer - 1, given_integer))
        for bit_index in range(given_integer):
            if power_of_two_list[bit_index] & given_integer:
                break
        edge_list.append((power_of_two_list[bit_index + 1] - 2, 2 * given_integer))
        print("Yes")
        for node_u, node_v in edge_list:
            print(node_u, node_v)
    return

# Problem D
def solve_problem_D():
    number_of_inputs = read_single_int()
    return

# Problem E
def solve_problem_E():
    number_of_inputs = read_single_int()
    return

# Problem F
def solve_problem_F():
    number_of_inputs = read_single_int()
    return

# Main Execution
if __name__ == "__main__":
    solve_problem_B()