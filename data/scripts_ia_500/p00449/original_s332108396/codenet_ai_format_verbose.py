from heapq import heappop, heappush
import sys

read_line = sys.stdin.readline

def find_shortest_path(number_of_nodes, adjacency_list, start_node, goal_node):
    
    max_distance = 10_000_000
    distances = [max_distance] * (number_of_nodes + 1)
    distances[start_node] = 0

    priority_queue = [(0, start_node)]

    while priority_queue:

        current_cost, current_node = heappop(priority_queue)

        if current_node == goal_node:
            return current_cost

        for edge_cost, neighbor_node in adjacency_list[current_node]:

            new_cost = current_cost + edge_cost

            if new_cost < distances[neighbor_node]:
                distances[neighbor_node] = new_cost
                heappush(priority_queue, (new_cost, neighbor_node))

    return -1


def process_commands(number_of_nodes, number_of_commands):

    adjacency_list = [[] for _ in range(number_of_nodes + 1)]

    for _ in range(number_of_commands):

        command_line = read_line()
        command_type_and_params = command_line.strip()

        command_type = command_type_and_params[0]
        parameters = command_type_and_params[2:].split()
        parameters_as_int = list(map(int, parameters))

        if command_type == '0':
            start_node, end_node = parameters_as_int
            shortest_path_cost = find_shortest_path(number_of_nodes, adjacency_list, start_node, end_node)
            print(shortest_path_cost)

        else:
            node_1, node_2, edge_cost = parameters_as_int
            adjacency_list[node_1].append((edge_cost, node_2))
            adjacency_list[node_2].append((edge_cost, node_1))


for input_line in iter(read_line, '0 0\n'):
    nodes_count, commands_count = map(int, input_line.split())
    process_commands(nodes_count, commands_count)