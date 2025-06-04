import sys
from collections import deque

def read_input():
    return sys.stdin.readline()

def write_output(s):
    sys.stdout.write(s)

def main_solve():
    num_edges, num_group1, num_group2 = map(int, read_input().split())
    if num_edges == num_group1 == num_group2 == 0:
        return False

    total_nodes = num_group1 + num_group2
    adjacency_list = [[] for _ in range(total_nodes)]

    for edge_idx in range(num_edges):
        node_x, node_y, edge_type = read_input().strip().split()
        node_x = int(node_x)
        node_y = int(node_y)
        is_no_edge = (edge_type == "no")
        if node_x == node_y:
            continue
        adjacency_list[node_x-1].append((node_y-1, is_no_edge))
        adjacency_list[node_y-1].append((node_x-1, is_no_edge))

    node_labels = [-1] * total_nodes
    is_valid = True
    component_list = []

    for start_node in range(total_nodes):
        if node_labels[start_node] != -1:
            continue
        processing_queue = deque([start_node])
        node_labels[start_node] = 0
        partition_nodes = [[], []]
        while processing_queue:
            current_node = processing_queue.popleft()
            current_label = node_labels[current_node]
            partition_nodes[current_label].append(current_node + 1)
            for neighbor_node, is_no_edge in adjacency_list[current_node]:
                if node_labels[neighbor_node] != -1:
                    continue
                node_labels[neighbor_node] = current_label ^ is_no_edge
                processing_queue.append(neighbor_node)
        size_a, size_b = map(len, partition_nodes)
        if size_a == size_b:
            is_valid = False
            break
        component_list.append((partition_nodes[0], partition_nodes[1]))

    if not is_valid:
        write_output("no\n")
        return True

    dp_current = [0] * (num_group1 + 1)
    dp_current[0] = 1
    dp_versions = [dp_current[:]]
    num_components = len(component_list)

    for group_a, group_b in component_list:
        size_a = len(group_a)
        size_b = len(group_b)
        dp_next = [0] * (num_group1 + 1)
        for count in range(num_group1 + 1):
            if dp_current[count]:
                if count + size_a <= num_group1:
                    dp_next[count + size_a] += dp_current[count]
                if count + size_b <= num_group1:
                    dp_next[count + size_b] += dp_current[count]
        dp_versions.append(dp_next[:])
        dp_current = dp_next

    if dp_current[num_group1] > 1:
        write_output("no\n")
        return True

    answer_nodes = []
    remaining = num_group1
    for idx in range(num_components-1, -1, -1):
        dp_prev = dp_versions[idx]
        group_a, group_b = component_list[idx]
        size_a = len(group_a)
        size_b = len(group_b)
        if remaining - size_a >= 0 and dp_prev[remaining - size_a]:
            answer_nodes.extend(group_a)
            remaining -= size_a
        else:
            answer_nodes.extend(group_b)
            remaining -= size_b

    if answer_nodes:
        answer_nodes.sort()
        write_output("\n".join(map(str, answer_nodes)))
        write_output("\n")
    write_output("end\n")
    return True

while main_solve():
    pass